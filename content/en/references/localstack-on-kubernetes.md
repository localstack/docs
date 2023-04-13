---
title: LocalStack on Kubernetes
weight: 110
categories: ["LocalStack Community", "LocalStack Pro"]
tags:
- kubernetes
- k8s
description: >
  Overview of how you can run LocalStack on Kubernetes
---

LocalStack can be deployed on [Kubernetes](https://kubernetes.io/) using the [LocalStack Helm chart](http://helm.localstack.cloud/).

## Helm Chart

To deploy LocalStack in your [Kubernetes](https://kubernetes.io/) cluster, you can use [Helm](https://helm.sh/).

### Prerequisites

- Kubernetes 1.19+
- Helm 3.2.0+

### Setup a Kubernetes cluster

For setting up Kubernetes refer to the Kubernetes  [getting started guide](https://kubernetes.io/docs/getting-started-guides/).

### Install Helm

Helm is a tool for managing Kubernetes charts. Charts are packages of pre-configured Kubernetes resources.

To install Helm, refer to the  [Helm install guide](https://github.com/helm/helm#install) and ensure that the `helm` binary is in the `PATH` of your shell.

### Add repository

The following command allows you to download and install all the charts from this repository:

{{< command >}}
$ helm repo add localstack https://localstack.github.io/helm-charts
{{< /command >}}

### Use Helm

After you have installed the Helm client, you can deploy a Helm chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/)  if you wish to get running in just a few commands, otherwise the [Using Helm guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on how to use the Helm client to manage packages on your Kubernetes cluster.

Some useful Helm client commands are:

-   View available charts: `helm search repo`
-   Install a chart: `helm install <name> localstack/<chart>`
-   Upgrade your application: `helm upgrade`

## Sample repository (`l8k`)

The [`localstack-on-k8s](https://github.com/localstack/localstack-on-k8s) sample repository that illustrates running LocalStack on Kubernetes (k8s).

### Prerequisites

This sample requires the following tools installed on your machine:

* Python 3.7+
* [`awslocal`](https://github.com/localstack/awscli-local)
* [Docker](https://www.docker.com)
* [Git](https://git-scm.com)
* [Helm](https://helm.sh)
* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl)
* [Serverless](https://www.npmjs.com/package/serverless)

### Installation

Clone the repository:

{{< command >}}
$ git@github.com:localstack/localstack-on-k8s.git
{{< /command >}}

To install the Python dependencies in a virtualenv:

{{< command >}}
$ make install
{{< /command >}}

To create an embedded Kubernetes (k3d) cluster in Docker and install LocalStack in it (via Helm):

{{< command >}}
$ make init
{{< /command >}}

After initialization, your `kubectl` command-line should be automatically configured to point to the local cluster context:

{{< command >}}
$ kubectl config current-context
k3d-ls-cluster
{{< /command >}}

### Deploy a sample application

Once LocalStack is installed in the Kubernetes cluster, we can deploy the sample app on the LocalStack instance:

{{< command >}}
$ make deploy
{{< /command >}}

### Test the sample application

Once the sample app is deployed, the Kubernetes environment should contain the following resources:

{{< command >}}
$ kubectl get all
NAME                              READY   STATUS    RESTARTS   AGE
pod/localstack-6fd5b98f59-zcx2t   1/1     Running   0          5m

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
service/kubernetes   ClusterIP   10.43.0.1       <none>        443/TCP                         5m
service/localstack   NodePort    10.43.100.167   <none>        4566:31566/TCP,4571:31571/TCP   5m

NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/localstack   1/1     1            1           5m

NAME                                    DESIRED   CURRENT   READY   AGE
replicaset.apps/localstack-6fd5b98f59   1         1         1       5m
{{< /command >}}

The LocalStack instance should be available via the local ingress port `8081`. We can verify that the resources were successfully created by running a few `awslocal` commands against the local endpoint:

{{< command >}}
$ awslocal sqs --endpoint-url=http://localhost:8081 list-queues
{
    "QueueUrls": [
        "http://localhost:8081/000000000000/requestQueue"
    ]
}
$ awslocal apigateway --endpoint-url=http://localhost:8081 get-rest-apis
{
    "items": [
        {
            "id": "ses2pi5oap",
            "name": "local-localstack-demo",
...
{{< /command >}}

We can then use a browser to open the [Web UI](http://localhost:8081/archive-bucket/index.html), which should have been deployed to an S3 bucket inside LocalStack. The Web UI can be used to interact with the sample application, send new requests to the backend, inspect the state of existing requests, etc.

{{< alert title="Note" >}}
LocalStack on Kubernetes can be used in conjunction with the [LocalStack Community image](https://hub.docker.com/r/localstack/localstack). However, specific features such as execution of Lambda functions as Kubernetes pods is only available in the [LocalStack Pro image](https://hub.docker.com/r/localstack/localstack-pro).
{{< /alert >}}
