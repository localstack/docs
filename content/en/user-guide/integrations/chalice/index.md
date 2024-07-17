---
title: "AWS Chalice"
linkTitle: "AWS Chalice"
description: >
  Use AWS Chalice with LocalStack
---

[AWS Chalice](https://aws.github.io/chalice/) is a serverless micro framework used to develop and deploy your serverless applications on AWS resources. Chalice provides integrated functionality with most of the AWS Toolings like S3 Storage, Simple Queue Service, API Gateway and more. It offers a handy CLI interface that allows you to easily create, develop & deploy your serverless applications.

LocalStack offers an [AWS Chalice client](https://github.com/localstack/chalice-local) that allows you to interact with your Chalice applications locally. Using LocalStack, you can kick-start your development process, create a new Chalice application, and test it application locally.

## Creating a new Chalice project

Start LocalStack inside a Docker container by running:

{{< command >}}
$ localstack start -d
{{< / command >}}

Install the `chalice-local` package by running:

{{< command >}}
$ pip install chalice-local
{{< / command >}}

You can now create a new Chalice project by running:

{{< command >}}
$ chalice-local new-project
{{< / command >}}

You will be prompted with an interactive menu where you can choose the name of your project and the project type. In this example, we are using `localstack-test` as the project name and `REST API` as the project type:

```sh
   ___  _  _    _    _     ___  ___  ___
  / __|| || |  /_\  | |   |_ _|/ __|| __|
 | (__ | __ | / _ \ | |__  | || (__ | _|
  \___||_||_|/_/ \_\|____||___|\___||___|


The python serverless microframework for AWS allows
you to quickly create and deploy applications using
Amazon API Gateway and AWS Lambda.

Please enter the project name
[?] Enter the project name: localstack-test
[?] Select your project type: REST API
 > REST API
   S3 Event Handler
   Lambda Functions only
   Legacy REST API Template
   [CDK] Rest API with a DynamoDB table

Your project has been generated in ./localstack-test
```

Let's take a look inside the project structure:

```sh
tree
.
├── app.py
├── chalicelib
│   └── __init__.py
├── requirements-dev.txt
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_app.py

2 directories, 6 files
```

The `app.py` is our main API file. It has only one Route that would assign the URL of the application to the function. The decorators here primarily "wrap" functions here which makes it easy to write Code Logic by breaking them down into separate routes. For now, our Application is serving only a JSON Message which is `{'hello': 'world'}`.

## Testing the Chalice API

Just as with AWS, you can now test your API using `chalice-local local`:

{{< command >}}
$ chalice-local local
Serving on http://127.0.0.1:8000
{{< / command >}}

You can also do a `curl` to test the API:

{{< command >}}
$ curl -X GET http://127.0.0.1:8000
{"hello":"world"}
{{< / command >}}

## Deploying the Chalice API

You can use `chalice-local deploy` to deploy the REST API now:

{{< command >}}
$ chalice-local deploy

Creating deployment package.
Creating IAM role: localstack-test-dev
Creating lambda function: localstack-test-dev
Creating Rest API
Resources deployed:
- Lambda ARN: arn:aws:lambda:us-east-1:000000000000:function:localstack-test-dev
- Rest API URL: https://y5iuni004m.execute-api.us-east-1.amazonaws.com/api/
{{< / command >}}

We now have our Chalice Application deployed on a Lambda Amazon Resource Name (ARN) along with a REST API URL.
