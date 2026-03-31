### KubeEdge 

**Kubernetes Native Edge Computing Framework** 

KubeEdge is an open source system for extending native containerized application orchestration capabilities to hosts at Edge. It is built upon kubernetes and provides fundamental infrastructure support for network, application deployment and metadata synchronization between cloud and edge. 

### High-level architecture
KubeEdge has two main parts: a cloud side and an edge side, connected over a bidirectional, message-based channel.

Cloud side (in your Kubernetes cluster):

* Runs standard Kubernetes control plane.

* Adds KubeEdge cloud components that sync metadata and manage edge nodes.

Edge side (on gateways, boxes, or even small ARM devices):

Runs a lightweight agent that:

* Talks to the cloud.

* Runs containers (via container runtime, usually containerd).

* Manages local devices and executes logic even when disconnected.

#### Key properties:

Uses Kubernetes-native APIs at the edge, so apps and controllers that depend on the Kubernetes API can run there.

* Supports x86, ARMv7, ARMv8 to run on a variety of edge hardware.

* Optimized footprint (tens of MBs) for constrained edge nodes.

