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
Cloud Pod Remotes is a feature that is currently in beta (available in the Team product tier).
{{< /alert >}}

A remote is the place where your Cloud Pods are stored.
By default, we store the Cloud Pods' artifacts in the LocalStack platform.
Although we provide the highest levels of security and isolation (incl. encryption in transit and at rest), there may be situations (e.g., due to data regulation and sovereignty) where your organization does not permit storing Cloud Pod assets in a remote storage infrastructure. 
Hence, you may want to persist Cloud Pods in a different storage location that is on-premise and fully under your control.

We currently offer two alternative remotes:
- S3 bucket remote storage;
- [ORAS](https://oras.land/) (OCI Registry as Storage) remote storage.

Our Cloud Pods command-line interface (CLI) has been expanded and now offers commands to create and delete remotes:

```bash
localstack pod remote --help
Usage: localstack pod remote [OPTIONS] COMMAND [ARGS]...

  Manage cloud pod remotes

Options:
  -h, --help  Show this message and exit.

Commands:
  add     Add a remote
  delete  Delete a remote
```

Moreover, the `localstack pod remotes` command will show all the registered remotes.

## S3 bucket remote storage
The S3 storage lets you store Cloud Pods into any arbitrary S3 bucket.
The first step is to export proper AWS credentials in the terminal session.

```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

A possible option is to obtain credentials via [AWS SSO CLI](https://github.com/synfinatic/aws-sso-cli).

Afterwards, we have to add a new remote that explicitly targets a S3 bucket.
With the command below, we are creating a new remote called `s3-storage-aws` that will store the Cloud Pods' artifacts into a S3 bucket name `ls-pods-bucket-test`.
The `access_key_id` and `secret_access_key` placeholder will make sure that the AWS credentials are correctly passed to the container.

```bash
$ localstack pod remote add s3-storage-aws 's3://ls-pods-bucket-test/?access_key_id={access_key_id}&secret_access_key={secret_access_key}'
```

Finally, we can use the usual `pod` CLI command to create a new pod that targets the created remote.

```bash
localstack pod save my-pod s3-storage-aws
```

After issuing the command, we can verify that the S3 buckets now contains the pod artifacts by simply running:

```bash
aws s3 ls s3://ls-pods-bucket-test
2023-09-27 13:50:10      83650 localstack-pod-my-pod-state-1.zip
2023-09-27 13:50:11      85103 localstack-pod-my-pod-version-1.zip
```

With the `pod load` command we can later load the same pod saved into this remote:

```bash
localstack pod load my-pod s3-storage-aws
```

## ORAS remote storage
The ORAS remote allows users to save Cloud Pods in registries such as Docker Hub, Nexus, or ECS registries.

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

### Miscellaneous
When not differently specified, all Cloud Pods' commands target our Platform as default remote.

The configuration for a custom remote is saved inside the LocalStack container.
Therefore, if you want to share Cloud Pods within your team using a custom remote, each team member would need to have the same remote configuration.
Once added, a remote is persisted across LocalStack restarts.