### Networking
Inside an AI‑centric data center, network architecture is split into multiple specialized networks **(fabrics)** to handle different kinds of traffic efficiently, reliably, and securely.

#### NVIDIA’s four network fabrics
NVIDIA defines four key fabrics inside an AI‑centric data center:
​
**Compute Network**
Carries application traffic between compute nodes (servers/GPUs) running AI workloads.
**Used for:** model training communication, parameter exchange, distributed compute coordination.
This is the main “conversation channel” for machines doing calculations and sharing results.​

**Storage network**
Dedicated network that connects compute nodes to storage systems so all nodes can access large datasets without bottlenecks.
**Goal:** high throughput, predictable performance, so GPUs never starve for data.
**Flow:** Compute node → Storage fabric → Data lakes / NAS / object stores, and back, at high speed.
​
**In‑band management network**
“Configuration/operations” network inside the running infrastructure. Used when the OS on servers is up and reachable.

**Typical uses:**
1. OS and application updates.
2. Configuration changes.
3. Monitoring agents sending metrics/logs.
4. Separation from compute/storage keeps management tools from competing with application traffic.
​

**Out‑of‑band (OOB) management network**
Used when the OS is down or crashed and traditional remote access (RDP, SSH, etc.) does not work. Relies on the BMC (Baseboard Management Controller) on each server.
​
Through BMC, you can:

1. Power cycle the server.

2. View console output.

3. Monitor hardware status and logs.

Purpose: remote control and recovery even if the server OS is dead or powered off.

#### Network Fabrics 

**Compute fabric:** east–west traffic among AI servers (training/inference clusters).

**Storage fabric:** compute‑to‑storage high‑bandwidth lanes.

**In‑band management fabric:** config/monitoring traffic while OS is healthy.

**Out‑of‑band management fabric:** hardware‑level access via BMC when OS is not responding.

### Compute Network Fabric
GPU‑to‑GPU communication within a node and across nodes. Backbone for training and inference jobs in distributed AI clusters.
**Implementation** - Built using high‑speed interconnects such as InfiniBand or NVIDIA’s NVLink/NVSwitch‑based fabrics.

