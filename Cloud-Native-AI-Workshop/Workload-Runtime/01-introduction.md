### Workload Runtime

**Workload Runtime** refers to the low‑level runtime that actually executes your workloads (containers, VMs, sandboxed processes, Wasm) on the nodes in your cluster, underneath Kubernetes or any higher‑level orchestrator. It works as the component that the scheduler talks to for starting, stopping, isolating, and securing workloads, often via the Kubernetes Container Runtime Interface (CRI) or similar APIs.

#### Conceptual Layering

1. Control plane / orchestrator (Kubernetes, Kueue, Ray operators, Slurm, etc.) decides what to run, where, and with which resources.

2. Workload runtime on each node is the local component that actually runs the workload (container, VM, sandbox, Wasm module) according to that decision.

3. Accelerator, storage, CNI, etc. plug into or sit beside the runtime to provide GPUs, volumes, and networking for those workloads.

So “Workload Runtime” here is not a scheduler, not an AI framework—it’s the **execution engine.**

### How a Workload Runtime Works (Mechanics)
Concretely, in a K8s‑like environment:

**Kubelet (or similar agent) receives a Pod spec**

1. The scheduler assigns a Pod to a node; kubelet on that node calls the configured runtime (e.g., containerd, CRI‑O) via CRI.

2. Runtime prepares and launches the workload

3. Pulls images or artifacts (container image, VM image, Wasm module, Singularity image, etc.).

4. Sets up namespaces, cgroups, seccomp/AppArmor profiles, mounts, and network interfaces according to config.

5. Invokes a lower‑level runtime (e.g., runc, Kata shim, Firecracker microVM, gVisor sandbox, WasmEdge VM) to actually create the process/VM/Wasm instance.

6. Runtime manages lifecycle and isolation

7. Start/stop/restart based on kubelet commands, health checks, and liveness/readiness probes.

8. Enforces resource limits (CPU, memory, possibly GPU via device plugins), cgroup constraints, and security context (privileged, user, capabilities).

9. Reporting and metrics

10. Reports container state back to kubelet (Running, Terminated, etc.).

11. Often integrates with node‑level logging and metrics collectors used by observability tools listed elsewhere in the landscape (Prometheus, OpenTelemetry, etc.).

For AI workloads this is still the same story; you’re just running GPU‑bound processes instead of generic app containers.