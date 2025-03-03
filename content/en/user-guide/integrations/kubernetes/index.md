---
title: Kubernetes
linktitle: Kubernetes
description: Running LocalStack on Kubernetes
---

## Introduction

[Kubernetes](https://kubernetes.io) is an open-source container orchestration platform that simplifies the deployment, scaling, and management of containerized applications.
LocalStack can be deployed on Kubernetes using the [LocalStack Helm chart](https://github.com/localstack/helm-charts).

{{< callout "warning" >}}
Creating shared/hosted LocalStack instances may have some licensing implications.
For example, a valid license might be necessary for each user who interacts with the instance.
If you have any questions or uncertainties regarding the licensing implications, we encourage you to [contact us](https://localstack.cloud/contact) for further details.
{{< /callout >}}

## Getting started

To deploy LocalStack in your [Kubernetes](https://kubernetes.io/) cluster, you can use [Helm](https://helm.sh/).

### Prerequisites

- Kubernetes 1.19+
- Helm 3.2.0+

### Setup a Kubernetes cluster

For setting up Kubernetes refer to the Kubernetes  [getting started guide](https://kubernetes.io/docs/getting-started-guides/).

### Install Helm

Helm is a tool for managing Kubernetes charts.
Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the  [Helm install guide](https://github.com/helm/helm#install) and ensure that the `helm` binary is in the `PATH` of your shell.

### Add repository

The following command allows you to download and install all the charts from this repository:

{{< command >}}
$ helm repo add localstack https://localstack.github.io/helm-charts
{{< /command >}}

### Using Helm

After you have installed the Helm client, you can deploy a Helm chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/)  if you wish to get running in just a few commands, otherwise the [Using Helm guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on how to use the Helm client to manage packages on your Kubernetes cluster.

Some useful Helm client commands are:

- View available charts: `helm search repo`
- Install a chart: `helm install <name> localstack/<chart>`
- Upgrade your application: `helm upgrade`
- Uninstall or delete a release: `helm uninstall <name>`

## LocalStack Pro

You can use this chart with LocalStack Pro by:

1. Changing the image to `localstack/localstack-pro`.
2. Providing your Auth Token as an environment variable.

You can set these values in a YAML file (in this example `pro-values.yaml`):

```yaml
image:
  repository: localstack/localstack-pro

extraEnvVars:
  - name: LOCALSTACK_AUTH_TOKEN
    value: "<your auth token>"
```

If you have the LocalStack Auth Token in a secret, you can also reference it directly with `extraEnvVars`:

```yaml
extraEnvVars:
- name: LOCALSTACK_AUTH_TOKEN
  valueFrom:
    secretKeyRef:
      name: <name of the secret>
      key: <name of the key in the secret containing the API key>
```

And you can use these values when installing the chart in your cluster:

{{< command >}}
$ helm repo add localstack-charts https://localstack.github.io/helm-charts
$ helm install my-release localstack-charts/localstack -f pro-values.yaml
{{< /command >}}

## Parameters

The following table lists the configurable parameters of the Localstack chart and their default values.

### Common parameters

| Parameter                                            | Description                                                                                                                                                                                                                           | Default                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `nameOverride`                                       | String to partially override common.names.fullname                                                                                                                                                                                    | `nil`                                                   |
| `fullnameOverride`                                   | String to fully override common.names.fullname                                                                                                                                                                                        | `nil`                                                   |
| `extraDeploy`                                        | Extra objects to deploy (value evaluated as a template)                                                                                                                                                                               | `[]`                                                    |

### Localstack common parameters

| Parameter                                            | Description                                                                                                                                                                                                                           | Default                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `image.repository`                                   | Localstack image name                                                                                                                                                                                                                 | `localstack/localstack`                                 |
| `image.tag`                                          | Localstack image tag                                                                                                                                                                                                                  | `latest`                                                |
| `image.pullPolicy`                                   | Localstack image pull policy                                                                                                                                                                                                          | `IfNotPresent`                                          |
| `image.pullSecrets`                                  | Specify docker-registry secret names as an array                                                                                                                                                                                      | `[]`                                                    |
| `podLabels`                                          | Additional pod labels for Localstack secondary pods                                                                                                                                                                                   | `{}`                                                    |
| `podAnnotations`                                     | Additional pod annotations for Localstack secondary pods                                                                                                                                                                              | `{}`                                                    |
| `podSecurityContext`                                 | Enable security context for Localstack pods                                                                                                                                                                                           | `{}`                                                    |
| `extraDeploy`                                        | Extra objects to deploy (value evaluated as a template)                                                                                                                                                                               | `{}`                                                    |
| `extraAnnotations`                                   | Add additional annotations to every resource (value evaluated as a template)                                                                                                                                                          | `{}`                                                    |
| `extraLabels`                                        | Add additional labels to every resource (value evaluated as a template)                                                                                                                                                               | `{}`                                                    |
| `securityContext`                                    | Localstack container securityContext                                                                                                                                                                                                  | `{}`                                                    |

### Localstack parameters

| Parameter                                            | Description                                                                                                                                                                                                                           | Default                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `debug`                                              | Specify if debug logs should be enabled                                                                                                                                                                                               | `false`                                                 |
| `kinesisErrorProbability`                            | Specify to randomly inject ProvisionedThroughputExceededException errors into Kinesis API responses                                                                                                                                   | `nil` (Localstack Default)                              |
| `startServices`                                      | Comma-separated list of AWS CLI service names which should be loaded right when starting LocalStack. If not set, each service is loaded and started on the first request for that service.                                            | `nil` (Localstack Default)                              |
| `lambdaExecutor`                                     | Specify Method to use for executing Lambda functions (partially supported)                                                                                                                                                            | `docker`                                                |
| `extraEnvVars`                                       | Extra environment variables to be set on Localstack primary containers                                                                                                                                                                | `nil` (Localstack Default)                              |
| `enableStartupScripts`                               | Mount `/etc/localstack/init/ready.d` to run startup scripts with `{{ template "localstack.fullname" . }}-init-scripts-config` configMap                                                                                               | `false`                                                 |
| `startupScriptContent`                               | Startup script content when `enableStartupScripts` is `true`. Note: You will need to add a shebang as your first line such as `!#/bin/sh` in order to ensure the startup script is not malformed.                                     | `nil` (Localstack Default)                              |

### Deployment parameters

| Parameter                                            | Description                                                                                                                                                                                                                           | Default                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `replicaCount`                                       | Number of Localstack pods                                                                                                                                                                                                             | `1`                                                     |
| `updateStrategy.type`                                | Update strategy type                                                                                                                                                                                                                  | `RollingUpdate`                                         |
| `nodeSelector`                                       | Node labels for pod assignment                                                                                                                                                                                                        | `{}`                                                    |
| `tolerations`                                        | Tolerations for pod assignment                                                                                                                                                                                                        | `[]`                                                    |
| `affinity`                                           | Affinity for pod assignment                                                                                                                                                                                                           | `{}`                                                    |
| `resources.limits`                                   | The resources limits for Localstack containers                                                                                                                                                                                        | `{}`                                                    |
| `resources.requests`                                 | The requested resources for Localstack containers                                                                                                                                                                                     | `{}`                                                    |
| `livenessProbe`                                      | Liveness probe configuration for Localstack containers                                                                                                                                                                                | Same with [Kubernetes defaults][k8s-probe]              |
| `readinessProbe`                                     | Readiness probe configuration for Localstack containers                                                                                                                                                                               | Same with [Kubernetes defaults][k8s-probe]              |
| `mountDind.enabled`                                  | Specify the mount of Docker daemon into Pod to enable some AWS services that got runtime dependencies such as Lambdas on GoLang                                                                                                       | `false`                                                 |
| `mountDind.forceTLS`                                 | Specify TLS enforcement on Docker daemon communications                                                                                                                                                                               | `true`                                                  |
| `mountDind.image`                                    | Specify DinD image tag                                                                                                                                                                                                                | `docker:20.10-dind`                                     |
| `volumes`                                            | Extra volumes to mount                                                                                                                                                                                                                | `[]`                                                    |
| `volumeMounts`                                       | Extra volumes to mount                                                                                                                                                                                                                | `[]`                                                    |

[k8s-probe]: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#configure-probes

### RBAC parameters

| Parameter                                            | Description                                                                                                                                                                                                                           | Default                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `serviceAccount.create`                              | Enable the creation of a ServiceAccount for Localstack pods                                                                                                                                                                           | `true`                                                  |
| `serviceAccount.name`                                | Name of the created ServiceAccount                                                                                                                                                                                                    | Generated using the `common.names.fullname` template    |
| `serviceAccount.annotations`                         | Annotations for Localstack Service Account                                                                                                                                                                                            | `{}`                                                    |

### Exposure parameters

| Parameter                                            | Description                                                                                                                                                                                                                           | Default                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `service.type`                                       | Kubernetes Service type                                                                                                                                                                                                               | `NodePort`                                              |
| `service.edgeService.targetPort`                     | Port number for Localstack edge service                                                                                                                                                                                               | `4566`                                                  |
| `service.externalServicePorts.start`                 | Start of the external service port range (included). service                                                                                                                                                                          | `4510`                                                  |
| `service.externalServicePorts.end`                   | End of the external service port range (excluded). service                                                                                                                                                                            | `4560`                                                  |
| `service.loadBalancerIP`                             | loadBalancerIP if Localstack service type is `LoadBalancer`                                                                                                                                                                           | `nil`                                                   |
| `service.dnsService`                                 | Expose the Service and Deployment's DNS port for TCP and UDP DNS traffic                                                                                                                                                              | `""`                                                    |
| `service.clusterIP`                                  | Set a static clusterIP for the service. Useful for DNS delegation to the Localstack Service                                                                                                                                           | `""`                                                    |
| `ingress.enabled`                                    | Enable the use of the ingress controller to access Localstack service                                                                                                                                                                 | `false`                                                 |
| `ingress.annotations`                                | Annotations for the Localstack Ingress                                                                                                                                                                                                | `{}`                                                    |
| `ingress.hosts[0].host`                              | Hostname to your Localstack Ingress                                                                                                                                                                                                   | `nil`                                                   |
| `ingress.hosts[0].paths`                             | Path within the url structure                                                                                                                                                                                                         | `[]`                                                    |
| `ingress.tls`                                        | Existing TLS certificates for ingress                                                                                                                                                                                                 | `[]`                                                    |

### Persistence Parameters

| Name                                                 | Description                                                                                                                                                                                                                           | Value                                                   |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| `persistence.enabled`                                | Enable persistence using Persistent Volume Claims                                                                                                                                                                                     | `false`                                                 |
| `persistence.storageClass`                           | Persistent Volume storage class                                                                                                                                                                                                       | `""`                                                    |
| `persistence.accessModes`                            | Persistent Volume access modes                                                                                                                                                                                                        | `[]`                                                    |
| `persistence.size`                                   | Persistent Volume size                                                                                                                                                                                                                | `8Gi`                                                   |
| `persistence.dataSource`                             | Custom PVC data source                                                                                                                                                                                                                | `{}`                                                    |
| `persistence.existingClaim`                          | The name of an existing PVC to use for persistence                                                                                                                                                                                    | `""`                                                    |
