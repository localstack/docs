---
title: "Lambda"
linkTitle: "Lambda"
categories: ["LocalStack Community", "LocalStack Pro"]
description: >
  Supporting local development and testing of AWS Lambdas on LocalStack
aliases:
  - /aws/lambda/
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
- [Lambda Function URL](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-function-urls): Simple demo application illustrating Lambda Function URLs using LocalStack, to call a Lambda Function via HTTP.

## Lambda Function URL

LocalStack supports [Lambda Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-configuration.html) for calling Lambda Functions via HTTP. Below is a simple example to deploy a Lamda function via a ZIP file before creating a Function URL:

{{< command >}}
$ awslocal lambda create-function \
    --function-name <function-name> \
    --runtime <lambda-runtime> \
    --zip-file fileb://<path/to/zip/file> \
    --handler index.handler \
    --role cool-stacklifter
{{< / command >}}

After the Lambda function is created, you can create a Function URL to call the Lambda function:

{{< command >}}
awslocal lambda create-function-url-config \
    --function-name <function-name> \
    --auth-type NONE
{{< / command >}}

## Lambda Container Images

LocalStack Pro supports [Lambda functions defined as container images](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html), so you can bundle your code and dependencies as one container image.

{{< alert >}}
If your Lambda custom image fails with the error `exec /tmp/xxx.sh: no such file or directory`, ensure `bash` and `python 2/3` is installed inside your container image for the integration with LocalStack to work.
{{< /alert >}}

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

## Lambda Event Filtering

Lambda Functions with the event-filtering enables ease of integration and developing cloud-native applications. LocalStack enables Lambda Event Filtering for DynamoDB Streams, and SQS. The filtering implements following filtering syntax:

| Comparison operator | Example                                             | Rule syntax                                       |
| ------------------- | --------------------------------------------------- | ------------------------------------------------- |
| Null                | UserID is null                                      | "UserID": [ null ]                                |
| Empty               | LastName is empty                                   | "LastName": [""]                                  |
| Equals              | Name is "Alice"                                     | "Name": [ "Alice" ]                               |
| And                 | Location is "New York" and Day is "Monday"          | "Location": [ "New York" ], "Day": ["Monday"]     |
| Or                  | PaymentType is "Credit" or "Debit"                  | "PaymentType": [ "Credit", "Debit"]               |
| Not                 | Weather is anything but "Raining"                   | "Weather": [ { "anything-but": [ "Raining" ] } ]  |
| Numeric (equals)    | Price is 100                                        | "Price": [ { "numeric": [ "=", 100 ] } ]          |
| Numeric (range)     | Price is more than 10, and less than or equal to 20 | "Price": [ { "numeric": [ ">", 10, "<=", 20 ] } ] |
| Exists              | ProductName exists                                  | "ProductName": [ { "exists": true } ]             |
| Does not exist      | ProductName does not exist                          | "ProductName": [ { "exists": false } ]            |
| Begins with         | Region is in the US                                 | "Region": [ {"prefix": "us-" } ]                  |

The filter expression uses a strict JSON format to match the filtering criteria. For example, in a DynamoDB Stream, JSON is validated against the key `dynamodb` which is part of the event JSON. An example of a filter expression is:

```json
{
    "Records": [
        {
            ...
            "dynamodb": { }
            ...
        }
    ]
}
```

If your DynamoDB event is being triggered, you can now apply additional logic via event filtering with patterns. The event filtering will use criteria checks mentioned above. However only five event filtering patterns is limited to a single Lambda function and each of the 5 patterns is validated against an OR condition. For more information, refer to the [official AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html).
