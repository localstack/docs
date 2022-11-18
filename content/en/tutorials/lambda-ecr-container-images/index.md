---
title: "Deploying Lambda container image locally with Elastic Container Registry (ECR) using LocalStack"
linkTitle: "Deploying Lambda container image locally with Elastic Container Registry (ECR) using LocalStack"
weight: 2
description: >
  You can create & deploy your Lambda functions using Lambda container image by packaging your code and dependencies in a Docker image! Learn how you can create a Lambda container image using a local Elastic Container Registry (ECR) in LocalStack.
cascade:
  type: docs
---

AWS Lambda is a serverless compute system that allows you to break down your application into many independent functions and deploy them as singular units that can run on the AWS ecosystem. Lambda is tightly integrated with other AWS services and allows you to write your serverless functions in different programming languages suited for various supported runtimes. You can deploy Lambda functions programmatically by uploading a ZIP file containing your code and dependencies or packaging your code in a container image and deploying it via Elastic Container Registry (ECR).

ECR allows users to push their software packaged inside containers into an AWS-managed registry. Using ECR, you can version, tag, and manage your image lifecycles independently of your application. ECR is tightly integrated with other AWS services, such as ECS, EKS, and Lambda, and allows you to deploy your container image to these services. You can create container images using Docker and your Lambda functions by implementing the Lambda Runtime API and following the Open Container Initiative (OCI) specifications.

