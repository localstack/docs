---
title: "Deploying Lambda container image locally with Elastic Container Registry (ECR) using LocalStack"
linkTitle: "Deploying Lambda container image locally with Elastic Container Registry (ECR) using LocalStack"
weight: 2
description: >
  Learn how to create and deploy Lambda functions using container images in LocalStack. This tutorial guides you through packaging your code and dependencies into a Docker image, creating a local Elastic Container Registry (ECR) in LocalStack, and deploying the Lambda container image.
type: tutorials
teaser: ""
services:
- ecr
- lmb
platform:
- python
deployment:
- awscli
tags:
- Lambda
- ECR
- Docker
- Container
- Container Image
pro: true
leadimage: "lambda-ecr-container-images-featured-image.png"
---

[Lambda](https://aws.amazon.com/lambda/) is a powerful serverless compute system that enables you to break down your application into smaller, independent functions. These functions can be deployed as individual units within the AWS ecosystem. Lambda offers seamless integration with various AWS services and supports multiple programming languages for different runtime environments. To deploy Lambda functions programmatically, you have two options: [uploading a ZIP file containing your code and dependencies](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-zip.html) or [packaging your code in a container image](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-images.html) and deploying it through Elastic Container Registry (ECR).

[ECR](https://aws.amazon.com/ecr/) is an AWS-managed registry that facilitates the storage and distribution of containerized software. With ECR, you can effectively manage your image lifecycles, versioning, and tagging, separate from your application. It seamlessly integrates with other AWS services like ECS, EKS, and Lambda, enabling you to deploy your container images effortlessly. Creating container images for your Lambda functions involves using Docker and implementing the Lambda Runtime API according to the Open Container Initiative (OCI) specifications.

[LocalStack Pro](https://localstack.cloud) extends support for Lambda functions using container images through ECR. It enables you to deploy your Lambda functions locally using LocalStack. In this tutorial, we will explore creating a Lambda function using a container image and deploying it locally with the help of LocalStack.

## Prerequisites

Before diving into this tutorial, make sure you have the following prerequisites:

- LocalStack Pro
- [awslocal]({{< ref "aws-cli#localstack-aws-cli-awslocal" >}})
- [`awslocal` CLI](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [Python](https://www.python.org/downloads/)
- [Docker](https://docker.io/)

## Creating a Lambda function

To package and deploy a Lambda function as a container image, we'll create a Lambda function containing our code and a Dockerfile. Create a new directory for your lambda function and navigate to it:

{{< command >}}
$ mkdir -p lambda-container-image
$ cd lambda-container-image
{{< / command >}}

Initialize the directory by creating two files: `handler.py` and `Dockerfile`. Use the following commands to create the files:

{{< command >}}
$ touch handler.py Dockerfile
{{< / command >}}

Open the `handler.py` file and add the following Python code, which represents a simple Lambda function that returns the message `'Hello from LocalStack Lambda container image!'`:

```python
def handler(event, context):
    print('Hello from LocalStack Lambda container image!')
```

In the code above, the `handler` function is executed by the Lambda service whenever a trigger event occurs. It serves as the entry point for the Lambda function within the runtime environment and accepts `event` and `context` as parameters, providing information about the event and invocation properties, respectively.

Following these steps, you have created the foundation for your Lambda function and defined its behaviour using Python code. In the following sections, we will package this code and its dependencies into a container image using the `Dockerfile`.

## Building the image

To package our Lambda function as a container image, we must create a Dockerfile containing the necessary instructions for building the image. Open the Dockerfile and add the following content. This Dockerfile uses the `python:3.8` base image provided by AWS for Lambda and copies the `handler.py` file into the image. It also specifies the function handler as `handler.handler` to ensure the Lambda runtime can locate it where the Lambda handler is available.

```Dockerfile
FROM public.ecr.aws/lambda/python:3.8

COPY ./handler.py ./

CMD [ "handler.handler" ]
```

{{< callout "note">}}
If your Lambda function has additional dependencies, create a file named `requirements.txt` in the same directory as the Dockerfile. List the required libraries in this file. You can install these dependencies in the `Dockerfile` under the `${LAMBDA_TASK_ROOT}` directory.
{{< /callout >}}

With the Dockerfile prepared, you can now build the container image using the following command, to check if everything works as intended:

{{< command >}}
$ docker build .
{{< / command >}}

By executing these steps, you have defined the Dockerfile that instructs Docker on how to build the container image for your Lambda function. The resulting image will contain your function code and any specified dependencies.

## Publishing the image to ECR

Now that the initial setup is complete let's explore how to leverage LocalStack's AWS emulation by pushing our image to ECR and deploying the Lambda container image. Start LocalStack by executing the following command. Make sure to replace `<your-auth-token>` with your actual auth token:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<your-auth-token> DEBUG=1 localstack start -d
{{< / command >}}

Once the LocalStack container is running, we can create a new ECR repository to store our container image. Use the `awslocal` CLI to achieve this. Run the following command to create the repository, replacing `localstack-lambda-container-image` with the desired name for your repository:

{{< command >}}
$ awslocal ecr create-repository --repository-name localstack-lambda-container-image
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:000000000000:repository/localstack-lambda-container-image",
        "registryId": "000000000000",
        "repositoryName": "localstack-lambda-container-image",
        "repositoryUri": "localhost.localstack.cloud:4510/localstack-lambda-container-image",
        "createdAt": <timestamp>,
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

{{< callout "note">}}
To further customize the ECR repository, you can pass additional flags to the `create-repository` command. For more details on the available options, refer to the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/ecr/create-repository.html).
{{< /callout >}}

Next, build the image and push it to the ECR repository. Execute the following commands:

{{< command >}}
$ docker build -t localhost:4510/localstack-lambda-container-image .
$ docker push localhost:4510/localstack-lambda-container-image
{{< / command >}}

In the above commands, we specify the `repositoryUri` as the image name to push the image to the ECR repository. After executing these commands, you can verify that the image is successfully pushed to the repository by using the `describe-images` command:

{{< command >}}
$ awslocal ecr describe-images --repository-name localstack-lambda-container-image
{
    "imageDetails": [
        {
            "registryId": "000000000000",
            "repositoryName": "localstack-lambda-container-image",
            "imageDigest": "sha256:459fce12258ff1048925e0f4e7fb039d8b54111a8e3cca5db4acb434a9e8af37",
            "imageTags": [
                "latest"
            ],
            "imageSizeInBytes": 184217147,
            "imagePushedAt": <timestamp>,
            "imageManifestMediaType": "application/vnd.docker.distribution.manifest.v2+json",
            "artifactMediaType": "application/vnd.docker.container.image.v1+json"
        }
    ]
}
{{< / command >}}

By running this command, you can confirm that the image is now in the ECR repository. It ensures it is ready for deployment as a Lambda function using LocalStack's AWS emulation capabilities.

## Deploying the Lambda function

To deploy the container image as a Lambda function, we will create a new Lambda function using the `create-function` command. Run the following command to create the function:

{{< callout "note">}}
Before creating the lambda function, please double check under which architecture you have built your image. If your image is built as arm64, you need to specify the lambda architecture when deploying or set `LAMBDA_IGNORE_ARCHTIECTURE=1` when starting LocalStack.
More information can be found [in our documentation regarding ARM support.]({{< ref "arm64-support" >}})
{{< /callout >}}

{{< command >}}
$ awslocal lambda create-function \
    --function-name localstack-lambda-container-image \
    --package-type Image \
    --code ImageUri="localhost.localstack.cloud:4510/localstack-lambda-container-image" \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --handler handler.handler
{
    "FunctionName": "localstack-lambda-container-image",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:localstack-lambda-container-image",
    "Role": "arn:aws:iam::000000000000:role/lambda-role",
    "Handler": "handler.handler",
    "CodeSize": 0,
    "Description": "",
    "Timeout": 3,
    "MemorySize": 128,
    "LastModified": <timestamp>,
    "CodeSha256": "9be73524cd5aa70fbcee3fc8d7aac4eb7e2a644e9ef2b13031719077a65c0031",
    "Version": "$LATEST",
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "cab4268c-2d56-4591-821a-9154e157b984",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    "PackageType": "Image",
    "Architectures": [
        "x86_64"
    ],
    "EphemeralStorage": {
        "Size": 512
    },
    "SnapStart": {
        "ApplyOn": "None",
        "OptimizationStatus": "Off"
    }
}
{{< / command >}}

The command provided includes several flags to create the Lambda function. Here's an explanation of each flag:

- `ImageUri`: Specifies the image URI of the container image you pushed to the ECR repository (`localhost.localstack.cloud:4510/localstack-lambda-container-image` in this case. Use the return `repositoryUri` from the create-repository command).
- `package-type`: Sets the package type to Image to indicate that the Lambda function will be created using a container image.
- `function-name`: Specifies the name of the Lambda function you want to create.
- `runtime`: Defines the runtime environment for the Lambda function. In this case, it's specified as provided, indicating that the container image will provide the runtime.
- `role`: Sets the IAM role ARN that the Lambda function should assume. In the example, a mock role ARN is used. For an actual role, please refer to the [IAM documentation]({{< ref "user-guide/aws/iam" >}}).

To invoke the Lambda function, you can use the `invoke` command:

{{< command >}}
$ awslocal lambda invoke --function-name localstack-lambda-container-image /tmp/lambda.out
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
{{< / command >}}

The command above will execute the Lambda function locally within the LocalStack environment. The response will include the StatusCode and ExecutedVersion. You can find the logs of the Lambda invocation in the Lambda container output:

{{< command >}}
Hello from LocalStack Lambda container image!
{{< / command >}}

## Conclusion

In conclusion, the Lambda container image support enables you to use Docker to package your custom code and dependencies for Lambda functions. With the help of LocalStack, you can seamlessly package, deploy, and invoke Lambda functions locally. It empowers you to develop, debug, and test your Lambda functions with a wide range of AWS services. For more advanced usage patterns, you can explore features like [Lambda Hot Reloading]({{< ref "hot-reloading" >}}) and [Lambda Debugging]({{< ref "debugging" >}}).

To further explore and experiment with the concepts covered in this tutorial, you can access the code and accompanying `Makefile` on our [LocalStack Pro samples over GitHub](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-container-image).
