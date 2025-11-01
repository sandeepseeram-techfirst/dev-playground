# Building Generative AI Services with FastAPI.

### Architecture

flowchart TD
    A[Client apps<br/>(web / mobile / other services)]
    B[FastAPI service]
    C[Responses returned to the client]

    A --> B --> C

    subgraph FastAPI Service Responsibilities
        B1[Handles routes and requests]
        B2[Enforces authentication and authorization]
        B3[Talks to a database<br/>for user data, prompts, configs, logs]
        B4[Calls generative AI models<br/>(local or cloud APIs)]
    end

    B --> B1
    B --> B2
    B --> B3
    B --> B4
