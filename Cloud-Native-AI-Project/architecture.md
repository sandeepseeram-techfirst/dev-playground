

### Training pipeline (Argo Workflows)
data-fetch -> train (K8s Job) -> push model to MinIO -> test inference -> done


### Supporting services (k8s): MinIO (object store), Argo Workflows (pipelines),
Prometheus+Grafana (observability). All run in k8s namespaces.