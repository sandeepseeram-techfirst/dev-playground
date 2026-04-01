root@dev-machine:workload-runtimes# **kubectl get nodes -o wide**
NAME        STATUS   ROLES           AGE     VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION    CONTAINER-RUNTIME
cplane-01   Ready    control-plane   4m8s    v1.36.0   172.16.0.2    <none>        Ubuntu 24.04.4 LTS   6.1.167 (amd64)   containerd://2.2.3
node-01     Ready    <none>          3m56s   v1.36.0   172.16.0.3    <none>        Ubuntu 24.04.4 LTS   6.1.167 (amd64)   containerd://2.2.3
node-02     Ready    <none>          3m56s   v1.36.0   172.16.0.4    <none>        Ubuntu 24.04.4 LTS   6.1.167 (amd64)   containerd://2.2.3

root@dev-machine:workload-runtimes# **kubectl get nodes -o custom-columns=NODE:.metadata.name,RUNTIME:.status.nodeInfo.containerRuntimeVersion**
NODE        RUNTIME
cplane-01   containerd://2.2.3
node-01     containerd://2.2.3
node-02     containerd://2.2.3
root@dev-machine:workload-runtimes#

**containerd is the standard, supported runtime for modern Kubernetes and is widely used in production clusters, including for GPU‑heavy workloads.**

