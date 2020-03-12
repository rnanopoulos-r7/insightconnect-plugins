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
