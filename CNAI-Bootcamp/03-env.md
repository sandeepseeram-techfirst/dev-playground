#### laborant@dev-machine:~$ kubectl cluster-info
Kubernetes control plane is running at https://172.16.0.2:6443
CoreDNS is running at https://172.16.0.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

#### laborant@dev-machine:~$ kubectl get nodes
NAME        STATUS   ROLES           AGE   VERSION
cplane-01   Ready    control-plane   64s   v1.36.1
node-01     Ready    <none>          52s   v1.36.1
node-02     Ready    <none>          53s   v1.36.1
laborant@dev-machine:~$

#### laborant@dev-machine:~$ kubectl describe node node-01 
Name:               node-01
Roles:              <none>
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=node-01
                    kubernetes.io/os=linux
Annotations:        flannel.alpha.coreos.com/backend-data: {"VNI":1,"VtepMAC":"02:94:6e:69:dd:57"}
                    flannel.alpha.coreos.com/backend-type: vxlan
                    flannel.alpha.coreos.com/kube-subnet-manager: true
                    flannel.alpha.coreos.com/public-ip: 172.16.0.3
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Wed, 29 Jul 2026 15:52:54 +0000
Taints:             <none>
Unschedulable:      false
Lease:
  HolderIdentity:  node-01
  AcquireTime:     <unset>
  RenewTime:       Wed, 29 Jul 2026 15:55:17 +0000
Conditions:
  Type                 Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----                 ------  -----------------                 ------------------                ------                       -------
  NetworkUnavailable   False   Wed, 29 Jul 2026 15:53:07 +0000   Wed, 29 Jul 2026 15:53:07 +0000   FlannelIsUp                  Flannel is running on this node
  MemoryPressure       False   Wed, 29 Jul 2026 15:53:24 +0000   Wed, 29 Jul 2026 15:52:54 +0000   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure         False   Wed, 29 Jul 2026 15:53:24 +0000   Wed, 29 Jul 2026 15:52:54 +0000   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure          False   Wed, 29 Jul 2026 15:53:24 +0000   Wed, 29 Jul 2026 15:52:54 +0000   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready                True    Wed, 29 Jul 2026 15:53:24 +0000   Wed, 29 Jul 2026 15:53:05 +0000   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  172.16.0.3
  Hostname:    node-01
Capacity:
  cpu:                2
  ephemeral-storage:  30876796Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3806072Ki
  pods:               110
Allocatable:
  cpu:                2
  ephemeral-storage:  28456055147
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3703672Ki
  pods:               110
System Info:
  Machine ID:                 dc1ed267bcc84ff8b4a8dd4ed2284fe0
  System UUID:                dc1ed267bcc84ff8b4a8dd4ed2284fe0
  Boot ID:                    e5d64e5d-6d98-4fdf-a126-d5c71be1ecc2
  Kernel Version:             6.1.167
  OS Image:                   Ubuntu 24.04.4 LTS
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  containerd://2.2.4
  Kubelet Version:            v1.36.1
PodCIDR:                      10.244.2.0/24
PodCIDRs:                     10.244.2.0/24
Non-terminated Pods:          (2 in total)
  Namespace                   Name                     CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                     ------------  ----------  ---------------  -------------  ---
  kube-flannel                kube-flannel-ds-pnwcq    100m (5%)     0 (0%)      50Mi (1%)        0 (0%)         2m32s
  kube-system                 kube-proxy-4d9hs         0 (0%)        0 (0%)      0 (0%)           0 (0%)         2m32s
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests   Limits
  --------           --------   ------
  cpu                100m (5%)  0 (0%)
  memory             50Mi (1%)  0 (0%)
  ephemeral-storage  0 (0%)     0 (0%)
  hugepages-1Gi      0 (0%)     0 (0%)
  hugepages-2Mi      0 (0%)     0 (0%)
Events:
  Type    Reason                Age    From             Message
  ----    ------                ----   ----             -------
  Normal  CIDRAssignmentFailed  2m32s  cidrAllocator    Node node-01 status is now: CIDRAssignmentFailed
  Normal  RegisteredNode        2m30s  node-controller  Node node-01 event: Registered Node node-01 in Controller

#### laborant@dev-machine:~$ kubectl describe node node-02 && kubectl describe node cplane-01 && kubectl get sc && kubectl get pods -A
Name:               node-02
Roles:              <none>
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=node-02
                    kubernetes.io/os=linux
