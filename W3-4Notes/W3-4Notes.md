# Weeks 3-4: **Kubernetes Networking and Storage**

## Networking

* A pod in a cluster gets its own unique cluster-wide IP address. It also contains a private network namespace shared by containers in the pod.
* A service API provides a stable IP address or hostname for a service implemented by one or more backend pods.

## ClusterIP

* A virtual IP address that is scoped inside the cluster.
* It is possible to have a service not assign an IP address by setting ``clusterIP`` to "None".

### Two ways to allocate Service ClusterIPs

* Dynamically: The cluster control plane automatically picks an IP address not used for an object using the
  configured IP range for Services.
* Statically: IP address in the configured IP range for services.

## NodePort

* Every node in the cluster is given the port called NodePort.
* NodePort is used to expose one or more nodes IP addresses directly.
* When a NodePort is created, another port is allocated matching the protocol of the service.
* The default range for NodePort is 30000-32767.

## LoadBalancer

* Can be used with cloud providers if they support external load balancers.
* Information about a LoadBalancer is located in .status.loadBalancer.
* This is used with NodePorts to basically forward traffic on a given node port.

### LoadBalancer Options if Supported

* A load-balanced service cannot assign a node port by setting spec.allocateLoadBalancerNodePorts to false. This is used for the LoadBalancer to route traffic to pods instead of a NodePort.
  * Note: spec.allocateLoadBalancerNodePorts being false will still have the NodePort available. You must specifically remove it.
* loadBalancerIP can be created with a user-specified loadBalancerIP.
* Cloud providers can provide health checks for their load balancers.

## DNS for Kubernetes

* Kubernetes creates DNS records that can be used for services and pods.
* Kubelet can configure the Pods DNS to look up services by name rather than IP.
* DNS query can return different results based on the namespace given to the Pod.
  * DNS queries are limited to Pod's namespace if no namespace is specified.
* DNS queries can also be expanded by using the Pod's /etc/resolv.conf file.

### DNS Records for Services and Pods

* A/AAAA Records for Services:
  * Record Example:
  * `<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
  * Note regarding Headless Services: These resolve to the set of IPs of all Pods selected by the Service rather than the cluster IP of the Service.
* SRV Records for Services:
  * Used for named ports for normal or headless services.
  * Record Example:
  * `<_port-name>.<_port-protocol>.<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
  * For normal services, this resolves to:
    * Port Number
    * Domain Name: `<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
  * For headless services, this resolves to multiple answers of:
    * Port Number
    * Domain Name of pod: `<hostname>.<my-svc>.<my-namespace>.svc.<cluster-domain.example>`
* A/AAAA Records for Pods:
  * Record Example:
  * `<pod-ipv4-address>.<my-namespace>.pod.<cluster-domain.example>`
* Notes regarding DNS for Pods:
  * The Pod's `metadata.name` value is the hostname.
  * Pod spec has an optional `hostname` field that will take precedence over the `metadata.name` value.
  * Pod spec also has an optional `subdomain` field to clarify that the pod is in the sub-group of the namespace.
  * DNS Policy for Pods using a `dnsPolicy` field for PodSpec.
    * "Default" : When the pod is created, grab the name resolution configuration from its node. Despite its name, ClutserFirst is the default DNS policy.
    * "ClusterFirst" : For a given DNS query, if it matches the configured cluster domain suffix, use the DNS in Kubernetes. Otherwise, use the upstream nameserver.
    * "None" : Ignores DNS settings from the Kubernetes environment.

## Persistent Volumes (PV) & Persistent Volume Claim (PVC)

* Persistent Volumes

  * PersistentVolume (PV) is storage in the cluster provisioned by an administrator or a Storage Class.
  * They are like volumes except the lifecycle does not depend on any pod using the PV.
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

  * PVC is created with its accessibility and storage amount that has to have the PV be greater or equal to what its asking.
  * The control loop checks for a new PVC, finds a matching PV, and binds them together.
  * PVC-to-PC are a one-to-one binding.
* Reclaiming a PVC

  * PVC objects can be deleted to where a PV can claim the resource. There are 3 reclaim policies that a PV can do. (Retrained, Recycled, Deleted). For Recycled, it has become deprecated.
  * Retain:
    * The PV and all the data stored in it will still exist.
  * Delete:
    * Remove the data inside the PV.
* Note regarding PV & PVC:
  * If another node tries to claim a node with a PV that has readWriteOnce on it, then it will not be mounted, will be in the containerCreating state.
