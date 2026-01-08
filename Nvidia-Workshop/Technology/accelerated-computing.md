### Accelerated Computing
Accelerated computing is a style of computing where specialized processors (like GPUs, TPUs, FPGAs or other accelerators) work alongside CPUs to offload and dramatically speed up the most compute‑intensive parts of applications using parallel processing.

**Core idea**
Traditional CPUs execute most work serially, excelling at control flow and general-purpose logic but becoming a bottleneck on highly math- or data‑parallel workloads.

Accelerated computing separates out the data‑intensive kernels (matrix multiplies, simulations, graphics, signal processing, etc.) and runs them on accelerators designed for massive parallelism, while the CPU handles orchestration and sequential tasks.

In a GPU‑accelerated AI workload, the CPU reads data, manages the training loop, and issues high‑level commands, while the GPU executes the core tensor operations (matrix multiplies, convolutions) on thousands of elements at once; this heterogeneous model is the essence of accelerated computing.