### GPU Virtualization 
GPU virtualization lets multiple virtual machines (VMs) share one physical GPU, similar to how CPU virtualization lets multiple VMs share physical CPUs. This improves utilization, reduces hardware cost, and allows flexible scaling in data centers.

#### GPU Virtualization Concept
* If a physical server also has a GPU, that GPU can be virtualized by the hypervisor.
​* Once virtualized, the GPU is presented to VMs as a virtual GPU (vGPU).
​
Any OS and application running inside the VM can now use this virtual GPU as if it were its own GPU.

**Pass‑through:** one physical GPU given directly to one VM → near‑native performance.
​**Shared vGPU:** one GPU divided across multiple VMs → performance varies based on slice size, contention, and implementation.

### GPU Virtualization Methods

**vGPU (virtual GPU)**
**MIG (Multi‑Instance GPU)**

**vGPU** = software slicing via hypervisor, many vGPUs (up to 64), good when you already use VMs heavily.
​
**MIG** = hardware slicing directly in the GPU, fewer but strongly isolated instances (up to 7), ideal for containerized AI workloads on bare‑metal Linux.

These mechanisms implement the actual “slicing” of a physical GPU into multiple isolated virtual GPUs with different performance and capacity characteristics.

#### MIG (Multi‑Instance GPU): hardware‑level isolation

**What MIG is?**
MIG = Multi‑Instance GPU, a hardware‑level isolation mechanism.
​Instead of a hypervisor doing the slicing, the GPU itself is partitioned into multiple hardware instances.
​
Each instance has its own GPU compute resources and GPU memory block.


