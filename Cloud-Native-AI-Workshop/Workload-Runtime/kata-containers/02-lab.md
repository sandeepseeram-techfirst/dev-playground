## Lab 1 – Install Kata on the cluster (but in two tiny steps)

We’ll use the official `kata-deploy` DaemonSet, which is the recommended way to add Kata to an existing “vanilla” Kubernetes cluster.  
This installs Kata binaries + hypervisor on each node and labels nodes that are ready.

### Step 1.1 – Apply RBAC for kata-deploy

From your `dev-machine` (where `kubectl` is configured):

```bash
kubectl apply -f \
  https://raw.githubusercontent.com/kata-containers/kata-containers/main/tools/packaging/kata-deploy/kata-rbac/base/kata-rbac.yaml
```

This just creates the service account / roles that the DaemonSet will use.  

```bash
 root@dev-machine:workload-runtimes# kubectl apply -f \
  https://raw.githubusercontent.com/kata-containers/packaging/master/kata-deploy/kata-rbac/base/kata-rbac.yaml
serviceaccount/kata-label-node created
clusterrole.rbac.authorization.k8s.io/node-labeler created
clusterrolebinding.rbac.authorization.k8s.io/kata-label-node-rb created
root@dev-machine:workload-runtimes# 
```

```bash
kubectl get sa -n kube-system | grep kata || echo "no kata SA yet?"
```

