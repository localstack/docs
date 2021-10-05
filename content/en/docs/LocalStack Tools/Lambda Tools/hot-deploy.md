---
title: "Hot Deployment"
date: 2021-09-27
weight: 5
description: >
  Hot-deploy your Lambdas using local code mounting
---

Quickly iterating over Lambda function code can be quite cumbersome, as you need to deploy your function on every change. 
With LocalStack you can avoid this hurdle by mounting your code directly from the source folder. 
This way, any saved change inside your source file directly affects the already deployed Lambda function -- without any redeployment!

We show you how you can do this with a simple example function, taken directly from the [AWS Lambda developer guide](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/lambda/boto_client_examples/lambda_handler_basic.py).
You can check out that code, or use your own lambda functions to follow along. 
To use the example just do:
```sh
cd /tmp
git clone git@github.com:awsdocs/aws-doc-sdk-examples.git
```


### Starting up LocalStack 

First, we need to make sure we start LocalStack with the right configuration.
This is as simple as setting `LAMBDA_REMOTE_DOCKER`(see the [Configuration Documentation]({{< ref "configuration#lambda" >}} for more information):

```sh
LAMBDA_REMOTE_DOCKER=0 localstack start
```

### Creating the Lambda Function

To create the Lambda function, you just need to take care of two things:
1. Deploy via an S3 Bucket. You need to use the magic variable `__local__` as the bucket.
2. Set the S3 key to the path of the directory your lambda function resides in.
   The handler is then referenced by the filename of your lambda code and the function in that code that needs to be invoked.

So, using the AWS example, this would be:

```sh
awslocal lambda create-function --function-name my-cool-local-function \
    --code S3Bucket="__local__",S3Key="/tmp/aws-doc-sdk-examples/python/example_code/lambda/boto_client_examples" \         
    --handler lambda_handler_basic.lambda_handler \
    --runtime python3.8 \
    --role cool-stacklifter
```

We can also quickly make sure that it works by invoking it with a simple payload:

```sh
awslocal lambda invoke --function-name my-cool-local-function --payload '{"action": "square", "number": 3}' output.txt 
```

The invocation returns itself returns:

```json
{
    "StatusCode": 200,
    "LogResult": "",
    "ExecutedVersion": "$LATEST"
}
```
and `output.txt` contains:
```json
{"result":9}
```

### Changing things up

Now, that we got everything up and running, the fun begins. 
Because the function is now mounted as a file in the executing container, any change that we save on the file will be there in an instant. 

For example, we can now make a minor change to the API and replace the response in [line 41](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/lambda/boto_client_examples/lambda_handler_basic.py#L41) with the following:
```python
    response = {'math_result': result}
```
Without redeploying or updating the function, the result of the previous request will look like this:
```json
{"math_result":9}
```
Cool!
