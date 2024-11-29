---
title: "Managed Service for Apache Flink"
linkTitle: "Managed Service for Apache Flink"
description: >
  Get started with Managed Service for Apache Flink on LocalStack
tags: ["Pro image"]
---

{{< callout >}}
This service was formerly known as 'Kinesis Data Analytics for Apache Flink'.
{{< /callout >}}

## Introduction

[Apache Flink](https://flink.apache.org/) is a framework for building applications that process and analyze streaming data.
[Managed Service for Apache Flink (MSAF)](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) is an AWS service that provides the underlying infrastructure and a hosted Apache Flink cluster that can run Apache Flink applications.

LocalStack lets you to run Flink applications locally and implements several [AWS-compatible API operations](https://docs.localstack.cloud/references/coverage/coverage_kinesisanalyticsv2/).

{{< callout "note" >}}
The emulated MSAF provider was introduced and made the default in LocalStack v4.1.

If you wish to use the older mock provider, you can set `PROVIDER_OVERRIDE_KINESISANALYTICSV2=legacy`.
{{< /callout >}}

## Getting Started

This guide builds a demo Flink application and deploys it to LocalStack.
The application generates synthetic records, processes them and sends the output to an S3 bucket.

Start the LocalStack container using your preferred method.

### Build Application Code

Begin by cloning the AWS sample repository.
We will use the [S3 Sink](https://github.com/localstack-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/S3Sink) application in this example.

{{< command >}}
$ git clone https://github.com/localstack-samples/amazon-managed-service-for-apache-flink-examples.git
$ cd java/S3Sink
{{< /command >}}

Next, use [Maven](https://maven.apache.org/) to compile and package the Flink application into a jar.

{{< command >}}
$ mvn package
{{< /command >}}

The Flink application jar file will be placed in the `./target/flink-kds-s3.jar` directory.

### Upload Application Code

MSAF requires that all application code resides in S3.

Create an S3 bucket and upload the compiled Flink application jar.

{{< command >}}
$ awslocal s3api create-bucket --bucket flink-bucket
$ awslocal s3api put-object --bucket flink-bucket --key job.jar --body ./target/flink-kds-s3.jar
{{< /command >}}

### Output Sink

As mentioned earlier, this Flink application writes the output to an S3 bucket.

Create the S3 bucket that will serve as the sink.

{{< command >}}
$ awslocal s3api create-bucket --bucket sink-bucket
{{< /command >}}

### Permissions

MSAF requires a service execution role which allows it to connect to other services.
Without the proper permissions policy and role, this example application will not be able to connect to S3 sink bucket to output the result.

Create an IAM role for the running MSAF application to assume.

```json
# role.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "kinesisanalytics.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}
```

{{< command >}}
$ awslocal iam create-role --role-name msaf-role --assume-role-policy-document file://role.json
{{< /command >}}

Next create add a permissions policy to this role that permits read and write access to S3.

```json
# policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:GetObjectVersion", "s3:PutObject"],
            "Resource": "*"
        }
    ]
}
```

{{< command >}}
$ awslocal iam put-role-policy --role-name msaf-role --policy-name msaf-policy --policy-document file://policy.json
{{< /command >}}

Now, when the running MSAF application assumes this role, it will have the necessary permissions to write to the S3 sink.

### Deploy Application

With all prerequisite resources in place, the Flink application can now be created and started.

{{< command >}}
$ awslocal kinesisanalyticsv2 create-application \
    --application-name msaf-app \
    --runtime-environment FLINK-1_20 \
    --application-mode STREAMING \
    --service-execution-role arn:aws:iam::000000000000:role/msaf-role \
    --application-configuration '{
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation": {
                    "BucketARN": "arn:aws:s3:::flink-bucket",
                    "FileKey": "job.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        },
        "EnvironmentProperties": {
            "PropertyGroups": [{
                "PropertyGroupId": "bucket", "PropertyMap": {"name": "sink-bucket"}
            }]
        }
    }'

$ awslocal kinesisanalyticsv2 start-application --application-name msaf-app
{{< /command >}}

Once the Flink cluster is up and running, the application will stream the results to the sink S3 bucket.
You can verify this with:

{{< command >}}
$ awslocal s3api list-objects --bucket sink-bucket
{{< /command >}}

## Supported Flink Versions

| Flink version | Supported by LocalStack | Supported by Apache |
|:---:|:---:|:---:|
| 1.20.0 | yes | yes |
| 1.19.1 | yes | yes |
| 1.18.1 | yes | yes |
| 1.15.2 | yes | yes |
| 1.13.1 | yes | no |

## Limitations

- Application versions are not maintained
- Only S3 zipfile code is supported
- Values of 20,000 ms for `execution.checkpointing.interval` and 5,000 ms for `execution.checkpointing.min-pause` are used for checkpointing. They can not be overridden.
- [Tagging](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging.html) is not supported
- In-place [version upgrades](https://docs.aws.amazon.com/managed-flink/latest/java/how-in-place-version-upgrades.html) and [roll-backs](https://docs.aws.amazon.com/managed-flink/latest/java/how-system-rollbacks.html) are not supported
- [Snapshot/savepoint management](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html) is not implemented
- CloudWatch and CloudTrail integration is not implemented
