---
title: "Deploy a full fledged containerised application using LocalStack"
linkTitle: "Deploy a full fledged containerised application using LocalStack"
weight: 2
description: >
  In this video we will do a walkthrough of the web application we are going to deploy. This application mimics a real world application’s complexity to some extent. We will try adding data to the dynamodb through the web application and then query the same data from the Localstack resource browser. We will see how Localstack has improved the developer experience of cloud applications. Post this we will discuss the architecture diagram and explain how the whole application flow goes through each of these AWS services. Towards the end we will try to manually create a few resources for the project, such as DynamoDB table.
length: 08:03
leadimage: deploy-app.png
videoUrl: https://www.youtube.com/embed/qIB79b-iw2U?si=n7j8WgvZZPoV95KD
type: lessons
url: "/academy/localstack-deployment/deploy-app-ls/"
---

- In this lesson, we'll do a walkthrough of the application we are going to deploy. We will be deploying the [application](https://github.com/localstack/localstack-workshop/tree/main/02-serverless-api-ecs-apigateway) that mimics a real world application’s complexity to some extent. We are using the following AWS services and their features to build our infrastructure:

  - [Elastic Container Service](https://docs.localstack.cloud/user-guide/aws/elastic-container-service/) to create and deploy our containerized application.
  - [DynamoDB](https://docs.localstack.cloud/user-guide/aws/dynamodb/) as a key-value and document database to persist our data.
  - [API Gateway](https://docs.localstack.cloud/user-guide/aws/apigatewayv2/) to expose the containerized services to the user through HTTP APIs.
  - [Cognito User Pools](https://docs.localstack.cloud/user-guide/aws/cognito/) for user authentication and authorizing requests to container APIs.
  - [Amplify](https://docs.localstack.cloud/user-guide/aws/amplify/) to create the user client with ReactJS to send requests to container APIs.
  - [S3](https://docs.localstack.cloud/user-guide/aws/s3/) to deploy the Amplify application to make the web application available to users.
  - [IAM](https://docs.localstack.cloud/user-guide/aws/iam/) to create policies to specify roles and permissions for various AWS services.

- Further, we will explore the Resource Browser that allow you to view, manage, and deploy AWS resources locally while building & testing their cloud applications locally.

- Towards the end we will manually create some resources using awslocal, a thin wrapper over awscli, into localstack.

Further reading:

- [An overview of LocalStack](https://localstack.cloud/)
- [LocalStack Documentation](https://docs.localstack.cloud/overview)
- [Resource Browser](https://docs.localstack.cloud/user-guide/web-application/resource-browser/)
- [LocalStack 101](https://docs.localstack.cloud/academy/localstack-101/)
- [LocalStack AWS CLI](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal)