---
title: "Elastic File System (EFS)"
linkTitle: "Elastic File System (EFS)"
description: >
  Get started with Elastic File System (EFS) on LocalStack
tags: ["Pro image"]
---

## Introduction

Elastic File System (EFS) is a fully managed file storage service provided by Amazon Web Services (AWS). EFS offers scalable and shared file storage that can be accessed by multiple EC2 instances and on-premises servers simultaneously. EFS utilizes the Network File System protocol to allow it to be used as a data source for various applications and workloads.

LocalStack allows you to use the EFS APIs in your local environment to create local file systems, lifecycle configurations, and file system policies. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_efs/), which provides information on the extent of EFS's integration with LocalStack.

## Getting started

This guide is designed for users new to Elastic File System and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to create a file system, apply an IAM resource-based policy, and create a lifecycle configuration using the AWS CLI.

### Create a filesystem

To create a new, empty file system you can use the [`CreateFileSystem`](https://docs.aws.amazon.com/goto/WebAPI/elasticfilesystem-2015-02-01/CreateFileSystem) API. Run the following command to create a new file system:

{{< command >}}
$ awslocal efs create-file-system \
    --performance-mode generalPurpose \
    --throughput-mode bursting \
    --encrypted \
    --tags Key=Name,Value=my-file-system
{{< /command >}}

The following output would be retrieved:

```bash
{
    "CreationToken": "53465731-0032-4cef-92f5-8aefe7c7b91e",
    "FileSystemId": "fs-34feac549e66b814",
    "FileSystemArn": "arn:aws:elasticfilesystem:us-east-1:000000000000:file-system/fs-34feac549e66b814",
    "CreationTime": 1692808338.424,
    "LifeCycleState": "available",
    "PerformanceMode": "generalPurpose",
    "Encrypted": true,
    "ThroughputMode": "bursting",
    "Tags": [
        {
            "Key": "Name",
            "Value": "my-file-system"
        }
    ]
}
```

You can also describe the locally available file systems using the [`DescribeFileSystems`](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystems.html) API. Run the following command to describe the local file systems available:

{{< command >}}
$ awslocal efs describe-file-systems
{{< /command >}}

You can alternatively pass the `--file-system-id` parameter to the `describe-file-system` command to retrieve information about a specific file system in AWS CLI.

### Put file system policy

You can apply an EFS `FileSystemPolicy` to an EFS file system using the [`PutFileSystemPolicy`](https://docs.aws.amazon.com/efs/latest/ug/API_PutFileSystemPolicy.html) API. Run the following command to apply a policy to the file system created in the previous step:

{{< command >}}
$ awslocal efs put-file-system-policy \
    --file-system-id <FILE_SYSTEM_ID> \
    --policy "{\"Version\":\"2012-10-17\",\"Id\":\"ExamplePolicy01\",\"Statement\":[{\"Sid\":\"ExampleSatement01\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":[\"elasticfilesystem:ClientMount\",\"elasticfilesystem:ClientWrite\"],\"Resource\":\"arn:aws:elasticfilesystem:us-east-1:000000000000:file-system/fs-34feac549e66b814\"}]}"
{{< /command >}}

You can list the file system policies using the [`DescribeFileSystemPolicy`](https://docs.aws.amazon.com/efs/latest/ug/API_DescribeFileSystemPolicy.html) API. Run the following command to list the file system policies:

{{< command >}}
$ awslocal efs describe-file-system-policy \
    --file-system-id <FILE_SYSTEM_ID>
{{< /command >}}

Replace `<FILE_SYSTEM_ID>` with the ID of the file system you want to list the policies for. The output will return the `FileSystemPolicy` for the specified EFS file system.

### Create a lifecycle configuration

You can create a lifecycle configuration for an EFS file system using the [`PutLifecycleConfiguration`](https://docs.aws.amazon.com/efs/latest/ug/API_PutLifecycleConfiguration.html) API. Run the following command to create a lifecycle configuration for the file system created in the previous step:

{{< command >}}
$ awslocal efs put-lifecycle-configuration \
    --file-system-id <FILE_SYSTEM_ID> \
    --lifecycle-policies "{\"TransitionToIA\":\"AFTER_30_DAYS\"}"
{{< /command >}}

The following output would be retrieved:

```bash
{
    "LifecyclePolicies": [
        {
            "TransitionToIA": "AFTER_30_DAYS"
        }
    ]
}
```

## Current Limitations

LocalStack's EFS implementation is limited and lacks support for functionalities like creating mount targets, configuring access points, and generating tags. LocalStack uses Moto to emulate the EFS APIs, and efforts are underway to incorporate support for these features in upcoming updates.
