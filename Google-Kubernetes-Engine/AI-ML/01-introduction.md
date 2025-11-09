### AI/ML on GKE 

1. Serving Large Language Models (LLMs) efficiently on Google Kubernetes Engine (GKE) requires understanding various architectural patterns and optimization strategies. 

2. Deploying LLMs in production isn't just about running a model. it's about balancing performance, cost, scalability, and reliability. Different models have different requirements: a 2B parameter model can run on a single GPU, while a 70B parameter model needs multiple GPUs working together.

Similarly, some workloads need low latency for real-time applications, while others prioritize throughput for batch processing.

### Single GPU Serving Pattern
The simplest LLM serving pattern uses a single GPU per model instance. This approach is ideal for smaller models (typically under 10B parameters) or when you need to deploy multiple independent model instances.
