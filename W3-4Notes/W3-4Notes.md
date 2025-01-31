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
* Default Range for NodePort is 30000-32767.

## LoadBalancer
* Can be used with cloud providers if they support external load balancers.
* Information about a LoadBalancer is located in .status.loadBalancer.
* This is used with NodePorts to basically forward traffic on a given node port.

### LoadBalancer Options if supported
* A load balanced Service can not assign a node port by setting spec.allocateLoadBalancerNodePorts to false. This is used for the LoadBalancer to route traffic to pods instead of a NodePort.
  * Note: spec.allocateLoadBalancerNodePorts being false will still have the NodePort available. You must specifically remove it.
* loadBalancerIP can be created with a user-specified loadBalancerIP.
* Cloud Providers can provide health checks for its load balancers.

## DNS for Kubernetes
* Kubernetes creates DNS records that can be used for Services and Pods.
* Kubelet can configure the Pods DNS to lookup Services by name rather than IP.
* DNS query can return different results based on the namespace given to the Pod.
  * DNS queries are limited to Pod's namespace if no namespace is specified.
* DNS queries can also be expanded by using the Pod's /etc/resolv.conf file. 

### DNS Records for Services and Pods
* A/AAAA Records for Services:
  * Record Example: 
  * `<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
  * Note regarding Headless Services: These resolve to the set of IPs of all Pods selected by the Service rather than the cluster IP of the Service.
* SRV Records for Services:
  * Used for Named ports for normal or headless services.
  * Record Example:
  * `<_port-name>.<_port-protocol>.<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
  * For Normal Services, this resolves to:
    * Port Number
    * Domain Name: `<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
  * For Headless Services, this resolves to multiple answers of:
    * Port Number
    * Domain Name of pod: `<hostname>.<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
* A/AAAA Records for Pods:
  * Record Example:
  * `<pod-ipv4-address>.<my-namespace>.pod.<cluster-domain.example>`
* Notes regards DNS for Pods:
  * The Pod's `metadata.name` value is the hostname.
  * Pod spec has an optional `hostname` field which will take precedence over the `metadata.name` value.
  * Pod spec also has an optional `subdomain` field to clarify that the pod is in the sub-group of the namespace.
  * DNS Policy for Pods using `dnsPolicy` field for PodSpec.
    * "Default" : When the pod is created, grab the name resolution configuration from its node. Despite its name, ClutserFirst is the default DNS policy.
    * "ClusterFirst" : For a given DNS query, if it matches the configured cluster domain suffix, use the DNS in Kubernetes. Otherwise, use the upstream nameserver.
    * "None" : Ignores DNS settings from Kubernetes environment. 

## Persistent Volumes (PV) & Persistent Volume Claim (PVC)
* Persistent Volumes
  * PersistentVolume (PV) is storage in the cluster provisioned by an administrator or a Storage Class.
  * They are like Volumes except the lifecycle does not depend on any Pod using the PV.
  * Two ways it can be created:
    * Statically:
      * Administrator creates PVs.
    * Dynamically:
      * Cluster will dynamically provision a volume specifically for the PVC when static PVs do not match the user's PVC.
      * Can be enabled by using `DefaultStorageClass` 
* Persistent Volume Claim
  * Used for a user to consume abstract storage resources.
  * Also used for claim checks to the resource.

* How PV and PVC are used in Kubernetes
  * PVC is created with its accessibilities and storage amount.
  * The control loop checks for new PVC, finds a matching PV, and binds them together.
  * PVC-to-PC are a one-to-one binding.

* Reclaiming a PVC
  * PVC objects can be deleted to where a PC can claim the resource. There are 3 reclaim policy that a PV can do. (Retrained, Recycled, Deleted). For Recycled, it has become deprecated.
  * Retain:
    *  It does manual reclamation of the resource.
  * Delete:
    * Removes the PV and the storage asset.