---
title: "Elastic Transcoder"
linkTitle: "Elastic Transcoder"
description: Get started with Elastic Transcoder on LocalStack
tags: ["Base"]
---

## Introduction

Elastic Transcoder is a managed service that facilitates the transcoding of multimedia files into various formats to ensure compatibility across devices.
Elastic Transcoder manages the underlying resources, ensuring high availability and fault tolerance.
It also supports a wide range of input and output formats, enabling users to efficiently process and deliver video content at scale.

LocalStack allows you to mock the Elastic Transcoder APIs in your local environment.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_elastictranscoder/), which provides information on the extent of Elastic Transcoder's integration with LocalStack.

## Getting started

This guide is designed for users new to Elastic Transcoder and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an Elastic Transcoder pipeline, read the pipeline, and list all pipelines using the AWS CLI.

### Create S3 buckets

You can create S3 buckets using the [`mb`](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html) API.
Execute the following command to create two buckets named `elasticbucket` and `outputbucket`:

{{< command >}}
$ awslocal s3 mb s3://elasticbucket
$ awslocal s3 mb s3://outputbucket
{{< /command >}}

### Create an Elastic Transcoder pipeline

You can create an Elastic Transcoder pipeline using the [`CreatePipeline`](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/create-pipeline.html) API.
Execute the following command to create a pipeline named `test-pipeline`:

{{< command >}}
$ awslocal elastictranscoder create-pipeline \
    --name Default \
    --input-bucket elasticbucket \
    --output-bucket outputbucket \
    --role arn:aws:iam::000000000000:role/Elastic_Transcoder_Default_Role
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Pipeline": {
        "Id": "0998507242379-vltecz",
        "Arn": "arn:aws:elastictranscoder:us-east-1:000000000000:pipeline/0998507242379-vltecz",
        "Name": "Default",
        "Status": "Active",
        "InputBucket": "elasticbucket",
        "OutputBucket": "outputbucket",
        "Role": "arn:aws:iam::000000000000:role/Elastic_Transcoder_Default_Role",
        "Notifications": {
            "Progressing": "",
            "Completed": "",
            "Warning": "",
            "Error": ""
        },
        "ContentConfig": {
            "Bucket": "outputbucket",
            "Permissions": []
        },
        "ThumbnailConfig": {
            "Bucket": "outputbucket",
            "Permissions": []
        }
    },
    "Warnings": []
}
```

### List the pipelines

You can list all pipelines using the [`ListPipelines`](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/list-pipelines.html) API.
Execute the following command to list all pipelines:

{{< command >}}
$ awslocal elastictranscoder list-pipelines
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Pipelines": [
        {
            "Id": "0998507242379-vltecz",
            "Arn": "arn:aws:elastictranscoder:us-east-1:000000000000:pipeline/0998507242379-vltecz",
            "Name": "Default",
            "Status": "Active",
            "InputBucket": "elasticbucket",
            "OutputBucket": "outputbucket",
            "Role": "arn:aws:iam::000000000000:role/Elastic_Transcoder_Default_Role",
            "Notifications": {
                "Progressing": "",
                "Completed": "",
                "Warning": "",
                "Error": ""
            },
            "ContentConfig": {
                "Bucket": "outputbucket",
                "Permissions": []
            },
            "ThumbnailConfig": {
                "Bucket": "outputbucket",
                "Permissions": []
            }
        }
    ]
}
```

### Read the pipeline

You can read a pipeline using the [`ReadPipeline`](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/read-pipeline.html) API.
Execute the following command to read the pipeline with the ID `0998507242379-vltecz`:

{{< command >}}
$ awslocal elastictranscoder read-pipeline --id 0998507242379-vltecz
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Pipeline": {
        "Id": "0998507242379-vltecz",
        "Arn": "arn:aws:elastictranscoder:us-east-1:000000000000:pipeline/0998507242379-vltecz",
        "Name": "Default",
        "Status": "Active",
        "InputBucket": "elasticbucket",
        "OutputBucket": "outputbucket",
        "Role": "arn:aws:iam::000000000000:role/Elastic_Transcoder_Default_Role",
        "Notifications": {
            "Progressing": "",
            "Completed": "",
            "Warning": "",
            "Error": ""
        },
        "ContentConfig": {
            "Bucket": "outputbucket",
            "Permissions": []
        },
        "ThumbnailConfig": {
            "Bucket": "outputbucket",
            "Permissions": []
        }
    }
}
```
