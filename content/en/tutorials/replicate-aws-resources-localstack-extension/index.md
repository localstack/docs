---
title: "Replicating AWS resources locally with LocalStack Replicator extension"
linkTitle: "Replicating AWS resources locally with LocalStack Replicator extension"
weight: 7
description: >
  Learn how you can replicate AWS resources in your local environment using the LocalStack Replicator extension. This tutorial provides step-by-step guidance on setting up and leveraging the Replicator extension to mirror cloud services locally, enabling efficient hybrid development and testing workflows without maintaining additional configurations.
type: tutorials
teaser: ""
services:
- sqs
- lambda
platform:
- Python
deployment:
- AWS CLI
tags:
- replicator-extension
- localstack-extensions
pro: true
leadimage: ""
---

## Introduction

LocalStack's core cloud emulator enables you to emulate various cloud services on your own local machine. This allows you to work on and test your cloud-based solutions without needing to connect to a remote cloud. However, sometimes you might need to smoothly switch between your local setup and actual cloud resources, especially in hybrid scenarios. This could be useful, for instance, if you want to share a database that your local Lambda function interacts with, or if you need to access S3 files stored remotely while running a Glue ETL job locally.

The LocalStack Replicator extension lets you replicate your cloud resources from AWS to your local machine, on the API level. This means your local setup can interact with real cloud resources. With the Replicator extension, you can make certain requests in LocalStack that will be forwarded to AWS without having to set up a complex proxy system using AWS SSM or similar tools.

In this tutorial, you'll go through an example where you'll trigger a local Lambda function with a message sent to a remote SQS queue. You'll also learn how to install the Replicator extension and use its different modes to seamlessly work in a hybrid environment.

## Prerequisites

