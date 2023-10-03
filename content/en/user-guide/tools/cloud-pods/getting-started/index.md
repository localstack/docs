---
title: "Getting started with the Cloud Pods CLI"
weight: 3
categories: ["LocalStack Pro", "Tools", "Persistence", "CLI"]
description: >
  LocalStack provides a command line tool to manage the state of your instance via Cloud Pods.
aliases:
  - /tools/cloud-pods/getting-started/
---

Using the LocalStack Cloud Pods command-line interface (CLI) via the `pod` command enables you to create and manage cloud pods directly from your terminal. The Cloud Pods CLI is particularly useful in these scenarios:

-   Saving a snapshot of your active and running LocalStack instance.
-   Sharing your snapshots with teams using LocalStack's collaboration features.
-   Pulling snapshots to a running instance without needing to restart it.

## Installation

The LocalStack Cloud Pods CLI is included in the [LocalStack CLI installation](https://docs.localstack.cloud/getting-started/installation/#localstack-cli), so there's no need for additional installations to begin using it. If you're a licensed user, we suggest setting the `LOCALSTACK_API_KEY` as an environment variable. This enables you to access the complete range of LocalStack Cloud Pods features.

You can access the Cloud Pods CLI by running the `pod` command from your terminal.

{{< command >}}
$ localstack pod --help
Usage: localstack pod [OPTIONS] COMMAND [ARGS]...
<disable-copy>
  Manage the state of your instance via Cloud Pods.

Options:
  -h, --help  Show this message and exit.

Commands:
  delete    Delete a Cloud Pod
  inspect
  list      List all available Cloud Pods
  load
  remote    Manage cloud pod remotes
  save      Create a new Cloud Pod
  versions
</disable-copy>
{{< / command >}}

## Getting started

This guide is designed for users new to Cloud Pods and assumes basic knowledge of the LocalStack CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can save a snapshot of your active LocalStack instance into your LocalStack account, and pull it to a running instance.

### Create AWS resources

You can use the `awslocal` CLI to create new AWS resources within your active LocalStack instance. For example, you can create an S3 bucket and add data to it using the `awslocal` CLI:

{{< command >}}
$ awslocal s3 mb s3://test
$ echo "hello world" > /tmp/hello-world
$ awslocal s3 cp /tmp/hello-world s3://test/hello-world
$ awslocal s3 ls s3://test/
{{< / command >}}

### Save your Pod state

You can now your Pod state using the `save` command, specifying the desired Cloud Pod name as the first argument. This action will save the pod and register it with the LocalStack Web Application:
   
{{< command >}}
$ localstack pod save s3-test
<disable-copy>
Cloud Pod `s3-test` successfully created ✅
Version: 1
Remote: platform
Services: s3
</disable-copy>
{{< / command >}}

Optionally, you can include a message with the saved Cloud Pod using the `--message` flag.

You can access the list of available Cloud Pods for both you and your organization by utilizing the `list` command:

{{< command >}}
$ localstack pod list
<disable-copy>
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Name                      ┃ Max Version ┃ Last Change ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ s3-test                   │ 1           │ n/a         │
└───────────────────────────┴─────────────┴─────────────┘
</disable-copy>
{{< / command >}}

### Inspect the contents of a Cloud Pod

4. Optional: You can inspect the contents of a Cloud Pod using the `inspect` command: 

{{< command >}}
$ localstack pod inspect s3-test --format json
<disable-copy>
{
    "000000000000": {
        "S3": {
            "global": {
                "listBuckets": {
                    "Buckets": [
                        {
                            "Name": "test",
                            "CreationDate": "2023-10-03T07:19:31.000Z"
                        }
                    ],
                }
            }
        }
    }
}
</disable-copy>
{{< / command >}}

### Pull your Pod state

 On a separate machine, start LocalStack while ensuring the API key is properly configured. Then, retrieve the previously created Cloud Pod by employing the `load` command, specifying the Cloud Pod name as the first argument:

{{< command >}}
$ localstack pod load s3-test
<disable-copy>
Cloud Pod s3-test successfully loaded
</disable-copy>
{{< / command >}}

Let's examine the S3 buckets within our Cloud Pod:

{{< command >}}
$ awslocal s3 ls s3://test/
<disable-copy>
2022-10-04 22:33:54         12 hello-world
</disable-copy>
{{< / command >}}

For comprehensive instructions, navigate to our [Command-Line Interface (CLI) Guide]({{< ref "pods-cli" >}}). To access your Cloud Pods through the LocalStack Web Application, simply go to the [Cloud Pods page](https://app.localstack.cloud/pods).
