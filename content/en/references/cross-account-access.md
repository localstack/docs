---
title: "Cross-Account and Cross-Region Access"
linkTitle: "Cross-Account and Cross-Region Access"
weight: 50
description: >
  Accessing resources in another account or region
---

LocalStack automatically namespaces all resources based on the account ID and, in some cases, the region.
However, there are certain resource types that can be accessed across multiple accounts or regions.
This document provides information to help design such setups.

{{< callout >}}
Cross-account support in LocalStack is being actively developed.
Please report any issues on our [GitHub issue tracker](https://github.com/localstack/localstack/issues/new/choose).
{{< /callout >}}

Cross-account/cross-region access happens when a client attempts to access a resource in another account or region than what it is configured with:

{{< command >}}
#
# Create a queue in one account and region
#

$ AWS_ACCESS_KEY_ID=111111111111 awslocal sqs create-queue \
    --queue-name my-queue \
    --region ap-south-1
{
    "QueueUrl": "http://sqs.ap-south-1.localhost.localstack.cloud:443/111111111111/my-queue"
}

#
# Set some attributes
#

$ AWS_ACCESS_KEY_ID=111111111111 awslocal sqs set-queue-attributes \
    --attributes VisibilityTimeout=60 \
    --queue-url http://sqs.ap-south-1.localhost.localstack.cloud:443/111111111111/my-queue \
    --region ap-south-1 

#
# Retrieve the queue attribute from another account and region.
# The required information for LocalStack to locate the queue is available in the queue URL.
#

$ AWS_ACCESS_KEY_ID=222222222222 awslocal sqs get-queue-attributes \
    --attribute-names VisibilityTimeout \
    --region eu-central-1 \
    --queue-url http://sqs.ap-south-1.localhost.localstack.cloud:443/111111111111/my-queue
{
    "Attributes": {
        "VisibilityTimeout": "60"
    }
}
{{< /command >}}

## Cross-Account

Resources that can be accessed across accounts are identified by their Amazon Resource Names (ARNs) or other schemes such as SQS Queue URLs.
The full list of resources and operations that allow cross-account access are listed below.

{{< callout "tip" >}}
LocalStack does not enforce IAM for cross-account access by default.
Use the `ENFORCE_IAM` [configuration]({{< ref "configuration#iam" >}}) option to enable it.
{{< /callout >}}

### EC2 Peering

It is possible to create peered VPCs and transit gateway peering attachments that are in a different region or account than the requester.
Ensure that the `PeerRegion` and `PeerOwnerId` arguments are correctly set when creating these resources.

### KMS keys

- `CreateGrant`
- `Decrypt`
- `DescribeKey`
- `Encrypt`
- `GenerateDataKey`
- `GenerateDataKeyPair`
- `GenerateDataKeyPairWithoutPlaintext`
- `GenerateDataKeyWithoutPlaintext`
- `GenerateMac`
- `GetKeyRotationStatus`
- `GetPublicKey`
- `ListGrants`
- `RetireGrant`
- `RevokeGrant`
- `Sign`
- `Verify`
- `VerifyMac`
<!--    - ReEncrypt (NOT IMPLEMENTED IN LOCALSTACK) -->

### Lambda functions and layers

- `AddLayerVersionPermission`
- `CreateAlias`
- `DeleteAlias`
- `DeleteFunction`
- `DeleteFunctionConcurrency`
- `DeleteLayerVersion`
- `GetAlias`
- `GetFunction`
- `GetFunctionConfiguration`
- `GetLayerVersion`
- `GetLayerVersionByArn`
- `GetLayerVersionPolicy`
- `GetPolicy`
- `Invoke`
- `ListAliases`
- `ListLayerVersions`
- `ListTags`
- `ListVersionsByFunction`
- `PublishVersion`
- `PutFunctionConcurrency`
- `RemoveLayerVersionPermission`
- `TagResource`
- `UntagResource`
- `UpdateAlias`
- `UpdateFunctionCode`

### S3 buckets

Like AWS, LocalStack S3 has a bucket namespace which is shared by all accounts.
This means that the bucket name has to be globally unique.

- `GetObject`
- `ListObjects`
- `PutObject`

### Secrets Manager

- `DeleteSecret`
- `DescribeSecret`
- `GetResourcePolicy`
- `GetSecretValue`
- `ListSecretVersionIds`
- `PutResourcePolicy`
- `PutSecretValue`
- `RestoreSecret`
- `TagResource`
- `UntagResource`
- `UpdateSecret`

### SNS topics

- `AddPermission`
- `DeleteTopic`
- `GetTopicAttributes`
- `ListSubscriptionByTopic`
- `Publish`
- `RemovePermission`
- `SetTopicAttributes`
- `Subscribe`

### SQS queues

On AWS, all operations except `AddPermission`, `CreateQueue`, `DeleteQueue`, `ListQueues`, `ListQueueTags`, `RemovePermission`, `SetQueueAttributes`, `TagQueue` and `UntagQueue` allow cross-account access.

On LocalStack, all operations allow cross-account access.

## Cross-Region

AWS provides individual API endpoints for each region, and typically, resources can only be accessed within their respective regions.

On the other hand, LocalStack operates on a unified API endpoint, allowing interactions with services across regions.
