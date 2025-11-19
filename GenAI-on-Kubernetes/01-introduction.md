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

### **Challenges running GenAI at scale**

1. **Model size & resources**
    - Models have billions of parameters, requiring huge GPU memory and storage (tens to hundreds of GB per model).
    - Infrastructure must dynamically allocate CPU, GPU, RAM, and storage so performance and reliability are preserved under variable load.
2. **Startup time & latency**
    - Long **warm‑up**: loading weights into memory and optimizing for inference takes much longer than starting a typical web app.
    - High **per‑request latency**: text is generated token‑by‑token, so responses are slower than simple REST calls.
    - Requires orchestration + techniques like **semantic caching** and **routing** to keep apps responsive.
3. **Hardware & scalability**
    - Heavy dependence on **GPUs** (and evolving GPU types) for both inference and tuning.
    - Need advanced orchestration to:
        - Allocate GPUs correctly across nodes.
        - Scale services while mixing models with different GPU requirements.
4. **Security & data privacy**
    - Models may be trained on or process sensitive data, so you need multi‑layer security:
        - Secure data pipelines.
        - Network boundaries and RBAC. 
        - Protection against model/API misuse.

## Tokens, prompts, and embeddings

### Tokenization

Naive word‑level vocabularies break on unknown words and explode in size, so modern LLMs use **subword tokenization**:

- Text is split into smaller units (tokens) like “regular” + “ization” instead of “regularization” as a single word.
- The same sentence may become a different token sequence for different models because tokenizers are **model‑specific**.

**Prompt → tokens visualization**

- Input string → tokenizer → `[token_1, token_2, ... token_n]` (integers mapped from a fixed vocabulary).

### Prompt structure and system prompts

- A **prompt** is the full request sent to an LLM, including user text and optional system instructions.
- A **system prompt** sets behavior, examples:
    - “You are a friendly AI assistant named John…” (assistant persona).
    - “Please summarize the following text in ≤500 words…” (summarization task).
- Changing the prompt to steer output is **prompt engineering**.
- The tokenizer preserves sentence structure via special tokens for start/end and punctuation, because structure affects meaning.

### How tokens map to words

- Each sentence element (word) maps to one or more tokens to keep vocabulary size fixed.
- Example:
    - `tall` → `[tall]`
    - `taller` → `[tall, er]`
    - `tallest` → `[tall, est]`
- Some tokens are **special** (end‑of‑text, system prompt boundaries, etc.).

### Tokenizer implementation

- A tokenizer is an algorithm: sentence in → sequence of token IDs out; each ID has a reversible mapping back to its text piece.
- Production tokenizers include normalization, language‑specific rules (e.g., for languages without spaces), and high‑performance implementations.
- Hugging Face’s `tokenizers` library is a common choice.
- You must use the **same tokenizer** at inference that was used in training, or token IDs will not match the model’s embedding layer.

### Embeddings 

Once you have token IDs, you need **embeddings**:

- Embedding maps each token ID to a dense vector capturing semantic meaning.
- Semantically similar tokens (e.g., “dog” and “puppy”) end up with embedding vectors that are close; dissimilar ones (e.g., “dog” and “car”) are far apart.
- The embedding matrix is **learned during training**, while the token vocabulary stays fixed.
- As the model processes a sequence, static token embeddings become **contextual** representations that depend on neighboring tokens.
- Embeddings are not limited to text—they can represent images, video, and audio for multimodal models.

### Tokens and cost

Most managed LLM services price by **tokens**, not words:

- Rough rule of thumb: in English, ≈4 characters ≈ 1 token (only an approximation).
- Tokenization is model‑specific, so the same text may yield different token counts for different models.
- Both **input and output tokens** are billed, and you cannot predict exactly how many output tokens will be generated; you only control a maximum.