---
title: "Cloud Pod Remotes"
weight: 5
categories: ["LocalStack Pro", "Tools", "Persistence", "CLI"]
description: >
  Guide to the usage of Cloud Pods remotes
aliases:
  - /tools/cloud-pods/remotes/
---

{{< alert title="Beta">}}
Cloud Pod Remotes is a feature that is currently in beta.
{{< /alert >}}

A remote is the place where your Cloud Pods are stored.
By default, we store the Cloud Pods' artifacts into the LocalStack platform.
However, for various reason, e.g., data regulation and sovereignty, you might want to store Cloud Pods in a different location that is under your control.

We currently offer two alternative remotes:
- S3 bucket remote storage;
- [ORAS](https://oras.land/) (OCI Registry as Storage) remote storage.

## S3 bucket remote storage

## ORAS remote storage
The ORAS remote allow users to save Cloud Pods in registries such as Docker Hub, Nexus, or ECS registries.

As an example, let us demonstrate how it is possible to leverage Docker Hub to store and retrieve Cloud Pods.

At first, we need to configure the new remote with the LocalStack CLI.
We are going to export two environment variables, `ORAS_USERNAME` and `ORAS_PASSWORD` that are needed to authenticate with DockerHub.

```bash
export ORAS_USERNAME=docker_hub_id
export ORAS_PASSWORD=ILoveLocalStack1!
```

Then, I can use the CLI to create a new remote called `oras-remote`.

```shell
localstack pod remote add oras-remote oras://{oras_username}:{oras_password}@registry.hub.docker.com/<docker_hub_id>
```

Finally, I can save a pod with the just-configured remote, where `my-pod` is the name of the Cloud Pod while `oras-remote` is the name of the remote itself.

```shell
localstack pod save my-pod oras-remote
```

Similarly, I could perform the opposite operation and load a Cloud Pod from `oras-remote` with the following command:

```shell
localstack pod load my-pod oras-remote
```
