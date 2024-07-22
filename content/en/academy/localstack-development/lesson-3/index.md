---
title: "LocalStack Integrations - Infrastructure-as-Code and CI tools "
linkTitle: "LocalStack Integrations - Infrastructure-as-Code and CI tools "
weight: 3
description: >
  In this video, we will see how LocalStack can be used with infrastructure-as-code (IaC) and continuous integration (CI) tools to enable local development more efficient, and foster team collaboration. LocalStack integrations allow you to use your favorite tools to create and manage AWS resources locally.
length: 03:09
leadimage: ls-integrations.png
videoUrl: https://www.youtube.com/embed/YV0Zs6UNI9I?si=dD8VzemepxA1Pzkg
type: lessons
url: "/academy/localstack-deployment/ls-integrations/"
---

LocalStack integrates with various Infrastructure as Code tools like [Terraform](https://docs.localstack.cloud/user-guide/integrations/terraform/) or [Pulumi](https://docs.localstack.cloud/user-guide/integrations/pulumi/) assist in configuration management with added advantages like version control, ease of editing, and reproducibility.
Additionally, LocalStack integrates with various CI platforms, such as [GitHub Actions](https://docs.localstack.cloud/user-guide/ci/github-actions/) or [CircleCI](https://docs.localstack.cloud/user-guide/ci/circle-ci/), to enable the cloud integrations tests before pushing changes to production.

We discuss how LocalStack integrates with infrastructure-as-code (IaC) and continuous integration (CI) tools.
Towards the end, we'll demonstrate a [Terraform deployment of a PostgreSQL Aurora cluster](https://github.com/terraform-aws-modules/terraform-aws-rds-aurora/tree/v8.1.1/examples/postgresql) on LocalStack, highlighting the time and resource savings compared to deploying directly on AWS.

Additionally, we'll provide examples of using LocalStack with Terraform and Pulumi for reference.

Further reading:

- [Terraform samples](https://github.com/localstack-samples/localstack-terraform-samples)
- [Pulumi samples](https://github.com/localstack-samples/localstack-pulumi-samples)
- [Infrastructure as Code with LocalStack](https://youtu.be/bx2XpR9xLFA)
