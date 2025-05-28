---
title: "Managed Service for Apache Flink"
linkTitle: "Managed Service for Apache Flink"
description: >
  Get started with Managed Service for Apache Flink on LocalStack
tags: ["Ultimate"]
---

{{< callout >}}
This service was formerly known as 'Kinesis Data Analytics for Apache Flink'.
{{< /callout >}}

## Introduction

[Apache Flink](https://flink.apache.org/) is a framework for building applications that process and analyze streaming data.
[Managed Service for Apache Flink (MSF)](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) is an AWS service that provides the underlying infrastructure and a hosted Apache Flink cluster that can run Apache Flink applications.

LocalStack lets you to run Flink applications locally and implements several [AWS-compatible API operations](https://docs.localstack.cloud/references/coverage/coverage_kinesisanalyticsv2/).

A separate Apache Flink cluster is started in [application mode](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/deployment/overview/#application-mode) for every Managed Flink application created.
Flink cluster deployment on LocalStack consists of two separate containers for [JobManager](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/flink-architecture/#jobmanager) and [TaskManager](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/flink-architecture/#taskmanagers).

{{< callout "note" >}}
The emulated MSF provider was introduced and made the default in LocalStack v4.1.

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

MSF requires that all application code resides in S3.

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

MSF requires a service execution role which allows it to connect to other services.
Without the proper permissions policy and role, this example application will not be able to connect to S3 sink bucket to output the result.

Create an IAM role for the running MSF application to assume.

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

Now, when the running MSF application assumes this role, it will have the necessary permissions to write to the S3 sink.

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

## CloudWatch Logging

LocalStack MSF supports [CloudWatch Logs integration](https://docs.aws.amazon.com/managed-flink/latest/java/cloudwatch-logs.html) to help monitor the Flink cluster for application events or configuration problems.
The logging option can be added at the time of creating the Flink application using the [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html) operation.
Logging options can also be managed at a later point using the [AddApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html) and [DeleteApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html) operations.

There are following prerequisites for CloudWatch Logs integration:
- You must create the application's log group and log stream.
  Flink will not create it for you.
- You must add the permissions your application needs to write to the log stream to the service execution role.
  Generally the following IAM actions are sufficient: `logs:DescribeLogGroups`, `logs:DescribeLogStreams` and `logs:PutLogEvents`

To add a logging option:

{{< command >}}
$ awslocal kinesisanalyticsv2 add-application-cloud-watch-logging-option \
    --application-name msaf-app \
    --cloud-watch-logging-option '{"LogStreamARN": "arn:aws:logs:us-east-1:000000000000:log-group:msaf-log-group:log-stream:msaf-log-stream"}'
{
    "ApplicationARN": "arn:aws:kinesisanalytics:us-east-1:000000000000:application/msaf-app",
    "ApplicationVersionId": 2,
    "CloudWatchLoggingOptionDescriptions": [
        {
            "CloudWatchLoggingOptionId": "1.1",
            "LogStreamARN": "arn:aws:logs:us-east-1:000000000000:log-group:msaf-log-group:log-stream:msaf-log-stream"
        }
    ]
}
{{< /command >}}

{{< callout >}}
Enabling CloudWatch Logs integration has a significant performance hit.
{{< /callout >}}

Configured logging options can be retrieved using [DescribeApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplication.html):

{{< command >}}
$ awslocal kinesisanalyticsv2 describe-application --application-name msaf-app | jq .ApplicationDetail.CloudWatchLoggingOptionDescriptions
[
  {
    "CloudWatchLoggingOptionId": "1.1",
    "LogStreamARN": "arn:aws:logs:us-east-1:000000000000:log-group:msaf-log-group:log-stream:msaf-log-stream"
  }
]
{{< /command >}}

Log events can be retrieved from CloudWatch Logs using the appropriate operation.
To retrieve all events:

{{< command >}}
$ awslocal logs get-log-events --log-group-name msaf-log-group --log-stream-name msaf-log-stream
{{< /command >}}

{{< callout >}}
Logs events are reported to CloudWatch every 10 seconds.
{{< /callout >}}

LocalStack reports both Flink application and Flink framework logs to CloudWatch.
However, certain extended information such as stack traces may be missing.
You may obtain this information by execing into the Flink Docker container created by LocalStack and inspecting `/opt/flink/log`.

## Resource Tagging

You can manage [resource tags](https://docs.aws.amazon.com/managed-flink/latest/java/how-tagging.html) using [TagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UntagResource.html) and [ListTagsForResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListTagsForResource.html).
Tags can also be specified when creating the Flink application using the [CreateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplication.html) operation.

{{< command >}}
$ awslocal kinesisanalyticsv2 tag-resource \
    --resource-arn arn:aws:kinesisanalytics:us-east-1:000000000000:application/msaf-app \
    --tags Key=country,Value=SE

$ awslocal kinesisanalyticsv2 list-tags-for-resource \
    --resource-arn arn:aws:kinesisanalytics:us-east-1:000000000000:application/msaf-app
{
    "Tags": [
        {
            "Key": "country",
            "Value": "SE"
        }
    ]
}

$ awslocal kinesisanalyticsv2 untag-resource \
    --resource-arn arn:aws:kinesisanalytics:us-east-1:000000000000:application/msaf-app \
    --tag-keys country
{{< /command >}}

## Supported Flink Versions

| Flink version | Supported by LocalStack | Supported by Apache |
|:---:|:---:|:---:|
| 1.20.0 | yes | yes |
| 1.19.1 | yes | yes |
| 1.18.1 | yes | yes |
| 1.15.2 | yes | no |
| 1.13.1 | yes | no |

## Limitations

- Application versions are not maintained
- Only S3 zipfile code is supported
- Values of 20,000 ms for `execution.checkpointing.interval` and 5,000 ms for `execution.checkpointing.min-pause` are used for checkpointing.
  They can not be overridden.
- In-place [version upgrades](https://docs.aws.amazon.com/managed-flink/latest/java/how-in-place-version-upgrades.html) and [roll-backs](https://docs.aws.amazon.com/managed-flink/latest/java/how-system-rollbacks.html) are not supported
- [Snapshot/savepoint management](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html) is not implemented
- CloudTrail integration and CloudWatch metrics is not implemented.
  The application logging level defaults to `INFO` and can not be overridden.
- Parallelism is limited to the default value of 1, with one TaskManager that has one [Task Slot](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/flink-architecture/#task-slots-and-resources) allocated.
  [Parallelism configuration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkApplicationConfiguration.html#APIReference-Type-FlinkApplicationConfiguration-ParallelismConfiguration) provided on Flink application creation or update is ignored.
