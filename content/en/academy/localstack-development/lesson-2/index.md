---
title: "Deploy a full fledged containerised application using LocalStack"
linkTitle: "Deploy a full fledged containerised application using LocalStack"
weight: 2
description: >
  In this video, we'll guide you through deploying a real-world application that uses various AWS services, such as DynamoDB, ECS, API Gateway, and more. We'll attempt to input data into DynamoDB using the deployed application and then retrieve the same data using the Localstack's DynamoDB resource browser to demonstrate how Localstack enhances the developer experience for cloud applications.
length: 08:03
leadimage: deploy-app.png
videoUrl: https://www.youtube.com/embed/qIB79b-iw2U?si=n7j8WgvZZPoV95KD
type: lessons
url: "/academy/localstack-deployment/deploy-app-ls/"
---

In this lesson, we'll guide you through deploying a [continer-based application](https://github.com/localstack/localstack-workshop/tree/main/02-serverless-api-ecs-apigateway), which mimics the complexity of a real-world application.
We are using the following AWS services and their features to build our infrastructure:

- [Elastic Container Service](https://docs.localstack.cloud/user-guide/aws/elastic-container-service/) to create and deploy our containerized application.
- [DynamoDB](https://docs.localstack.cloud/user-guide/aws/dynamodb/) as a key-value and document database to persist our data.
- [API Gateway](https://docs.localstack.cloud/user-guide/aws/apigatewayv2/) to expose the containerized services to the user through HTTP APIs.
- [Cognito User Pools](https://docs.localstack.cloud/user-guide/aws/cognito/) for user authentication and authorizing requests to container APIs.
- [Amplify](https://docs.localstack.cloud/user-guide/aws/amplify/) to create the user client with ReactJS to send requests to container APIs.
- [S3](https://docs.localstack.cloud/user-guide/aws/s3/) to deploy the Amplify application to make the web application available to users.
- [IAM](https://docs.localstack.cloud/user-guide/aws/iam/) to create policies to specify roles and permissions for various AWS services.

Additionally, we'll explore the **Resource Browser**, that enables you to perform basic management operations for the locally deployed AWS resources during the development and testing process, in a fashion similar to the AWS Management Console.

Finally, we'll manually generate certain resources using `awslocal`, a wrapper over the `aws` CLI which re-routes requests to LocalStack, to demonstrate how LocalStack can be used to create and manage resources locally.

Further reading:

- [Field Notes: Serverless Container-based APIs with Amazon ECS and Amazon API Gateway](https://aws.amazon.com/blogs/architecture/field-notes-serverless-container-based-apis-with-amazon-ecs-and-amazon-api-gateway/)
- [What is `awslocal` CLI?](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [LocalStack Resource Browser](https://docs.localstack.cloud/user-guide/web-application/resource-browser/)
