---
title: "Cross-Account and Cross-Region Access"
linkTitle: "Cross-Account and Cross-Region Access"
categories: ["LocalStack"]
tags: ["multi-tenant", "multi-account", "namespaces"]
weight: 5
description: >
  Accessing resources in another account or region
---

LocalStack namespaces all resources by the account ID and (in some cases) region.
Certain resource types can be accessed across accounts or regions.
This page covers the specifics of facilitating such setups.

{{< alert title="Note">}}
Cross-account support in LocalStack is being actively developed.
Please report any issues on our GitHub issue tracker.
{{< /alert >}}


## Cross-Account

Resources that are accessible across accounts are always identified by ARNs.

This includes:
- Lambda functions and layers
- SQS queues 
- KMS keys

## Cross-Region

AWS provides separate API endpoints for each region.
Generally, resources can only be accessed in the region where they are created.

In contrast, LocalStack runs on a single API endpoint.
Most services do not enforce the restriction that the region parameter in the request must match the region in the resource identifier (ARN).

