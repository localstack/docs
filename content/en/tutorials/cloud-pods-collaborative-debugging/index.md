---
title: "How To: Collaborative AWS local development with LocalStack’s Cloud Pods"
linkTitle: "How To: Collaborative AWS local development with LocalStack’s Cloud Pods"
weight: 7
description: >
  Replicating development environments ensures that all developers, regardless of their local machine configurations or operating systems, work within an environment that closely mirrors production. This consistency helps identify and solve environment-specific issues early in the development cycle, reducing the "it works on my machine" problem where code behaves differently on different developers' machines.
type: tutorials
teaser: ""
services:
- iam
- ddb
- agw
- lmb
platform:
- Java
deployment:
- Terraform
tags:
- BASH
- Cloud Pods
- Terraform
- API Gateway
- Lambda
- DynamoDb
- IAM
- CloudWatch
pro: true
leadimage: "collab-debugging-cloud-pod.png"
---

# **Introduction**


By replicating environments, teams can share the exact conditions under which a bug occurs.

For developing AWS applications locally, the tool of choice is obviously LocalStack, which can sustain a full-blown comprehensive stack.
However, when turbulent situations occur, and engineers need a second opinion from a colleague, recreating the environment from scratch can leave
details slipping through the cracks. This is where Cloud Pods come in, to encapsulate the state of the LocalStack instance and allow for seamless
collaboration. While databases have snapshots, LocalStack uses Cloud Pods for reproducing state and data.

