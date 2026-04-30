### Cloud Native AI - Workshop 

Cloud Native AI (CNAI) is the application of cloud‑native principles—containers, Kubernetes, microservices, declarative APIs, and automation—to the full lifecycle of AI/ML workloads so they can be portable, scalable, and operable across modern cloud environments.

AI stack — data pipelines, training, inference, feature stores, observability—is built on containers, Kubernetes, microservices, immutable infrastructure, and declarative APIs rather than monolithic, tightly coupled systems.

## Core Domains inside Cloud Native AI
  
## 1. Infrastructure & Orchestration for AI Workloads

This domain covers how you provision, schedule, and run AI workloads on cloud‑native infrastructure. Typical components include container runtimes, Kubernetes clusters (possibly GPU‑aware), service meshes, and declarative IaC (Terraform, Crossplane, etc.) to encode infrastructure as code. 

AI workloads—data processing, training, and inference—are packaged as containers and orchestrated by Kubernetes or similar platforms so they can scale horizontally and be rescheduled across nodes and clouds as needed. This domain also includes GPU scheduling, node pools for different workload classes, and multi‑cluster/multi‑cloud federation to avoid lock‑in and create failure‑domain isolation. 

## 2. AI/ML Pipeline & Workflow Automation

CNAI emphasizes repeatable pipelines for data ingestion, feature engineering, training, evaluation, and deployment, implemented as containerized workflows. Tools like Kubernetes operators, workflow engines, and CI/CD systems orchestrate these pipelines using declarative specs and GitOps, so changes to models and data flows are versioned and automatically rolled out. 

This domain includes automation around dataset versioning, experiment tracking, model registry integration, and promotion of models from staging to production through automated quality gates. The focus is on making ML lifecycle steps cloud‑native: composable, observable, and easy to roll back or scale. 

## 3. Model Serving, Inference, and Microservices

In CNAI, inference is exposed as microservices—HTTP/gRPC endpoints, streaming processors, or event‑driven functions—rather than embedded in monoliths. Each serving component (e.g., feature retrieval, pre‑processing, model scoring, post‑processing) can be its own microservice, enabling independent scaling and deployment. 

Containers provide portability, so the same model server image can run on different clouds, on‑prem clusters, or at the edge. Service meshes and API gateways handle traffic management, retries, rate limiting, and security policy enforcement around these AI microservices. 

## 4. Data & Storage for AI, Cloud‑Native Style

CNAI assumes data and storage are themselves cloud‑native, with object storage, distributed filesystems, and specialized databases (including vector stores) integrated with container orchestration. AI‑native storage platforms increasingly embed intelligence, such as self‑optimization and autonomous scaling based on workload patterns, directly into the cloud‑native storage layer. 

This domain covers data locality for training and inference, dynamic volume provisioning via CSI, policy‑based data governance across hybrid/multicloud, and use of registries and artifact stores for datasets and models. It also includes edge data handling, where AI logic is pushed closer to where data is generated to meet latency requirements. 
## 5. Observability, Reliability, and Governance for AI Systems

Cloud‑native AI systems rely heavily on observability tooling—metrics, logs, traces—and on ML‑specific monitoring like drift detection, performance tracking, and model health. CNAI extends traditional SRE practices with AI‑aware signals, integrating runtime metrics, data quality alerts, and inference‑level SLIs/SLOs into platform dashboards and alerting. 

Governance domain includes policy‑based automation for compliance, security, and cost controls across hybrid multicloud environments running AI workloads. This often uses declarative policies enforced by controllers and AI‑driven analysis of infrastructure telemetry to anticipate failures or violations. 

## 6. Edge and Hybrid/Multicloud AI

Cloud‑native AI architectures commonly extend from central clusters to edge locations and multiple cloud providers. Edge intelligence processes data locally in containerized AI services to meet latency and bandwidth constraints, while central systems orchestrate and govern these distributed workloads. 

Hybrid and multicloud CNAI solutions use the same container and orchestration stack across providers so AI workloads can be placed where GPU capacity, data locality, or regulatory requirements dictate. This matches your cloud‑agnostic preference: the emphasis is on portability and repeatable deployment patterns rather than any single provider’s managed AI suite. 