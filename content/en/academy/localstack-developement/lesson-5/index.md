---
title: "Creating infra with CloudFormation locally"
linkTitle: "Creating infra with CloudFormation locally"
weight: 5
description: >
  In this video, we'll explore how you can use AWS CloudFormation with LocalStack. AWS CloudFormation allows you to declaratively define your AWS cloud architecture, specifying resources like S3 Buckets and Lambda Functions. To deploy using AWS CloudFormation, we'll use `awslocal`, a wrapper CLI around the `aws` command line interface.
length: 03:41
leadimage: infra-cloudformation.png
videoUrl: https://www.youtube.com/embed/K0OgQ5eq588?si=djvJJwwz794l2L_o
type: lessons
url: "/academy/localstack-deployment/infra-cloudformation/"
---

In this video, we'll utilize AWS CloudFormation to deploy AWS resources locally through LocalStack. These resources, including DynamoDB tables, API Gateway, and VPC. We'll use `awslocal`, a wrapper CLI that serves as a wrapper on the `aws` CLI to execute Terraform commands against LocalStack.

- We'll guide you through the entire CloudFormation Stack, demonstrating various configuration options for creating the infrastructure for our application.
- After deploying the CloudFormation Stack, we'll examine some outputted resources, including API URLs, ECS cluster names, VPC ID, and more.
- Finally, we'll verify the deployment and confirm the creation of resources using the Resource Browser.
