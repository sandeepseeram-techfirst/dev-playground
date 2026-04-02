## Lab 3 – Install Kata via kata‑deploy DaemonSet

Goal: Actually drop Kata binaries + hypervisor on each node using the `kata-deploy` DaemonSet. 
Concepts for this step:

- `kata-deploy` runs a privileged pod on each node and installs Kata into `/opt/kata` (or similar), then labels the node as Kata‑ready.  
- Once this finishes successfully, we’ll be able to see Kata node labels and later tie them to a RuntimeClass.

### Command to install kata‑deploy

Run this from `dev-machine`:

```bash
kubectl apply -f \
  https://raw.githubusercontent.com/kata-containers/packaging/master/kata-deploy/kata-deploy/base/kata-deploy.yaml
```

Then watch the DaemonSet pods:

```bash
kubectl -n kube-system get pods -l name=kata-deploy
```

Give it ~30–60 seconds and then:

```bash
kubectl -n kube-system get pods -l name=kata-deploy -o wide
```

