---
title: "Serverless Application Repository" 
linkTitle: "Serverless Application Repository"
description: >
  Get started with Serverless Application Repository on LocalStack
tags: ["Pro image"]
---

## Introduction

[Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/) allows developers to discover, deploy, and share serverless applications and components.
Using Serverless Application Repository, developers can build & publish applications and components once and share them across the community and organizations, making them accessible to others.
Serverless Application Repository provides a user-friendly interface to search, filter, and browse through a diverse catalog of serverless applications.

LocalStack allows you to use the Serverless Application Repository APIs in your local environment to create, update, delete, and list serverless applications and components.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_serverlessrepo/), which provides information on the extent of Serverless Application Repository's integration with LocalStack.

## Getting started

This guide is designed for users new to Serverless Application Repository and assumes basic knowledge of the SAM CLI and our [`samlocal`](https://github.com/localstack/aws-sam-cli-local) wrapper script.

Start your LocalStack container using your preferred method, such as via docker-compose.
We will demonstrate how to create a SAM application that comprises a Hello World serverless application with a simple API backend using the SAM CLI and then publish it to the Serverless Application Repository by defining it using a SAM template.

### Setup the SAM application

To create a sample SAM application using the `samlocal` CLI, execute the following command:

{{< command >}}
$ samlocal init --runtime python3.9
{{< /command >}}

This command downloads a sample SAM application template and generates a `template.yml` file in the current directory. 
The template includes a Lambda function and an API Gateway endpoint that supports a `GET` operation.

### Package the SAM application

Next, we can use the `samlocal` CLI to create a deployment package and a packaged SAM template.
Add a Metadata section to your SAM template file (`template.yaml`), and specify the following properties:

To create a deployment package and a packaged SAM template using the `samlocal` CLI, add a Metadata section to your SAM template file (`template.yaml`) and specify the desired properties:

```yaml
Metadata:
  AWS::ServerlessRepo::Application:
    Name: helloworld
    Description: hello world
    Author: author
    SpdxLicenseId: Apache-2.0
    Labels: ['tests']
    SemanticVersion: 0.0.1
```

Once the Metadata section is added, run the following command to create the Lambda function deployment package and the packaged SAM template:

{{< command >}}
samlocal package \
    --template-file template.yaml \
    --output-template-file packaged.yaml
{{< /command >}}

This command generates a `packaged.yaml` file in the current directory containing the packaged SAM template.
The packaged template will be similar to the original template file, but it will now include a `CodeUri` property for the Lambda function, as shown in the example below:

```yaml
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: s3://aws-sam-cli-managed-default-samclisourcebucket-b6325dc3/c6ce8fa8b5a97dd022ecd006536eb5a4
```

### Retrieve the Application ID

To retrieve the Application ID for your SAM application, you can utilize the [`awslocal`](https://github.com/localstack/awscli-local) CLI by running the following command:

{{< command >}}
awslocal serverlessrepo list-applications
{{< /command >}}

In the output, you will observe the `ApplicationId` property in the output, which is the Application ID for your SAM application, along with other properties such as the `Author`, `Description`, `Name`, `SpdxLicenseId`, and `Version` providing further details about your application.

### Publish the SAM application

To publish your application to the Serverless Application Repository, execute the following command:

{{< command >}}
samlocal publish \
    --template packaged.yaml \
    --region us-east-1
{{< /command >}}

### Delete the SAM application

To remove a SAM application from the Serverless Application Repository, you can use the following command:

{{< command >}}
awslocal serverlessrepo delete-application \
    --application-id <application-id>
{{< /command >}}

Replace `<application-id>` with the Application ID of your SAM application that you retrieved in the previous step.

You can also create a CloudFormation changeset using the [`CreateCloudFormationChangeSet`](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-publish.html) API, and then execute the changeset to deploy the SAM application using the [`ExecuteChangeSet`](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html) API.

## Current Limitations

- Keep in mind, since the application is only registered in your individual localstack instance, you won't be able to share them with other developers.
- Currently LocalStack only supports one AWS-hosted application (`"arn:aws:serverlessrepo:us-east-1:297356227824:applications/SecretsManagerRDSPostgreSQLRotationMultiUser`).
