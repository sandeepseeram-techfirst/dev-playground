### NVLink
NVLink is NVIDIA’s high‑speed interconnect that creates a direct, fast “express highway” between GPUs (and sometimes between CPU and GPU), instead of forcing all traffic through the slower, shared PCIe bus.

#### What NVLink is (definition and components)
NVLink is a high‑speed, wire‑based interconnect for:
GPU ↔ GPU communication.
GPU ↔ CPU communication (in some systems).
​
It is both:

**Hardware:** physical links/bridges or embedded NVLink chips/traces.

**Software:** protocols, drivers, and memory‑pooling logic to manage data transfer and shared memory across GPUs.
​
Effect: Faster, more efficient data transfer and memory sharing between GPUs than standard PCIe, especially when many GPUs are present.

#### Issues 
* PCIe can become a bottleneck if multiple GPUs and devices share the bus.
​* Latency and bandwidth are not optimal for heavy inter‑GPU communication (e.g., large‑model training).