In this tutorial, we’ll examine a realistic scenario in which a simple IAM misconfiguration can lead to spending too much time looking for the
right answer. We’ll also have a look at what’s the best solution to avoid that, and what are some of the options for Cloud Pod storage configuration.
The full sample application can be found [on GitHub](https://github.com/localstack-samples/cloud-pods-collaboration-demo) to clone, for quickly following along.

### **Prerequisites**

- [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) (preferably using `pip`)
- [Docker](https://docs.docker.com/engine/install/)
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) or [OpenTofu](https://opentofu.org/docs/intro/install/) and [terraform-local](https://docs.localstack.cloud/user-guide/integrations/terraform/#install-the-tflocal-wrapper-script)
- Optional for Lambda build & editing: [Maven 3.9.4](https://maven.apache.org/install.html) & [Java 21](https://www.java.com/en/download/help/download_options.html)

### Nice to have

- Basic knowledge of AWS services (API Gateway, Lambda, DynamoDB, IAM)
- Basic understanding of Terraform for provisioning AWS resources

So let’s say a new colleague joins, clones the application repository, and starts working on the Lambda code. They will add the necessary 
resources in the Terraform configuration file and some IAM policies that the functions need to be allowed to access the database (after all,
they’re following good practices), but something doesn't work out as expected.

# Reproducing the issue locally

## 1. Architecture Overview

The stack consists of an API Gateway that exposes some endpoints and integrates with two Lambda functions responsible for adding and fetching
products from a DynamoDB database. IAM policies are enforced to ensure compliance with the
**[principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**, and the logs will be sent to the CloudWatch service.

### Note

This demo application is suitable for AWS and behaves the same as on LocalStack. You can try this out by running the Terraform configuration file against the real AWS.

![Application Diagram](cloud-pod-collab.png)

## 2. Starting LocalStack

In the root directory, there is a `docker-compose.yml` file that will spin up version 3.2.0 of LocalStack, with an 
important configuration flag, `ENFORCE_IAM=1`, which will facilitate IAM policy evaluation and enforcement. For this 
example, a `LOCALSTACK_AUTH_TOKEN` is needed, which you can find in the LocalStack web app on the 
[Getting Started](https://app.localstack.cloud/getting-started) page.

{{< command >}}
$ export LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ docker compose up
{{</ command >}}

## 3. The Terraform Configuration File

The entire Terraform configuration file for setting up the application stack is available in the same repository at
https://github.com/localstack-samples/cloud-pods-collaboration-demo/blob/main/terraform/main.tf. To deploy all the resources on LocalStack, 
navigate to the project's root folder and use the following commands:

{{< command >}}
$ cd terraform
$ tflocal init
$ tflocal plan
$ tflocal apply --auto-approve
{{</ command >}}

`tflocal` is a small wrapper script to run Terraform against LocalStack. The endpoints for all services are configured to point to the
LocalStack API, which allows you to deploy your unmodified Terraform scripts against LocalStack.

- **`init`**: This command initializes the Terraform working directory, installs any necessary plugins, and sets up the backend.
- **`plan`**: Creates an execution plan, which allows you to review the actions Terraform will take to change your infrastructure.
- **`apply`**: Finally, the **`apply`** command applies the changes required to reach the desired state of the configuration. 
If **`-auto-approve`** is used, it bypasses the interactive approval step normally required.

As mentioned previously, there is something missing from this configuration, and that is the **`GetItem`** operation permission 
for one of the Lambda functions:

```java
resource "aws_iam_policy" "lambda_dynamodb_policy" {
  name        = "LambdaDynamoDBAccess"
  description = "IAM policy for accessing DynamoDB from Lambda"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "dynamodb:Scan",
          "dynamodb:Query",
          "dynamodb:UpdateItem",
          "dynamodb:PutItem",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```

The new teammate working on this has mistakenly used `dynamodb:Scan` and `dynamodb:Query` as a replacement.

## **4. Reproducing the issue locally**

Let’s test out the current state of the application. The Terraform configuration file outputs the REST API ID of the API Gateway.
We can capture that value and use it further to invoke the **`add-product`** Lambda:

{{< command >}}
$ export rest_api_id=$(cd terraform; tflocal output --raw rest_api_id)
{{</ command >}}

The endpoint for the API Gateway is constructed similarly to the one on AWS:

**`
https://<apiId>.execute-api.localhost.localstack.cloud:4566/<stageId>/<path>
`**

So adding two products to the database should be straightforward using `curl`:

```bash
$ curl --location "http://$rest_api_id.execute-api.localhost.localstack.cloud:4566/dev/productApi" \
--header 'Content-Type: application/json' \
--data '{
  "id": "34534",
  "name": "EcoFriendly Water Bottle",
  "description": "A durable, eco-friendly water bottle designed to keep your drinks cold for up to 24 hours and hot for up to 12 hours. Made from high-quality, food-grade stainless steel, it'\''s perfect for your daily hydration needs.",
  "price": "29.99"
}'

$ curl --location "http://$rest_api_id.execute-api.localhost.localstack.cloud:4566/dev/productApi?id=82736" \
--header 'Content-Type: application/json' \
--data '{
  "id": "82736",
  "name": "Sustainable Hydration Flask",
  "description": "This sustainable hydration flask is engineered to maintain your beverages at the ideal temperature—cold for 24 hours and hot for 12 hours. Constructed with premium, food-grade stainless steel, it offers an environmentally friendly solution to stay hydrated throughout the day.",
  "price": "31.50"
}'
```

The response is the one that we expect: `Product added/updated successfully.`

However, retrieving one of the products does not return the desired result:

{{< command >}}
$ curl --location "http://$rest_api_id.execute-api.localhost.localstack.cloud:4566/dev/productApi?id=34534"
{{</ command >}}

```bash
Internal server error⏎  
```

An `Internal server error⏎`  does not give out too much information. The new colleague doesn’t know for sure what could be 
causing this. The Lambda code looks fine, the configurations also look ok.

# **Using Cloud Pods for fast collaborative debugging**

## 1. Creating a Cloud Pod

To share this exact environment and issue with a teammate, the new colleague only needs to run a simple `localstack pod` command:

{{< command >}}
$ localstack pod save cloud-pod-product-app
{{</ command >}}

```bash
Cloud Pod `cloud-pod-product-app` successfully created ✅
Version: 1
Remote: platform
Services: sts,iam,apigateway,dynamodb,lambda,s3,cloudwatch,logs
```

LocalStack provides a remote storage backend that can be used to store the state of your application and share it with your team members.

The Cloud Pods CLI is included in the LocalStack CLI installation, so there’s no need for additional plugins to begin using it. 
The `LOCALSTACK_AUTH_TOKEN` needs to be set as an environment variable.

Additionally, there are other commands for managing Cloud Pods included in the CLI:

```bash
$ localstack pod --help
Usage: localstack pod [OPTIONS] COMMAND [ARGS]...

  Manage the state of your instance via Cloud Pods.

Options:
  -h, --help  Show this message and exit.

Commands:
  delete    Delete a Cloud Pod
  list      List all available Cloud Pods
  load      Load the state of a Cloud Pod into the application runtime/ Users can import Cloud Pods from...
  remote    Manage cloud pod remotes
  save      Create a new Cloud Pod
  versions  List all available versions for a Cloud Pod

```

## 2. Pulling and Loading the Cloud Pod

Now, in a fresh LocalStack instance, the helper colleague can immediately load the Cloud Pod, because they’re part of the 
same organization, and their licences permit this:

{{< command >}}
$ localstack pod load  cloud-pod-product-app
{{</ command >}}
```bash
Cloud Pod cloud-pod-product-app successfully loaded
```

## **3. Debugging and Resolving the Issue**

Not only can someone else easily reproduce the bug now, but they also have access to the state and data of the services 
involved, meaning that the Lambda logs are still in the CloudWatch log groups.

![CloudWatch Logs](cloudwatch-logs.png)

By spotting the error message, there’s an instant starting point for checking the source of the problem. The error message displayed in the logs is quite specific:

`"Error: User: arn:aws:sts::000000000000:assumed-role/productRole/get-product is not authorized to perform: dynamodb:GetItem on resource: arn:aws:dynamodb:us-east-1:000000000000:table/Products because no identity-based policy allows the dynamodb:GetItem action (Service: DynamoDb, Status Code: 400, Request ID: d50e9dad-a01a-4860-8c21-e844a930ba7d)"`

## 4. Identifying the Misconfiguration

At a first glance, this error points to a permissions issue related to accessing DynamoDB. The action **`dynamodb:GetItem`** is 
not authorized for the role, preventing the retrieval of a product by its ID. This kind of error was not really foreseen as one 
of the exceptions to be handled in the application. Honest mistake, IAM policies are not always easy and straightforward.

To confirm the suspicion, adding and retrieving a product by ID is tested once more, and indeed, the action failed due to missing 
permission. This discovery leads to the next step in troubleshooting: **inspecting the Terraform configuration file** responsible 
for defining the permissions attached to the lambda role interacting with DynamoDB.

## 5. Fixing the Terraform Configuration

Upon review, it is found that the Terraform configuration did not include the necessary permission **`dynamodb:GetItem`** in the
policy attached to the lambda role. This oversight explains why the error was occurring. The Terraform configuration file acts as a 
blueprint for AWS resource permissions, and any missing action can lead to unauthorized errors, just like what happened here.

This scenario underscores the importance of thorough review and testing of IAM roles and policies when working with AWS resources. 
It's easy to overlook a single action in a policy, but as we've seen, such an omission can significantly impact application 
functionality. By carefully checking the Terraform configuration files and ensuring that all necessary permissions are included, 
developers can avoid similar issues and ensure a smoother, error-free interaction with AWS services.

The allowed actions should look like this list:

```bash
resource "aws_iam_policy" "lambda_dynamodb_policy" {
  name        = "LambdaDynamoDBAccess"
  description = "IAM policy for accessing DynamoDB from Lambda"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "dynamodb:GetItem",
          "dynamodb:UpdateItem",
          "dynamodb:PutItem",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
```

To confirm this error, the teammate also creates the stack on AWS, and indeed the source of the issue is the same policy 
misconfiguration:

![AWS CloudWatch Logs](aws-cloudwatch-logs.png)

## 6. Other Remote Options

After seeing how LocalStack Cloud Pods help teams work together better, let's look at the other ways companies can keep their 
snapshots in their own court. For environments with stricter security policies, there are a few storage options that help protect data,
making it easy to keep everything secure and accessible no matter what your needs are.

### **1. S3 bucket remote storage**

The S3 remote allows for the storage of Cloud Pod assets in an existing S3 bucket located in a real AWS account. The first
action to take is to export the required AWS credentials during the terminal session.

Side note: the S3 remote feature for Cloud Pods is only accessible when the localstack CLI is installed through `pip`, for now.

Let’s try it out:

{{< command >}}
$ export AWS_ACCESS_KEY_ID=<YOUR_AWS_ACCESS_KEY_ID>
$ export AWS_SECRET_ACCESS_KEY=<YOUR_AWS_SECRET_ACCESS_KEY>
{{</ command >}}

Next, we set up a new remote connection specifically for an S3 bucket. By using the command below, we create a remote
called `s3-storage-aws`. This remote is for saving Cloud Pod items in an S3 bucket named `localstack-pod-storage`.

{{< command >}}
$ localstack pod remote add s3-storage-aws 's3://ls-pods-bucket-test/?access_key_id={access_key_id}&secret_access_key={secret_access_key}'
{{</ command >}}

### Note

When setting this up, we might encounter an error message like:
`SSL validation failed for https://localstack-pod-storage.s3.amazonaws.com/ hostname.`

To fix this, we can have a list of exceptions that point to AWS instead of LocalStack by using the following configuration
flag in the docker-compose file:
**`DNS_NAME_PATTERNS_TO_RESOLVE_UPSTREAM=.*localstack-pod-storage.s3.amazonaws.com`**

This setting is generally used for hybrid setups, where certain API calls target AWS, whereas other services will target LocalStack.

Now we can save the pod:

{{< command >}}
$ localstack pod save cloud-pod-product-app s3-storage-aws
{{</ command >}}

```bash
Cloud Pod `cloud-pod-product-app` successfully created ✅
Version: 1
Remote: s3
Services: sts,s3,iam,apigateway,dynamodb,lambda
```

The Cloud Pod is visible in the AWS S3 dashboard:

![S3 Bucket Storage](s3-bucket-storage-dashboard.png)

To load the state into a new LocalStack instance, we use:

{{< command >}}
$ localstack pod load cloud-pod-product-app s3-storage-aws
{{</ command >}}

```bash
Cloud Pod cloud-pod-product-app successfully loaded
```

### 2. ORAS remote storage

ORAS, which stands for OCI Registry As Storage, is a tool designed to help you use OCI (Open Container Initiative) registries 
for storing and sharing a wide range of content. While OCI registries were originally created for container images, ORAS 
extends their use to other types of artifacts. Essentially, ORAS allows you to push and pull any content to and from 
OCI-compliant registries using the same workflows you'd use for container images.

Docker Hub comes into play as a popular, OCI-compliant container registry. It's primarily known for hosting Docker container
images but, thanks to the OCI specification's flexibility, it can also serve as a storage and distribution point for other 
types of artifacts through tools like ORAS. This makes Docker Hub not just a hub for Docker images but a versatile cloud 
registry for various types of application artifacts, supporting the broader ecosystem of cloud-native development and deployment
practices.

Let’s illustrate how you can utilize Docker Hub to store and retrieve Cloud Pods. This is very similar to the S3 bucket 
storage setup:

{{< command >}}
$ export ORAS_USERNAME=your_docker_hub_id
$ export ORAS_PASSWORD=your_docker_hub_password
{{</ command >}}

We can now use the CLI to create a new remote called `oras-remote`

{{< command >}}
$ localstack pod remote add oras-remote 'oras://{oras_username}:{oras_password}@registry.hub.docker.com/<your_docker_hub_id>'
{{</ command >}}

A Cloud Pod can be stored on the newly configured remote:

{{< command >}}
$ localstack pod save cloud-pod-product-app oras-remote
{{</ command >}}
```bash
Cloud Pod `cloud-pod-product-app` successfully created ✅
Version: 1
Remote: oras
Services: sts,s3,iam,apigateway,dynamodb,lambda
```

After saving the Cloud Pod, it will appear in the Docker Hub repositories dashboard:

![Docker Hub Repositories](docker-hub-repositories.png)

### Viewing all the remotes

By using the command `localstack pod remote list`, you can view all the configured remote options for saving Cloud Pods,
including the AWS S3 bucket and the Docker Hub repository configuration, with the default set to the LocalStack platform.

{{< command >}}
$ localstack pod remote list
{{</ command >}}

```bash
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Remote Name    ┃ URL                                                                                              ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ s3-storage-aws │ s3://localstack-pod-storage/?access_key_id={access_key_id}&secret_access_key={secret_access_key} │
│ oras-remote    │ oras://{oras_username}:{oras_password}@registry.hub.docker.com/msmuzitiger210                    │
│ default        │ platform://localstack                                                                            │
└────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Conclusions

Cloud Pods play a crucial role in team collaboration, significantly speeding up development processes. The multiple and 
versatile options for remote storage can support different business requirements for companies that prefer using the 
environments they control. Cloud Pods are not just for teamwork; they also excel in other areas, such as creating 
resources in Continuous Integration (CI) for ultra-fast testing pipelines. By streamlining these aspects, Cloud Pods offer
a versatile tool that enhances both collaboration and efficiency in various development scenarios.

## Additional resources

- [Cloud Pods documentation](https://docs.localstack.cloud/user-guide/state-management/cloud-pods/)
- [Terraform for AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)