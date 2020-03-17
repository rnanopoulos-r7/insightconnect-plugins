# Deployment 


### Minikube (local testing)

- [Install minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- Minikube run in a separate VM and it has no access to host Docker server and images.
  to push the image to Minikube Docker daemon, you need to point your docker/kubectl
  clients to the minikube's docker daemion and build it.
  ```bash
  eval $(minikube docker-env)
  ```
- build the image 
  ```bash
  make 
  ```
- docker vars cleanup 
  ```bash
  for E in $(minikube docker-env); do  EV=$(echo $E|egrep DOCKER|cut -d"=" -f1); unset $EV; done 
  ```
- apply the pod
  ```bash
  kubectl apply -f deployment/k8s/pod.yaml 
  ```  
- see the status
  ```bash
  
  kubectl get pods
  NAME     READY   STATUS    RESTARTS   AGE
  vulndb   1/1     Running   0          19m 
  
  kubectl logs vulndb
  [2020-03-12 16:36:12 +0000] [1] [INFO] Starting gunicorn 19.7.1
  [2020-03-12 16:36:12 +0000] [1] [INFO] Listening at: http://0.0.0.0:10001 (1)
  [2020-03-12 16:36:12 +0000] [1] [INFO] Using worker: threads
  [2020-03-12 16:36:12 +0000] [7] [INFO] Booting worker with pid: 7
  
  ```
- connect from localhost by forwarding the port
  ```bash
  kubectl port-forward vulndb 10001:10001
  Forwarding from 127.0.0.1:10001 -> 10001 
  Forwarding from [::1]:10001 -> 10001
  
  # make requests from another shell to http://localhost:10001
  Handling connection for 10001
  Handling connection for 10001
  ```
### Deployment management

- Deployment creates replicaset for high availability and manages
  rollout and rollback strategies.
- apply deployment to deploy
```bash
kubectl apply -f deployment/k8s/deploy.yaml
```

- to roll out new version update the `deployment/k8s/deploy.yaml` and re-apply
```yaml
      containers:
        - name: rapid7-vulndb
          image: rapid7/rapid7_vulndb:1.1.1 --> 2.0.0
          imagePullPolicy: IfNotPresent
```

- to rollback 
```mysql based
kubectl rollout undo deployment vulndb
```

- to track deployment status

```bash
kubectl describe deployments.apps vulndb
Name:                   vulndb
Namespace:              default
CreationTimestamp:      Fri, 13 Mar 2020 15:29:46 -0400
Labels:                 <none>
Annotations:            deployment.kubernetes.io/revision: 4
                        kubectl.kubernetes.io/last-applied-configuration:
                          {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{},"name":"vulndb","namespace":"default"},"spec":{"replicas":1,"sele...
Selector:               app=vulndb,type=plugin,vendor=rapid7
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  1 max unavailable, 1 max surge
Pod Template:
  Labels:  app=vulndb
           type=plugin
           vendor=rapid7
  Containers:
   rapid7-vulndb:
    Image:      rapid7/rapid7_vulndb:1.1.1
    Port:       10001/TCP
    Host Port:  0/TCP
    Args:
      http
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   vulndb-d845f74f6 (1/1 replicas created)
Events:
  Type    Reason             Age                From                   Message
  ----    ------             ----               ----                   -------
  Normal  ScalingReplicaSet  49m (x2 over 64m)  deployment-controller  Scaled up replica set vulndb-776557568f to 1
  Normal  ScalingReplicaSet  49m                deployment-controller  Scaled down replica set vulndb-d845f74f6 to 0
  Normal  ScalingReplicaSet  4s (x2 over 50m)   deployment-controller  Scaled up replica set vulndb-d845f74f6 to 1
  Normal  ScalingReplicaSet  4s (x2 over 50m)   deployment-controller  Scaled down replica set vulndb-776557568f to 0

```
- since deployment and pods are completely decoupled it `labels` 
  used as a mechanism to map deployment to pods that are going to
  be managed by the deployment. So we should pay close attention to
  the the values on pods and deployment and make sure they match
  
  ```yaml
   type: plugin
   app: vulndb
   vendor: rapid7
  ```
  
### Service management
- service allows to assign unique stable ip address to multiple
  pods managed by the same replicaset/deployment

- create service
```bash
kubectl apply -f deployment/k8s/service.yaml
```
- describe service

```bash
kubectl describe service vulndb
Name:              vulndb
Namespace:         default
Labels:            <none>
Annotations:       kubectl.kubernetes.io/last-applied-configuration:
                     {"apiVersion":"v1","kind":"Service","metadata":{"annotations":{},"name":"vulndb","namespace":"default"},"spec":{"ports":[{"port":80,"targe...
Selector:          app=vulndb,type=plugin,vendor=rapid7
Type:              ClusterIP
IP:                10.104.23.51
Port:              <unset>  80/TCP
TargetPort:        10001/TCP
Endpoints:         172.17.0.4:10001
Session Affinity:  None
Events:            <none>

```


- service injects env vars for each exposed service in the namespace

```bash
kubectl exec vulndb-d845f74f6-hrdf6 env|egrep VULNDB
VULNDB_PORT_80_TCP_PROTO=tcp
VULNDB_SERVICE_PORT=80
VULNDB_PORT=tcp://10.104.23.51:80
VULNDB_PORT_80_TCP_ADDR=10.104.23.51
VULNDB_PORT_80_TCP_PORT=80
VULNDB_SERVICE_HOST=10.104.23.51
VULNDB_PORT_80_TCP=tcp://10.104.23.51:80
```

- service makes the DNS record available for the service, 
for example for the service `rapid7-rapid7-vulndb-2-0-0` it creates following DNS record

```bash
kubectl exec -it vulndb-76ccc4877b-6fpqr nslookup 10.108.137.149
nslookup: can't resolve '(null)': Name does not resolve

Name:      10.108.137.149
Address 1: 10.108.137.149 rapid7-rapid7-vulndb-2-0-0.default.svc.cluster.local
```
