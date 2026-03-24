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

Example: support agent that can read a customer’s tickets and post to one Slack channel, but not manage org settings.


