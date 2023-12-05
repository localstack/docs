---
title: "Resource Access Manager (RAM)"
linkTitle: "Resource Access Manager (RAM)"
description: Get started with RAM on LocalStack
---

Resource Access Manager (RAM) helps resources to be shared across AWS accounts, within or across organizations.

On AWS, RAM is an abstraction on top of AWS Identity and Access Management (IAM) which can manage resource-based policies to supported resource types.

LocalStack supports RAM in the Pro edition.
The supported API operations can be found on the [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_ram/).

## Limitations

RAM on LocalStack currently functions as a CRUD interface only.
Resource shares do not lead to the specified principals being granted access to the specified resources.
