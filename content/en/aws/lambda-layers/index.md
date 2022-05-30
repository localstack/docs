---
title: "Lambda Layers"
linkTitle: "Lambda Layers"
categories: ["LocalStack Pro"]
description: >
  Lambda Layers
---

[Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) are an AWS feature that allows to pull in additional code and content into your Lambda functions.

Simply point your Lambda client code at your LocalStack instance, e.g., running on http://localhost. For more details on how to use Lambda layers, please follow the documentation and examples on the [AWS website](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Creating Lambda layers locally

The simplest approach is to create Lambda layers locally, by using the `PublishLayerVersion` API against LocalStack.
Below is a simple example for creating a Lambda layer in Python with a `util()` function that prints some output.

{{< command >}}
$ mkdir -p /tmp/python/
$ echo 'def util():' > /tmp/python/testlayer.py
$ echo '  print("Output from Lambda layer util function")' >> /tmp/python/testlayer.py
$ (cd /tmp; zip -r testlayer.zip python)
$ awslocal lambda publish-layer-version --layer-name layer1 --zip-file fileb:///tmp/testlayer.zip
{{< / command >}}

We can then create a simple Lambda function which references the Lambda layer:
{{< command >}}
$ echo 'def handler(*args, **kwargs):' > /tmp/testlambda.py
$ echo '  import testlayer; testlayer.util()' >> /tmp/testlambda.py
$ echo '  print("Debug output from Lambda function")' >> /tmp/testlambda.py
$ (cd /tmp; zip testlambda.zip testlambda.py)
$ awslocal lambda create-function --function-name func1 --runtime python3.8 --role r1 --handler testlambda.handler --timeout 30 --zip-file fileb:///tmp/testlambda.zip --layers arn:aws:lambda:$AWS_DEFAULT_REGION:000000000000:layer:layer1:1
{{< / command >}}

Once we invoke the Lambda function, we should see the following logs in the LocalStack container (with `DEBUG=1` enabled), which includes the output from the layer util function:
```
>START RequestId: a8bc4ce6-e2e8-189e-cf58-c2eb72827c23 Version: $LATEST
> Output from Lambda layer util function
> Debug output from Lambda function
> END RequestId: a8bc4ce6-e2e8-189e-cf58-c2eb72827c23
```

## Referencing Lambda layers from real AWS

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
