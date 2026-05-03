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

laborant@dev-machine:~$ kubectl create namespace cnai-lab
namespace/cnai-lab created
laborant@dev-machine:~$ 

laborant@dev-machine:~$ kubectl get ns
NAME                 STATUS   AGE
cnai-lab             Active   64s
default              Active   73m
kube-flannel         Active   73m
kube-node-lease      Active   73m
kube-public          Active   73m
kube-system          Active   73m
local-path-storage   Active   12m
laborant@dev-machine:~$ 

laborant@dev-machine:~$ kubectl config set-context --current --namespace=cnai-lab
Context "kubernetes-admin@kubernetes" modified.
laborant@dev-machine:~$ 

laborant@dev-machine:~$ kubectl get pods
NAME                          READY   STATUS    RESTARTS   AGE
claims-api-78ff646598-sfbxc   1/1     Running   0          42s
minio-65c6854779-cr5mj        1/1     Running   0          6m24s

laborant@dev-machine:~$ kubectl get svc
NAME         TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
claims-api   NodePort   10.111.208.84   <none>        8000:30800/TCP                  2m19s
minio        NodePort   10.105.225.56   <none>        9000:30900/TCP,9001:30901/TCP   8m1s
laborant@dev-machine:~$ 

laborant@dev-machine:~$ curl -s http://172.16.0.2:30800/
{"service":"claims-api","version":"0.1.0","bucket":"claims-fnol"}

laborant@dev-machine:~$ curl -s -X POST http://172.16.0.2:30800/bootstrap/storage
{"bucket":"claims-fnol","status":"created"}

laborant@dev-machine:~$ 

laborant@dev-machine:~$ curl -s -X POST http://172.16.0.2:30800/claims \
  -H 'Content-Type: application/json' \
  -d '{
    "policyNumber": "AUTO-123456",
    "claimant": {
      "fullName": "John Doe",
      "contactPhone": "+91-9876543210",
      "contactEmail": "john.doe@example.com"
    },
    "incident": {
      "incidentType": "MOTOR_COLLISION",
      "incidentDate": "2026-07-20T18:45:00Z",
      "location": {
        "city": "Visakhapatnam",
        "state": "Andhra Pradesh",
        "country": "IN"
      },
      "description": "Rear-ended at traffic signal, visible bumper damage."
    },
    "vehicle": {
      "registrationNumber": "AP31AB1234",
      "make": "Toyota",
      "model": "Corolla",
      "year": 2022
    },
    "channel": "WEB_PORTAL",
    "reportedAt": "2026-07-20T19:00:00Z"
  }'
{"claimId":"CLM-CE4434656358","status":"INTAKE_RECEIVED","createdAt":"2026-07-29T17:38:16.675831+00:00"}


laborant@dev-machine:~$ curl -s http://172.16.0.2:30800/claims/CLM-CE4434656358
{"claimId":"CLM-CE4434656358","status":"INTAKE_RECEIVED","createdAt":"2026-07-29T17:38:16.675831+00:00","policyNumber":"AUTO-123456","claimant":{"fullName":"John Doe","contactPhone":"+91-9876543210","contactEmail":"john.doe@example.com"},"incident":{"incidentType":"MOTOR_COLLISION","incidentDate":"2026-07-20T18:45:00+00:00","location":{"city":"Visakhapatnam","state":"Andhra Pradesh","country":"IN"},"description":"Rear-ended at traffic signal, visible bumper damage."},"vehicle":{"registrationNumber":"AP31AB1234","make":"Toyota","model":"Corolla","year":2022},"channel":"WEB_PORTAL","reportedAt":"2026-07-20T19:00:00+00:00","documents":[]}laborant@dev-machine:~$ 