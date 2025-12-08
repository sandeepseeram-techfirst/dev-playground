### Compute Power 

What “compute” means here
- Compute is the processing power that runs AI workloads.
- ​Historically this meant CPU (central processing unit), but an AI‑centric data center today is incomplete without GPU (graphics processing unit).

**Compute layer** = CPU + GPU (now heavily GPU‑weighted for AI).

**Above it:** AI workloads (training, inference).

**Below it:** Power, cooling, and physical infrastructure.


### CUDA 
**2006: NVIDIA released CUDA (Compute Unified Device Architecture)**
1. CUDA let developers program GPUs for general purpose computing, not only graphics pipelines.
2. ​This opened GPUs to broader workloads: numerical computing, simulations, and eventually ML/DL.

**CPU: orchestration, sequential logic.**

**GPU: massively parallel numeric workloads (matrix multiplications, convolutions) → ideal for ML/DL training.**


#### Why GPUs matter in AI‑centric data centers? 
GPUs can run thousands of operations in parallel, which matches the math of neural networks (matrix/vector ops).
​
**In AI‑centric data centers:**

1. Compute ≈ “how many and what kind of GPUs (plus CPUs) you have.”

2. The rest of the architecture (network, storage, power, cooling) must be sized so these GPUs stay fully utilized.

### CPU vs GPU 
Mapped to compute:

**CPU:** Few, very powerful cores, excellent for diverse, complex, general‑purpose tasks.

**GPU:** Many simpler cores, excellent for massively parallel tasks where many similar operations are done at once.

#### Number and type of cores

**CPU**
1. Few cores (dual‑core, quad‑core, etc.).
​2. Each core is very powerful and optimized for complex, branching logic and general‑purpose computing (OS, applications).

**GPU**
1. Many cores: hundreds to thousands; a typical modern NVIDIA GPU may have 5,000–10,000 cores.
​

Cores are simpler and specialized for doing the same kind of operation repeatedly across large datasets.