Annotations:        flannel.alpha.coreos.com/backend-data: {"VNI":1,"VtepMAC":"a6:00:c1:30:84:b3"}
                    flannel.alpha.coreos.com/backend-type: vxlan
                    flannel.alpha.coreos.com/kube-subnet-manager: true
                    flannel.alpha.coreos.com/public-ip: 172.16.0.4
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Wed, 29 Jul 2026 15:52:53 +0000
Taints:             <none>
Unschedulable:      false
Lease:
  HolderIdentity:  node-02
  AcquireTime:     <unset>
  RenewTime:       Wed, 29 Jul 2026 16:08:13 +0000
Conditions:
  Type                 Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----                 ------  -----------------                 ------------------                ------                       -------
  NetworkUnavailable   False   Wed, 29 Jul 2026 15:53:04 +0000   Wed, 29 Jul 2026 15:53:04 +0000   FlannelIsUp                  Flannel is running on this node
  MemoryPressure       False   Wed, 29 Jul 2026 16:04:16 +0000   Wed, 29 Jul 2026 15:52:53 +0000   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure         False   Wed, 29 Jul 2026 16:04:16 +0000   Wed, 29 Jul 2026 15:52:53 +0000   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure          False   Wed, 29 Jul 2026 16:04:16 +0000   Wed, 29 Jul 2026 15:52:53 +0000   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready                True    Wed, 29 Jul 2026 16:04:16 +0000   Wed, 29 Jul 2026 15:53:02 +0000   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  172.16.0.4
  Hostname:    node-02
Capacity:
  cpu:                2
  ephemeral-storage:  30876796Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3806072Ki
  pods:               110
Allocatable:
  cpu:                2
  ephemeral-storage:  28456055147
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3703672Ki
  pods:               110
System Info:
  Machine ID:                 99e888e702fc4764b150ebb480ac57c9
  System UUID:                99e888e702fc4764b150ebb480ac57c9
  Boot ID:                    1a72cb4c-7ac8-40c6-855a-351de2a86897
  Kernel Version:             6.1.167
  OS Image:                   Ubuntu 24.04.4 LTS
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  containerd://2.2.4
  Kubelet Version:            v1.36.1
PodCIDR:                      10.244.1.0/24
PodCIDRs:                     10.244.1.0/24
Non-terminated Pods:          (2 in total)
  Namespace                   Name                     CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                     ------------  ----------  ---------------  -------------  ---
  kube-flannel                kube-flannel-ds-lmdxm    100m (5%)     0 (0%)      50Mi (1%)        0 (0%)         15m
  kube-system                 kube-proxy-5w7xd         0 (0%)        0 (0%)      0 (0%)           0 (0%)         15m
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests   Limits
  --------           --------   ------
  cpu                100m (5%)  0 (0%)
  memory             50Mi (1%)  0 (0%)
  ephemeral-storage  0 (0%)     0 (0%)
  hugepages-1Gi      0 (0%)     0 (0%)
  hugepages-2Mi      0 (0%)     0 (0%)
Events:
  Type    Reason          Age   From             Message
  ----    ------          ----  ----             -------
  Normal  RegisteredNode  15m   node-controller  Node node-02 event: Registered Node node-02 in Controller
Name:               cplane-01
Roles:              control-plane
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=cplane-01
                    kubernetes.io/os=linux
                    node-role.kubernetes.io/control-plane=
                    node.kubernetes.io/exclude-from-external-load-balancers=
Annotations:        flannel.alpha.coreos.com/backend-data: {"VNI":1,"VtepMAC":"26:f0:50:9d:af:48"}
                    flannel.alpha.coreos.com/backend-type: vxlan
                    flannel.alpha.coreos.com/kube-subnet-manager: true
                    flannel.alpha.coreos.com/public-ip: 172.16.0.2
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Wed, 29 Jul 2026 15:52:42 +0000
Taints:             <none>
Unschedulable:      false
Lease:
  HolderIdentity:  cplane-01
  AcquireTime:     <unset>
  RenewTime:       Wed, 29 Jul 2026 16:08:11 +0000
