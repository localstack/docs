---
title: "Rancher Desktop"
linkTitle: "Rancher Desktop"
weight: 91
description: Use the Rancher Desktop to manage your LocalStack container in a Kubernetes cluster
---

## Introduction

Rancher Desktop is a desktop application designed to simplify the local deployment of Kubernetes clusters. It leverages `k3s`, a lightweight and certified Kubernetes distribution offered by Rancher. For container management, Rancher Desktop provides flexibility by supporting either the `docker` CLI (powered by Moby/dockerd) or `nerdctl` (`containerd`) as container runtimes.

## Installation

To use LocalStack with Rancher Desktop, the following prerequisites need to be met:

* [Rancher Desktop](https://rancherdesktop.io) installed on your machine
* [Helm](https://helm.sh) installed on your machine
* [kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl) installed on your machine

### Setup a Kubernetes Cluster

Launch Rancher Desktop and create a new Kubernetes cluster. You can switch your `kubectl` context to the new cluster by running the following command:

{{< command >}}
$ kubectl config use-context rancher-desktop
{{< /command >}}

### Deploy LocalStack via Helm

To deploy LocalStack in the Kubernetes cluster, we can use the [LocalStack Helm chart](https://github.com/localstack/helm-charts) as follows:

{{< command >}}
$ helm repo add localstack https://localstack.github.io/helm-charts
$ helm repo update
{{< /command >}}

You can install LocalStack in the Kubernetes cluster by running the following command:

{{< command >}}
$ helm upgrade --install localstack localstack/localstack --namespace localstack --create-namespace --wait
{{< /command >}}

### Access LocalStack

Once the installation is complete, you can query the status of the LocalStack deployment by running the following command:

{{< command >}}
$ export NODE_PORT=$(kubectl get --namespace "localstack" -o jsonpath="{.spec.ports[0].nodePort}" services localstack)
{{< /command >}}

You can now configure `AWS_ENDPOINT_URL` to allow your integrations, such as the AWS CLI, to connect to LocalStack:

{{< command >}}
export NODE_IP=127.0.0.1 
export AWS_ENDPOINT__URL=http://$NODE_IP:$NODE_PORT
awslocal s3api create-bucket --bucket test-bucket
{{< /command >}}

The `awslocal` CLI will now connect to LocalStack running in the Kubernetes cluster and create a new S3 bucket named `test-bucket`.
