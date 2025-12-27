### GPU Virtualization 
GPU virtualization lets multiple virtual machines (VMs) share one physical GPU, similar to how CPU virtualization lets multiple VMs share physical CPUs. This improves utilization, reduces hardware cost, and allows flexible scaling in data centers.

#### GPU Virtualization Concept
* If a physical server also has a GPU, that GPU can be virtualized by the hypervisor.
​* Once virtualized, the GPU is presented to VMs as a virtual GPU (vGPU).
​
Any OS and application running inside the VM can now use this virtual GPU as if it were its own GPU.


