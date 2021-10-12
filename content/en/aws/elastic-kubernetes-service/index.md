---
title: "Elastic Kubernetes Service (EKS)"
linkTitle: "Elastic Kubernetes Service (EKS)"
categories: ["LocalStack Pro"]
description: >
  Elastic Kubernetes Service (EKS)
---
LocalStack Pro allows you to use the [EKS](https://docs.aws.amazon.com/eks/) API to create Kubernetes clusters and easily deploy containerized apps locally.

There are two modes for creating EKS clusters on LocalStack:
* spinning up an embedded kube cluster in your local Docker engine (preferred, simpler), or
* using an existing Kubernetes installation you can access from your local machine (defined in `$HOME/.kube/config`)

## Auto-installing an embedded Kubernetes cluster

The default method for creating Kubernetes clusters via the local EKS API is to spin up an embedded [k3d](https://k3d.io) kube cluster within Docker. LocalStack handles the download and installation transparently - on most systems the installation is performed automatically, and no customizations should be required.

A new cluster can be created using the following command:
{{< command >}}
$ awslocal eks create-cluster --name cluster1 --role-arn r1 --resources-vpc-config '{}'
{{</ command >}}

You should then see some Docker containers getting started, e.g.:
{{< command >}}
$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS          PORTS                                           NAMES
b335f7f089e4   rancher/k3d-proxy:5.0.1-rc.1   "/bin/sh -c nginx-pr…"   1 minute ago   Up 1 minute   0.0.0.0:8081->80/tcp, 0.0.0.0:44959->6443/tcp   k3d-cluster1-serverlb
f05770ec8523   rancher/k3s:v1.21.5-k3s2       "/bin/k3s server --t…"   1 minute ago   Up 1 minute
{{</ command >}}

Once the cluster has been created and initialized, we can determine the server `endpoint`:
{{< command >}}
% awslocal eks describe-cluster --name cluster1
{
    "cluster": {
        "name": "cluster1",
        "status": "ACTIVE",
        "endpoint": "https://localhost.localstack.cloud:4513",
        ...
    }
}
{{</ command >}}

We can then configure the `kubectl` command line with the new cluster endpoint:
{{< command >}}
$ kubectl config set-cluster cluster1 --server=https://localhost.localstack.cloud:4513
{{</ command >}}

### Troubleshooting

In case you're seeing an SSL certificate error when creating an EKS cluster using Terraform:
```
Error: Kubernetes cluster unreachable: Get "https://localhost.localstack.cloud:4510/version?timeout=32s": x509: certificate signed by unknown authority
```
... you may need to download the following key file which contains a test SSL certificate:
{{< command >}}
$ wget https://github.com/localstack/localstack-artifacts/raw/master/local-certs/server.key
{{</ command >}}
... and then add the following config to your Terraform provider section:
```terraform
provider "kubernetes" {
  cluster_ca_certificate = "${file("server.key")}"
}
```

## Using an existing Kubernetes installation

You can also use the EKS API using an existing local Kubernetes installation. This works by mounting the `$HOME/.kube/config` file into the LocalStack container - e.g., when using docker-compose.yml:
```yaml
volumes:
  - "${HOME}/.kube/config:/root/.kube/config"
```

In recent versions of Docker, you can simply enable Kubernetes as an embedded service running inside Docker. See below for a screenshot of the Docker settings for Kubernetes in MacOS (similar configurations apply for Linux/Windows). By default, it is asssumed that Kubernetes API runs on the local TCP port `6443`.

<img src="kubernetes.png" alt="Kubernetes in Docker" title="Kubernetes in Docker" width="450" />

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
