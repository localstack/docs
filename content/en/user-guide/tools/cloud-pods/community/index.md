---
title: "Community Cloud Pods"
weight: 4
description: >
  Get started with LocalStack Community Cloud Pods to to save and load your container state at will
---

{{< alert title="Note" >}}
With the release of LocalStack 2.3, we have officially marked Community Cloud Pods as **deprecated**. In our upcoming 3.0 release, we will be removing Community Cloud Pods entirely. Moving forward, Cloud Pods will only be accessible to Pro/Team users. We understand this may affect some users and we are open to feedback, through our [GitHub Issues](https://github.com/localstack/localstack) or [Discuss Forum](https://discuss.localstack.cloud/).
{{< /alert >}}

LocalStack supports Community Cloud Pods to give our community users a limited Cloud Pods experience. Using Community Cloud Pods, you get two commands: `save` and `load` to save the container state in a Cloud Pod and dump it into their running LocalStack container at any given time, respectively.

## Getting started

In this getting started guide, we will demonstrate how community users can leverage Community Cloud Pods to save the state of their running LocalStack instance permanently. To get started, you would only need `awscli` installed. We intend this feature to be open to community users; hence no `LOCALSTACK_API_KEY` is required.

Let us start by creating some AWS resources in LocalStack. Just a mere example, let us create a S3 bucket and a SQS queue:

{{< command >}}
$ awslocal s3 mb s3://test
$ awslocal sqs create-queue --queue-name test-queue
{{< /command >}}

Let us dump such a simple state into a Cloud Pod using the `save` command. This command takes a file URI as an argument and creates a ZIP file in the specified directory. Assuming we want to create a pod named `awesome-pod` in our Desktop folder, we will run the below commands to save an `awesome-pod` in your Desktop directory:

{{< command >}}
$ localstack pod save file:///Users/<my_username>/Desktop/awesome-pod
Cloud Pods file:///Users/<my_username>/Desktop/awesome-pod successfully exported
{{< /command >}}

This exported ZIP file now contains the state we previously created, and we can restore it at any time with the inverse command, i.e., `load`. For instance, the following command will restore the same state of a fresh instance of LocalStack:

{{< command >}}
$ localstack pod load file:///Users/<my_username>/Desktop/awesome-pod
Cloud Pods file:///Users/<my_username>/Desktop/awesome-pod successfully loaded
{{< /command >}}

It is worth noting that the `load` command also allows loading a Cloud Pod stored at a given URL. We also provide a short-hand option to load Cloud Pods saved in a public GitHub repository. To showcase this possibility, we opened a new public repository at [localstack/cloud-pods](https://github.com/localstack/cloud-pods), where we started storing several Cloud Pods for demonstration purposes.

For example, we uploaded a Cloud Pod named `s3-trigger-thumbnail` based on an [official AWS documentation tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html). This Cloud Pod stores a simple application consisting of two S3 buckets and a Lambda function. For each `jpg` image uploaded in one of the buckets, the Lamda function will create a thumbnail of it and store it in the other bucket.

To load this Cloud Pod, you can run the following command:

{{< command >}}
$ localstack pod load git://localstack/cloud-pods/s3-trigger-thumbnail
{{< /command >}}

{{< alert title="Note" >}}
The above command is equivalent to:

{{< command >}}
$ localstack pod load https://raw.githubusercontent.com/localstack/cloud-pods/main/s3-trigger-thumbnail
{{< /command >}}
{{< /alert >}}

To test the loaded pod, you can run the following command:

{{< command >}}
$ awslocal s3 cp <path_to_file>.jpg s3://img-bucket
{{< /command >}}

To check the content of the destination bucket run the following command:

{{< command >}}
$ awslocal s3 ls s3://img-bucket-resized
{{< /command >}}

## Limitations

Community Cloud Pods have some limitations:

- Only Community-available AWS services can be saved and loaded in a Community Cloud Pod.
- Users are responsible for storing their saved states. Pro users can use our Cloud Pods platform to make storing and sharing their saved states easier.
- Cloud Pods for Community users do not support versioning out of the box. 
