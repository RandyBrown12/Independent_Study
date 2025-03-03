# Weeks 7-8: **Deployments and Scaling**

## Deployments

Using Deployments can be beneficial to perform CI/CD with zero downtime for the user.

### Rolling Updates

* Rolling update replaces each old pod one-by-one with a new pod that is ready.
* In a rolling update, the default number for the maximum number of pods can be unavailable ``maxUnavailable`` during the update and the maximum number of new pods that can be created ``maxSurge`` is one.
* Can be used to rollback to previous versions.

> **Note regarding ``maxSurge`` and ``maxUnavailable``:** You can specify a number or a percentage in which the percentage will be rounded up to an integer on ``maxSurge`` or rounded down to an integer on ``maxUnavailable``.

### Canary Deployment

* Have a small percentage of users go to the new pods and everyone else to the old pods.
* Those users will now test the pod, leading to either a rollback or moving them to the new pods.
* It is called Canary Deployment because small users (canaries) will detect the problems before the other users notice them.

> **Note:** A/B Testing and Canary Deployment are similar due to splitting up users into different groups.

### Blue-Green Deployment

* Creating all the new pods and has the deployment point to all the new pods instead of the old pods.
* Older version would be classified as blue and the newer version would be classified as green.

## Pod Autoscalers

* There are 2 ways you can scale your software.
  * Horizontally: Adding more processes such as servers or containers to handle workloads.
    * Ex: There are too many connections to the database container, which may lead to slower response times. This can be mitigated by deploying an additional database container to distribute the load.
  * Vertically: Increasing the efficiency of your hardware components (CPU, RAM, etc.)

### Horizontal Pod Autoscaler (HPA)

* HPA automatically scales the number of pods based on the workload.
* To utilize HPA for reading metrics, you need to manually install the needed components. Here are a couple options:
  * For Resource Metrics such as CPU and memory usage: Use a Kubernetes Metric Server.
  * For Custom Metrics: Use a Kubernetes API Aggregation Layer with a custom metrics adapter.

### Vertical Pod Autoscaler (VPA)

* VPA automatically adjusts the CPU and memory request/limit of the pods.
* Request: Minimum amount of resources the container needs.
* Limit: Maximum amount of resources the container needs.
* VPA comes with four modes:
  * Off: VPA does not automatically change the resource requirements of the pods.
  * Initial: VPA assigns resource request on pod creation and does not change.
  * Recreate: VPA assigns resource request on pod creation and updates them on existing pods by evicting and recreating them.
  * Auto: Recreates pod by adjusting resource request based off recommendation.

> Note: The recommendation is found in the label ``status`` in the VPA object.
> Note: Kubernetes Metric Server also needs to be installed to use VPA.

## Ingress

* A OSI-Layer 7 Load balancer that routes HTTP/HTTPS requests to the respective service.
* Ingress allows users to access services in a Kubernetes cluster using a domain name.
* Ingress is not accessed externally. You need an Ingress Controller that connects to the Ingress.
  * Examples of Ingress Controllers: NGINX Ingress Controller, Kong Ingress Controller, AKS Application Gateway Ingress Controller.

> Note: For an Ingress to work in production, it must have a valid DNS subdomain name.

### Ingress Rules

* Can contain an optional host to where rules can be applied to.
  * Hostname wildcards (*) can also be used to match domains without specifying subdomains.
* A list of paths that each point to a backend that has a service name and service port name/number.
  * Path Types:
    * ``Exact``: URL path must be exactly the same as the rule given. (Ex: /foo, /foo/ would not match)
    * ``Prefix``: URL path matched by prefix split by /. (Ex: /foo, /foo/ would match)
    * ``ImplementationSpecific``: IngressClass decides what to match.
    * Note: If a request matches multiple rules, The following steps will happen to break ties.
      * First, precedence will be given first of longest matching path.
      * If they are equal path lengths, precedence will be given to exact path types over prefix path types.

> Note: A DefaultBackend is created if there is a request that does not match a path listed in the Ingress Rules.
