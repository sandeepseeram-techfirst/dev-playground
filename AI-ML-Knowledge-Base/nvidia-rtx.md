### Nvidia RTX

NVIDIA RTX is a class of NVIDIA GPUs and a whole platform that combines traditional CUDA cores with dedicated RT cores for ray tracing and Tensor Cores for AI, aimed at real‑time graphics and AI workloads on PCs and workstations. It powers things like realistic lighting in games, AI upscaling (DLSS), and local generative‑AI / LLM workloads on “RTX PCs.”

### What “RTX” actually is? 

* RTX is both a hardware family (GeForce RTX / RTX PRO / data‑center RTX) and a software platform (SDKs, drivers, APIs) for ray tracing and AI.

* RTX GPUs started with Turing and continue through Ampere, Ada Lovelace, and Blackwell architectures, each adding newer RT and Tensor Cores.

* On consumer PCs, “RTX AI PCs” just means Windows machines with GeForce RTX GPUs plus the NVIDIA AI software stack to run local AI apps and models.

### How RTX works under the hood? 

Inside an RTX GPU you effectively have three main hardware blocks working together:

**CUDA cores:** General‑purpose programmable shaders for classic rasterization and GPGPU compute (CUDA kernels, physics, etc.).

**RT cores:** Fixed‑function blocks that accelerate BVH traversal and ray–triangle intersection, which are the core operations for real‑time ray tracing.

**Tensor Cores:** Matrix‑math units optimized for mixed‑precision (FP16, INT8, FP8, etc.) operations, used to accelerate deep‑learning inference and AI‑based graphics like DLSS.