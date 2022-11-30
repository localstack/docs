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

This tutorial is intended for licensed users. The Community users can replicate a similar workflow by leveraging the `save` and `load` commands available to them. For more details, look at our [Community Cloud Pods guide]({{< ref "community" >}}).

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

2. Save your Pod state using the `save` command by specifying the desired name as the first argument. This command will save the pod and register it to the remote platform. Optionally you can attach a message to the saved Cloud Pod with the `--message` flag:
   
   {{< command >}}
   $ localstack pod save <pod-name> --message "<description-message>"
   {{< / command >}}

3. Check the list of Cloud Pods available to you and your organization using the `list` command:

   {{< command >}}
   $ localstack pod list
    ┏━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
    ┃ local/remote ┃ Name      ┃
    ┡━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
    │ local+remote │ pod-name  │
    └──────────────┴───────────┘
   {{< / command >}}

4. Optional: You can inspect the contents of a Cloud Pod using the `inspect` command: 

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

5. On an alternate machine, start LocalStack with the API key configured, and pull the Cloud Pod we created previously using `load` command with the Cloud Pod name as the first argument:

   {{< command >}}
   $ localstack pod load <pod-name>

   Done.
   {{< / command >}}

   Let's check the S3 buckets in our Cloud Pod: 
   {{< command >}}
   $ awslocal s3 ls s3://test/

   2022-10-04 22:33:54         12 hello-world
   {{< / command >}}

6. Optional: You can make the Cloud Pod available to users outside your organization by making it public:

   {{< command >}}
   $ localstack pod save <pod-name> --visibility public
   {{< / command >}}

For a more detailed manual, refer to our [command-line interface (CLI) guide]({{< ref "pods-cli" >}}). To check your Pods on the LocalStack Web user interface, navigate to [Cloud Pods page](https://app.localstack.cloud/pods).