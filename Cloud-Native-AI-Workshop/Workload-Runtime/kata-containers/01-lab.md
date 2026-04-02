## Lab 0 – Baseline: understand your current cluster and hardware

Goal: Verify that your 3‑node cluster and nodes can support Kata (KVM, VT‑x/AMD‑V, etc.) and get a mental map of what’s running where.  

**Concepts for this lab:**

- Kubernetes uses **containerd + runc** right now as your “normal” runtime. Kata will be added *alongside* this as an extra runtime, not a replacement.  

- Kata needs hardware virtualization (KVM) because each Kata pod will run inside a lightweight VM.  

### Step 0.1 – See your nodes clearly

From your admin machine:

```bash
kubectl get nodes -o wide
```

```bash
 root@dev-machine:workload-runtimes# kubectl get nodes -o wide
NAME        STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION    CONTAINER-RUNTIME
cplane-01   Ready    control-plane   49m   v1.36.0   172.16.0.2    <none>        Ubuntu 24.04.4 LTS   6.1.167 (amd64)   containerd://2.2.3
node-01     Ready    <none>          49m   v1.36.0   172.16.0.3    <none>        Ubuntu 24.04.4 LTS   6.1.167 (amd64)   containerd://2.2.3
node-02     Ready    <none>          49m   v1.36.0   172.16.0.4    <none>        Ubuntu 24.04.4 LTS   6.1.167 (amd64)   containerd://2.2.3
root@dev-machine:workload-runtimes# 
```
 

***

### Step 0.2 – Check virtualization support on one worker

SSH into one worker node (say `node-01`) and run:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
lsmod | grep kvm
```

```bash
root@node-01:laborant# egrep -c '(vmx|svm)' /proc/cpuinfo
lsmod | grep kvm
2
root@node-01:laborant
```

Interpretation:

- If the first command prints `0`, hardware virtualization is not exposed (we’d need to fix BIOS / nested virt).  
- The second should show `kvm_intel` or `kvm_amd` loaded.  

Run those two commands on one worker and tell me:

1) The `egrep` numeric output  
2) The `lsmod | grep kvm` lines  

 