---
title: "Generate IAM Policies with LocalStack IAM Policy Stream"
linkTitle: "Generate IAM Policies with LocalStack IAM Policy Stream"
weight: 15
description: >
  Learn how to generate IAM policies for your AWS API requests on your local machine using LocalStack's IAM Policy Stream.
type: tutorials
services:
- s3
- sns
deployment:
- terraform
- awscli
pro: true
leadimage: ""
teaser: ""
platform:
- HCL
---

## Introduction

When you're developing cloud and serverless applications, you need to grant access to various AWS resources like S3 buckets and RDS databases. To handle this, you create IAM roles and assign permissions through policies. However, configuring these policies can be challenging, especially if you want to ensure minimal access of all principals to your resources.

[LocalStack's IAM Policy Stream](https://app.localstack.cloud/policy-stream) automates the generation of IAM policies for your AWS API requests on your local machine. This stream helps you identify the necessary permissions for your cloud application and allows you to detect logical errors, such as unexpected actions in your policies.

This tutorial will guide you through setting up IAM Policy Stream for a locally running AWS application. We'll use a basic example involving an S3 bucket, an SQS queue, and a bucket notification configuration. You'll generate the policy for the bucket notification configuration and insert it into the SQS queue.

## Why use IAM Policy Stream?

LocalStack enables you to create and enforce local IAM roles and policies using the [`ENFORCE_IAM` feature](https://docs.localstack.cloud/user-guide/security-testing/iam-enforcement/). However, users often struggle to figure out the necessary permissions for different actions. It's important to find a balance, avoiding giving too many permissions while making sure the right ones are granted.

This challenge becomes more complex when dealing with AWS services that make requests not directly visible to users. For instance, if an SNS topic sends a message to an SQS queue and the underlying call fails, there might be no clear error message, causing confusion, especially for those less familiar with the services.

IAM Policy Stream simplifies this by automatically generating the needed policies and showing them to users. This makes it easier to integrate with resources, roles, and users, streamlining the development process. Additionally, it serves as a useful learning tool, helping users understand the permissions linked to various AWS calls and improving the onboarding experience for newcomers to AWS.

## Prerequisites

-   [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)  with  [`LOCALSTACK_AUTH_TOKEN`](https://docs.localstack.cloud/getting-started/auth-token/)
-   [Docker](https://docs.docker.com/get-docker/)
-   [AWS](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)  CLI with  [`awslocal` wrapper](https://github.com/localstack/awscli-local)
-   [LocalStack Web Application account](https://app.localstack.cloud/sign-up)
-   [jq](https://jqlang.github.io/jq/download/)

## Tutorial: Configure an S3 bucket for event notifications using SQS
