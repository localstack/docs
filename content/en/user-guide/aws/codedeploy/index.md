---
title: CodeDeploy
linkTitle: CodeDeploy
description: >
  Get started with CodeDeploy on LocalStack
tags: ["Pro image"]
---

## Introduction

CodeDeploy is a service that automates application deployments.
On AWS, it supports deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services.
Furthermore, based on the target it is also possible to use an in-place deployment or a blue/green deployment.

LocalStack supports a mocking of CodeDeploy API operations.
The supported operations are listed on the [API coverage page]({{< ref "coverage_codedeploy" >}}).

## Getting Started

This guide will walk through the process of creating CodeDeploy applications, deployment configuration, deployment groups, and deployments.

Basic knowledge of the AWS CLI and the [`awslocal`](https://github.com/localstack/awscli-local) wrapper is expected.

Start LocalStack using your preferred method.

### Applications

An application is a CodeDeploy construct that uniquely identifies your targetted application.
Create an application with the [CreateApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateApplication.html) operation:

{{< command >}}
$ awslocal deploy create-application --application-name hello --compute-platform Server
<disable-copy>
{
    "applicationId": "063714b6-f438-4b90-bacb-ce04af7f5e83"
}
</disable-copy>
{{< /command >}}

Make note of the application name, which can be used with other operations such as [GetApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetApplication.html), [UpdateApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateApplication.html) and [DeleteApplication](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteApplication.html).

{{< command >}}
$ awslocal deploy get-application --application-name hello
<disable-copy>
{
    "application": {
        "applicationId": "063714b6-f438-4b90-bacb-ce04af7f5e83",
        "applicationName": "hello",
        "createTime": 1747663397.271634,
        "computePlatform": "Server"
    }
}
</disable-copy>
{{< /command >}}

You can list all application using [ListApplications](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListApplications.html).

{{< command >}}
$ awslocal deploy list-applications
<disable-copy>
{
    "applications": [
        "hello"
    ]
}
</disable-copy>
{{< /command >}}

{{< command >}}
<disable-copy>
</disable-copy>
{{< /command >}}

### Deployment configuration

A deployment configuration consists of rules for deployment along with success and failure criteria.

Create a deployment configuration using [CreateDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentConfig.html):

{{< command >}}
$ awslocal deploy create-deployment-config --deployment-config-name hello-conf \
    --compute-platform Server  \
    --minimum-healthy-hosts '{"type": "HOST_COUNT", "value": 1}'
<disable-copy>
{
    "deploymentConfigId": "0327ce0a-4637-4884-8899-49af7b9423b6"
}
</disable-copy>
{{< /command >}}


[ListDeploymentConfigs](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentConfigs.html) can be used to list all available configs:

{{< command >}}
$ awslocal deploy list-deployment-configs
<disable-copy>
{
    "deploymentConfigsList": [
        "hello-conf"
    ]
}
</disable-copy>
{{< /command >}}

Use [GetDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentConfig.html) and [DeleteDeploymentConfig](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentConfig.html) to manage deployment configurations.

{{< command >}}
$ awslocal deploy get-deployment-config --deployment-config-name hello-conf
<disable-copy>
{
    "deploymentConfigInfo": {
        "deploymentConfigId": "0327ce0a-4637-4884-8899-49af7b9423b6",
        "deploymentConfigName": "hello-conf",
        "minimumHealthyHosts": {
            "type": "HOST_COUNT",
            "value": 1
        },
        "createTime": 1747663716.208291,
        "computePlatform": "Server"
    }
}
</disable-copy>
{{< /command >}}

### Deployment groups

### Deployments

Operations related to deployment management are: CreateDeployment, GetDeployment, ListDeployments


Furthermore, ContinueDeployment and StopDeployment can be used to control the deployment flows.


## Limitations
