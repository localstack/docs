---
title: eksctl
linktitle: eksctl
description: Running `eksctl` on LocalStack to create EKS clusters
---

## Introduction

[eksctl](https://eksctl.io/) is a CLI tool for creating and managing EKS clusters, Amazon's managed Kubernetes service. LocalStack supports running `eksctl` on LocalStack to create EKS clusters locally. LocalStack's EKS spin up embedded Kubernetes clusters using [K3s](https://github.com/k3s-io/k3s) to allow you to use the EKS APIs in your local environment.

{{< callout >}}
The support for `eksctl` is currently experimental and may not work in all cases. We are working on improving the support for `eksctl` in LocalStack.
{{< /callout >}}

## Getting started

This guide is designed for users new to `eksctl` and running EKS clusters with LocalStack. Start LocalStack using your preferred method. We will demonstrate how you can create a local EKS cluster using `eksctl` and fetch the nodes in the cluster.

### Pre-requisites

- LocalStack with `LOCALSTACK_AUTH_KEY` configured
- [Docker](https://www.docker.com/)
- [`eksctl`](https://eksctl.io/) (version 0.167.0 or higher)
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl)

### Create a cluster

To create a cluster, you can use the `eksctl create cluster` command. You can use the `--profile` flag to [specify the LocalStack profile](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#configuring-a-custom-profile) to use for the cluster. 

Run the following command to create a cluster:

{{< command >}}
$ eksctl create cluster --nodes 1 --profile localstack
{{< / command >}}

### Get the nodes

You can use the `kubectl` command to get the nodes in the cluster:

{{< command >}}
$ kubectl get nodes
{{< / command >}}
