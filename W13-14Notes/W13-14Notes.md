# Weeks 13-14: **Kubernetes Operators and Custom Resources**

## Kubernetes Operators

* Kubernetes Operators are custom controllers for Custom Resources within the Kubernetes API.
* The Operators were designed to be used for automation of complex tasks.
* To create an Operator, you will use an Operator SDK like Operator Framework.

## Custom Resource Definitions

* To create Custom Resources, you must first create a Custom Resource Definition (CRD), which registers the Custom Resource type with the Kubernetes API.
* The Kubernetes API serves and handles the storage of Custom Resources.
* Rules when creating a CRD:
  * The name must be <plural>.<group>
* > Note: The Kubernetes API endpoint for a namespace-scoped Custom Resource will look like ``/apis/<group>/<version>/namespaces/<namespace>/<plural>``
