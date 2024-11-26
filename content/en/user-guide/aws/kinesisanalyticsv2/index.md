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
[Managed Service for Apache Flink (MSAF)](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) is an AWS service that provides the underlying infrastructure for running Apache Flink applications.

LocalStack lets you to run your Flink applications locally and implements [several common API operations](https://docs.localstack.cloud/references/coverage/coverage_kinesisanalyticsv2/).

{{< callout "note" >}}
The emulated MSAF provider was introduced in LocalStack v4.1 and was made the default.

If you wish to use the older mock provider, you can set `PROVIDER_OVERRIDE_KINESISANALYTICSV2=legacy`.
{{< /callout >}}


## Getting Started

This guide builds and deploys a demo Flink appplication to LocalStack.
The application generates synthetic records, processes them and sends the output to an S3 bucket.

Start your LocalStack container using your preferred method.

### Build Application Code

Start by clone the AWS sample repository.
We will use the [S3 Sink](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/S3Sink) application in this example.

{{< command >}}
$ git clone https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples.git
$ cd java/S3Sink
{{< /command >}}

Next, use [Maven](https://maven.apache.org/) to compile and package the Flink application.

{{< command >}}
$ mvn package
{{< /command >}}

This will build the Flink application jar file in the `./target/flink-kds-s3.jar` directory, which we will deploy to LocalStack MSAF next.

### Upload to S3

MSAF requires that all application code resides in S3.

Create an S3 bucket and upload the compiled Flink jar.

{{< command >}}
$ awslocal s3api create-bucket --bucket demo
$ awslocal s3api put-object --bucket demo --key job.jar --body ./target/flink-kds-s3.jar
{{< /command >}}

### Permissions

MSAF requires a service execution role which allows it to connect to other services.
Without the proper permissions policy and role, our example application will not be able to connect to S3 and save the output.

Create a permissions policy that allows read and write to S3.

```json
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
$ TODO
{{< /command >}}

Next, this policy is attached to an IAM role. MSAF assumes this role, and this gives it the necessary permissions to write to the sink.

```json
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


### Deploy Application



### Runtime Properties



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
- [Tagging](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging.html) is not supported
- In-place [version upgrades](https://docs.aws.amazon.com/managed-flink/latest/java/how-in-place-version-upgrades.html) and [roll-backs](https://docs.aws.amazon.com/managed-flink/latest/java/how-system-rollbacks.html) are not supported
- [Snapshot/savepoint management](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html) is not implemented
- Only S3 zipfile code is supported
- CloudWatch integration is not implemented
