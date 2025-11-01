# Building Generative AI Services with FastAPI.

### Architecture

Client apps (web/mobile/other services)
↓
FastAPI service

 - Handles routes and requests
 - Enforces authentication and authorization
 - Talks to a database for storing user data, prompts, configs, logs

Calls generative AI models (local or cloud APIs)
↓
Responses returned to the client