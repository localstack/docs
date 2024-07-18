---
title: "Setting up Elastic Load Balancing (ELB) Application Load Balancers using LocalStack, deployed via the Serverless framework"
linkTitle: "Setting up Elastic Load Balancing (ELB) Application Load Balancers using LocalStack, deployed via the Serverless framework"
weight: 3
description: >
  Learn how to configure Elastic Load Balancing (ELB) Application Load Balancers and set up Node.js Lambda functions as targets. This tutorial demonstrates how to forward requests to the target group for your Lambda function using the Serverless Framework and the `serverless-localstack` plugin to effortlessly deploy and manage your infrastructure locally with LocalStack.
type: tutorials
teaser: ""
services:
- elb
- lmb
platform:
- JavaScript
deployment:
- serverless
tags:
- Elastic Load Balancing
- Lambda
- Serverless Framework
- Node.js
- JavaScript
- serverless-localstack plugin
pro: true
leadimage: "elb-load-balancing-featured-image.png"
---

[Elastic Load Balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/) is a service that distributes incoming application traffic across multiple targets, such as EC2 instances, containers, IP addresses, and Lambda functions. ELBs can be physical hardware or virtual software components. They accept incoming traffic and distribute it across multiple targets in one or more Availability Zones. Using ELB, you can quickly scale your load balancer to accommodate changes in traffic over time, ensuring optimal performance for your application and workloads running on the AWS infrastructure.

ELB provides three types of load balancers: [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html), [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html), [Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html), and [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html).

In this tutorial we focus on the Application Load Balancer (ALB), which operates at the Application layer of the OSI model and is specifically designed for load balancing HTTP and HTTPS traffic for web applications. ALB works at the request level, allowing advanced load-balancing features for HTTP and HTTPS requests. It also enables you to register Lambda functions as targets. You can configure a listener rule that forwards requests to a target group for your Lambda function, triggering its execution to process the request.

