# Architecture (/docs/architecture)



MemexAI has two runtime modes that share the same Postgres schema. The recommended default is the containerized service. Direct Postgres runtime is available for apps that intentionally own database credentials.

## Containerized service mode [#containerized-service-mode]

Use service mode when teams or production apps should not hold database credentials.

```txt
TypeScript app -> @memexai/sdk -> MemexAI service -> Postgres
Python app -> memexai.MemexAI -> MemexAI service -> Postgres
MCP client -> MemexAI service -> Postgres
```

The service handles:

* API key verification.
* Path validation and virtual-to-physical translation.
* SQL reads and writes to `mx_file`, `mx_revision`, and `mx_access_log`.
* The admin UI at `/admin`.
* MCP transport over SSE and stdio.
* Optional background memory consolidation.

## Advanced: direct Postgres runtime mode [#advanced-direct-postgres-runtime-mode]

Use direct Postgres mode only when your application should own database access.

```txt
Your JavaScript app -> @memexai/core -> Postgres
Your Python app -> memexai Python SDK -> Postgres
```

There is no HTTP layer, no service auth, and no separate MemexAI container. Your app passes a Postgres URL, calls `migrate()` on startup or during deploy, then executes memory tools in-process.

## Tool layers [#tool-layers]

### Agentic tools [#agentic-tools]

| Tool              | What it does                                                                     |
| ----------------- | -------------------------------------------------------------------------------- |
| `memory_memorize` | Feeds raw text to an inner model that decides what to remember and writes files. |
| `memory_search`   | Recalls relevant memory with BM25 fallback or model-backed answer synthesis.     |

### Raw tools [#raw-tools]

| Tool                | What it does                                         |
| ------------------- | ---------------------------------------------------- |
| `memory_list`       | Lists visible files for a user.                      |
| `memory_read`       | Reads one file by virtual path.                      |
| `memory_write`      | Creates or overwrites a user file.                   |
| `memory_patch`      | Appends under a heading or replaces exact text.      |
| `memory_smart_read` | Builds one bounded context block from visible files. |

## Background dreaming [#background-dreaming]

Service mode can run an opt-in background memory consolidation loop. It is invisible to end users during chat: after a user's memory has been quiet for a configured grace period, the service reads that user's `user/` files and asks a consolidation agent to merge duplicate facts, clean up fragmented notes, resolve direct contradictions, and keep long-running memory files readable for the next agent trajectory.

Dream writes use the same `memory_write` and `memory_patch` path as normal tools, so revisions and access logs still work. The actor is `dream-agent`. Dream reads exclude `user/log.md`, `user/dream-log.md`, files ending in `-log.md`, and files ending in `.log`.

Each scheduler tick only selects users who have **non-excluded file writes newer than their last dream**. If a tick finds no qualifying users it logs a skip message to stdout and returns immediately — no LLM calls are made. When the agent runs but determines nothing needs merging, `files_touched` in `mx_dream_run` is `0` and no `dream-log.md` entry is written. The agent only writes to `dream-log.md` when it actually consolidates something, keeping user memory free of no-op noise.

The operator UX is available both via API and the admin Dreams panel:

| Endpoint                                   | Purpose                                                      |
| ------------------------------------------ | ------------------------------------------------------------ |
| `GET /v1/admin/dream/config`               | Read `dream_*` settings.                                     |
| `PUT /v1/admin/dream/config`               | Update cadence, grace period, write budget, and concurrency. |
| `GET /v1/admin/dream/users`                | List dream status, pause flags, errors, and run counts.      |
| `PUT /v1/admin/dream/users/:userId/paused` | Pause or resume dreaming for one user.                       |

Enable the scheduler with `MEMEX_DREAM_ENABLED=true`. The database `dream_enabled` key remains the runtime master switch.

See [Background Dreaming](/docs/operations/dreaming) for skip behavior, no-op runs, pause controls, and deployment guidance.

## Tool call flow [#tool-call-flow]

1. The AI model emits a tool call.
2. A framework adapter receives the call.
3. MemexAI validates the tool name, arguments, and context.
4. Virtual paths like `user/profile.md` are translated to physical paths like `users/user_123/profile.md`.
5. Reads and writes execute against Postgres.
6. Writes create revision snapshots, and reads/writes create access log entries.
7. The result returns to the model or application.

Every step after tool execution is shared by the containerized service, MCP, and in-process runtimes.


# MemexAI Docs (/docs)



