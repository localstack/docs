---
title: CodePipeline
linkTitle: CodePipeline
description: >
  Get started with CodePipeline on LocalStack
tags: ["Pro image"]
---

## Introduction

CodePipeline is a continuous integration/continuous delivery (CI/CD) service offered by AWS.
CodePipeline can be used to create automated pipelines that handle the build, test and deployment of software.

LocalStack comes with a bespoke execution engine that can be used to create, manage and execute pipelines.
It supports a variety of actions that integrate with S3, CodeBuild, CodeConnections and more.
The available operations can be found on the [API coverage](https://docs.localstack.cloud/references/coverage/coverage_codepipeline/) page.

## Getting started

This guide is for users that are new to IoT and assumes a basic knowledge of the AWS CLI and LocalStack [`awslocal`](https://github.com/localstack/awscli-local) wrapper.

Start LocalStack using your preferred method.

In this guide, we will create a simple pipeline that fetches an object from an S3 bucket and uploads it to a different S3 bucket.

### Create prerequisite buckets

Start by creating the S3 buckets that will serve as the source and target.

{{< command >}}
$ awslocal s3 mb s3://source-bucket
$ awslocal s3 mb s3://target-bucket
{{< / command >}}

It is important to note the CodePipeline requires source S3 buckets to have versioning enabled.
This can be done using the S3 [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) operation.

{{< command >}}
$ awslocal s3api put-bucket-versioning \
    --bucket source-bucket \
    --versioning-configuration Status=Enabled
{{< /command >}}

Now create a placeholder file that will flow through the pipeline and upload it to the source bucket.

{{< command >}}
$ echo "Hello LocalStack!" > file
{{< /command >}}

{{< command >}}
$ awslocal s3 cp file s3://source-bucket
<disable-copy>
upload: ./file to s3://source-bucket/file
</disable-copy>
{{< /command >}}

Pipelines also require an artifact store, which is also an S3 bucket that is used as intermediate storage.

{{< command >}}
$ awslocal s3 mb s3://artifact-store-bucket
{{< / command >}}

### Configure IAM

Depending on the specifics of the declaration, CodePipeline pipelines need access other AWS services.
In this case we want our pipeline to retrieve and upload files to S3.
This requires a properly configured IAM role that our pipeline can assume.

Create the role as follows:

```json
# role.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "codepipeline.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

{{< command >}}
$ awslocal iam create-role --role-name role --assume-role-policy-document file://role.json
{{< /command >}}

Now add a permissions policy to this role that permits read and write access to S3.

```json
# policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}
```

The permissions in the above example policy are relatively broad.
You might want to use a more focused policy for better security.

{{< command >}}
$ awslocal iam put-role-policy --role-name role --policy-name policy --policy-document file://policy.json
{{< /command >}}

### Create pipeline

Now we can turn our attention to the pipeline declaration.

```json
{
  "name": "pipeline",
  "executionMode": "SUPERSEDED",
  "pipelineType": "V1",
  "roleArn": "<TODO>",
  "artifactStore": {
    "type": "S3",
    "location": "<TODO>"
  },
  "version": 1,
  "stages": [
    {
      "name": "stage1",
      "actions": [
        {
          "name": "action1",
          "actionTypeId": {
            "category": "Source",
            "owner": "AWS",
            "provider": "S3",
            "version": "1"
          },
          "runOrder": 1,
          "configuration": {
            "S3Bucket": "<TODO>",
            "S3ObjectKey": "<TODO>",
            "PollForSourceChanges": "false"
          },
          "outputArtifacts": [
            {
              "name": "intermediate-artifact-file"
            }
          ],
          "inputArtifacts": []
        }
      ]
    },
    {
      "name": "stage2",
      "actions": [
        {
          "name": "action1",
          "actionTypeId": {
            "category": "Deploy",
            "owner": "AWS",
            "provider": "S3",
            "version": "1"
          },
          "runOrder": 1,
          "configuration": {
            "BucketName": "<TODO>",
            "Extract": "false",
            "ObjectKey": "output-artifact-file"
          },
          "inputArtifacts": [
            {
              "name": "intermediate-artifact-file"
            }
          ],
          "outputArtifacts": []
        }
      ]
    }
  ]
}
```

## Tips

- Use `runOrder`


## Actions

CodePipeline on LocalStack supports the following actions:

### S3 Source

The [S3 Source](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3.html) action is used to specify an S3 bucket object as input to the pipeline.

### S3 Deploy

The [S3 Deploy](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3Deploy.html) action is used to upload artifacts to a given S3 bucket as the output of the pipeline.

### CodeConnections Source

The [CodeConnections Source](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html) action is used to specify a VCS repo as the input to the pipeline.

Currently LocalStack supports integration with [GitHub](https://github.com/).
Please set the environment configuration option `CODEPIPELINE_GH_TOKEN` with the GitHub Personal Access Token to be able to fetch private repositories.

### CodeBuild Source and Test

The [CodeBuild Source and Test](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeBuild.html) action can be used to start a CodeBuild container and run the given buildspec.

## Limitations

- [V2 pipeline types](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html) are not supported.
- [Rollbacks and stage retries](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-stages.html) are not available.
- [Triggers](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-triggers.html) are not implemented.
  Pipelines are executed only when [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html) and [StartPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html) are invoked.
