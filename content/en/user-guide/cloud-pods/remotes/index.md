---
title: "Remotes"
weight: 5
description: The reference guide for LocalStack Cloud Pods remotes and how to get started on using them!
aliases:
  - /user-guide/cloud-pods/remotes/
---

A remote is the location where Cloud Pods are stored. By default, Cloud Pod artifacts are stored in the LocalStack platform. However, if your organization's data regulations or sovereignty requirements prohibit storing Cloud Pod assets in a remote storage infrastructure, you have the option to persist Cloud Pods in an on-premises storage location under your complete control.

{{< alert title="Beta">}}
Cloud Pod Remotes is a beta feature exclusively accessible within the Team product tier.
{{< /alert >}}

## Overview

LocalStack provides two types of alternative remotes:

-   S3 bucket remote storage.
-   [ORAS](https://oras.land/) (OCI Registry as Storage) remote storage.

Cloud Pods command-line interface (CLI) allows you to create, delete, and list remotes.

{{< command >}}
$ localstack pod remote --help
<disable-copy> 
Usage: localstack pod remote [OPTIONS] COMMAND [ARGS]...

  Manage cloud pod remotes

Options:
  -h, --help  Show this message and exit.

Commands:
  add     Add a remote
  delete  Delete a remote
  list    List the available remotes
</disable-copy>
{{< / command >}}

## S3 bucket remote storage

The S3 remote enables you to store Cloud Pod assets in an existing S3 bucket within an actual AWS account. The initial step is to export the necessary AWS credentials within the terminal session.

```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

A possible option is to obtain credentials via [AWS SSO CLI](https://github.com/synfinatic/aws-sso-cli).

One option is to acquire credentials using [AWS SSO CLI](https://github.com/synfinatic/aws-sso-cli).

Next, we establish a new remote specifically designed for an S3 bucket. By running the following command, we create a remote named `s3-storage-aws` responsible for storing Cloud Pod artifacts in an S3 bucket called `ls-pods-bucket-test`. 

The `access_key_id` and `secret_access_key` placeholders ensure the correct transmission of AWS credentials to the container.

{{< command >}}
$ localstack pod remote add s3-storage-aws 's3://ls-pods-bucket-test/?access_key_id={access_key_id}&secret_access_key={secret_access_key}'
{{< / command >}}

Lastly, you can utilize the standard `pod` CLI command to generate a new Cloud Pod that points to the previously established remote.

{{< command >}}
$ localstack pod save my-pod s3-storage-aws
{{< / command >}}

Once the command has been executed, you can confirm the presence of Cloud Pod artifacts in the S3 bucket by simply running:

```bash
aws s3 ls s3://ls-pods-bucket-test
2023-09-27 13:50:10      83650 localstack-pod-my-pod-state-1.zip
2023-09-27 13:50:11      85103 localstack-pod-my-pod-version-1.zip
```

You can use the `pod load` command to load the same pod that was previously saved in this remote:

{{< command >}}
$ localstack pod load my-pod s3-storage-aws
{{< / command >}}

## ORAS remote storage

The ORAS remote enables users to store Cloud Pods in OCI-compatible registries like Docker Hub, Nexus, or ECS registries. ORAS stands for "OCI Registry as Service," and you can find additional information about this standard [on the official website](https://oras.land/).

For example, let's illustrate how you can utilize Docker Hub to store and retrieve Cloud Pods.

To begin, you must configure the new remote using the LocalStack CLI. You'll need to export two essential environment variables, `ORAS_USERNAME` and `ORAS_PASSWORD`, which are necessary for authenticating with Docker Hub.

```bash
export ORAS_USERNAME=docker_hub_id
export ORAS_PASSWORD=ILoveLocalStack1!
```

You can now use the CLI to create a new remote called `oras-remote`.

{{< command >}}
$ localstack pod remote add oras-remote 'oras://{oras_username}:{oras_password}@registry.hub.docker.com/<docker_hub_id>'
{{< / command >}}

Lastly, you can store a pod using the newly configured remote, where `my-pod` represents the Cloud Pod's name, and `oras-remote` is the remote's name.

{{< command >}}
$ localstack pod save my-pod oras-remote
{{< / command >}}

Likewise, you can execute the reverse operation to load a Cloud Pod from `oras-remote` using the following command:

{{< command >}}
$ localstack pod load my-pod oras-remote
{{< / command >}}

### Miscellaneous

Unless explicitly specified, all Cloud Pods commands default to targeting the LocalStack Platform as the storage remote. It's important to note that the CLI must be authenticated correctly with our Platform, and a Team/Enterprise subscription is mandatory.

Custom remote configurations are stored within the [LocalStack volume directory](https://docs.localstack.cloud/references/filesystem/#localstack-volume-directory) and are managed by the LocalStack container. Consequently, when sharing Cloud Pods among your team using a custom remote, each team member must define the identical remote configuration. Once added, a remote persists even after LocalStack restarts.
