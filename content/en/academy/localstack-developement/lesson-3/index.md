---
title: "LocalStack Integrations - Infrastructure-as-Code and CI tools "
linkTitle: "LocalStack Integrations - Infrastructure-as-Code and CI tools "
weight: 3
description: >
  In the previous video, we deployed various AWS resources using the AWS CLI and the corresponding `awslocal` wrapper. However, manually deploying resources can be error-prone and time-consuming. In this video, we will see how LocalStack can be used with infrastructure-as-code (IaC) and continuous integration (CI) tools to enable local development more efficient, and foster team collaboration.
length: 03:09
leadimage: ls-integrations.png
videoUrl: https://www.youtube.com/embed/YV0Zs6UNI9I?si=dD8VzemepxA1Pzkg
type: lessons
url: "/academy/localstack-deployment/ls-integrations/"
---

In this video, we'll explore the how LocalStack integrates with infrastructure-as-code (IaC) and continuous integration (CI) tools. Creating resources manually can be prone to errors and time-consuming — LocalStack integrations allow you to directly use your favorite tools to create and manage AWS resources locally.

- Infrastructure as Code tools like Terraform or Pulumi assist in configuration management with added advantages like version control, ease of editing, and reproducibility.
- LocalStack integrates with various CI platforms, such as GitHub Actions or CircleCI, to enable the cloud integrations tests before pushing changes to production.

Towards the end, we'll demonstrate a Terraform deployment of a PostgreSQL Aurora cluster on LocalStack, highlighting the time and resource savings compared to deploying directly on AWS. Additionally, we'll provide examples of using LocalStack with [Terraform](https://github.com/localstack-samples/localstack-terraform-samples) and [Pulumi](https://github.com/localstack-samples/localstack-pulumi-samples) for reference.
