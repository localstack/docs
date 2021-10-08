---
title: "Elastic Kubernetes Service (EKS)"
linkTitle: "Elastic Kubernetes Service (EKS)"
categories: ["LocalStack Pro"]
description: >
  Elastic Kubernetes Service (EKS)
---
LocalStack Pro allows you to use the [EKS](https://docs.aws.amazon.com/eks/) API to create Kubernetes clusters and easily deploy containerized apps locally.

Please note that EKS requires an existing local Kubernetes installation. In recent versions of Docker, you can simply enable Kubernetes as an embedded service running inside Docker. See below for a screenshot of the Docker settings for Kubernetes in MacOS (similar configurations apply for Linux/Windows). By default, it is asssumed that Kubernetes API runs on the local TCP port `6443`.

![Kubernetes in Docker](kubernetes.png)

The example below illustrates how to create an EKS cluster configuration (assuming you have [`awslocal`](https://github.com/localstack/awscli-local) installed):
{{< command >}}
$ awslocal eks create-cluster --name cluster1 --role-arn r1 --resources-vpc-config '{}'
{
    "cluster": {
        "name": "cluster1",
        "arn": "arn:aws:eks:eu-central-1:000000000000:cluster/cluster1",
        "createdAt": "Sat, 05 Oct 2019 12:29:26 GMT",
        "endpoint": "https://172.17.0.1:6443",
        "status": "ACTIVE",
        ...
    }
}
$ awslocal eks list-clusters
{
    "clusters": [
        "cluster1"
    ]
}
{{< / command >}}
Simply configure your Kubernetes client (e.g., `kubectl` or other SDK) to point to the `endpoint` specified in the `create-cluster` output above. Depending on whether you're calling the Kubernetes API from the local machine or from within a Lambda, you may have to use different endpoint URLs (`https://localhost:6443` vs `https://172.17.0.1:6443`).
