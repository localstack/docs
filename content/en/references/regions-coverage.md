---
title: "Regions Coverage"
linkTitle: "Regions Coverage"
weight: 99
description: >
    This page lists the AWS Region Coverage for LocalStack's emulation of AWS services.
cascade:
  type: docs
---

## Introduction

LocalStack ships with multi-region support, enabling users to emulate different AWS regions and namespace resources based on the region.
With IAM Policy Enforcement, you can ensure that access control and permissions are applied accurately across supported regions.
LocalStack supports a wide range of AWS regions, including commercial, government, and China regions, providing a realistic environment for development and testing across multiple regions on your local machine.

## Supported Regions

| Region Code     | Supported  | Notes                                      |
|-----------------|------------|--------------------------------------------|
| us-east-1       | ✔️         | Commonly used as the default region        |
| us-east-2       | ✔️         |                                              |
| us-west-1       | ✔️         |                                              |
| us-west-2       | ✔️         |                                              |
| ca-central-1    | ✔️         |                                              |
| ca-west-1       | ❌         | Not supported in LocalStack                |
| eu-north-1      | ✔️         |                                              |
| eu-west-1       | ✔️         |                                              |
| eu-west-2       | ✔️         |                                              |
| eu-west-3       | ✔️         |                                              |
| eu-central-1    | ✔️         |                                              |
| eu-south-1      | ✔️         |                                              |
| eu-south-2      | ✔️         |                                              |
| eu-central-2    | ✔️         |                                              |
| ap-south-1      | ✔️         |                                              |
| ap-south-2      | ✔️         |                                              |
| ap-northeast-1  | ✔️         |                                              |
| ap-northeast-2  | ✔️         |                                              |
| ap-northeast-3  | ✔️         |                                              |
| ap-southeast-1  | ✔️         |                                              |
| ap-southeast-2  | ✔️         |                                              |
| ap-southeast-3  | ✔️         |                                              |
| ap-southeast-4  | ✔️         |                                              |
| ap-southeast-5  | ❌         | Not supported in LocalStack                |
| ap-east-1       | ✔️         |                                              |
| sa-east-1       | ✔️         |                                              |
| af-south-1      | ✔️         |                                              |
| me-south-1      | ✔️         |                                              |
| me-central-1    | ✔️         |                                              |
| cn-north-1      | ✔️         |                                              |
| cn-northwest-1  | ✔️         |                                              |
| us-gov-east-1   | ✔️         | Available in LocalStack Enterprise only    |
| us-gov-west-1   | ✔️         | Available in LocalStack Enterprise only    |
| il-central-1    | ✔️         |                                              |
