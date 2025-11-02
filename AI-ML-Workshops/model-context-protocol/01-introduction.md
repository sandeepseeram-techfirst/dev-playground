### Model Context Protocol 
The Model Context Protocol (MCP) establishes a standard interface for connecting AI assistants to data systems.

### Big picture of MCP

- MCP defines a standard way for an AI assistant to talk to a **host**, and for that host to talk to one or more **servers** that expose data and actions.
- Communication follows a **Client–Host–Server** architecture and uses **JSON‑RPC** messages over transports like stdio or Server‑Sent Events (SSE).
- Servers expose three core primitives to the LLM: **Resources** (readable data), **Prompts** (reusable prompt templates), and **Tools** (callable actions, often hitting APIs or databases).