### AI Centric Data Center 
An AI‑centric data center has the same basic blocks as a traditional one, but they are stressed much harder by GPU‑heavy AI workloads, so design and constraints change noticeably.

Core building blocks inside an AI data center
Think of four fundamental pillars you must design for:
​
**Compute nodes**

Servers (often GPU‑enabled) that train models and run inference.

Single server is not enough for large models; you typically deploy many nodes in parallel clusters.
​

**Network**

High‑speed links so compute nodes can talk to each other and coordinate parallel training.

Critical for synchronizing model parameters and moving training data between nodes.
​

**Storage**

Holds training data (existing datasets) and newly generated data (logs, checkpoints, results).

Must deliver high throughput to keep GPUs fed with data.
​

**Support infrastructure**

Power delivery, cooling systems, physical security, and facility services that keep everything running.


### What makes it AI‑centric (vs traditional)
Traditional data center: Often CPU‑centric, mixed enterprise workloads, moderate power and cooling density.

AI‑centric data center:
1. High‑density GPU racks.

2. Very power‑hungry and heat‑intensive workloads.

3. Needs higher bandwidth network and storage to keep accelerators utilized.
​
So the basic components are familiar, but their capacity and constraints are very different.