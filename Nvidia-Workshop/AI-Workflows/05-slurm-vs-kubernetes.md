### Slurm vs. Kubernetes
* popular tools for managing large-scale computing tasks in AI environments.
**Slurm** and **Kubernetes** are both used in AI environments, but Slurm is a batch job scheduler for training/data-processing jobs, while Kubernetes is a container orchestrator for always‑on services and inference workloads.

#### Slurm
**Focus:** resource allocation and batch job management.
**​Used for:** HPC workloads, long‑running training jobs, and heavy data‑processing jobs.
**​Behavior:** jobs are submitted, queued, run to completion, then exit (e.g., a 10‑hour training run).

#### Kubernetes
**Focus:** container life‑cycle management (start, scale, heal, decommission containers).
​**Used for:** AI inference workloads, microservices, and sometimes data pipelines as services.
​**Behavior:** services are always‑on, auto‑scaled, and kept healthy to serve continuous traffic.