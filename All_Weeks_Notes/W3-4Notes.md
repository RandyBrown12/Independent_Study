### Weeks 3-4: **Kubernetes Networking and Storage**

* **Topics** : Networking basics (ClusterIP, NodePort, LoadBalancer), DNS within Kubernetes, Persistent Volumes (PV), Persistent Volume Claims (PVC).
* **Hands-On** : Create services with different types and configure DNS. Experiment with PV and PVC for storage.
* **Resources** : Kubernetes documentation on networking, CNCF’s Cloud Native tutorials.

## Networking
* A pod in a cluster gets its own unique cluster-wide IP address. It also contains a private network namespace shared by containers in the pod.
* A service API provides a stable IP address or hostname for a service implemented by one or more backend pods.

## ClusterIP
* A virtual IP address that is scoped inside the cluster.
* It is possible to have a service not assign IP address by setting ```clusterIP``` to "None"

### Two ways to allocate Service ClusterIPs
* Dynamically: Cluster control plane automatically picks an IP address not used for an object using the
  configured IP range for Services.
* Statically: IP address in the configured IP range for services

## NodePort
* Every node in the cluster is given the port called NodePort
* NodePort is used to expose one or more nodes IP addresses directly
* When a NodePort is created, another port is allocated matching the protocol of the Service. 