### Data Center GPU Manager [DCGM]

DCGM is a cluster‑level GPU monitoring and management platform for NVIDIA data centers, providing health, diagnostics, policies, and metric export for many GPUs and nodes.

#### What DCGM is for? 
DCGM = Data Center GPU Manager, designed for enterprise‑scale GPU health monitoring and diagnostics.
​* It works across multi‑node GPU clusters, supports continuous monitoring, and has alerting capabilities.
​* It focuses on monitoring + configuration/policies, not on job scheduling.

#### Installation and runtime model

DCGM is not installed by default; you must install it separately (from NVIDIA or cloud vendor docs).
* ​You download and install the DCGM package, then run it as a service/daemon on the node.
​* It can be installed directly or via GPU operator in Kubernetes‑style environments.

#### Metric export and integration (Prometheus/Grafana)
1. DCGM itself is the monitoring/control engine; DCGM Exporter is a separate package to expose metrics via HTTP.
​2. DCGM Exporter runs as an agent on each node, scraping DCGM and exposing metrics for tools like Prometheus and Grafana.

