### DGX Platform 
The NVIDIA DGX platform is a data center AI system built to run large‑scale training, inference, and analytics workloads.

#### What a DGX system is? 
DGX is a platform, i.e., a complete AI server/node, not just a GPU.
​It is designed for AI training, inference, and high‑throughput analytics in data centers.
​
**Example shown: DGX A100 system with:**

1. 8 NVIDIA A100 GPUs.

2. High‑speed interconnect between the GPUs.

3. 15 TB of NVMe SSD storage.

4. NVSwitch for intra‑node GPU communication.

5. Advanced cooling and power modules.
​
You can think of a DGX as a “ready‑made AI supercomputer in a box” that you rack and connect into your data center.

#### Primary use cases
DGX systems are used when you need heavy, multi‑GPU AI or HPC workloads:
​
**AI / ML training** 

Massive deep learning models (e.g., NLP, CV, speech).

Multi‑user, multi‑workload AI environments in one or more DGX nodes.
​
**AI inference at scale**

Serve many inference requests for NLP, computer vision, and speech models from the same DGX infrastructure.
​

High‑performance computing (HPC)

Scientific workloads.

Analytics workloads with very high throughput demands.
​

Federated learning deployments

Enterprise setups where training is distributed across sites but DGX nodes form the central high‑power training resource.
​

Cloud‑native/containerized AI

Run workloads in containers, orchestrated by cloud‑native tooling, on top of DGX nodes.
