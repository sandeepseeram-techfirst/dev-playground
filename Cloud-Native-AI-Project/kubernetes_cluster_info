controlplane:~/cnai-project$ kubectl cluster-info
Kubernetes control plane is running at https://172.16.36.5:6443
CoreDNS is running at https://172.16.36.5:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.


controlplane:~/cnai-project$ kubectl get nodes
NAME           STATUS   ROLES           AGE     VERSION
controlplane   Ready    control-plane   2m28s   v1.34.0
node01         Ready    <none>          2m18s   v1.34.0


controlplane:~/cnai-project$ kubectl get pods --all-namespaces
NAMESPACE      NAME                                    READY   STATUS    RESTARTS   AGE
kube-flannel   kube-flannel-ds-bv5tc                   1/1     Running   0          2m25s
kube-flannel   kube-flannel-ds-dcz89                   1/1     Running   0          2m23s
kube-system    coredns-66bc5c9577-mgjxc                1/1     Running   0          2m24s
kube-system    coredns-66bc5c9577-z4mxm                1/1     Running   0          2m24s
kube-system    etcd-controlplane                       1/1     Running   0          2m30s
kube-system    hostpath-provisioner-6d757b8976-85fvw   1/1     Running   0          2m24s
kube-system    kube-apiserver-controlplane             1/1     Running   0          2m30s
kube-system    kube-controller-manager-controlplane    1/1     Running   0          2m30s
kube-system    kube-proxy-sfx58                        1/1     Running   0          2m25s
kube-system    kube-proxy-vlf5v                        1/1     Running   0          2m23s
kube-system    kube-scheduler-controlplane             1/1     Running   0          2m30s
kube-system    kubelet-csr-approver-5f5f49cd67-4fjzm   1/1     Running   0          2m24s
kube-system    kubelet-csr-approver-5f5f49cd67-zdwv8   1/1     Running   0          2m24s