###For this setup we require helm kubectl docker and minikube to be pre installed on our system.
###for creating minikube cluster

minikube start

###To check status of minikube cluster
minikube status

###First install rabbitmq using helm chart
helm install rabbitmq bitnami/rabbitmq

###Install matrics server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

###Install KEDA operator since rabbitmq is not a standard metric provided by kubernetes.
kubectl apply -f https://github.com/kedacore/keda/releases/latest/download/keda-operator.yaml

###Now deploy producer and consumer application
& minikube -p minikube docker-env --shell powershell | Invoke-Expression 
Note: (fow windows machine)
###First go to producer folder then run docker command to build producer docker image
docker build -t producer:latest .

###Now go to consumer folder then run docker command to build consumer docker image
docker build -t consumer:latest .

###Now deploy both deployments
kubectl apply -f deploy.yml

###Now deploy scaling object
kubectl apply -f scaledobject.yaml

