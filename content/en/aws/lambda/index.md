---
title: "Lambda"
linkTitle: "Lambda"
categories: ["LocalStack Community", "LocalStack Pro"]
description: >
  Supporting local development and testing of AWS Lambdas on LocalStack
---

AWS Lambda is a Serverless Function as a Service (FaaS) system that allows you to write code in your favorite programming language and run it on the AWS ecosystem. Unlike deploying your code on a server, you can now break down your application into many independent functions and deploy them as a singular units. With the help of AWS Lambda, you can strive for more modular code that can be tested and debugged while integrated with the AWS infrastructure and your core system.

LocalStack allows you to execute your Lambda functions locally, without the need to deploy them to AWS. This is a great way to test your code, and to learn more about how your Lambda functions work, before deploying them to AWS. LocalStack allows you to execute your Lambda functions, in various execution modes, which is detailed on our [Lambda execution modes]({{< ref "lambda-executors" >}}) page.

## Special tooling for Lambdas

We also provide tools to help you develop, debug and test your Lambda functions more efficiently:

- [Hot swapping]({{< ref "hot-swapping" >}}): Hot code swapping for Lambda functions using LocalStack’s code mounting feature.
- [Remote debugging]({{< ref "debugging" >}}): Attaching a debugger to your Lambda function using your IDE.

## Lambda sample applications

LocalStack Pro samples contains a number of code examples that demonstrate how to use LocalStack to execute Lambda functions:

- [Lambda XRay Tracing](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-xray): Simple demo application illustrating Lambda XRay tracing using LocalStack, deployed via the Serverless framework.
- [Lambda Container Images](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-container-image): Simple demo application illustrating Lambda container images in LocalStack. The Lambda image is built using Docker and pushed to a local ECR registry.
- [Lambda Code Mounting and Debugging](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-mounting-and-debugging): Simple demo application to illustrate debugging Lambdas locally.
- [Lambda Layers](https://github.com/localstack/localstack-pro-samples/blob/master/serverless-lambda-layers): Simple demo application illustrating Lambda layers using LocalStack, deployed via the Serverless framework.

## Lambda Layers

[Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) are an AWS feature that allows to pull in additional code and content into your Lambda functions.

LocalStack Pro provides support for deploying Lambda layers locally - for more details on general usage, please follow the documentation and examples in the [AWS documentation on Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

### Creating Lambda layers locally

To create a Lambda layer locally, you can simply use the `PublishLayerVersion` API against LocalStack.
Below is a simple example for creating a Lambda layer in Python with a `util()` function that prints some test output.

{{< command >}}
$ mkdir -p /tmp/python/
$ echo 'def util():' > /tmp/python/testlayer.py
$ echo '  print("Output from Lambda layer util function")' >> /tmp/python/testlayer.py
$ (cd /tmp; zip -r testlayer.zip python)
$ LAYER_ARN=$(awslocal lambda publish-layer-version --layer-name layer1 --zip-file fileb:///tmp/testlayer.zip | jq -r .LayerArn)
{{< / command >}}

We can then create a simple Lambda function which references and imports the Lambda layer:
{{< command >}}
$ echo 'def handler(*args, **kwargs):' > /tmp/testlambda.py
$ echo '  import testlayer; testlayer.util()' >> /tmp/testlambda.py
$ echo '  print("Debug output from Lambda function")' >> /tmp/testlambda.py
$ (cd /tmp; zip testlambda.zip testlambda.py)
$ awslocal lambda create-function --function-name func1 --runtime python3.8 --role r1 --handler testlambda.handler --timeout 30 --zip-file fileb:///tmp/testlambda.zip --layers $LAYER_ARN:1
{{< / command >}}

Once we invoke the Lambda function, we should see the following logs in the LocalStack container (with `DEBUG=1` enabled), which includes the output from the layer util function:
```
> START RequestId: a8bc4ce6-e2e8-189e-cf58-c2eb72827c23 Version: $LATEST
> Output from Lambda layer util function
> Debug output from Lambda function
> END RequestId: a8bc4ce6-e2e8-189e-cf58-c2eb72827c23
```

### Referencing Lambda layers from real AWS

Alternatively, if your Lambda function references a layer in real AWS, there is also a mechanism to integrate such a remote layer into your local dev environment.

In order to achieve that, you'll need to make your Lambda layer accessible from the `886468871268` AWS account ID (this is an account managed by LocalStack on AWS).
Assuming you've created a layer named `test-layer` with version `1`, you can use the following command to grant access to your layer:

{{< command >}}
$ aws lambda add-layer-version-permission
  --layer-name test-layer
  --version-number 1
  --statement-id layerAccessFromLocalStack
  --principal 886468871268
  --action lambda:GetLayerVersion
{{< / command >}}

Next time you reference this layer (with the real AWS Lambda layer ARN) in one of your local Lambda functions, it will get automatically pulled down and integrated into your local dev environment.
