# Week 1 - 2

* **Hands-On** : Set up a local Kubernetes cluster using Minikube or Kind (Kubernetes in Docker).

## Kubernetes Components

### Pods

A Pod is a group of one or more containers that share the same storage and network resources and instructions to run the containers.
A Pod can contain one or more init containers which are initial containers that are run first before application containers.

#### Notes regarding Init containers:
* Init containers always run to completeion.
* They must be completed sequentially.
* If an Init container fails, kubelet repeatedly restarts that init container until it is completed. This can be overwritten to treat the pod as failed if the Pod has a ```restartPolicy``` of never.

### Nodes
* Nodes are a virtual or physical machine that uses a control plane and contains the services needed to run Pods.
* Components on a node inclue kubelet, container runtime, and kube-proxy.
* Nodes also contains a status with following information: Addresses, Conditions, Metadata on Node such as CPU, memory, and number of pods.
* The naming for the nodes has to be unique in relation to other nodes.

### kubelet
* Node Agent that runs a node.
* To use a kublet, it needs a YAML or JSON object to describe the pod.

#### To add a Node to the API server
* Kubelet on a node self-registers to the control-plane.
* User manually add a Node object.

### kube-apiserver
* This process is using REST operations to validate & configure data api objects such as pods, services, etc.
* The API server is used to act as an entrypoint for Kubernetes control plane.

### etcd
* Used to store key values for cluster data.

### Controllers for kube-controller-manager
* They are a control loop that watches the shared state of the cluster thought kube-apiserver. It also updates the changes to the state to push it towards the desired state. 
* Examples are namespace controller, endpoints controller.

### Control Plane
* Container orchestration layer that uses the kube-apiserver and other interfaces such as etcd, Controller Manager, etc.
* This Control plane is used to define, deploy, and manage lifecycle of the containers.

### Kubernetes architecture (Kubernetes Cluster)
* Consists of a control plane that contains a kube-api-server that runs nodes.
* Control plane manages the worker nods and Pods in the cluster.

## Setting up Kubernetes Cluster
* 
*

## Best Practices
Recommend to use container images vs containers to run Kubernetes components.
