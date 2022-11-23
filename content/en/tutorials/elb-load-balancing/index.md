---
title: "Setting up Elastic Load Balancing (ELB) Application Load Balancers using LocalStack, deployed via the Serverless framework"
linkTitle: "Setting up Elastic Load Balancing (ELB) Application Load Balancers using LocalStack, deployed via the Serverless framework"
weight: 3
description: >
  Set up Elastic Loading Balance (ELB) Application Load Balancers to configure Node.js Lambda functions as targets to forward requests to the target group for your Lambda function using LocalStack. Learn how you can use Serverless framework to setup and deploy your infrastructure locally with LocalStack using Serverless-LocalStack plugin.
cascade:
  type: docs
---

AWS Elastic Load Balancer (ELB) distributes incoming application traffic across multiple targets, such as EC2 instances, containers, IP addresses and Lambda functions. ELBs are either physical hardware or virtual software, which accepts incoming traffic and distributes it across multiple targets, in one or more Availability Zones. Using ELB, you can scale your load balancer in accordance with the traffic changes over time, to scale to the needs of your application and the majority of workloads that are running on the AWS infrastructure.

ELB supports, Application Load Balancer, Network Load Balancer, and Classic Load Balancer. Application Load Balancer (ALB) operates at the Application layer of the OSI model, and supports load balancing of applications using HTTP and HTTPS requests. ALB operates at request level and is majorly used in web applications, for advanced load balancing of HTTP and HTTPS traffic. Using ALB, you can register your Lambda functions as targets. A listener rule takes care of forwarding requests to the target group for your Lambda function, which is then invoked to process the request.

[LocalStack Pro](https://localstack.cloud) supports the creation of ELB Application Load Balancers and configuring target groups, such as Lambda functions. In this tutorial, we will set up an ELB Application Load Balancer to configure Node.js Lambda functions as targets using the Serverless framework via our `Serverless-LocalStack plugin` and setup ELB endpoints to forward requests to the target group for your Lambda functions.

## Prerequisites

- [LocalStack Pro](https://localstack.cloud/pricing/)
- [Serverless framework](https://www.serverless.com/framework/docs/getting-started/)
- [Node.js & `npm`](https://nodejs.org/en/download/)

If you don't have LocalStack Pro, you can [sign up for a free trial](https://localstack.cloud/pricing/).

## Setup a Serverless project

Serverless Framework is an open source framework for building, packaging and deploying serverless applications across multiple cloud providers and platforms. Using Serverless framework, you can setup your serverless development environment, define your applications as functions and events, and deploy your entire infrastructure to the cloud with a single command. You can use Serverless framework by installing `serverless` framework via `npm`:

{{< command >}}
$ npm install -g serverless
{{< / command >}}

After installation, you can verify the installation by running the following command:

{{< command >}}
$ serverless --version

Framework Core: 3.24.1
Plugin: 6.2.2
SDK: 4.3.2
{{< / command >}}

Let us now go ahead and create a new Serverless project using the `serverless` command:

{{< command >}}
$ serverless create --template aws-nodejs --path serverless-elb
{{< / command >}}

We are using the `aws-nodejs` template to create our Serverless project. This template consists of a simple Node.js Lambda function that returns a message when invoked. The template also creates a `serverless.yml` file that contains the configuration for the project. 

The `serverless.yml` file contains the configuration for the project, such as the name of the service, the provider, the functions, and example events that trigger the functions. If you need to setup your project using a different template, you can refer to the [Serverless templates](https://www.serverless.com/framework/docs/providers/aws/cli-reference/create/) documentation. We can now go ahead and configure our Serverless project to use LocalStack.

## Configure Serverless project to use LocalStack

To configure your Serverless project to use LocalStack, we need to install the `serverless-localstack` plugin. Before that, let us initialize our project and install some dependencies:

{{< command >}}
$ npm init -y
$ npm install -D serverless serverless-localstack serverless-deployment-bucket
{{< / command >}}

The `serverless-localstack` plugin allows your Serverless project to redirect AWS API calls to LocalStack. The `serverless-deployment-bucket` plugin creates a deployment bucket in LocalStack, which is used to store the deployment artifacts, to ensure that old deployment buckets don't linger around after a deployment. We can now set up the plugin by adding the following properties to our `serverless.yml` file:

```yaml
...
plugins:
  - serverless-deployment-bucket
  - serverless-localstack

custom:
  localstack:
    stages:
      - local
```

This sets up Serverless to use the LocalStack plugin but only for the stage **local**. To ensure that our Serverless project deploys only on LocalStack, and not real AWS Cloud, we need to set a `--stage` flag with `serverless deploy` command and set the flag variable to `local`. 

You can also configure `serverless deploy --stage local` as a `deploy` script in your `package.json`, to allow you to run the `serverless deploy` command directly over your local infrastructure. The `package.json` file should look like this:

{{< command >}}
{
  "name": "serverless-elb",
  "version": "1.0.0",
  "description": "",
  "main": "handler.js",
  "scripts": {
    "deploy": "sls deploy --stage local"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "serverless": "^3.25.0",
    "serverless-deployment-bucket": "^1.6.0",
    "serverless-localstack": "^1.0.1"
  }
}
{{< / command >}}

We can now move ahead, and create Lambda functions to work with a Node.js runtime and configure ELB Application Load Balancers via our `serverless.yml` configuration.

## Create Lambda functions & ELB Application Load Balancers
