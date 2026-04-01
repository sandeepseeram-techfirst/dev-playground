### Workload Runtime

**Workload Runtime** refers to the low‑level runtime that actually executes your workloads (containers, VMs, sandboxed processes, Wasm) on the nodes in your cluster, underneath Kubernetes or any higher‑level orchestrator. It works as the component that the scheduler talks to for starting, stopping, isolating, and securing workloads, often via the Kubernetes Container Runtime Interface (CRI) or similar APIs.

#### Conceptual Layering

1. Control plane / orchestrator (Kubernetes, Kueue, Ray operators, Slurm, etc.) decides what to run, where, and with which resources.

2. Workload runtime on each node is the local component that actually runs the workload (container, VM, sandbox, Wasm module) according to that decision.

3. Accelerator, storage, CNI, etc. plug into or sit beside the runtime to provide GPUs, volumes, and networking for those workloads.

