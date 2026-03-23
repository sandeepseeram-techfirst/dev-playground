### Agent Authorization and Authentication 

For agentic AI, authentication and authorization look like a layered version of normal API security: humans/auth backends get tokens, and agents are given scoped, delegated tokens to call tools and APIs on their behalf.

### Core concepts

**Authentication:** Prove who is acting (user, service, or agent runtime) using OAuth/OIDC, API keys, JWTs, or managed identities.

**Authorization:** Decide what that identity is allowed to do, at what time and in what context, usually via scopes, RBAC/ABAC, or fine‑grained policy engines.

In an agentic system, the “identity” is often not just a human or app, but also the agent instance as a non‑human identity with its own permissions and logs.