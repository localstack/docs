---
title: "Ephemeral Instances"
linkTitle: "Ephemeral Instances"
weight: 1
description: Create an Ephemeral Instance in the cloud using the LocalStack Web Application
---

## Introduction

Ephemeral Instances allows you to run a LocalStack instance in the cloud. You can interact with these instances via the LocalStack Web Application, or by configuring your integrations and developer tools with the endpoint URL of the ephemeral instance.

## Getting started

This guide is designed for users new to Ephemeral Instance and assumes basic knowledge of the LocalStack Web Application. In this guide, we will create an Ephemeral Instance and interact with it via the LocalStack Web Application and the AWS CLI.

### Create a new Ephemeral Instance

Navigate to the [**LocalStack Ephemeral Instance Management**](https://app.localstack.cloud/instances/ephemeral) page. In the form, enter the name of the new Ephemeral Instance, select the lifetime of the instance by dragging the slider, and click on **Launch**.

<img src="ephemeral-instance-creation.png" alt="Creating an Ephemeral Instance" title="Creating an Ephemeral Instance" width="800" />

Optionally, you can specify a LocalStack Extension to be installed in the Ephemeral Instance. You can select the extension from the **Extension settings** dropdown list before launching the Ephemeral Instance.
In case you have access to cloud pods and a pod you want to start your instance with, you can also choose it from the **Cloud Pod Settings** dropdown.

### Interact with the Ephemeral Instance

After the Ephemeral Instance is created, you will be able to see the instance in the **LocalStack Instance Management** page.

You will also be able to access the following features with your Ephemeral Instance:

- Status Page
- Resource Browser
- State Management
- Extensions

<img src="localstack-ephemeral-instance.png" alt="LocalStack Ephemeral Instance" title="LocalStack Ephemeral Instance" width="800" />

### Access the Ephemeral Instance via AWS CLI

You can access the Ephemeral Instance via the AWS CLI by configuring the AWS CLI with the endpoint URL of the Ephemeral Instance. You can find the endpoint URL of the Ephemeral Instance in the **LocalStack Instance Management** page. Copy the endpoint URL and set it as the `--endpoint-url` parameter in the AWS CLI command.

To create an S3 bucket in the Ephemeral Instance, run the following command:

{{< command >}}
$ aws --endpoint-url=<EPHEMERAL_INSTANCE_ENDPOINT_URL> s3 mb s3://<BUCKET_NAME>
{{< /command >}}

You can replace `<EPHEMERAL_INSTANCE_ENDPOINT_URL>` with the endpoint URL of the Ephemeral Instance and `<BUCKET_NAME>` with the name of the S3 bucket you want to create. To query the list of S3 buckets in the Ephemeral Instance, run the following command:

{{< command >}}
$ aws --endpoint-url=<EPHEMERAL_INSTANCE_ENDPOINT_URL> s3 ls
{{< /command >}}

You can also use integrations, such as [CDK](https://docs.localstack.cloud/user-guide/integrations/aws-cdk/), [SAM CLI](https://docs.localstack.cloud/user-guide/integrations/aws-sam/), and [Terraform](https://docs.localstack.cloud/user-guide/integrations/terraform/), to interact with the Ephemeral Instance. In these integrations, you can change the `AWS_ENDPOINT_URL` environment variable to the endpoint URL of the Ephemeral Instance.

### Shut Down the Ephemeral Instance

You can shut down the instance by navigating to the [Ephemeral Instances page](https://app.localstack.cloud/instances/ephemeral) and clicking on the **Shut Down** button.

<img src="shutdown-ephemeral-instance.png" alt="Shutdown the LocalStack Ephemeral Instance" title="Shutdown the LocalStack Ephemeral Instance" width="800" />

## Load Cloud Pod into an Ephmeral Instance

You can load a Cloud Pod into an Ephemeral Instance to seed your pre-existing cloud resources into a freshly created Ephemeral Instance. You can further use AWS CLI or other integrations to interact with these resources, along with using other features of the LocalStack Web Application.

To load a pre-defined Cloud Pod, navigate to the [Cloud Pods page](https://app.localstack.cloud/pods), click on the Cloud Pod you want to load into the Ephemeral Instance, and click on the **Load Into Instance** button. Select the Ephemeral Instance you want to load the Cloud Pod into and click on **Load**.

You will be redirected to the **Export/Import State** page where you can click on **Load State From Pod** to load the Cloud Pod into the Ephemeral Instance.
Alternatively, you can also specify a Cloud Pod to be loaded on startup, when filling out the instance creation form.
<img src="cloud-pod-details-page.png" alt="Cloud Pod Details page" title="Cloud Pod Details page" width="800" />
<br><br>

You can copy the endpoint URL of the Ephemeral Instance and use it to manage your cloud resources.

{{< callout "warning" >}}
Ephemeral Instances, by default, are created with the latest version of LocalStack. If you have created a Cloud Pod from an older version of LocalStack, you need to update the Cloud Pod to the latest version before loading it into an Ephemeral Instance.
{{< /callout >}}

## Credit Consumption

Ephemeral Instances consume credits based on the duration of the instance. Currently, for every 1 credit, you can run an Ephemeral Instance for 1 minute. You can view the available minutes under the **Lifetime in minutes** slider when creating an Ephemeral Instance. You can view existing credit consumption of your workspace in the **Credit consumption** card at the bottom. 

<img src="credit-consumption.png" alt="Credit Consumption" title="Credit Consumption" width="800" />
<br><br>
