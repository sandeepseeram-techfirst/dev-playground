# Model Context Protocol (MCP)
Large language models (LLMs) are powerful, but they have two major limitations: their knowledge is frozen at the time of their training, and they can't interact with the outside world. 

- This means they can't access real-time data or perform actions like booking a meeting or updating a customer record. 

The Model Context Protocol (MCP) is an open standard designed to solve this. Introduced by Anthropic in November 2024, MCP provides a secure and standardized "language" for LLMs to communicate with external data, applications, and services. It acts as a bridge, allowing AI to move beyond static knowledge and become a dynamic agent that can retrieve current information and take action, making it more accurate, useful, and automated.


* "The MCP creates a standardized, two-way connection for AI applications, allowing LLMs to easily connect with various data sources and tools. MCP builds on existing concepts like tool use and function calling but standardizes them. This reduces the need for custom connections for each new AI model and external system. It enables LLMs to use current, real-world data, perform actions, and access specialized features not included in their original training." 

### MCP Architecture and Components 

### MCP host
The LLM is contained within the MCP host, an AI application or environment such as an AI-powered IDE or conversational AI. This is typically the user's interaction point, where the MCP host uses the LLM to process requests that may require external data or tools.

### MCP client
The MCP client, located within the MCP host, helps the LLM and MCP server communicate with each other. It translates the LLM's requests for the MCP and converts the MCP's replies for the LLM. It also finds and uses available MCP servers.

* MCP server
The MCP server is the external service that provides context, data, or capabilities to the LLM. It helps LLMs by connecting to external systems like databases and web services, translating their responses into a format the LLM can understand which helps developers provide diverse functionalities.

* Transport layer
The transport layer uses JSON-RPC 2.0 messages to communicate between the client and server, mainly through two transport methods:

- Standard input/output (stdio): Works well for local resources, offering fast, synchronous message transmission
- Server-sent events (SSE): Preferred for remote resources, allowing efficient, real-time data streaming