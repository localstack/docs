---
title: "Getting started with the Cloud Pods CLI"
weight: 3
categories: ["LocalStack Pro", "Tools", "Persistence", "CLI"]
description: >
  LocalStack provides a command line tool to manage the state of your instance via Cloud Pods.
aliases:
  - /tools/cloud-pods/getting-started/
---

With the LocalStack Cloud Pods command-line interface (CLI), the `pod` command, you can create cloud pods and manage them from a terminal. The Cloud Pods CLI is ideal in the following situations:

- Taking a snapshot of your running LocalStack instance.
- Sharing your snapshot across teams with LocalStack Team features.
- Injecting snapshots into a running instance without a restart.

## Installation

LocalStack Cloud Pods CLI is directly available with the LocalStack installation, and no further installation is required to get started. If you are a Pro user, we recommend you to export the `LOCALSTACK_API_KEY` as an environment variable to allow you to use the full spectrum of LocalStack Cloud Pods feature. 

For Community users, we recommend you to use a different remote, with public GitHub repositories being the recommended way to store your Cloud Pods data. The creation of pods (with the `export` command) would require a Pro account, but the pulling and injection of public community pods (read-only) would work with Community as well.

## Basic example

In this tutorial, you'll learn how to make a basic usage of LocalStack Cloud Pods CLI. This tutorial is intended for Pro users who wish to get more acquainted with Cloud Pods CLI. It assumes you have basic knowledge of:

- LocalStack
- `awscli` commands 
- Understanding of Cloud Pods workflow 

By the end of this tutorial, you would be able to create a snapshot of your running LocalStack instance, commit it and would be able to push this to your LocalStack account.

### Procedure

To get started, start your LocalStack instance with your `LOCALSTACK_API_KEY` configured as an environment variable: 

1. Use the `awslocal` CLI to create AWS resources inside your running LocalStack instance.
   
   As an example, we will create a S3 bucket using the `awslocal` CLI and enter some data inside it:

   {{< command >}}
   $ awslocal s3 mb s3://test
   $ echo "hello world" > /tmp/hello-world
   $ awslocal s3 cp /tmp/hello-world s3://test/hello-world
   $ awslocal s3 ls s3://test/
   {{< / command >}}

2. Create a Cloud Pod using the `--name` flag to specify the Pod name:

   {{< command >}}
   $ localstack pod config --name <pod-name>
   {{< / command >}}

3. Optional: You can also specify a list of services for your Cloud Pod with the following command:

   {{< command >}}
   $ localstack pod config --services <comma-seperated-services-names>
   {{< / command >}}

4. Commit your Pod state using the `commit` command by specifying the `--name` and `--message` flag to specify the Pod name your created previously and the commit message associated with the change:
   
   {{< command >}}
   $ localstack pod commit --name <pod-name> --message "<commit-message>"
   {{< / command >}}

5. Check the list of Cloud Pods on your machine using the `list` command:

   {{< command >}}
   $ localstack pod list
    ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
    ┃ local/remote ┃ Name      ┃
    ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
    │ local        │ pod-name  │
    └──────────────┴───────────┘
   {{< / command >}}

6. Optional: You can inspect the contents of a Cloud Pod using the `inspect` command: 

   {{< command >}}
   $ localstack pod inspect --name <pod-name>
    - 000000000000
        - S3
        - global
            - listBuckets
            - Buckets
                - 0
                - Name = test
                - CreationDate = 2022-10-04T17:03:47.000Z
            - Owner
                - DisplayName = webfile
                - ID = bcaf1ffd86f41161ca5fb16fd081034f
   {{< / command >}}

7. Push the Cloud Pod to LocalStack's remote storage using `push` command with the `--name` flag and the `--message` flag:

   {{< command >}}
   $ localstack pod push --name <pod-name> --message "<message>"

   Successfully pushed the current state
   Successfully registered <pod-name> with remote!
   {{< / command >}}

   To publish your Cloud Pod locally, prefer using the `--local` flag to publish it.

8. On an alternate machine, start LocalStack with the API key configured, and pull the Cloud Pod we created previously using `pull` command with the `--name` flag:

   {{< command >}}
   $ localstack pod pull --name <pod-name>

   Done.
   {{< / command >}}

   Let's check the S3 buckets in our Cloud Pod: 
   {{< command >}}
   $ awslocal s3 ls s3://test/

   2022-10-04 22:33:54         12 hello-world
   {{< / command >}}

For a more detailed manual, refer to our [command-line interface (CLI) guide]({{< ref "pods-cli" >}}). To check your Pods on the LocalStack Web user-interface, navigate to [Cloud Pods page](https://app.localstack.cloud/pods).