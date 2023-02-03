---
title: "Quickstart"
linkTitle: "Quickstart"
weight: 4
description: >
  This quickstart gives an overview of how you can get a simple AWS application up and running on your local machine to understand local cloud development with LocalStack!
cascade:
  type: docs
---

This quickstart guide will walk you through starting LocalStack on your local machine to deploying a sample AWS application locally using LocalStack's cloud emulation. This guide assumes that you have [installed LocalStack on your local machine]({{< ref "installation" >}}), [signed up](https://app.localstack.cloud) for a LocalStack account and configured your [API key]({{< ref "api-key" >}}) to authenticate your LocalStack container on startup.

{{< alert title="Note" >}}
The quickest way to experiment with LocalStack is to use one of our [LocalStack quickstart samples](https://app.localstack.cloud/quickstart) to deploy a thumbnail creator, request worker application, or an asynchronous microservice with tracing/debugging. The quickstart samples will automatically connect to your running LocalStack container on your local machine and run the applications.
{{< /alert >}}

## Start your LocalStack container

After installing LocalStack and configuring your API key, let us start LocalStack. You can start LocalStack via the `localstack` CLI, Docker, or a Docker Compose setup. To run our sample AWS application, we will start LocalStack with the `EXTRA_CORS_ALLOWED_ORIGINS=http://localhost:3000` configuration. In this guide, we will use the `localstack` CLI to start LocalStack.

{{< command >}}
$ EXTRA_CORS_ALLOWED_ORIGINS=http://localhost:3000 localstack start 
{{< / command >}}

You can optionally run your LocalStack container in background mode by adding the `-d` flag to the `localstack start` command.

{{< alert title="Note" >}}
LocalStack supports setting environment variables as Configuration options to alter the behavior of LocalStack. The `EXTRA_CORS_ALLOWED_ORIGINS` configuration allows other services to communicate with LocalStack. Refer to our [comprehensive documentation on LocalStack Configuration options]({{< ref "references/configuration" >}}).
{{< /alert >}}

## Setup the sample AWS application

With LocalStack ready, you are ready to run your first AWS application locally. Clone our [sample application](https://github.com/localstack/localstack-demo) using Git on your local machine:

{{< command >}}
$ git clone git@github.com:localstack/localstack-demo.git
{{< / command >}}

The sample app illustrates a typical web application scenario with asynchronous request processing happening in the background, all running locally inside LocalStack.

<img src="../sample-app-architecture.png" alt="Application architecture for the sample application, with the different components and services involved in processing the requests." title="Application architecture for the sample application, with the different components and services involved in processing the requests." width="600px" />

In this sample application:

- Users can send a new request through a locally deployed API Gateway which is connected to a Lambda function for further processing.
- The Lambda function then puts the request through an SQS queue which then triggers another Lambda function that reads off the SQS queue.
- The Lambda function then puts it on a Step Functions State Machine which consists of two steps: A processing Lambda function that processes the requests and updates a local DynamoDB table, and an archiving Lambda function that puts the result in an S3 bucket.
- As the request is going through different stages of processing, the table below will be updated with the current request status (**QUEUED** -> **PROCESSING** -> **FINISHED**).
- Once the request is FINISHED, the processing result will become available as a link to a file stored in an S3 bucket.

All of these resources will be deployed to the local `us-east-1` region on LocalStack using Serverless framework.

Let us install all the dependencies for our sample application. You need to ensure that you have Node.js and `npm` available, to install Serverless framework and other dependencies. Run the command:

{{< command >}}
$ npm install
$ npm install -g serverless
{{< / command >}}

## Run the sample AWS application

With the initial setup now completed, you can deploy the application via `serverless` CLI:

{{< command >}}
$ serverless deploy --stage local
{{< / command >}}

Navigate to [`localhost:4566/archive-bucket/index.html`](http://localhost:4566/archive-bucket/index.html) to access the web application. You can enable the **Auto-Refresh** and click on **Create new request**. You will see the request being processed in the table below after an alert that your request has been sent and queued. After the processing is complete, you will see an option in the table to download the result from S3. Click on it to download a text file with the message: `Archive result for request XXXXXXX`.

If you have the `awslocal` CLI installed, you can run the following command to see the archive results in the local S3 bucket:

{{< command >}}
$ awslocal s3 ls s3://archive-bucket/
{{< / command >}}

You can optionally send a request to the API Gateway REST API using the `make send-request` command.

## Destroy the local infrastructure

Now that you’ve seen how to deploy a local AWS infrastructure for your sample application, let’s clean up and tear down the resources that are part of the project:

{{< command >}}
$ localstack stop
{{< / command >}}

LocalStack is ephemeral in nature and will not persist any data across restarts. LocalStack runs inside a Docker container and once it is spinned down, all the locally created resources are removed automatically. To persist data across restarts, consider looking at our [persistence mechanism documentation]({{< ref "references/persistence-mechanism" >}}) or [Cloud Pods]({{< ref "user-guide/tools/cloud-pods" >}}), our next generation state management utility.

## Next Steps

Congratulations! You’ve successfully provisioned local AWS resources using LocalStack. By completing this quickstart guide you have successfully:

- Started LocalStack on your local machine.
- Provisioned a local AWS infrastructure using LocalStack.
- Installed and locally deployed a request processing application.
- Tested the application by sending requests across an API Gateway.
- Destroyed the local resources you have provisioned.

To do more with LocalStack, explore the following depending on your expertise level:

- [Tutorials]({{< ref "tutorials" >}}): Learn about using LocalStack across various AWS services, application stacks, and wider use-cases through our tutorials.
- [User Guide]({{< ref "user-guide" >}}): Explore various LocalStack's emulated AWS services, third-party integrations, toolings, CI service providers, and more with our User Guide.
- [References]({{< ref "references" >}}): Dive into LocalStack references for a comprehensive understanding of key LocalStack internals & technical know-how for navigating our ecosystem.
- [Blog](https://localstack.cloud/blog): Read our latest blog posts about LocalStack and the new enhancements that we are bringing to power a local development & testing experience for cloud developers and beyond!
