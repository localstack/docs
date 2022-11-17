---
title: "Deploying Lambda container image locally with Elastic Container Registry (ECR) using LocalStack"
linkTitle: "Deploying Lambda container image locally with Elastic Container Registry (ECR) using LocalStack"
weight: 2
description: >
  You can create & deploy your Lambda functions using Lambda container image by packaging your code and dependencies in a Docker Image! Learn how you can create a Lambda container image using a local Elastic Container Registry (ECS) in LocalStack.
cascade:
  type: docs
---

AWS Lambda is a serverless compute system that allows you to break down your application into many independent functions and deploy them as singular units that can run on the AWS ecosystem. Lambda is tightly integrated with other AWS services and allows you to write your serverless functions in different programming languages suited for various supported runtimes. You can deploy Lambda functions programmatically by uploading a ZIP file containing your code and dependencies or packaging your code in a container image and deploying it via Elastic Container Registry (ECR).

Elastic Container Registry (ECR) allows users to push their software packaged inside containers into an AWS-managed registry. Using ECR, you can version, tag, and manage your image lifecycles independently of your application. ECR is tightly integrated with other AWS services, such as ECS, EKS, and Lambda, and allows you to deploy your container image to these services. You can create container images using Docker and your Lambda functions by implementing the Lambda Runtime API and following the Open Container Initiative (OCI) specifications.

[LocalStack Pro](https://localstack.cloud) supports the creation of Lambda functions using container images via Elastic Container Registry and allows you to deploy your Lambda functions locally using LocalStack. In this tutorial, we will learn how to create a Lambda function using a container image and deploy it locally using LocalStack.

## Prerequisites

For this tutorial you will need:

- [LocalStack Pro](https://localstack.cloud/pricing/) to emulate Amazon ECS and AWS Lambda locally
  - Don't worry, if you don't have a subscription yet, you can just get a trial license for free.
- [awslocal](https://docs.localstack.cloud/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [Docker](https://docker.io/)
