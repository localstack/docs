---
title: "Creating infra with CloudFormation locally"
linkTitle: "Creating infra with CloudFormation locally"
weight: 5
description: >
  In the previous video, we saw how we can use terraform to deploy resources on localstack. In this one, we will see how cloudformation, which is an AWS offering that can be used to deploy resources on localstack. AWS CloudFormation is AWS’s primary Infrastructure-as-Code (IaC) service. It is used to declaratively define your architecture on the AWS cloud, including resources such as S3 Buckets, Lambda Functions, and much more. For deploying using AWS cloudformation we will be using awslocal - which is a thin wrapper around the aws command line interface for use with LocalStack.
length: 03:41
leadimage: infra-cloudformation.png
videoUrl: https://www.youtube.com/embed/K0OgQ5eq588?si=djvJJwwz794l2L_o
type: lessons
url: "/academy/localstack-deployment/infra-cloudformation/"
---

In this video we will use CloudFormation to deploy resources on localstack. AWS CloudFormation is AWS’s primary Infrastructure-as-Code (IaC) service. It is used to declaratively define your architecture on the AWS cloud, including resources such as S3 Buckets, Lambda Functions, and much more. For deploying using AWS cloudformation we will be using [`awslocal`](https://github.com/localstack/awscli-local) - which is a thin wrapper around the aws command line interface for use with LocalStack.

- We will walk you through the whole CloudFormation Stack code and show the different configuration options for creating the infrastructure for our demo application.
- Once we deploy the CloudFormation Stack, we will see some of the resources that are created as output such as API URLs, ECS cluster name, VPC ID etc.
- Towards the end we will check the deployment and that the resources have been created using the Resource Browser.

Further reading:

- [LocalStack CloudFormation Docs](https://docs.localstack.cloud/user-guide/aws/cloudformation/)
- [LocalStack CloudFormation Coverage](https://docs.localstack.cloud/references/coverage/coverage_cloudformation/)
- [Resource Groups](https://docs.localstack.cloud/user-guide/aws/resourcegroups/)
- [Infrastructure-as-Code with LocalStack — Building & testing your configurations locally!](https://www.youtube.com/watch?v=bx2XpR9xLFA)
- [Serverless Application Model](https://github.com/localstack-samples/sample-sam-sns-fifo-dynamodb-lambda)