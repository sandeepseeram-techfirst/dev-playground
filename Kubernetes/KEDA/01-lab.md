# KEDA (Kubernetes Event-Driven Autoscaler)

## Concepts

### KEDA Operator: 
Controller that watches ScaledObject / ScaledJob CRDs and runs scalers to compute desired replica counts; it creates/updates an HPA behind the scenes. 

### Scaler: 
Plugin that reads an external metric (e.g., RabbitMQ queue length, Prometheus query, Azure Queue, AWS SQS etc.) and reports metric values to KEDA. KEDA ships many scalers (RabbitMQ, Prometheus, Kafka, HTTP, Cron, etc.). 

### ScaledObject: 
CRD that ties a Kubernetes workload (Deployment/StatefulSet/CustomResource) to one or more scalers and contains scaling rules. KEDA will create an HPA for the target resource. 

### ScaledJob: 
like ScaledObject but for running jobs (batch work) — KEDA will create Jobs rather than scale long-running pods. 

### Scale-to-zero: 
KEDA can scale a Deployment down to 0 replicas when no events are present (great for intermittent workloads).  