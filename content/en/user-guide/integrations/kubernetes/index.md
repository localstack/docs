---
title: Kubernetes
linktitle: Kubernetes
description: Running LocalStack on Kubernetes
---

## Introduction

[Kubernetes](https://kubernetes.io) is an open-source container orchestration platform that simplifies the deployment, scaling, and management of containerized applications. LocalStack can be deployed on Kubernetes using the [LocalStack Helm chart](http://helm.localstack.cloud).

{{< callout "warning" >}}
Creating shared/hosted LocalStack instances may have some licensing implications. For example, a valid license might be necessary for each user who interacts with the instance. If you have any questions or uncertainties regarding the licensing implications, we encourage you to [contact us](https://localstack.cloud/contact) for further details.
{{< /callout >}}

## Getting started

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

### Using Helm

After you have installed the Helm client, you can deploy a Helm chart into a Kubernetes cluster.

Please refer to the [Quick Start guide](https://helm.sh/docs/intro/quickstart/)  if you wish to get running in just a few commands, otherwise the [Using Helm guide](https://helm.sh/docs/intro/using_helm/) provides detailed instructions on how to use the Helm client to manage packages on your Kubernetes cluster.

Some useful Helm client commands are:

-   View available charts: `helm search repo`
-   Install a chart: `helm install <name> localstack/<chart>`
-   Upgrade your application: `helm upgrade`

## LocalStack on Kubernetes (`l8k`)

The [`localstack-on-k8s`](https://github.com/localstack/localstack-on-k8s) sample repository illustrates running LocalStack on Kubernetes (k8s).

### Prerequisites

This sample requires the following tools installed on your machine:

* Python 3.7+
* [`awslocal`](https://github.com/localstack/awscli-local)
* [Docker](https://www.docker.com)
* [Git](https://git-scm.com)
* [Helm](https://helm.sh)
* [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl)
* [Serverless](https://www.npmjs.com/package/serverless)

### Clone the sample repository

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
<disable-copy>
k3d-ls-cluster
</disable-copy>
{{< /command >}}

### Deploy the sample application

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

## Lambda on Kubernetes

LocalStack on Kubernetes can be used in conjunction with the [LocalStack Community image](https://hub.docker.com/r/localstack/localstack). However, specific features such as execution of Lambda functions as Kubernetes pods are only available in the [LocalStack Pro image](https://hub.docker.com/r/localstack/localstack-pro). To configure LocalStack Lambdas to use Kubernetes Pods, you need to configure values in the [LocalStack Helm Chart](https://github.com/localstack/helm-charts/blob/ce47b1590605901650ab788556bc871efbd78b8d/charts/localstack/values.yaml#L178-L208).

### Scaling Lambda Execution

The Kubernetes Lambda Executor in LocalStack handles Lambda execution scaling by spawning new environments (running in pods) when no existing environment is available due to concurrent invocations. An environment shuts down if it remains inactive for 10 minutes, a duration customizable through the `LAMBDA_KEEPALIVE_MS` variable. All environments terminate when LocalStack stops running.

### Lambda Scheduling Strategy

For multiple Lambda functions, the executor schedules according to Kubernetes cluster defaults without specifying node affinity. Users can assign labels to lambda pods using the `LAMBDA_K8S_LABELS` variable (e.g., `LAMBDA_K8S_LABELS=key=value,key2=value2`). The [Helm Charts](https://github.com/localstack/helm-charts), facilitates such advanced configurations, ensuring flexibility in node affinity decisions.

### Lambda Limitations and Configuration

LocalStack enforces timeout configurations similar to AWS, using the `Timeout` function parameter. There are no intrinsic limits on the number of Lambdas, with configurable limits on concurrent executions set at 1000 by default (`LAMBDA_LIMITS_CONCURRENT_EXECUTIONS`).

### Custom DNS for Lambda on Kubernetes

You can setup custom DNS configuration for Lambda on Kubernetes through the `LAMBDA_DOCKER_DNS` configuration variable.

### Customizing Lambda Runtime Behavior

Users can customize Lambda runtime behavior by building custom images based on provided ones, pushing them to their registry, and specifying these images using the `LAMBDA_RUNTIME_IMAGE_MAPPING` configuration variable, as detailed in the [documentation](https://docs.localstack.cloud/references/configuration/#lambda).

### Warm Start and Persistence

Lambda on Kubernetes supports Warm Start and Persistence. Persistence has to be configured for the LocalStack pod. The `/var/lib/localstack` directory has to be persisted over LocalStack runs, in a volume for example.

### Debugging Lambda on Kubernetes

Debugging is currently not supported. Lambda hot-reloading will not function, as the bind mounting into pods cannot be done at runtime.
