laborant@dev-machine:~$ 

kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.35/deploy/local-path-storage.yaml

kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

kubectl get pods -n local-path-storage

kubectl get sc

namespace/local-path-storage created
serviceaccount/local-path-provisioner-service-account created
role.rbac.authorization.k8s.io/local-path-provisioner-role created
clusterrole.rbac.authorization.k8s.io/local-path-provisioner-role created
rolebinding.rbac.authorization.k8s.io/local-path-provisioner-bind created
clusterrolebinding.rbac.authorization.k8s.io/local-path-provisioner-bind created
deployment.apps/local-path-provisioner created
storageclass.storage.k8s.io/local-path created
configmap/local-path-config created
storageclass.storage.k8s.io/local-path patched

NAME                                      READY   STATUS              RESTARTS   AGE
local-path-provisioner-678c9d975f-76cqg   0/1     ContainerCreating   0          0s

NAME                   PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
local-path (default)   rancher.io/local-path   Delete          WaitForFirstConsumer   false                  0s

laborant@dev-machine:~$ 

laborant@dev-machine:~$ kubectl get pods -n local-path-storage
NAME                                      READY   STATUS    RESTARTS   AGE
local-path-provisioner-678c9d975f-76cqg   1/1     Running   0          3m9s
laborant@dev-machine:~$ 


laborant@dev-machine:~$ kubectl apply -f lp-test.yaml
persistentvolumeclaim/lp-test-pvc created
pod/lp-test-pod created
laborant@dev-machine:~$ kubectl get pvc,pv,pod
NAME                                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
persistentvolumeclaim/lp-test-pvc   Bound    pvc-ff73a10b-86a5-4d1e-a472-1bf3675b80bc   1Gi        RWO            local-path     <unset>                 29s

NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                 STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
persistentvolume/pvc-ff73a10b-86a5-4d1e-a472-1bf3675b80bc   1Gi        RWO            Delete           Bound    default/lp-test-pvc   local-path     <unset>                          22s

NAME              READY   STATUS    RESTARTS   AGE
pod/lp-test-pod   1/1     Running   0          29s
laborant@dev-machine:~$ 


laborant@dev-machine:~$ kubectl exec -it lp-test-pod -- cat /data/health.txt
local-path-ok
laborant@dev-machine:~$