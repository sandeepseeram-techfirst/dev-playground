### Skills vs. other Claude Code features

**CLAUDE.md, subagents, hooks, and MCP servers.**

**Key takeaways** 

1. CLAUDE.md loads into every conversation and is best for always-on project standards. 

2. Skills load on demand and are best for task-specific expertise. 

3. Subagents run in isolated execution contexts — use them for delegated work. Skills add knowledge to your current conversation.

4. Hooks are event-driven (fire on file saves, tool calls). Skills are request-driven (activate based on what you're asking)

5. MCP servers provide external tools and integrations — a different category entirely from skills

Each feature handles its own specialty — combine them rather than forcing everything into one approach

### Putting It All Together
A typical setup might include:

1. CLAUDE.md — always-on project standards
2. Skills — task-specific expertise that loads on demand
3. Hooks — automated operations triggered by events
4. Subagents — isolated execution contexts for delegated work
5. MCP servers — external tools and integrations