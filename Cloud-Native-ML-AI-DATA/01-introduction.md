# Cloud Native ML-AI-DATA 

Cloud-Native AI/ML/Data refers to designing, developing, deploying, and operating AI and ML systems natively on the cloud, using cloud-native principles such as:

1. Containerization (Docker)

2. Orchestration (Kubernetes)

3. Microservices Architecture

4. Serverless computing

5. Managed data and AI services

6. Automation & scalability

Instead of running ML models on-premise or static VMs, you build end-to-end pipelines that are scalable, portable, and automated — fully integrated with the cloud ecosystem (e.g., GCP, AWS, Azure).



| Stage                     | What Happens                                      | Cloud-Native Implementation                                   |
| ------------------------- | ------------------------------------------------- | ------------------------------------------------------------- |
| **1. Data Ingestion**     | Gather data from sources (IoT, apps, logs, etc.)  | Cloud Pub/Sub, Kafka, AWS Kinesis, Azure Event Hub            |
| **2. Data Storage**       | Store structured/unstructured data                | Cloud Storage, BigQuery, S3, Azure Data Lake                  |
| **3. Data Processing**    | Clean, transform, and enrich data                 | Dataflow, Databricks, Glue, Spark on Kubernetes               |
| **4. Model Training**     | Train ML models using cloud GPU/TPU/CPU           | Vertex AI, SageMaker, Azure ML, Kubeflow, Ray                 |
| **5. Model Deployment**   | Deploy as scalable microservices                  | KServe, Seldon Core, Vertex AI Prediction, SageMaker Endpoint |
| **6. MLOps / Monitoring** | Automate CI/CD, model versioning, drift detection | MLflow, TFX, Kubeflow Pipelines, Prometheus, Grafana          |
