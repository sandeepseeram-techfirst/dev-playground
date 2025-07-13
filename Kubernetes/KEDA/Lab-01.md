## Hands-on lab: end-to-end example (RabbitMQ → workers autoscaled by KEDA)

### Goal: 
Deploy RabbitMQ in-cluster, a worker consumer app that pulls messages from a queue, and a ScaledObject that makes Kubernetes scale workers based on queue length (scale out when backlog exists; scale down to zero when empty).

Works on any Kubernetes cluster (minikube, microk8s, EKS, GKE, AKS) with kubectl and helm configured.