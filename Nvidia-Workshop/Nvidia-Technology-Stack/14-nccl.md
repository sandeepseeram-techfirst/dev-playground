### NVIDIA Collective Communications Library (NCCL)
NCCL is a multi‑GPU communication library that automatically chooses and optimizes how GPUs talk to each other (within a node or across nodes) using NVLink, NVSwitch, PCIe, or RDMA, exposing simple collective APIs like all‑reduce and broadcast.

* In real training/inference setups, multiple GPUs must exchange data: synchronize gradients, share parameters, or aggregate results.
​
* GPUs may be on the same host (connected by NVLink/NVSwitch/PCIe) or on different hosts (using RDMA over the network).
​
* Manually managing connections, choosing NVLink vs RDMA, opening/closing channels, and designing optimal communication patterns is complex and error‑prone.

#### What NCCL is and does? 
NVIDIA Collective Communications Library (NCCL) is a multi‑GPU communication library that abstracts and optimizes communication patterns across many GPUs.
​
Instead of you manually initiating and closing connections and picking transports, NCCL detects the available interconnects (NVLink, NVSwitch, PCIe, RDMA) and uses them to maximize bandwidth.
​
It hides communication complexity and provides high‑level collective operations such as:

**all_reduce**
**broadcast**
**all_gather**
**reduce_scatter**
