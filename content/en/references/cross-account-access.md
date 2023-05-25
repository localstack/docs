---
title: "Cross-Account and Cross-Region Access"
linkTitle: "Cross-Account and Cross-Region Access"
categories: ["LocalStack"]
tags: ["multi-tenant", "multi-account", "namespaces"]
weight: 5
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

These resource types include:

- Lambda functions and layers
- Simple Queue Service (SQS) queues
- Key Management Service (KMS) keys

## Cross-Region

AWS provides individual API endpoints for each region, and typically, resources can only be accessed within their respective regions.

On the other hand, LocalStack operates on a unified API endpoint, allowing interactions with services across regions.

Unlike AWS, LocalStack does not strictly enforce the requirement that the region parameter in the request must match the region specified in the resource identifier (ARN).
