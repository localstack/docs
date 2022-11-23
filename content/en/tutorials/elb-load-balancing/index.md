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
- [`awslocal`](https://docs.localstack.cloud/integrations/aws-cli/#localstack-aws-cli-awslocal)

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

```json
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
```

You can give the above setup a run, by deploying your Serverless project and checking the Lambda function that has been created via our existing Serverless project:

{{< command >}}
$ npm run deploy
$ awslocal lambda list-functions

{
    "Functions": [
        {
            "FunctionName": "serverless-elb-local-hello",
            "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:serverless-elb-local-hello",
            "Runtime": "nodejs12.x",
            "Role": "arn:aws:iam::000000000000:role/serverless-elb-local-us-east-1-lambdaRole",
            "Handler": "handler.hello",
            ...
        }
    ]
}
{{< / command >}}

We can now move ahead, and create our target Lambda functions to work with Node.js runtime and configure ELB Application Load Balancers via our `serverless.yml` configuration.

## Create Lambda functions & ELB Application Load Balancers

Let us now create two Lambda functions, named `hello1` and `hello2`, which can run over Node.js 12.x runtime. Open `handler.js` and replace the existing code with the following:

```js
'use strict';

module.exports.hello1 = async (event) => {
  console.log(event);
  return {
    "isBase64Encoded": false,
    "statusCode": 200,
    "statusDescription": "200 OK",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": "Hello 1"
  };
};

module.exports.hello2 = async (event) => {
  console.log(event);
    return {
    "isBase64Encoded": false,
    "statusCode": 200,
    "statusDescription": "200 OK",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": "Hello 2"
  };
};
```

In the above code, we have created `hello1` and `hello2` Lambda functions, and created a response body for them which includes the Base64 encoding status, status code, and headers. If you wish to include a binary content in the response body, set the `isBase64Encoded` property to `true`. The load balancer requires to retrieve the binary content to send it in the body of an HTTP response.

Let us now move to `serverless.yml` file and specify our deployment bucket, and the functions that we want to deploy. Our initial configuration in the `serverless.yml` file should look like this:

```yaml
service: serverless-elb

provider:
  name: aws
  runtime: nodejs12.x
  deploymentBucket:
    name: testbucket

functions:
  hello1:
    handler: handler.hello1
    events:
    - alb:
        listenerArn: !Ref HTTPListener
        priority: 1
        conditions:
          path: /hello1
  hello2:
    handler: handler.hello2
    events:
    - alb:
        listenerArn: !Ref HTTPListener
        priority: 2
        conditions:
          path: /hello2
```

In the above configuration, we specify our Lambda functions `hello1` and `hello2`, and specify an HTTP listener that forwards requests to the target group. We have also specified a `deploymentBucket` property, which is used to store the deployment artifacts. Before deploying our Serverless project, we would need to create an S3 bucket named `testbucket` in LocalStack. 

Let us now create a VPC, a subnet, an Application Load Balancer, and an an HTTP listener on the load balancer, which redirects the traffic to the target group. We can do this by adding the following resources to our `serverless.yml` file:

```yaml
resources:
  Resources:
    LoadBalancer:
      Type: AWS::ElasticLoadBalancingV2::LoadBalancer
      Properties:
        Name: lb-test-1
        Subnets:
          - !Ref Subnet
    HTTPListener:
      Type: AWS::ElasticLoadBalancingV2::Listener
      Properties:
        DefaultActions:
          - Type: redirect
            RedirectConfig:
              Protocol: HTTPS
              Port: 443
              Host: "#{host}"
        LoadBalancerArn: !Ref LoadBalancer
        Protocol: HTTP
    Subnet:
      Type: AWS::EC2::Subnet
      Properties:
        VpcId: !Ref VPC
        CidrBlock: 12.2.1.0/24
        AvailabilityZone: !Select
          - 0
          - Fn::GetAZs: !Ref "AWS::Region"
    VPC:
      Type: AWS::EC2::VPC
      Properties:
        EnableDnsSupport: "true"
        EnableDnsHostnames: "true"
        CidrBlock: 12.2.1.0/24
```

With this, we have now completed our Serverless project's configuration. We can now create our local AWS infrastructure on LocalStack and deploy our Application Load Balancers with two Lambda functions as targets.

## Creating the infrastructure on LocalStack

Now that the initial setup is done, we can give LocalStack's AWS emulation a run on our local machine. Let's start LocalStack:

{{< command >}}
$ LOCALSTACK_API_KEY=<your-api-key> localstack start -d
{{< / command >}}

Let us first create an S3 bucket named `testbucket` in LocalStack to store our deployment artifacts. We can do this by running the following command:

{{< command >}}
$ awslocal s3api create-bucket --bucket testbucket
{
    "Location": "/testbucket"
}
{{< / command >}}

We can now deploy our Serverless project and check the created resources in LocalStack. We can do this by running the following command:

{{< command >}}
$ npm run deploy

> serverless-elb@1.0.0 deploy
> sls deploy --stage local

Using serverless-localstack

Deploying test-elb-load-balancing to stage local (us-east-1)
Creating deployment bucket 'testbucket'...
Using deployment bucket 'testbucket'
Skipping template validation: Unsupported in Localstack

✔ Service deployed to stack test-elb-load-balancing-local (15s)

functions:
  hello1: test-elb-load-balancing-local-hello1 (157 kB)
  hello2: test-elb-load-balancing-local-hello2 (157 kB)
{{< / command >}}

You can check the Lambda functions and the Application Load Balancer created in LocalStack by running the following commands:

{{< command >}}
$ awslocal lambda list-functions

{
    "Functions": [
        {
            "FunctionName": "test-elb-load-balancing-local-hello1",
            "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:test-elb-load-balancing-local-hello1",
            "Runtime": "nodejs12.x",
            "Role": "arn:aws:iam::000000000000:role/test-elb-load-balancing-local-us-east-1-lambdaRole",
            "Handler": "handler.hello1",
            ...
        },
        {
            "FunctionName": "test-elb-load-balancing-local-hello2",
            "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:test-elb-load-balancing-local-hello2",
            "Runtime": "nodejs12.x",
            "Role": "arn:aws:iam::000000000000:role/test-elb-load-balancing-local-us-east-1-lambdaRole",
            "Handler": "handler.hello2",
            ...
        }
    ]
}

$ awslocal elbv2 describe-load-balancers
{
    "LoadBalancers": [
        {
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:000000000000:loadbalancer/app/lb-test-1/<ID>",
            "DNSName": "lb-test-1.elb.localhost.localstack.cloud",
            "CanonicalHostedZoneId": "<ID>",
            "CreatedTime": "<TIMESTAMP>",
            "LoadBalancerName": "lb-test-1",
            "Scheme": "None",
            ...
        }
    ]
}
{{< / command >}}

The ALB endpoints for the two Lambda functions that we created are accessible at `http://lb-test-1.elb.localhost.localstack.cloud:4566/hello1` and `http://lb-test-1.elb.localhost.localstack.cloud:4566/hello2`. We can test this by running the following commands:

{{< command >}}
$ curl http://lb-test-1.elb.localhost.localstack.cloud:4566/hello1 | jq
"Hello from hello1"
$ curl http://lb-test-1.elb.localhost.localstack.cloud:4566/hello2 | jq
"Hello from hello2"
{{< / command >}}

## Conclusion

In this post, we have seen how to create an Application Load Balancer with two Lambda functions as targets using LocalStack. We have also seen how to create, configure, and deploy a Serverless project with LocalStack serving as an emulated local AWS environment that allows you to develop and test your Cloud & Serverless applications with AWS locally. 

LocalStack also offers integrations with other popular tools such as Terraform, Pulumi, Severless Application Model (SAM), and more. You can find more information about LocalStack integrations on our [Integration documentation]({{< ref "integration" >}}). The code for this tutorial (including a `Makefile` to execute it step-by-step) can be found in our [LocalStack Pro samples over GitHub](https://github.com/localstack/localstack-pro-samples/tree/master/elb-load-balancing).
