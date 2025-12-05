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


### Key constraints for high‑density GPU deployments
When you deploy high‑density GPU workloads, three main constraints dominate design.
​
**Power capacity**

* Each rack has a maximum electrical capacity (kW per rack).

* GPU‑heavy racks can approach or exceed traditional per‑rack power limits.

* GPUs need high, consistent power delivery; brownouts or undersized feeds directly reduce performance or reliability.
​
**Cooling**

* Dense GPU clusters generate a lot of heat.

* Traditional data centers may not have enough cooling capacity per rack or per room.

* You must plan for advanced cooling (higher airflow, hot/cold aisles, liquid cooling, etc.) so cooling does not become the bottleneck.
​

**Physical space (floor space)**

* Even if you have enough power and cooling on paper, you still need physical room for racks and their airflow envelopes.

* Space constraints can cap how many GPU nodes you can deploy, limiting cluster scale.

### Power Usage Effectiveness