Conditions:
  Type                 Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----                 ------  -----------------                 ------------------                ------                       -------
  NetworkUnavailable   False   Wed, 29 Jul 2026 15:53:02 +0000   Wed, 29 Jul 2026 15:53:02 +0000   FlannelIsUp                  Flannel is running on this node
  MemoryPressure       False   Wed, 29 Jul 2026 16:04:08 +0000   Wed, 29 Jul 2026 15:52:41 +0000   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure         False   Wed, 29 Jul 2026 16:04:08 +0000   Wed, 29 Jul 2026 15:52:41 +0000   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure          False   Wed, 29 Jul 2026 16:04:08 +0000   Wed, 29 Jul 2026 15:52:41 +0000   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready                True    Wed, 29 Jul 2026 16:04:08 +0000   Wed, 29 Jul 2026 15:53:00 +0000   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  172.16.0.2
  Hostname:    cplane-01
Capacity:
  cpu:                4
  ephemeral-storage:  30876796Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3805600Ki
  pods:               110
Allocatable:
  cpu:                4
  ephemeral-storage:  28456055147
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3703200Ki
  pods:               110
System Info:
  Machine ID:                 857b094a3d3d48578a56a86f1e8e140b
  System UUID:                857b094a3d3d48578a56a86f1e8e140b
  Boot ID:                    28951848-a23d-41c7-ac82-f87220106e54
  Kernel Version:             6.1.167
  OS Image:                   Ubuntu 24.04.4 LTS
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  containerd://2.2.4
  Kubelet Version:            v1.36.1
PodCIDR:                      10.244.0.0/24
PodCIDRs:                     10.244.0.0/24
Non-terminated Pods:          (8 in total)
  Namespace                   Name                                 CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                 ------------  ----------  ---------------  -------------  ---
  kube-flannel                kube-flannel-ds-sz65l                100m (2%)     0 (0%)      50Mi (1%)        0 (0%)         15m
  kube-system                 coredns-589f44dc88-4tbql             100m (2%)     0 (0%)      70Mi (1%)        170Mi (4%)     15m
  kube-system                 coredns-589f44dc88-hjqzw             100m (2%)     0 (0%)      70Mi (1%)        170Mi (4%)     15m
  kube-system                 etcd-cplane-01                       100m (2%)     0 (0%)      100Mi (2%)       0 (0%)         15m
  kube-system                 kube-apiserver-cplane-01             250m (6%)     0 (0%)      0 (0%)           0 (0%)         15m
  kube-system                 kube-controller-manager-cplane-01    200m (5%)     0 (0%)      0 (0%)           0 (0%)         15m
  kube-system                 kube-proxy-rn9wv                     0 (0%)        0 (0%)      0 (0%)           0 (0%)         15m
  kube-system                 kube-scheduler-cplane-01             100m (2%)     0 (0%)      0 (0%)           0 (0%)         15m
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests    Limits
  --------           --------    ------
  cpu                950m (23%)  0 (0%)
  memory             290Mi (8%)  340Mi (9%)
  ephemeral-storage  0 (0%)      0 (0%)
  hugepages-1Gi      0 (0%)      0 (0%)
  hugepages-2Mi      0 (0%)      0 (0%)
Events:
  Type    Reason          Age   From             Message
  ----    ------          ----  ----             -------
  Normal  RegisteredNode  15m   node-controller  Node cplane-01 event: Registered Node cplane-01 in Controller
 
NAMESPACE      NAME                                READY   STATUS    RESTARTS   AGE
kube-flannel   kube-flannel-ds-lmdxm               1/1     Running   0          15m
kube-flannel   kube-flannel-ds-pnwcq               1/1     Running   0          15m
kube-flannel   kube-flannel-ds-sz65l               1/1     Running   0          15m
kube-system    coredns-589f44dc88-4tbql            1/1     Running   0          15m
kube-system    coredns-589f44dc88-hjqzw            1/1     Running   0          15m
kube-system    etcd-cplane-01                      1/1     Running   0          15m
kube-system    kube-apiserver-cplane-01            1/1     Running   0          15m
kube-system    kube-controller-manager-cplane-01   1/1     Running   0          15m
kube-system    kube-proxy-4d9hs                    1/1     Running   0          15m
kube-system    kube-proxy-5w7xd                    1/1     Running   0          15m
kube-system    kube-proxy-rn9wv                    1/1     Running   0          15m
kube-system    kube-scheduler-cplane-01            1/1     Running   0          15m
laborant@dev-machine:~$