MemexAI gives agents durable memory that can actually influence the next response. It stores memory as scoped Markdown-like files in Postgres, injects the right context through a prompt block, and gives teams revisions, access logs, search, and an admin UI.

## Start with the service [#start-with-the-service]

<Cards>
  <Card title="Recommended: Containerized service" href="/docs/quickstart/docker-service" description="Run MemexAI as a separate service, then connect over the TypeScript SDK, Python SDK, or MCP." />

  <Card title="Admin Console" href="/docs/operations/admin-console" description="Inspect memory files, revisions, access logs, observability, tool calls, and background dreaming." />

  <Card title="Advanced: Direct Postgres runtime" href="/docs/quickstart/direct-postgres" description="Skip the service only when your app intentionally owns database credentials." />
</Cards>

## How the two paths work [#how-the-two-paths-work]

### 1. Recommended: containerized service [#1-recommended-containerized-service]

Run the MemexAI service alongside Postgres. Your app never gets database credentials; it connects to the service over HTTP with the TypeScript or Python SDK, or through MCP over SSE/stdio.

Use this when you want a deployable memory service with API key auth and the admin UI built in.

### 2. Advanced: direct Postgres runtime [#2-advanced-direct-postgres-runtime]

Skip the MemexAI service container only when your JavaScript or Python app should own the Postgres connection directly. Your app imports the MemexAI runtime, passes a Postgres URL, runs migrations, and executes memory tools in-process.

Use this for embedded deployments, local experiments, or environments where sharing database credentials with the app is an intentional tradeoff.

## Two integration paths [#two-integration-paths]

### Agentic tools [#agentic-tools]

Use this for most assistants. The model gets two tools, and your system prompt gets the MemexAI prompt block.

```ts
const system = await memory.getSystemPrompt('You are a helpful assistant with durable user memory.')
const tools = memory.createAgenticToolset()
// memory_memorize, memory_search
```

Pass both `system` and `tools` into your model call. Tools store and retrieve memory; the prompt block is what makes stored memory available to the next answer.

### Raw tools [#raw-tools]

Use this when your agent or application should manage memory files directly.

```ts
const tools = memory.createRawToolset()
// memory_list, memory_read, memory_write, memory_patch, memory_smart_read
```

## Framework adapters [#framework-adapters]

Drop Memex into the framework you already use.

<Cards>
  <Card title="Vercel AI SDK" href="/docs/adapters/vercel-ai" description="Use memory tools with generateText and streamText in TypeScript." />

  <Card title="Anthropic SDK" href="/docs/adapters/anthropic" description="Integrate with claude-opus-4-7 and other Claude models via @memexai/core." />

  <Card title="LangChain" href="/docs/adapters/langchain" description="Add memory tools to LangChain agents in TypeScript or Python." />

  <Card title="OpenAI SDK" href="/docs/adapters/openai" description="Wire memory tool definitions into OpenAI chat completions calls." />

  <Card title="LlamaIndex" href="/docs/adapters/llamaindex" description="Use FunctionTool memory tools with LlamaIndex agents in Python." />

  <Card title="CrewAI" href="/docs/adapters/crewai" description="Add memory tools to CrewAI agents and crews in Python." />
</Cards>

## Shared memory can guide behavior [#shared-memory-can-guide-behavior]

User memory stores per-user facts, preferences, and project state. Shared memory stores global guidance that every agent can read, such as tool rules, product policies, escalation criteria, and evaluation rubrics.

<Cards>
  <Card title="How MemexAI works" href="/docs/concepts/how-it-works" description="Understand the loop from model tool call to memory files, prompt injection, revisions, and later recall." />

  <Card title="Memory tools" href="/docs/concepts/memory-tools" description="Choose between two agentic tools and the raw file-level tool set." />

  <Card title="Prompt block" href="/docs/concepts/prompt-block" description="Make stored memory part of the system prompt so the next response can change." />

  <Card title="Shared memory as behavior guide" href="/docs/concepts/shared-memory" description="Use shared memory files as durable tool guidance, policies, and behavior instructions for agents." />

  <Card title="Why memory evals matter" href="/blog/stop-running-evals-only-on-prompts" description="Evaluate the memory state and memory writes, not only the prompt text." />
</Cards>

## What MemexAI stores [#what-memexai-stores]

Memory lives in Postgres tables:

