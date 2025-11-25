## Programming Kubernetes 
- This workshop notes is about writing software that directly talks to and extends Kubernetes. 
Kubernetes is written in Go. 

#### Types of Apps on K8S

Apps running on Kubernetes   
 1. COTS apps         
 2. Bespoke apps      
 3. K8s-native 

#### Ways to Extend Kubernetes (Extension Patterns)

Kubernetes is designed to be extensible.

- **Cloud providers**
    - Historically in-tree code in the controller manager.
    - Now support out-of-tree via a `cloud-controller-manager`.
    - Allows integration with cloud-specific:
        - Load balancers
        - VMs
        - Other infra primitives
- **kubelet binary plugins**
    - Network plugins (e.g., CNI implementations)
    - Device plugins (e.g., GPUs)
    - Storage plugins
    - Container runtime plugins (CRI integrations)
- **kubectl plugins**
    - Extend the `kubectl` CLI with custom subcommands.
- **API server access extensions**
    - Dynamic admission control via webhooks.
    - Used for validation/mutation of objects on create/update.
- **Custom resources and controllers**
    - CRDs (CustomResourceDefinitions) plus controllers.
- **Custom API servers**
    - Secondary API servers aggregated under Kubernetes’ main API.
    - Used for more advanced scenarios (e.g., dedicated APIs backed by non-etcd stores).
- **Scheduler extensions**
    - E.g., a scheduler extender via webhooks to influence placement decisions.
- **Authentication webhooks**
    - Integrate custom auth systems.
