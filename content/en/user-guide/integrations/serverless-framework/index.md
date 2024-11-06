---
title: "Serverless Framework"
linkTitle: "Serverless Framework"
description: >
  Use the Serverless Framework with LocalStack
---

<img src="serverless-logo.png" width="600px" alt="Serverless logo">

## Overview

This guide explains how to integrate LocalStack with the [Serverless Framework](https://www.serverless.com/).
Although it probably requires a few code changes, integrating LocalStack with the Serverless Framework is fairly straightforward.

In particular, the setup consists of the following two steps.

1. Installing and configuring the [Serverless-LocalStack plugin](https://github.com/localstack/serverless-localstack).
2. Adjusting AWS endpoints in Lambda functions.

{{< callout "note" >}}
Currently, the Serverless Framework integration with LocalStack via the `serverless-localstack` plugin only provides support up to Serverless Framework version 3.39.
Serverless Framework V4 requires a subscription and a license to use.

The `serverless-localstack` plugin has not been updated or tested against version 4 of the Serverless Framework, and breaking changes are expected if attempted.
Currently there is no timeline on when an update will be released to enable compatibility with Serverless Framework V4.
{{< /callout >}}

## Prerequisites

This guide assumes that you have the following tools installed.

* LocalStack ([Install](https://docs.localstack.cloud/get-started/#installation))
* Serverless ([Install](https://www.serverless.com/framework/docs/getting-started/))

It also assumes that you already have a Serverless app set up consisting of a couple of Lambda functions and a `serverless.yml` file similar to the following.
An example Serverless app integrated with LocalStack can be found here: <a href="https://github.com/localstack/serverless-python-rest-api-with-dynamodb"><i class="fab fa-github"></i>  Simple REST API using the Serverless Framework and LocalStack</a>

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
{{< command >}}
$ npm install -D serverless-localstack
{{< / command >}}

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

By default, this call attempts to create a connection via the usual AWS endpoints.
However, when running services in LocalStack, we need to make sure, our applications creates a connection via the LocalStack endpoint instead.

Usually, all of LocalStack's services are available via a specific port on localhost (e.g. `localhost:4566`).
However, this endpoint only works when accessing LocalStack from outside its Docker runtime.

Since the Lambda functions execute within the LocalStack Docker container, Lambda functions cannot access other services via the usual localhost endpoint.

Instead, LocalStack provides a special environment variable `AWS_ENDPOINT_URL` which contains the internal endpoint of the LocalStack services from within its runtime environment.

Hence, you need to configure the Lambda functions to use the `AWS_ENDPOINT_URL` endpoint when accessing other AWS services in LocalStack.

In Python, this may look something like.
The code detects if it is running in LocalStack by checking if the `AWS_ENDPOINT_URL` variable exists and then configures the endpoint URL accordingly.

```python
...
if 'AWS_ENDPOINT_URL' in os.environ:
    dynamodb = boto3.resource('dynamodb', endpoint_url=os.environ['AWS_ENDPOINT_URL'])
else:
    dynamodb = boto3.resource('dynamodb')
...
```

In LocalStack Pro, no code changes are required using our [Transparent Endpoint Injection]({{< ref "user-guide/tools/transparent-endpoint-injection" >}}).

## Deploying to LocalStack

You can now deploy your Serverless service to LocalStack.

First, start LocalStack by running
{{< command >}}
$ localstack start
{{< / command >}}

Then deploy the endpoint by running
{{< command >}}
$ serverless deploy --stage local
{{< / command >}}

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

## Custom API deployment IDs
By default localstack generates random dployment ids for the API gateway which in turn get populated into the endpoint URLs. As these IDs can literally change every time you deploy (depending on your setup) This makes continual local development practically impossibly in situations where you rely on consistant urls (eg the url for your api for your frontend code)

localstack provides a method to use a fixed custom id instead by passing a tag _custom_id_ to the API during creation. It has to be done during creation and it has to be on either the v2 API or the v1 RestApi.

Serverless can do this out of the box with resource extensions. See below for the v1/v2 implementation.

This will produce endpoints like
http://localhost:4566/restapis/mytag/development/_user_request_  (v1)

rather than a continually changing ID
http://localhost:4566/restapis/jh345798dx/development/_user_request_

```
resources:
  extensions:
    ApiGatewayRestApi:  #for v1
      Properties:
        Tags:
          - Key: _custom_id_
            Value: mytag

    MyHTTPApi:  #for v2
      Properties:
        Tags:
          - Key: _custom_id_
            Value: mytag

```
 

## Ran into trouble?

If you run into any issues or problems while integrating LocalStack with your Serverless app, please [submit an issue](https://github.com/localstack/serverless-localstack/issues).
