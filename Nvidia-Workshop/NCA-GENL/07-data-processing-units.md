### Data Processing Units [DPU] 
A Data Processing Unit (DPU) is a specialized processor that offloads data‑centric and infrastructure tasks (network, storage, security) from CPUs and GPUs so they can focus on application and math work.

#### What a DPU actually does? 
DPU = specialized processor for data‑centric tasks in an AI data center.
​
Main offloaded domains:

**Networking**
​
1. Packet creation and processing.

2. Load balancing.

3. Overlay/underlay networking.

4. RDMA (Remote Direct Memory Access) operations.

**Storage**

​1. Compression and decompression.

2. Encryption and decryption.

3. Deduplication.

**Security**
​
1. Firewall and packet inspection.

2. IPsec / TLS offload.

3. Multi‑tenant isolation.

4. Zero‑trust policy enforcement.


#### Architecture 

**CPU:** Application logic, OS, decision flows.

**GPU:** Parallel math for AI training/inference.

**DPU:** Network, storage, security, and infrastructure offload (data movement + control).