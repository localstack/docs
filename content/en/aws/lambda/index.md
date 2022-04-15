---
title: "Lambda"
linkTitle: "Lambda"
categories: ["LocalStack Community"]
description: >
  Supporting local development and testing of AWS Lambdas on LocalStack
---

AWS Lambda is a Serverless Function as a Service (FaaS) system that allows you to write code in your favorite programming language and run it on the AWS ecosystem. Unlike deploying your code on a server, you can now break down your application into many independent functions and deploy them as a singular units. With the help of AWS Lambda, you can strive for more modular code that can be tested and debugged while integrated with the AWS infrastructure and your core system.

LocalStack allows you to execute your Lambda functions locally, without the need to deploy them to AWS. This is a great way to test your code, and to learn more about how your Lambda functions work, before deploying them to AWS. LocalStack allows you to execute your Lambda functions, in various execution modes, which is detailed on our [Lambda execution modes]({{< ref "lambda-executors" >}}) page.

We also provide tools to help you develop, debug and test your Lambda functions more efficiently:

- [Hot swapping]({{< ref "hot-swapping" >}}): Hot code swapping for Lambda functions using LocalStack’s code mounting feature.
- [Remote debugging]({{< ref "debugging" >}}): Attaching a debugger to your Lambda function using your IDE.

LocalStack Pro samples contain significant code examples that demonstrate how to use LocalStack to execute Lambda functions:

- [Lambda XRay Tracing](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-xray): Simple demo application illustrating Lambda XRay tracing using LocalStack, deployed via the Serverless framework.
- [Lambda Container Images](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-container-image): Simple demo application illustrating Lambda container images in LocalStack. The Lambda image is built using Docker and pushed to a local ECR registry.
- [Lambda Code Mounting and Debugging](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-mounting-and-debugging): Simple demo application to illustrate debugging Lambdas locally.
- [Lambda Layers](https://github.com/localstack/localstack-pro-samples/blob/master/serverless-lambda-layers/README.md): Simple demo application illustrating Lambda layers using LocalStack, deployed via the Serverless framework.
