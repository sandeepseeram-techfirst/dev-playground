# Gen AI on Kubernetes 
Implementation of enterprise-grade composite GenAI solutions on Kubernetes.

### Microservices: Flexible and Scalable Architecture
The GenAI Microservices describes a suite of microservices, each microservice is designed to perform a specific function or task within the application architecture. By breaking down the system into these smaller, self-contained services, microservices promote modularity, flexibility, and scalability.

#### We are now in an era where AI algorithms and models!!!

Recently, the practices for developing AI solutions have undergone significant transformation. Instead of considering AI model (e.g., a GenAI LLM) as the complete solution, these models are now being integrated into more comprehensive end-to-end AI solutions. These solutions consist of multiple components, including retrieval subsystems with embedding agents, a Vector Database for efficient storage and retrieval, and prompt engines, among others. 

This shift has led to the emergence of Composition Frameworks (such as LangChain or Haystack), which are used to assemble these components into end-to-end GenAI flows, like RAG solutions, for the development and deployment of AI solutions.

The ecosystem offers a range of composition frameworks, some are open-source (e.g., LangChain and LlamaIndex), while others are closed-sourced and come bundled with professional services (e.g., ScaleAI). Additionally, some are offered by cloud service providers (e.g. AWS) or hardware/software providers (e.g., NVIDIA).  


#### GenAI models – 
Large Language Models (LLMs), Large Vision Models (LVMs), multimodal models, etc.

#### Other modules - 
AI system components (other than LLM/LVM models) including Ingest/Data Processing module, Embedding Models/Services, Vector 

#### Databases - 
(aka Indexing or Graph data stores), Prompt Engines, Memory systems, etc.


#### Audience 
MLOps Engineers, Platform/Kubernetes Engineers, and Architects who deploy, scale, observe, and secure LLM services at scale.


### What’s special about LLM workloads?

- Very large models: multi‑GB weights, long init times, complex memory footprints.
- Specialized hardware: high‑performance GPUs, possibly multi‑GPU per Pod.
- Varied data paths:
    - Inference usually sees small prompts;
    - RAG and batch jobs may read large corpora or process big batches.
- Scheduling pressure: GPUs are scarce and expensive, so scheduling must be aware of GPU topology and utilization.

### **High‑level Solution Diagram:**

1. **Platform layer:** Kubernetes cluster, node pools (CPU/GPU), storage, CNI, ingress.
2. **ML/AI services:**
    - Model servers (e.g., vLLM) as Deployments.
    - Tuning/training Jobs on GPU nodes.
    - Vector DB, feature stores, message queues.
3. **Application layer:**
    - Microservices calling LLM APIs.
    - RAG/agent orchestrators.
    - Frontends (web/chat) and external integrations.