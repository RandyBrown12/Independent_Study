# Week 1 - 2: (Setting up Kubernetes)

## Best Practices

Recommend to use container images vs containers to run Kubernetes components.

## Kubernetes Components

This is Kubernetes in the big picture.
We will start small and work our way up.
![Kubernetes Image](https://kubernetes.io/images/docs/kubernetes-cluster-architecture.svg)

### Pods

* A Pod is a group of one or more containers that share the same storage and network resources and instructions to run the containers.
* A Pod can contain one or more init containers which are initial containers that are run first before application containers.

#### Notes regarding Init containers

* Init containers always run to completion.
* They must be completed sequentially.
* If an init container fails, kubelet repeatedly restarts that init container until it is completed. This can be overwritten to treat the pod as failed if the Pod has a ``restartPolicy`` of never.

#### Applications for init containers

* Lets say you have data stored in another server that you do not have any space on your computer for it. An init
  container can be used to grab the data in the server.
* Another example is testing if the pod is ready for the user to connect to.

### Nodes

* Nodes are a virtual or physical machine that uses a control plane and contains the services needed to run Pods.
* Components on a node include kubelet, container runtime, and kube-proxy.
* Nodes also contains a status with following information: Addresses, Conditions, Metadata on Node such as CPU, memory, and number of pods.
* The naming for the nodes has to be unique in relation to other nodes.

#### To add a Node to the API server

* Kubelet on a node self-registers to the control-plane.
* User manually add a Node object.

### kubelet

* Node Agent that runs a node.
* This also communicates with kube-apiserver
* To use a kublet, it needs a YAML or JSON object to describe the pod.

### kube-apiserver

* This process is using REST operations to validate & configure data API objects such as pods, services, etc.
* The API server is used to act as an entry point for Kubernetes control plane.

### etcd

* Used to store key values for cluster data.

### Controllers for kube-controller-manager

* They are a control loop that watches the shared state of the cluster thought kube-apiserver. It also updates the changes to the state to push it towards the desired state.
* Examples are namespace controller, endpoints controller.

### Control Plane

* Container orchestration layer that uses the kube-apiserver and other interfaces such as etcd, Controller Manager, etc.
* This control plane is used to define, deploy, and manage lifecycle of the containers.

### Kubernetes architecture (Kubernetes Cluster)

* Consists of a control plane that contains a kube-apiserver that runs nodes.
* Control plane manages the worker nods and pods in the cluster.

### Deployment

* Manages set of Pods to run an application.
* Used when making sure the desired state stays at that state, such as replacing a pod.

### Service

* Used to expose a network application running one or more pods in your cluster.
* When using deployment, it will control what is happening with the pods.
* In YAML files, we could bind the targetPort of the service to the pod by naming the port and using it in the service.