| Table           | Purpose                               |
| --------------- | ------------------------------------- |
| `mx_file`       | Current memory file contents          |
| `mx_revision`   | Full write snapshots for auditability |
| `mx_access_log` | Lightweight read/write activity       |
| `mx_migration`  | Applied schema migrations             |

Agents use virtual paths like `user/profile.md` and `shared/policy.md`. MemexAI translates those paths to physical database paths and enforces user isolation.

## Community / Support [#community--support]

Got a question, found a bug, or want to share how you're using MemexAI? [Join us on Slack →](https://join.slack.com/t/memexaispace/shared_invite/zt-3yy24alf6-t1wRQsErf09JViHww_qlGw)


# MCP Clients (/docs/mcp)



The MemexAI service exposes the same core tool engine over Model Context Protocol. REST and MCP share path validation, tool execution, revisions, and access logs.

## SSE transport [#sse-transport]

```txt
http://localhost:8080/v1/mcp/sse?userId=user_123&actor=claude&apiKey=dev-agent-key
```

`userId` defaults to `default`, and `actor` defaults to `mcp-client`.

The API key can be sent as:

* `Authorization: Bearer ...`
* `apiKey` query parameter
* `token` query parameter

Query auth exists for MCP clients that cannot set headers on SSE GET requests.

Messages for SSE sessions are posted back to:

```txt
http://localhost:8080/v1/mcp/messages?connectionId=...
```

## Stdio transport [#stdio-transport]

Build the service first:

```bash
bun run build:service
```

Then run the compiled service in stdio mode:

```bash
DATABASE_URL=postgresql://memexai:memexai@localhost:5433/memexai \
MEMEX_API_KEY=dev-agent-key \
node apps/service/dist/index.js --stdio --user-id user_123 --actor claude-desktop
```

## Exposed tools [#exposed-tools]

MCP clients can call the same memory tools as the REST and direct-mode APIs:

* `memory_memorize`
* `memory_search`
* `memory_list`
* `memory_read`
* `memory_write`
* `memory_patch`
* `memory_smart_read`


# Anthropic SDK (/docs/adapters/anthropic)



The Anthropic SDK adapter is available in `@memexai/core` for direct Postgres mode. It converts MemexAI tool definitions into the format the Anthropic API expects and provides a handler for executing tool use blocks.

## Before you start [#before-you-start]

* Use this page when your app runs [direct Postgres mode](/docs/architecture#advanced-direct-postgres-runtime-mode).
* Read [How MemexAI works](/docs/concepts/how-it-works) for the tool-call-to-Postgres flow.
* Read [Prompt block](/docs/concepts/prompt-block) to understand why memory must be included in the system prompt.
* Read [Memory tools](/docs/concepts/memory-tools) to choose agentic tools or raw file tools.
* Read [Memory scopes](/docs/concepts/scopes) before writing paths like `user/profile.md`.

## Install [#install]

```bash
npm install @memexai/core @anthropic-ai/sdk
```

## Usage [#usage]

```ts
import Anthropic from '@anthropic-ai/sdk'
import { createMemex } from '@memexai/core'
import { createAnthropicTools, handleAnthropicToolCall } from '@memexai/core/adapters/anthropic'

const anthropic = new Anthropic()
const memex = createMemex({ databaseUrl: process.env.DATABASE_URL! })
await memex.migrate()

const memory = memex.forUser({ userId: 'user_123', actor: 'assistant' })
const tools = createAnthropicTools(memory)
const system = await memory.getSystemPrompt('You are a helpful assistant with durable user memory.')

const messages: Anthropic.MessageParam[] = [
  { role: 'user', content: 'Remember that I prefer concise answers.' },
]

while (true) {
  const response = await anthropic.messages.create({
    model: 'claude-opus-4-7',
    max_tokens: 1024,
    system,
    tools,
    messages,
  })

  if (response.stop_reason === 'end_turn') {
    console.log(response.content)
    break
  }

  if (response.stop_reason === 'tool_use') {
    const toolResults: Anthropic.ToolResultBlockParam[] = []

    for (const block of response.content) {
      if (block.type !== 'tool_use') continue
      const result = await handleAnthropicToolCall(block.name, block.input, memory, undefined, block.id)
      toolResults.push({ type: 'tool_result', tool_use_id: block.id, content: JSON.stringify(result) })
    }

    messages.push({ role: 'assistant', content: response.content })
    messages.push({ role: 'user', content: toolResults })
  }
}

await memex.end()
```

## API reference [#api-reference]
