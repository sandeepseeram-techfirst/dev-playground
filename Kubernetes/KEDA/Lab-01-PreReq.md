### 0 — Prerequisites

1. kubectl access to the cluster (cluster admin for installing KEDA).

2. helm (v3) installed locally.

3. A container registry (if you build/push images). Alternatively use the sample images referenced below.

              (Optional) rabbitmqadmin or kubectl exec access to publish messages while testing.

If you’re on a managed cluster (GKE / AKS / EKS) you’re good. KEDA docs say Helm is the recommended installation path.