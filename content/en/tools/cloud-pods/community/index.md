---
title: "Cloud Pods for Community users"
weight: 3
categories: ["LocalStack", "Tools", "Persistence", "CLI"]
description: >
  LocalStack provides to community users a way to save and load your container state at will.
---

With the 1.3. release, we opened the Cloud Pods experience to our community users.
We introduced two new commands, `localstack pod save` and `localstack pod load`. 
With these two simple commands, community users are now able to dump their LocalStack container state, at any given moment in time, into a Cloud Pod. 

## Example
In this short tutorial, we will demonstrate how community users can leverage Cloud Pods to save permanently save their state.

To get started, you would only need `awscli` installed. No `LOCALSTACK_API_KEY` is required.

Let us start by creating some AWS resources in LocalStack. Just a mere example, let us create a S3 bucket and a SQS queue:

```bash
$ awslocal s3 mb s3://test
$ awslocal sqs create-queue --queue-name test-queue
```

Let us now dump such a simple state into a Cloud Pod, with the usage of the `localstack pod save` command. This command takes a file URI as an argument and creates a zip file in the specified directory.
Assume we want to create a pod named _awesome-pod_ in our Desktop folder (this example assumes you are on MacOS).
The following command will save a _awesome-pod_ zip file in your Desktop directory.

```bash
$ localstack pod save file:///Users/<my_username>/Desktop/awesome-pod
$ Cloud Pods file:///Users/<my_username>/Desktop/awesome-pod successfully exported
```

This exported zip file contains now the state we previously created and it can be restored at any time with the inverse command, i.e., `localstack pod load`.

For instance, the following command will restore the same state of a fresh instance of LocalStack:

```bash
$ localstack pod load file:///Users/<my_username>/Desktop/awesome-pod
$ Cloud Pods file:///Users/<my_username>/Desktop/awesome-pod successfully loaded
```

It is worth noting that the `load` command also offers the possibility to load a Cloud Pod stored at a given URL. We also provide a short-hand option to load Cloud Pods saved in a public GitHub repository.
To showcase this possibility, we opened a new public repository at [localstack/cloud-pods](https://github.com/localstack/cloud-pods) where we started storing several Cloud Pods for demonstration purposes.
As an example, we uploaded a Cloud Pod named _s3-trigger-thumbnail_ based on a [tutorial](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html) from the official AWS documentation.
This Cloud Pods stores a simple application consisting of two S3 buckets and a lambda function. For each _jpg_ image uploaded in one of the buckets, the lambda function will create a thumbnail of it and store it in the other bucket.

To load this Cloud Pod, you can run the following command:

```bash
$ localstack pod load git://localstack/cloud-pods/s3-trigger-thumbnail
```

Please not that the command above is equivalent to:

```bash
$ localstack pod load https://raw.githubusercontent.com/localstack/cloud-pods/main/s3-trigger-thumbnail
```

To test the loaded pod, you can just run

```bash
$ awslocal s3 cp <path_to_file>.jpg s3://img-bucket
```

and then check the content of the destination bucket

```bash
$ awslocal s3 ls s3://img-bucket-resized
```

## Limitations
Cloud Pods for community users have some limitations:
- only community-available services can be saved and loaded;
- users are responsible for storing their saved states; Pro users can take advantage of our Cloud Pods platform to make this task easier;
- Cloud Pods for community users do not support versioning out of the box;



