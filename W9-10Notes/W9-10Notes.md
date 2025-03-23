# Weeks 9-10: **Kubernetes Security**

## Role Based Access Control (RBAC):

* RBAC is used to give limited access based on the roles of the users.
* For RBAC to be enabled in the Cluster, start up the API server with ``--authorization-config`` flag with an AuthorizationConfiguration yaml file that includes the ``RBAC`` authorizer.

## Authentication

* Kubernetes manages service accounts which are bounded toward specific namespaces.
* There are many methods that Kubernetes can do to perform authentication
  * Client Certificates (API Server has a file containing certificate authorities to validate client certificates)
  * Service Account Token (Uses signed bearer tokens to verify requests)

## Authorization

* Kubernetes contains roles that give permissions to users based on the names assigned.

### Role Types:

* Roles: Permissions that are allowed in the given namespace.
* Cluster Roles: Permissions that are allowed in any namespace within the cluster.
* > Note: When a user has multiple roles, their permissions are accumulative. (no "deny" rules)
  >

### RoleBinding Types:

* RoleBinding: Bind a role within the same namespace to a set of users.
* ClusterRoleBinding: Bind a role to all namespaces within the cluster to a set of users.
* > Note: There are use cases where you can do RoleBindings to ClusterRoles.
  >

## Namespaces:

* Namespaces are used to classify groups of resources in a single cluster.
* Objects within a namespace must have a unique name.
* Kubernetes sets the default namespace to default.
* > Note: Namespaces are only applied to namespaced objects and not cluster-wide objects.
  >

## Network Policies:

* Pods, by default, allow access for all outbound and inbound connections.
* We can use a network policy to control traffic control outside and/or inside the cluster.
* Two things a network policy needs:
  * Pod(s) must be selected
  * Policy types (Ingress and/or Egress)
* Pods can have many network policies and these policies can be applied together as a combined set of rules.
* > Note: To create Network Policies, a network plugin must be installed.
  >

## Security Contexts:

* Security Contexts are privilege and access control settings for a pod or containers.
* An example is: ``runAsUser: {UID}`` where all containers specified will run with UserID provided.
