# W3-4 Lab (ClusterIP & NodePort):

For this lab we will demonstrate ClusterIP and NodePort and how these 2 services work.

We will also use the concepts of PV and PVCs to create volumes for our pods.

Here is a diagram:

![Lab Diagram](W3-4LabPicture.png)

## How to setup:

Set up docker install

```
docker build . -t <dockerusername>/flaskapp-frontend-w3-4:latest
```

Set up a private hub repository:

```
docker push <dockerusername>/flaskapp-frontend-w3-4:latest
```

Create a data directory in W3-4Notes Directory for mounting of PV:

```
mkdir data
```

Update the hostPath in the PV.YAML to match the file in your folder:

```
/run/desktop/mnt/host/<WSL-file-path-to-data-directory>
```

Run the yaml files:

```
kubectl apply -f Kubernetes/
```

## Connecting to flaskapp on NodePort:

```
curl http://localhost:30000
```

## Connecting to flaskapp2 on ClusterIP from flaskapp:

```
kubectl exec -it flaskapp-pod -- curl cluster-ip-service-to-flaskapp2:81
```
