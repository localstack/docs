---
title: "AWS Serverless Application Model (SAM)"
linkTitle: "AWS Serverless Application Model (SAM)"
description: >
  Use the AWS SAM (Serverless Application Model) with LocalStack
---

## Introduction

The AWS Serverless Application Model (SAM) is an open-source framework for developing serverless applications. It uses a simplified syntax to define functions, APIs, databases, and event source mappings.
When you deploy, SAM converts its syntax into AWS CloudFormation syntax, helping you create serverless applications more quickly.

LocalStack can work with SAM using the AWS SAM CLI for LocalStack. This CLI comes in the form of a `samlocal` wrapper script, which lets you deploy SAM applications on LocalStack.
This guide explains how to set up local AWS resources using the `samlocal` wrapper script.


## `samlocal` wrapper script

`samlocal` is a wrapper for the `sam` command line interface, facilitating the use of SAM framework with LocalStack.
When executing deployment commands like `samlocal ["build", "deploy", "validate", "package"]`, the script configures the SAM settings for LocalStack and runs the specified SAM command.

### Install the `samlocal` wrapper script

You can install the `samlocal` wrapper script by running the following command:

{{< command >}}
$ pip install aws-sam-cli-local
{{< / command >}}

### Create a new SAM project

You can initialize a new SAM project using the following command:

{{< command >}}
$ samlocal init
{{< / command >}}

Select `1` to create a new SAM application using an AWS Quick Start template. The SAM CLI will ask you for the project name and the runtime for the Lambda function.

For this example, select `1` for the Hello World example.
Choose the Python runtime and `zip` for the packaging type.
Optionally, you can enable X-Ray tracing, monitoring, and structured JSON logging.
Then, enter the project name and press `Enter`.

### Deploy the SAM application

After initializing the SAM project, enter the project directory and deploy the application using the following command:

{{< command >}}
$ samlocal deploy --guided
{{< / command >}}

Enter the default values for the deployment, such as the stack name, region, and confirm the changes.
The `samlocal` wrapper will package and deploy the application to LocalStack.

### Configuration

| Environment Variable   | Default value                                    | Description                                                             |
|------------------------|--------------------------------------------------|-------------------------------------------------------------------------|
| AWS_ENDPOINT_URL       | `http://localhost.localstack.cloud:4566`        | URL at which the `boto3` client can reach LocalStack                   |
| EDGE_PORT (Deprecated)              | `4566`                              | Port number under which the LocalStack edge service is available        |
| LOCALSTACK_HOSTNAME (Deprecated)     | `localhost`                         | Host under which the LocalStack edge service is available

## Debugging on VS Code

To debug your Lambda functions in VS Code while using the SAM CLI's `sam local` command alongside other services provided by LocalStack, set up a launch configuration in the `.vscode/launch.json` file.
Insert the following settings into the file:


```json
{
            "type": "aws-sam",
            "request": "direct-invoke",
            "name": "Job dispatcher lambda",
            "invokeTarget": {
                "target": "code",
                "projectRoot": "${workspaceFolder}",
                "lambdaHandler": "lambda/lambda.handler"
            },
            "lambda": {
                "runtime": "python3.8",
                "payload": {},
                "environmentVariables": {
                    "ENDPOINT_URL": "http://localstack:4566/",
                    "S3_ENDPOINT_URL": "http://s3.localhost.localstack.cloud:4566/",
                    "AWS_ACCESS_KEY_ID": "test",
                    "AWS_SECRET_ACCESS_KEY": "test",
                    "AWS_SESSION_TOKEN": "test",
                    "AWS_REGION": "us-east-1",
                    "MAIN_DOCKER_NETWORK": "localstack-network"
                }
            },
            "sam": {
                "dockerNetwork": "localstack-network"
            }
        }
```

The `dockerNetwork` property is essential as it allows the LocalStack container to use the `sam invoke` commands within the same network as the LocalStack container itself. Adjust the Lambda function handler and environment variables as needed.
