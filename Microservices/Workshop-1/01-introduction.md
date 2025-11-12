### Building production-ready microservices using Spring Boot and Spring Cloud. 

### What is a microservice?

Microservice architecture = decomposing a monolith into a set of cooperating autonomous components to get:

- Faster development and continuous deployment. 
- Easier manual or automatic scaling.

A microservice is an **autonomous software component** that is independently upgradeable, replaceable, and scalable, with these properties:

- Shared-nothing data: no shared database tables between services.
- Communication via stable, versioned, well-documented interfaces (APIs or messages), preferably asynchronous.
- Deployed as separate runtime processes (e.g., separate Docker containers).
- Instances are stateless so any instance can serve any request.

This allows deploying many small services on multiple smaller servers instead of a single big machine, scaling only the hot services, and upgrading one service without touching the rest.

**Rule-of-thumb service size:** small enough for one developer to keep in their head; large enough to avoid serious latency and consistency problems when data relationships span multiple services.