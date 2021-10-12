---
title: "Hot Swapping"
date: 2021-09-27
weight: 5
categories: ["LocalStack Community", "LocalStack Pro"]
description: >
  Hot code swapping for Lambda functions using LocalStack's code mounting
---

| Complexity   | ★☆☆☆☆             |
|--------------|-------------------|
| Time to read | 5 minutes         |
| Edition      | community/pro     |
| Platform     | any               |

Quickly iterating over Lambda function code can be quite cumbersome, as you need to deploy your function on every change.
With LocalStack you can avoid this hurdle by mounting your code directly from the source folder.
This way, any saved change inside your source file directly affects the already deployed Lambda function -- without any redeployment!

## Covered Topics

[Application Configuration Examples](#application-configuration-examples):
* [Code hot-swapping for JVM Lambdas](#code-hot-swapping-for-jvm-lambdas)
* [Code hot-swapping for Python Lambdas](#code-hot-swapping-for-python-lambdas)
* Debugging Nodejs lambdas (under development)

[Deployment Configuration Examples](#deployment-configuration-examples):
* [Serverless Framework Configuration](#serverless-framework-configuration)
* [AWS Cloud Development Kit (CDK) Configuration](#aws-cloud-development-kit-cdk-configuration)
* [Terraform Configuration](#terraform-configuration)

[Useful Links](#useful-links)

## Application Configuration Examples

### Code hot-swapping for JVM Lambdas

Since lambda containers lifetime is usually limited, regular hot code swapping
techniques are not applicable here.

In our implementation, we will be watching for fs changes under the project folder,
then build a `FatJar`, unzip it, and mount it into the Lambda Docker Container.

We assume you already have:
* [watchman](https://facebook.github.io/watchman/)
* configured JVM project capable of building FatJars using your preferred build tool

First, create a watchman wrapper by using
[one of our examples](https://github.com/localstack/localstack-pro-samples/tree/master/spring-cloud-function-microservice/bin/watchman.sh)

Don't forget to adjust permissions:
{{< command >}}
$ chmod +x bin/watchman.sh
{{< / command >}}

Now configure your build tool to unzip the FatJar to some folder, which will be
then mounted to LocalStack. We are using `Gradle` build tool to unpack the
`FatJar` into the `build/hot` folder:

```gradle
// We assume you are using something like `Shadow` plugin that comes with `shadowJar` task
task buildHot(type: Copy) {
    from zipTree("${project.buildDir}/libs/${project.name}-all.jar")
    into "${project.buildDir}/hot"
}
buildHot.dependsOn shadowJar
```

Now run the following command to start watching your project in a hot-swapping mode:

{{< command >}}
$ bin/watchman.sh src "./gradlew buildHot"
{{< / command >}}

Please note that you still need to configure your deployment tool to use
local code mounting. Read the "[Deployment Configuration Examples](#deployment-configuration-examples)"
for more information.

### Code hot-swapping for Python Lambdas

We will show you how you can do this with a simple example function, taken directly from the
[AWS Lambda developer guide](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/lambda/boto_client_examples/lambda_handler_basic.py).

You can check out that code, or use your own lambda functions to follow along. To use the example just do:

{{< command >}}
$ cd /tmp
$ git clone git@github.com:awsdocs/aws-doc-sdk-examples.git
{{< / command >}}

#### Starting up LocalStack

First, we need to make sure we start LocalStack with the right configuration.
This is as simple as setting `LAMBDA_REMOTE_DOCKER`(see the [Configuration Documentation]({{< ref "configuration#lambda" >}}) for more information):

{{< command >}}
$ LAMBDA_REMOTE_DOCKER=0 localstack start
{{< / command >}}

Accordingly, if you are launching LocalStack via Docker or Docker Compose:

```yaml
#docker-compose.yml

services:
  localstack:
    ...
    environment:
      ...
      - LAMBDA_REMOTE_DOCKER=false
```

#### Creating the Lambda Function

To create the Lambda function, you just need to take care of two things:
1. Deploy via an S3 Bucket. You need to use the magic variable `__local__` as the bucket.
2. Set the S3 key to the path of the directory your lambda function resides in.
   The handler is then referenced by the filename of your lambda code and the function in that code that needs to be invoked.

So, using the AWS example, this would be:

{{< command >}}
$ awslocal lambda create-function --function-name my-cool-local-function \
    --code S3Bucket="__local__",S3Key="/tmp/aws-doc-sdk-examples/python/example_code/lambda/boto_client_examples" \
    --handler lambda_handler_basic.lambda_handler \
    --runtime python3.8 \
    --role cool-stacklifter
{{< / command >}}

You can also check out some of our "[Deployment Configuration Examples](#deployment-configuration-examples)".

We can also quickly make sure that it works by invoking it with a simple payload:

{{< command >}}
$ awslocal lambda invoke --function-name my-cool-local-function --payload '{"action": "square", "number": 3}' output.txt
{{< / command >}}

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

#### Changing things up

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

#### Usage with Virtualenv

For Virtualenv-driven projects, all dependencies should be available under the same folder as the project itself.
The easiest way to achieve that is to implement a watchman script that will be preparing a special folder for hot code swapping.

In our example, we are using `build/hot` folder as a mounting point for our Lambdas.

First, create a watchman wrapper by using
[one of our examples](https://github.com/localstack/localstack-pro-samples/tree/master/spring-cloud-function-microservice/bin/watchman.sh)

After that, you can use the following `Makefile` snippet, or implement another shell script to prepare the codebase for hot swapping:

```make
VENV_DIR ?= .venv
VENV_RUN ?= . $(VENV_DIR)/bin/activate
BUILD_FOLDER ?= build
PROJECT_MODULE_NAME = my_project_module

build-hot:
	$(VENV_RUN);
  rm -rf $(BUILD_FOLDER)/hot && mkdir -p $(BUILD_FOLDER)/hot;
	cp -r $(VENV_DIR)/lib/python$(shell python --version | grep -oE '[0-9]\.[0-9]')/site-packages/* $(BUILD_FOLDER)/hot;
	cp -r $(PROJECT_MODULE_NAME) $(BUILD_FOLDER)/hot/$(PROJECT_MODULE_NAME);
	cp *.toml $(BUILD_FOLDER)/hot;

watch:
	bin/watchman.sh $(PROJECT_MODULE_NAME) "make build-hot"

.PHONY: build-hot watch
```

As you can see, all we do here is just copying the project module `PROJECT_MODULE_NAME`
along with all dependencies into the `build/hot` folder, which is then mounted to
LocalStack's Lambda container.

To run the example above run `make watch`

## Deployment Configuration Examples

### Serverless Framework Configuration

Enable local code mounting

```yaml
custom:
  localstack:
    ...
    lambda:
      mountCode: true

# or if you need to enable code mounting only for specific stages
custom:
  stages:
    local:
      mountCode: true
    testing:
      mountCode: false
  localstack:
    stages:
      - local
      - testing
    lambda:
      mountCode: ${self:custom.stages.${opt:stage}.mountCode}
```

Pass `LAMBDA_MOUNT_CWD` env var with path to the built code directory
(in our case to the folder with unzipped FatJar):

{{< command >}}
$ LAMBDA_MOUNT_CWD=$(pwd)/build/hot serverless deploy --stage local
{{< / command >}}

### AWS Cloud Development Kit (CDK) Configuration

{{< highlight kotlin "linenos=table" >}}
package org.localstack.cdkstack

import java.util.UUID
import software.amazon.awscdk.core.Construct
import software.amazon.awscdk.core.Duration
import software.amazon.awscdk.core.Stack
import software.amazon.awscdk.services.lambda.*
import software.amazon.awscdk.services.s3.Bucket

private val STAGE = System.getenv("STAGE") ?: "local"
private val LAMBDA_MOUNT_CWD = System.getenv("LAMBDA_MOUNT_CWD") ?: ""
private const val JAR_PATH = "build/libs/localstack-sampleproject-all.jar"

class ApplicationStack(parent: Construct, name: String) : Stack(parent, name) {

    init {
        val lambdaCodeSource = this.buildCodeSource()

        SingletonFunction.Builder.create(this, "ExampleFunctionOne")
            .code(lambdaCodeSource)
            .handler("org.localstack.sampleproject.api.LambdaApi")
            .environment(mapOf("FUNCTION_NAME" to "functionOne"))
            .timeout(Duration.seconds(30))
            .runtime(Runtime.JAVA_11)
            .uuid(UUID.randomUUID().toString())
            .build()
    }

    /**
     * Mount code for hot-reloading when STAGE=local
     */
    private fun buildCodeSource(): Code  {
        if (STAGE == "local") {
            val bucket = Bucket.fromBucketName(this, "HotReloadingBucket", "__local__")
            return Code.fromBucket(bucket, LAMBDA_MOUNT_CWD)
        }

        return Code.fromAsset(JAR_PATH)
    }
}
{{< / highlight >}}

Then to bootstrap and deploy the stack run the following shell script

{{< command >}}
$ STAGE=local && LAMBDA_MOUNT_CWD=$(pwd)/build/hot &&
  cdklocal bootstrap aws://000000000000/$(AWS_REGION) && \
  cdklocal deploy
{{< / command >}}

### Terraform Configuration

```hcl
ariable "STAGE" {
    type    = string
    default = "local"
}

variable "AWS_REGION" {
    type    = string
    default = "us-east-1"
}

variable "JAR_PATH" {
    type    = string
    default = "build/libs/localstack-sampleproject-all.jar"
}

variable "LAMBDA_MOUNT_CWD" {
    type    = string
}

provider "aws" {
    access_key                  = "test_access_key"
    secret_key                  = "test_secret_key"
    region                      = var.AWS_REGION
    s3_force_path_style         = true
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_requesting_account_id  = true

    endpoints {
        apigateway       = var.STAGE == "local" ? "http://localhost:4566" : null
        cloudformation   = var.STAGE == "local" ? "http://localhost:4566" : null
        cloudwatch       = var.STAGE == "local" ? "http://localhost:4566" : null
        cloudwatchevents = var.STAGE == "local" ? "http://localhost:4566" : null
        iam              = var.STAGE == "local" ? "http://localhost:4566" : null
        lambda           = var.STAGE == "local" ? "http://localhost:4566" : null
        s3               = var.STAGE == "local" ? "http://localhost:4566" : null
    }
}

resource "aws_iam_role" "lambda-execution-role" {
    name = "lambda-execution-role"

    assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "exampleFunctionOne" {
    s3_bucket     = var.STAGE == "local" ? "__local__" : null
    s3_key        = var.STAGE == "local" ? var.LAMBDA_MOUNT_CWD : null
    filename      = var.STAGE == "local" ? null : var.JAR_PATH
    function_name = "ExampleFunctionOne"
    role          = aws_iam_role.lambda-execution-role.arn
    handler       = "org.localstack.sampleproject.api.LambdaApi"
    runtime       = "java11"
    timeout       = 30
    source_code_hash = filebase64sha256(var.JAR_PATH)
    environment {
        variables = {
            FUNCTION_NAME = "functionOne"
        }
    }
}
```

{{< command >}}
$ terraform init && \
  terraform apply -var "STAGE=local" -var "LAMBDA_MOUNT_CWD=$(pwd)/build/hot"
{{< / command >}}

## Useful Links

* [Lambda Code Mounting and Debugging (Python)](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-mounting-and-debugging)
* [Spring Cloud Function on LocalStack (Kotlin JVM)](https://github.com/localstack/localstack-pro-samples/tree/master/spring-cloud-function-microservice)
