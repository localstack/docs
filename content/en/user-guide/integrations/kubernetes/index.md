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

{{< github repo="localstack/helm-charts" file="charts/localstack/README.md#parameters" lang="markdown" >}}
