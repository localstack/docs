---
title: "Serverless Framework"
tags: ["serverless-framework"] 
weight: 4
description: >
  Use the Serverless Framework with LocalStack
---

This guide explains how to integrate LocalStack with the [Serverless Framework](https://www.serverless.com/).
Although it probably requires a few code changes, integrating LocalStack with the Serverless Framework is fairly straightforward. 

In particular, the setup consists of the following two steps.

1. Installing and configuring the [Serverless-LocalStack plugin](https://github.com/localstack/serverless-localstack).
2. Adjusting AWS endpoints in Lambda functions.

## Prerequisites
This guide assumes that you have the following tools installed.

* LocalStack ([Install](https://localstack.cloud/docs/getting-started/installation/))
* Serverless ([Install](https://www.serverless.com/framework/docs/getting-started/))

It also assumes that you already have a Serverless app set up consisting of a couple of Lambda functions and a `serverless.yml` file similar to the following. An example Serverless app integrated with LocalStack can be found here: <a href="https://github.com/localstack/serverless-python-rest-api-with-dynamodb"><i class="fab fa-github"></i>  Simple REST API using the Serverless Framework and LocalStack</a>


```yaml
service: my-service

frameworkVersion: ">=1.1.0 <=2.50.0"

provider:
  name: aws
  runtime: python3.8
  environment:
    DYNAMODB_TABLE: ${self:service}-${opt:stage, self:provider.stage}
  iamRoleStatements:
    - Effect: Allow
      Action:
        - dynamodb:Query
        - ...
      Resource: "arn:aws:dynamodb:${opt:region, self:provider.region}:*:table/${self:provider.environment.DYNAMODB_TABLE}"

functions:
  create:
    handler: todos/create.create
    events:
      - http:
          path: todos
          method: post
          cors: true

  ...

resources:
  Resources:
    TodosDynamoDbTable:
      Type: 'AWS::DynamoDB::Table'
      DeletionPolicy: Retain
      Properties:
        ...
        TableName: ${self:provider.environment.DYNAMODB_TABLE}
```

## Install and configure Serverless-LocalStack Plugin
To install the plugin, execute the following command in the root of your project.
```bash
npm install -D serverless-localstack
```

Next, set up the plugin by adding the following properties to `serverless.yml`.
```yaml
...

plugins:
  - serverless-localstack

custom:
  localstack:
    stages:
      - local
```

This sets up Serverless to use the LocalStack plugin but only for the stage "local". 
Next, you need make minor adjustments to your function code in order to make your application work no matter if it is deployed on AWS or LocalStack.

## Adjust AWS endpoints in Lambda functions
You are likely using an AWS SDK (such as [Boto3](https://github.com/boto/boto3) for Python) in your Lambda functions to interact with other AWS services such as DynamoDB.

For example, in Python, your code to set up a connection to DynamoDB may look like this:
```python
...
dynamodb = boto3.resource('dynamodb')
...
```

By default, this call attempts to create a connection via the usual AWS endpoints. However, when running services in LocalStack, we need to make sure, our applications creates a connection via the LocalStack endpoint instead.

Usually, all of LocalStack's services are available via a specific port on localhost (e.g. `localhost:4566`). However, this endpoint only works when accessing LocalStack from outside its Docker runtime. 

Since the Lambda functions execute within the LocalStack Docker container, Lambda functions cannot access other services via the usual localhost endpoint. 

Instead, LocalStack provides a special environment variable `LOCALSTACK_HOSTNAME` which contains the internal endpoint of the LocalStack services from within its runtime environment.

Hence, you need to configure the Lambda functions to use the `LOCALSTACK_HOSTNAME` endpoint when accessing other AWS services in LocalStack.

In Python, this may look something like. The code detects if it is running in LocalStack by checking if the `LOCALSTACK_HOSTNAME` variable exists and then configures the endpoint URL accordingly.

```python
...
if 'LOCALSTACK_HOSTNAME' in os.environ:
    dynamodb_endpoint = 'http://%s:4566' % os.environ['LOCALSTACK_HOSTNAME']
    dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_endpoint)
else:
    dynamodb = boto3.resource('dynamodb')
...
```

> Ideally, we want to make LocalStack's Lambda execution environment "LocalStack-agnostic", so that you are not required to adjust endpoints in your function code anymore. You want to help us with that? [Drop us a line in Slack](https://localstack-community.slack.com)!.

## Deploying to LocalStack
You can now deploy your Serverless service to LocalStack.

First, start LocalStack by running
```bash
localstack start
```

Then deploy the endpoint by running
```bash
serverless deploy --stage local
```

The expected result should be similar to:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service my-service.zip file to S3 (38.3 KB)...
Serverless: Validating template...
Serverless: Skipping template validation: Unsupported in Localstack
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.....................................
Serverless: Stack update finished...
Service Information
service: my-service
stage: local
region: us-east-1
stack: my-service-local
resources: 35
api keys:
  None
endpoints:
  http://localhost:4566/restapis/XXXXXXXXXX/local/_user_request_
functions:
  ...
layers:
  None
```

Use the displayed endpoint `http://localhost:4566/restapis/XXXXXXXXXX/local/_user_request_/my/custom/endpoint` to make requests to the deployed service. 


## Advanced topics

### Local code mounting for lambda functions

serverless-localstack supports a feature for lambda functions that allows local code mounting:

```yaml
# serverless.yml

custom:
  localstack:
    # ...
    lambda:
      mountCode: True
```

When this flag is set, the lambda code will be mounted into the container running the function directly from your local directory instead of packaging and uploading it.

If you want to use this feature together with the local lambda executor (`LAMBDA_EXECUTOR=local`), you need to make sure the container running localstack itself can find the code.
To do that, you need to manually mount the code into the localstack container, here is a snippet using a `docker-compose.yml` with the essentials.
Where `/absolute/path/to/todos` is the path on your local machine that points to the `todos/` directory containing the lambda code from our previous example.

```yaml
# docker-compose.yml to start localstack

services:
  localstack:
    # ...
    environment:
      - LAMBDA_EXECUTOR=local
      - LAMBDA_REMOTE_DOCKER=0
      # ...
    volumes:
      # ...
      - "/absolute/path/to/todos:/absolute/path/to/todos"
```

## Ran into trouble?

If you run into any issues or problems while integrating LocalStack with your Serverless app, please [submit an issue](https://github.com/localstack/serverless-localstack/issues).
