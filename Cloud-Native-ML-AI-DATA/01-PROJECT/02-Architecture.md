  ┌────────────┐        ┌────────────┐        ┌──────────────┐
  │ Synthetic  │  ->    │  Kafka     │  ->    │ Spark (Job)  │
  │ Producer   │        │ (Strimzi)  │        │ (Spark-Op)   │
  └────────────┘        └────────────┘        └──────┬───────┘
                                                       │ writes parquet
                                                       ▼
                                                   ┌─────────┐
                                                   │ MinIO   │  <-- object store for parquet/artifacts
                                                   └─────────┘
                                                       ▲
                                                       │
                                    ┌──────────┐       │            ┌───────────┐
                                    │ Trino    │ <-- query parquet  │ Feast     │  <-- feature store (MinIO + Redis)
                                    └──────────┘                    └───────────┘
                                                       │
                                                       ▼
                                                  ┌───────── ┐
                                                  │ Argo /   │  <-- orchestrates pipeline steps
                                                  │ Workflows│
                                                  └───────── ┘
                                                       │
                                                   train container
                                                       ▼
                                                  ┌─────────┐
                                                  │ MLflow  │  <-- experiment tracking & model registry
                                                  └─────────┘
                                                       │
                                                       ▼
                                                  ┌─────────┐
                                                  │ Katib   │  <-- hyperparameter tuning
                                                  └─────────┘
                                                       │
                                                       ▼
                                                  ┌─────────┐
                                                  │ KServe  │  <-- model serving / inference
                                                  └─────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────-┐
                                              │ Prometheus /     │
                                              │ Grafana (metrics)│
                                              └─────────────────-┘
