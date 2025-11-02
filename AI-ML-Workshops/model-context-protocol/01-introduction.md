### Model Context Protocol 
The Model Context Protocol (MCP) establishes a standard interface for connecting AI assistants to data systems.

### Big picture of MCP

- MCP defines a standard way for an AI assistant to talk to a **host**, and for that host to talk to one or more **servers** that expose data and actions.
- Communication follows a **Client–Host–Server** architecture and uses **JSON‑RPC** messages over transports like stdio or Server‑Sent Events (SSE).
- Servers expose three core primitives to the LLM: **Resources** (readable data), **Prompts** (reusable prompt templates), and **Tools** (callable actions, often hitting APIs or databases).

### Architecture diagram (text visualization)
Think of the flow like this:
- LLM Client (e.g., Claude Desktop) ⇄ Host (plugin / bridge) ⇄ MCP Server (your code exposing resources/tools).
- Messages are JSON‑RPC requests/responses flowing both ways, wrapped by the chosen transport (stdio or SSE).

### MCP 

- Why MCP exists: to avoid building separate custom connectors for every LLM + data source combination by standardizing how data providers talk to LLM clients.
- That there are three main roles: Client, Host, and Server, each with clear responsibilities.
​- That MCP uses JSON‑RPC 2.0 for all requests, responses, and notifications.
​- That communication can run over stdio (local processes) or SSE (HTTP streaming), and you must pick based on your deployment.
​- That there is an initial capabilities negotiation handshake when a connection starts. 
