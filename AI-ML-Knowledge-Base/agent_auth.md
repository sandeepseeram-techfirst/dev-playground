### Agent Authorization and Authentication 

For agentic AI, authentication and authorization look like a layered version of normal API security: humans/auth backends get tokens, and agents are given scoped, delegated tokens to call tools and APIs on their behalf.

### Core concepts

**Authentication:** Prove who is acting (user, service, or agent runtime) using OAuth/OIDC, API keys, JWTs, or managed identities.

**Authorization:** Decide what that identity is allowed to do, at what time and in what context, usually via scopes, RBAC/ABAC, or fine‑grained policy engines.

In an agentic system, the “identity” is often not just a human or app, but also the agent instance as a non‑human identity with its own permissions and logs.

### Service-to-service (agent on its own behalf)
Use API keys, client credentials, or JWTs when the agent is acting as a system, not tied to a specific human.

**Example:** analytics agent pulling internal metrics with a pre‑issued service token.


### Delegated user access (agent on behalf of a user)
Use OAuth/OIDC tokens that represent a specific human and are delegated to the agent with limited scopes and expiry.

**Example:** support agent that can read a customer’s tickets and post to one Slack channel, but not manage org settings.

### Capability / tool tokens
Some designs issue per‑tool capability tokens that say “this agent can call Tool A with operations X, Y, Z.”

The agent is stateless regarding long‑term credentials; a broker or gateway hands it short‑lived tool tokens.

### Human‑in‑the‑loop
Human‑in‑the‑loop is increasingly common: for high‑risk actions (delete, wire transfer, production changes), the agent pauses and requests human approval, often via inline approve/deny UX or time‑boxed holds. 

### Where OAuth/OIDC and gateways fit 

1. OAuth/OIDC remain the base standard for delegating access from users to agents and from agents to APIs.

2. LLM gateways (TrueFoundry, Gravitee, etc.) centralize model and tool access: agents authenticate to the gateway, and the gateway manages provider keys, rotation, and access control.

3. Specialist tools (Auth0, Aembit, Nango, etc.) add agent‑aware token brokering, ensuring agents never touch raw API credentials and only get scoped tokens.