[LocalStack Pro](https://localstack.cloud) supports the creation of Lambda functions using container images via ECR and allows you to deploy your Lambda functions locally using LocalStack. In this tutorial, we will learn how to create a Lambda function using a container image and deploy it locally using LocalStack.

## Prerequisites

For this tutorial you will need:

- [LocalStack Pro](https://localstack.cloud/pricing/) to emulate Amazon ECS and AWS Lambda locally
  - Don't worry, if you don't have a subscription yet, you can just get a trial license for free.
- [awslocal](https://docs.localstack.cloud/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [Docker](https://docker.io/)

## Creating a Lambda function

To package & deploy a Lambda as a container image, we'll first create a Lambda function containing our code and a Dockerfile. Create a new directory and initialize it with two files: `handler.py`, to save our Python-based Lambda function, and `Dockerfile`, to package our code and dependencies into a container image.

{{< command >}}
$ mkdir -p lambda-container-image
$ cd lambda-container-image
$ touch handler.py Dockerfile
{{< / command >}}

Let us use the following Python code to create a Lambda function that returns a simple `'Hello from LocalStack Lambda container image!'` message.

```python
def handler(event, context):
    print('Hello from LocalStack Lambda container image!')
```

In the above example, the `handler` function is executed by the Lambda service every time a trigger event occurs. The above function serves as an entrypoint for the Lambda function inside a runtime environment and accepts `event` and `context`, to receive information about the event and the invocation properties.

## Building the image

To package our Lambda function as a container image, we need to create a `Dockerfile` that contains the instructions to build our image. The image should be able to execute a read-only file system with access to a `/tmp` directory. We would be using [AWS base images for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html#runtimes-images-lp) to preload the runtimes and dependencies that are required to create Lambda images.

To build the container image for Python, we would use a `python:3.8 base image`. Open the `Dockerfile` and specify the function handler to ensure that the Lambda runtime can locate it where the Lambda handler is available:

```Dockerfile
FROM public.ecr.aws/lambda/python:3.8

COPY ./handler.py ./

CMD [ "handler.handler" ]
```

{{< alert title="Note" color="primary">}}
If you have additional dependencies specificed, create a file named `requirements.txt` and list the libraries in the file. Install the dependencies in the Dockerfile under the `${LAMBDA_TASK_ROOT}` directory.
{{< /alert >}}

Use Docker to build an image using this function code:

{{< command >}}
$ docker build -t localstack-lambda-container-image .
{{< / command >}}

## Publishing the image to ECR

Now that the initial setup is done, we can give LocalStack's AWS emulation a try to push our image to ECR and deploy the Lambda container image. Let's start LocalStack:

{{< command >}}
$ LOCALSTACK_API_KEY=<your-api-key> localstack start -d
{{< / command >}}

Once LocalStack is started, we can create a new ECR repository to store our container image. We will use the `awslocal` CLI to create a new ECR repository using the `create-repository` command. We will pass the repository name using the `repository-name` flag.

{{< command >}}
$ awslocal ecr create-repository --repository-name localstack-lambda-container-image
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:000000000000:repository/localstack-lambda-container-image",
        "registryId": "000000000000",
        "repositoryName": "localstack-lambda-container-image",
        "repositoryUri": "localhost:4510/localstack-lambda-container-image",
        "createdAt": "<timestamp>",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
{{< / command >}}

{{< alert title="Note" color="primary">}}
To further customize the repository, you can pass additional flags to the `create-repository` command. For more information, refer to the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html).
{{< /alert >}}

Let us now build the image and push it to the ECR repository:

{{< command >}}
$ docker build -t localhost:4510/localstack-lambda-container-image .
$ docker push localhost:4510/localstack-lambda-container-image
{{< / command >}}

In the above commands, we have specified the `repositoryUri` as the image name to push the image to the ECR repository. We can now verify that the image is pushed to the repository by using the `describe-images` command:

{{< command >}}
$ awslocal ecr describe-images --repository-name localstack-lambda-container-image
{
    "imageDetails": [
        {
            "registryId": "000000000000",
            "repositoryName": "localstack-lambda-container-image",
            "imageDigest": "sha256:<digest>",
            "imageTags": [
                "latest"
            ],
            "imageSizeInBytes": 181885144,
            "imagePushedAt": "<timestamp>",
            "imageManifestMediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "artifactMediaType": "application/vnd.docker.container.image.v1+json"
        }
    ]
}
{{< / command >}}

Now that we have pushed the image to the ECR repository, we can deploy the Lambda function using the container image.

## Deploying the Lambda function

To deploy the container image as a Lambda function, we need to create a new Lambda function using the `create-function` command. We will pass the `ImageUri` flag to specify the image URI of the container image that we have pushed to the ECR repository.

{{< command >}}
$ awslocal lambda create-function \
    --function-name localstack-lambda-container-image \
    --package-type Image \
    --code ImageUri="localstack-lambda-container-image" \
    --role arn:aws:iam::000000000:role/lambda-r1 \
    --handler handler.handler
{
    "FunctionName": "localstack-lambda-container-image",
    "FunctionArn": "arn:aws:lambda:<REGION>:000000000000:function:localstack-lambda-container-image",
    "Role": "arn:aws:iam::000000000:role/lambda-r1",
    "Handler": "handler.handler",
    "Description": "",
    "Timeout": 3,
    "LastModified": "<TIMESTAMP>",
    "Version": "$LATEST",
    "VpcConfig": {},
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "<REVISION_ID>",
    "Layers": [],
    "State": "Active",
    "LastUpdateStatus": "Successful",
    "PackageType": "Image",
    "Architectures": [
        "x86_64"
    ]
}
{{< / command >}}

The above command has taken various flags to create the Lambda function. We have specified the `ImageUri` flag to specify the image URI of the container image that we have pushed to the ECR repository. We have also specified the `package-type` flag to specify the package type as `Image`. For the role, we have specified a mock role ARN. To create an actual role, refer to the [IAM documentation]({{< ref "iam" >}}).

Let us know invoke the Lambda function using the `invoke` command:

{{< command >}}
$ awslocal lambda invoke --function-name localstack-lambda-container-image /tmp/lambda.out
{
    "StatusCode": 200,
    "LogResult": "",
    "ExecutedVersion": "$LATEST"
}
{{< / command >}}

The logs of the Lambda invocation should be visible in the LocalStack container output (with `DEBUG=1` enabled):

{{< command >}}
Starting XRay server loop on UDP port 2000
Starting DNS server loop on UDP port 53
-----
Hello from LocalStack Lambda container image!
{{< / command >}}

## Conclusion

With the Lambda container image support, you can use Docker to package your custom code and dependencies for Lambda functions. LocalStack allows you to package, deploy, and invoke Lambda functions locally. Using LocalStack, you can develop, debug, and test your Lambda functions in conjunction with a wide range of AWS services. Check out [Lambda Hot Swapping]({{< ref "hot-swapping" >}}) and [Lambda Hot Reloading]({{< ref "debugging" >}}) for advanced usage patterns.

The code for this tutorial (including a `Makefile` to execute it step-by-step) can be found in our [LocalStack Pro samples over GitHub](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-container-image).