-   [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli)  with  [`LOCALSTACK_AUTH_TOKEN`](https://docs.localstack.cloud/getting-started/auth-token/)
-   [Docker](https://docs.localstack.cloud/getting-started/auth-token/)
-   [AWS](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)  CLI with  [`awslocal`  wrapper](https://github.com/localstack/awscli-local)
-   [LocalStack Web Application account](https://app.localstack.cloud/sign-up) 
-   [AWS Account](https://aws.amazon.com/) with an [`AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)

## Install the Replicator extension

To install the Replicator Extension, follow these steps:

1.  Launch your LocalStack container using the `localstack` CLI, ensuring that `LOCALSTACK_AUTH_TOKEN` is available in the environment.
3.  Visit the [Extensions library](https://app.localstack.cloud/extensions/library) page on the LocalStack Web Application.
4.  Scroll down to find the **AWS replicator** card, then click on the **Install on Instance** button.

Once the installation is complete, you'll notice that your LocalStack container has restarted with the Replicator extension successfully installed. To confirm the installation, execute the following command:

```bash 
$ localstack extensions list
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Name                         ┃ Summary                      ┃ Version ┃ Author          ┃ Plugin name    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ localstack-extension-aws-re… │ LocalStack Extension: AWS    │ 0.1.11  │ LocalStack Team │ aws-replicator │
│                              │ replicator                   │         │                 │                │
└──────────────────────────────┴──────────────────────────────┴─────────┴─────────────────┴────────────────┘
```

After verifying the successful installation, you can shut down the LocalStack container to re-start it with additional configuration variables.

## Create the Lambda function

In this tutorial, you'll set up a basic example consisting of:

-   A Lambda function named `func1` that prints a simple statement when invoked.
-   An SQS queue named `test-local-proxy` where messages are sent.
-   An event source mapping that triggers the Lambda function when a message is sent to the SQS queue.

In this scenario, you'll create the SQS queue on your local machine and the remote cloud to showcase how you can switch between the two with the Replicator extension. 

Begin by running your LocalStack container with the following configuration:

```bash 
EXTRA_CORS_ALLOWED_ORIGINS=https://aws-replicator.localhost.localstack.cloud:4566 \
DEBUG=1 \
localstack start
```

In the above command:

-   The `EXTRA_CORS_ALLOWED_ORIGINS` variable allows the Replicator extension's user interface to connect with the LocalStack container.
-   The `DEBUG` variable enables verbose logging allowing you to see the printed statements from the Lambda function.

Next, create a file named `testlambda.py` and add the following Python code to it:

```python 
def handler(*args, **kwargs):
  print("Debug output from Lambda function")
```

Execute the following commands to create the local Lambda function:

```bash 
$ (zip testlambda.zip testlambda.py)
$ awslocal lambda create-function \
    --function-name func1 \
    --runtime python3.8 \
    --role arn:aws:iam::000000000000:role/r1 --handler testlambda.handler \
    --timeout 30 \
    --zip-file fileb://./testlambda.zip
```

Once the Lambda function is successfully created, you'll see output similar to this:

```bash 
{
    "FunctionName": "func1",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:func1",
    "Runtime": "python3.8",
    "Role": "arn:aws:iam::000000000000:role/r1",
    "Handler": "testlambda.handler",
    "CodeSize": 250,
    ...
}
```

## Create the SQS queue

You can create the local SQS queue named `test-local-proxy` by executing the following command:

```bash 
$ awslocal sqs create-queue --queue-name test-local-proxy
```

The output will display the Queue URL:

```bash 
{
    "QueueUrl": "http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/test-local-proxy"
}
```

Additionally, you can create the remote SQS queue on the real AWS cloud to test invocation after starting the Replicator extension. 

Use the following command to set up the SQS queue on AWS:

```bash 
$ aws sqs create-queue --queue-name test-local-proxy
```

## Invoke the Lambda function 

Before invoking, set up an event source mapping between the SQS queue and the Lambda function. Configure the queue for Lambda using the following command:

```bash 
$ awslocal lambda create-event-source-mapping \
    --function-name func1 \
    --batch-size 1 \
    --event-source-arn arn:aws:sqs:us-east-1:000000000000:test-local-proxy
```

The following output would be retrieved:

```bash 
{
    ...
    "MaximumBatchingWindowInSeconds": 0,
    "EventSourceArn": "arn:aws:sqs:us-east-1:000000000000:test-local-proxy",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:func1",
    ..
    "FunctionResponseTypes": []
}
```

You can then send a message to the SQS queue to trigger the local Lambda function:

```bash 
awslocal sqs send-message \
    --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/test-local-proxy \
    --message-body '{}'
```

Upon successful execution, you'll receive a message ID and MD5 hash of the message body.

```bash 
{
    "MD5OfMessageBody": "99914b932bd37a50b983c5e7c90ae93b",
    "MessageId": "64e8297c-f0b2-4b68-a482-6cd3317f5096"
}
```

In the LocalStack logs, you'll see confirmation of the Lambda function invocation along with any debug messages.

```bash 

2024-03-26T07:23:47.842 DEBUG --- [5119b27cdf1e] l.s.l.i.version_manager    : [func1-381c6f7c-3ad8-4c79-aad8-5119b27cdf1e] START RequestId: 381c6f7c-3ad8-4c79-aad8-5119b27cdf1e Version: $LATEST
2024-03-26T07:23:47.842 DEBUG --- [5119b27cdf1e] l.s.l.i.version_manager    : [func1-381c6f7c-3ad8-4c79-aad8-5119b27cdf1e] Debug output from Lambda function
2024-03-26T07:23:47.842 DEBUG --- [5119b27cdf1e] l.s.l.i.version_manager    : [func1-381c6f7c-3ad8-4c79-aad8-5119b27cdf1e] END RequestId: 381c6f7c-3ad8-4c79-aad8-5119b27cdf1e
```

## Run the Replicator extension

To run the Replicator extension:


-   Access [`https://aws-replicator.localhost.localstack.cloud:4566`](https://aws-replicator.localhost.localstack.cloud:4566/) via your web browser.
-   Provide your AWS Credentials: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and optionally `AWS_SESSION_TOKEN`.
- Add a new YAML-based Proxy configuration to proxy requests for specific resources to AWS. For this scenario, configure it to proxy requests for the SQS queue created earlier.
  ```yaml 
  services:
    sqs:
      resources:
        - '.*:test-local-proxy'
   ```
- Save the configuration to enable the Replicator extension. Once enabled, you'll see the proxy status as **Enabled**.

To invoke the local Lambda function with the remote SQS queue:

-   Navigate to your AWS Management Console and access **Simple Queue Service**.
-   Select the **test-local-proxy** queue.
-   Send a message with a body (e.g., `Hello LocalStack`) by clicking **Send Message**.

You will observe the local Lambda function being invoked once again, with corresponding debug messages visible in the logs.

```bash 
2024-03-26T07:45:16.524 DEBUG --- [db58fad602e5] l.s.l.i.version_manager    : [func1-ed938bb0-e1ee-41fb-a844-db58fad602e5] START RequestId: ed938bb0-e1ee-41fb-a844-db58fad602e5 Version: $LATEST
2024-03-26T07:45:16.524 DEBUG --- [db58fad602e5] l.s.l.i.version_manager    : [func1-ed938bb0-e1ee-41fb-a844-db58fad602e5] Debug output from Lambda function
2024-03-26T07:45:16.524 DEBUG --- [db58fad602e5] l.s.l.i.version_manager    : [func1-ed938bb0-e1ee-41fb-a844-db58fad602e5] END RequestId: ed938bb0-e1ee-41fb-a844-db58fad602e5
```

You can even run the standard `awslocal` commands in your terminal that would query the remote cloud resources, instead of the local ones.

Upon completion, you can click **Disable** on the Replicator extension web interface to deactivate the proxy configuration.
Additionally, you can delete the remote SQS queue to avoid AWS billing for long-running resources.
To remove local resources, stop the LocalStack container to clear the local Lambda function and SQS queue.

## Conclusion 

In this tutorial, you've discovered how the Replicator extension bridges the gap between local and remote cloud resources by mirroring resources from real AWS accounts into your LocalStack instance. You can explore additional use-cases with the Replicator extension, such as:

-   Developing a local Lambda function that interacts with a remote DynamoDB table
-   Executing a local Athena SQL query in LocalStack, accessing files in a real S3 bucket on AWS
-   Testing a local Terraform script with SSM parameters from a real AWS account
-   And many more!