[LocalStack Pro](https://localstack.cloud) extends support for ELB Application Load Balancers and the configuration of target groups, including Lambda functions. This tutorial will guide you through setting up an ELB Application Load Balancer to configure Node.js Lambda functions as targets. We will utilize the [Serverless framework](http://serverless.com/) along with the [`serverless-localstack` plugin](https://www.serverless.com/plugins/serverless-localstack) to simplify the setup. Additionally, we will demonstrate how to set up ELB endpoints to efficiently forward requests to the target group associated with your Lambda functions.

## Prerequisites

- LocalStack Pro
- [Serverless framework](https://www.serverless.com/framework/docs/getting-started/)
- [Node.js & `npm`](https://nodejs.org/en/download/)
- [awslocal]({{< ref "aws-cli#localstack-aws-cli-awslocal" >}})
- `cURL` & `jq`

## Setup a Serverless project

Serverless is an open-source framework that enables you to build, package, and deploy serverless applications seamlessly across various cloud providers and platforms. With the Serverless framework, you can easily set up your serverless development environment, define your applications as functions and events, and deploy your entire infrastructure to the cloud using a single command. To start using the Serverless framework, install the Serverless framework globally by executing the following command using `npm`:

{{< command >}}
$ npm install -g serverless
{{< / command >}}

The above command installs the Serverless framework globally on your machine. After the installation is complete, you can verify it by running the following command:

{{< command >}}
$ serverless --version

Framework Core: 3.24.1
Plugin: 6.2.2
SDK: 4.3.2
{{< / command >}}

This command displays the version numbers of the Serverless framework's core, plugins, and SDK you installed. Now, let's proceed with creating a new Serverless project using the `serverless` command:

{{< command >}}
$ serverless create --template aws-nodejs --path serverless-elb
{{< / command >}}

In this example, we use the `aws-nodejs` template to create our Serverless project. This template includes a simple Node.js Lambda function that returns a message when invoked. It also generates a `serverless.yml` file that contains the project's configuration.

The `serverless.yml` file is where you configure your project. It includes information such as the service name, the provider (AWS in this case), the functions, and example events that trigger those functions. If you prefer to set up your project using a different template, refer to the [Serverless templates documentation](https://www.serverless.com/framework/docs/providers/aws/cli-reference/create/) for more options.

Now that we have created our Serverless project, we can proceed to configure it to use LocalStack.

## Configure Serverless project to use LocalStack

To configure your Serverless project to use LocalStack, you need to install the `serverless-localstack` plugin. Before that, let's initialize the project and install some dependencies:

{{< command >}}
$ npm init -y
$ npm install -D serverless serverless-localstack serverless-deployment-bucket
{{< / command >}}

In the above commands, we use `npm init -y` to initialize a new Node.js project with default settings and then install the necessary dependencies, including `serverless`, `serverless-localstack`, and `serverless-deployment-bucket`, as dev dependencies.

The `serverless-localstack` plugin enables your Serverless project to redirect AWS API calls to LocalStack, while the `serverless-deployment-bucket` plugin creates a deployment bucket in LocalStack. This bucket is responsible for storing the deployment artifacts and ensuring that old deployment buckets are properly cleaned up after each deployment.

We have a `serverless.yml` file in the directory to define our Serverless project's configuration, which includes information such as the service name, the provider (AWS in this case), the functions, and example events that trigger those functions. To set up the plugins we installed earlier, you need to add the following properties to your `serverless.yml` file:

```yaml
service: serverless-elb

frameworkVersion: '3'

provider:
  name: aws
  runtime: nodejs12.x


functions:
  hello:
    handler: handler.hello

plugins:
  - serverless-deployment-bucket
  - serverless-localstack

custom:
  localstack:
    stages:
      - local
```

To configure Serverless to use the LocalStack plugin specifically for the `local` stage and ensure that your Serverless project only deploys to LocalStack instead of the real AWS Cloud, you need to set the `--stage` flag when using the `serverless deploy` command and specify the flag variable as `local`.

Configure a `deploy` script in your `package.json` file to simplify the deployment process. It lets you run the `serverless deploy` command directly over your local infrastructure. Update your `package.json` file to include the following:

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

With this configuration, you can now run the deployment script using:

{{< command >}}
$ npm run deploy
{{< / command >}}

This will execute the `serverless deploy --stage local` command, deploying your Serverless project to LocalStack.

## Create Lambda functions & ELB Application Load Balancers

Now, let's create two Lambda functions named `hello1` and `hello2` that will run on the Node.js 12.x runtime. Open the `handler.js` file and replace the existing code with the following:

```js
'use strict';

module.exports.hello1 = async (event) => {
  console.log(event);
  return {
    "isBase64Encoded": false,
    "statusCode": 200,
    "statusDescription": "200 OK",
    "headers": {
        "Content-Type": "text/plain"
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
        "Content-Type": "text/plain"
    },
    "body": "Hello 2"
  };
};
```

We have defined the `hello1` and `hello2` Lambda functions in the updated code. Each function receives an event parameter and logs it to the console. The function then returns a response with a status code of 200 and a plain text body containing the respective `"Hello"` message. It's important to note that the `isBase64Encoded` property is not required for plain text responses. It is typically used when you need to include binary content in the response body and want to indicate that the content is Base64 encoded.

Let us now configure the `serverless.yml` file to create an Application Load Balancer (ALB) and attach the Lambda functions to it.

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

plugins:
  - serverless-deployment-bucket
  - serverless-localstack

custom:
  localstack:
    stages:
      - local
```

In the above configuration, we specify the service name (`serverless-elb` in this case) and set the provider to AWS with the Node.js 12.x runtime. We include the necessary plugins, `serverless-localstack` and `serverless-deployment-bucket`, for LocalStack support and deployment bucket management. Next, we define the `hello1` and `hello2` functions with their respective handlers and event triggers. In this example, both functions are triggered by HTTP GET requests to the `/hello1` and `/hello2` paths.

Lastly, let's create a VPC, a subnet, an Application Load Balancer, and an HTTP listener on the load balancer that redirects traffic to the target group. To do this, add the following resources to your `serverless.yml` file:

```yaml
...
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

With these resource definitions, you have completed the configuration of your Serverless project. Now you can create your local AWS infrastructure on LocalStack and deploy your Application Load Balancers with the two Lambda functions as targets.

## Creating the infrastructure on LocalStack

Now that we have completed the initial setup let's run LocalStack's AWS emulation on our local machine. Start LocalStack by running the following command:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<your-auth-token> localstack start -d
{{< / command >}}

This command launches LocalStack in the background, enabling you to use the AWS services locally. Now, let's deploy our Serverless project and verify the resources created in LocalStack. Run the following command:

{{< command >}}
$ npm run deploy
{{< / command >}}

This command deploys your Serverless project using the "local" stage. The output will resemble the following:

```bash
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
```

This output confirms the successful deployment of your Serverless service to the `local` stage in LocalStack. It also displays information about the deployed Lambda functions (`hello1` and `hello2`). You can run the following command to verify that the functions and the load balancers have been deployed:

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


The ALB endpoints for the two Lambda functions, hello1 and hello2, are accessible at the following URLs:

- [`http://lb-test-1.elb.localhost.localstack.cloud:4566/hello1`](http://lb-test-1.elb.localhost.localstack.cloud:4566/hello1)
- [`http://lb-test-1.elb.localhost.localstack.cloud:4566/hello2`](http://lb-test-1.elb.localhost.localstack.cloud:4566/hello2)

To test these endpoints, you can use the curl command along with the jq tool for better formatting. Run the following commands:

{{< command >}}
$ curl http://lb-test-1.elb.localhost.localstack.cloud:4566/hello1 | jq
"Hello 1"
$ curl http://lb-test-1.elb.localhost.localstack.cloud:4566/hello2 | jq
"Hello 2"
{{< / command >}}

Both commands send an HTTP GET request to the endpoints and uses `jq` to format the response. The expected outputs are `Hello 1` & `Hello 2`, representing the Lambda functions' response.

## Conclusion

In this tutorial, we have learned how to create an Application Load Balancer (ALB) with two Lambda functions as targets using LocalStack. We have also explored creating, configuring, and deploying a Serverless project with LocalStack. This enables developers to develop and test Cloud and Serverless applications locally conveniently.

LocalStack offers integrations with various popular tools such as Terraform, Pulumi, Serverless Application Model (SAM), and more. For more information about LocalStack integrations, you can refer to our [Integration documentation]({{< ref "user-guide/integrations">}}). To further explore and experiment with the concepts covered in this tutorial, you can access the code and resources on our [LocalStack Pro samples over GitHub](https://github.com/localstack/localstack-pro-samples/tree/master/elb-load-balancing) along with a `Makefile` for step-by-step execution.
