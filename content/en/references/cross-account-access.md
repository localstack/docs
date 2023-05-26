---
title: "Cross-Account and Cross-Region Access"
linkTitle: "Cross-Account and Cross-Region Access"
categories: ["LocalStack"]
tags: ["multi-tenant", "multi-account", "namespaces"]
weight: 50
description: >
  Accessing resources in another account or region
---

LocalStack automatically assigns namespaces to all resources based on the account ID and, in some cases, the region.
However, there are certain resource types that can be accessed across multiple accounts or regions.
This document provides detailed information on how to configure and facilitate such setups effectively.

{{< alert title="Note">}}
Cross-account support in LocalStack is being actively developed.
Please report any issues on our [GitHub issue tracker](https://github.com/localstack/localstack/issues/new/choose).
{{< /alert >}}

## Cross-Account

Resources that can be accessed across multiple accounts are always identified by their Amazon Resource Names (ARNs).

List of resources and operations that allow cross-account access are listed below:

- Lambda functions and layers:
    - AddLayerVersionPermission
    - CreateAlias
    - DeleteAlias
    - DeleteFunction
    - DeleteFunctionConcurrency
    - DeleteLayerVersion
    - GetAlias
    - GetFunction
    - GetFunctionConfiguration
    - GetLayerVersion
    - GetLayerVersionByArn
    - GetLayerVersionPolicy
    - GetPolicy
    - Invoke
    - ListAliases
    - ListLayerVersions
    - ListTags
    - ListVersionsByFunction
    - PublishVersion
    - PutFunctionConcurrency
    - RemoveLayerVersionPermission
    - TagResource
    - UntagResource
    - UpdateAlias
    - UpdateFunctionCode
- SQS queues: All operations
- KMS keys:
    - CreateGrant
    - Decrypt
    - DescribeKey
    - Encrypt
    - GenerateDataKey
    - GenerateDataKeyPair
    - GenerateDataKeyPairWithoutPlaintext
    - GenerateDataKeyWithoutPlaintext
    - GenerateMac
    - GetKeyRotationStatus
    - GetPublicKey
    - ListGrants
    - RetireGrant
    - RevokeGrant
    - Sign
    - Verify
    - VerifyMac
<!--    - ReEncrypt (NOT IMPLEMENTED IN LOCALSTACK) -->
- SNS topics:
    - AddPermission
    - DeleteTopic
    - GetTopicAttributes
    - ListSubscriptionByTopic
    - Publish
    - RemovePermission
    - SetTopicAttributes
    - Subscribe
- S3 buckets: The bucket namespace is shared by all accounts
    - GetObject
    - PutObject
    - ListObjects

{{< alert title="Note">}}
IAM currently does not enforce cross-account access.
Any identity-based or resource-based policy attached to these operations or resources will be ignored.
{{< /alert >}}

## Cross-Region

AWS provides individual API endpoints for each region, and typically, resources can only be accessed within their respective regions.

On the other hand, LocalStack operates on a unified API endpoint, allowing interactions with services across regions.

LocalStack also does not enforce the requirement that the region parameter in the request must match the region specified in the resource identifier (ARN).
