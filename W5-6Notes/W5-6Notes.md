# Weeks 5-6: **ConfigMaps and Secrets**

## Notes regarding ConfigMaps and Secrets

* These can be set to immutable.
* Both are limited to 1 MiB in etcd.

## ConfigMaps

* Stores non-confidential data in key-values.
* Pods treats ConfigMaps as environment variables, command-line args, or as config files in a volume (used if data exceeds 1 MiB)
* The Pod and ConfigMap must be in the same namespace.
* If a ConfigMap has a volume that updates its values, the keys will also be updated as well.
  * This is not true for environment variables and containers using a ConfigMap as a subPath volume.

### ConfigMaps object

* Containers fields that have ``data`` and ``binaryData`` which are optional

## Secrets

* Object that is a small amount of sensitive data that should not be in the application.
* These secrets can also be mounted as data volumes.

### Notes regarding Secrets:

* By default, your secrets must be Base-64 encoded which is unencrypted. They also can be accessed by anyone with API or etcd access.
* Kubernetes has built-in secrets for common scenarios such as kubernetes.io/ssh-auth, which is credentials for SSH authentication.

### How to prevent secrets from unwanted access

* Use Encryption at Rest for Secrets.
  * This uses a provider like aescbc that is used with etcd to encrypt/decrypt secrets.
* Add RBAC rules that do least-privilege access.
* Restrict secret access to other containers.
* Use a reputable external Secret store provider.
* Create logging to where a secret has been accessed.

### Password Vaults for use of Kubernetes

* We can use the idea of a password vault to lessen the impact of showing sensitive environment variables in a pod.
* We will focus on two ways to achieve this:
  * API Calls:
    * HashiCorp offers API calls that allow you to access the secret in your runtime environment.
  * Vault Agent Sidecar:
    * We can have a sidecar (container running with main application) that grabs secrets from the vault.
    * After that, it will be written to a volume to where the application can read it.
* A well-known service is HashiCorp Vault
