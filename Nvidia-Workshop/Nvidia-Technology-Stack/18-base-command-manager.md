### Base Command Manager [BCM] 

Base Command Manager (BCM) is a licensed, enterprise‑grade cluster and workload management system for NVIDIA‑based AI infrastructure, acting as a central “command center” for both resources and jobs across data centers and clouds.

#### Purpose and scope
BCM manages and monitors your entire AI infrastructure, not just individual GPUs or nodes.
​* It covers both resources (GPUs, CPUs, networking, storage) and workloads (jobs, clusters, user quotas, performance).
​* It targets data centers and large clusters (edge, on‑prem, multi‑cloud, hybrid), and is often overkill for very small deployments.

#### Licensing and deployment model
BCM is a separate NVIDIA product; it requires an enterprise license and is not included for free with drivers.
​* It has multiple components to deploy and needs a dedicated management node, which collects data from all other nodes and presents it in dashboards and APIs.
​* Deployment is more complex than tools like nvidia-smi or DCGM and is intended for serious, large‑scale environments.

**[Management Node]**
   - Base Command Manager services
   - Web UI + REST API
   - Integrations (Prometheus/Grafana, Slurm, Kubernetes, Run:AI)

**[Cluster Nodes]**
   - GPU servers
   - DCGM, drivers, agents exporting metrics to BCM

**[BCM Web UI sections]**
- Clusters: utilization, health, size
- Devices: GPUs, CPUs, DPUs, switches
- Networking: links, health
- Storage: NFS/Lustre/NVMe metrics
- Jobs: status, performance, resource usage
- Users: quotas, consumption
