laborant@dev-machine:~$ kubectl cluster-info
Kubernetes control plane is running at https://172.16.0.2:6443
CoreDNS is running at https://172.16.0.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
laborant@dev-machine:~$ kubectl get nodes
NAME        STATUS   ROLES           AGE   VERSION
cplane-01   Ready    control-plane   64s   v1.36.1
node-01     Ready    <none>          52s   v1.36.1
node-02     Ready    <none>          53s   v1.36.1
laborant@dev-machine:~$
