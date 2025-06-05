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

Deployment groups can be managed with [CreateDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentGroup.html), [ListDeploymentGroups](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeploymentGroups.html), [UpdateDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_UpdateDeploymentGroup.html), [GetDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeploymentGroup.html) and [DeleteDeploymentGroup](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_DeleteDeploymentGroup.html).

{{< command >}}
$ awslocal deploy create-deployment-group \
    --application-name hello \
    --service-role-arn arn:aws:iam::000000000000:role/role \
    --deployment-group-name hello-group
<disable-copy>
{
    "deploymentGroupId": "09506586-9ba9-4005-a1be-840407abb39d"
}
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal deploy list-deployment-groups --application-name hello
<disable-copy>
{
    "deploymentGroups": [
        "hello-group"
    ]
}
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal deploy get-deployment-group --application-name hello \
    --deployment-group-name hello-group
<disable-copy>
{
    "deploymentGroupInfo": {
        "applicationName": "hello",
        "deploymentGroupId": "09506586-9ba9-4005-a1be-840407abb39d",
        "deploymentGroupName": "hello-group",
        "deploymentConfigName": "CodeDeployDefault.OneAtATime",
        "autoScalingGroups": [],
        "serviceRoleArn": "arn:aws:iam::000000000000:role/role",
        "triggerConfigurations": [],
        "deploymentStyle": {
            "deploymentType": "IN_PLACE",
            "deploymentOption": "WITHOUT_TRAFFIC_CONTROL"
        },
        "outdatedInstancesStrategy": "UPDATE",
        "computePlatform": "Server",
        "terminationHookEnabled": false
    }
}
</disable-copy>
{{< /command >}}

### Deployments

Operations related to deployment management are: [CreateDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeployment.html), [GetDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_GetDeployment.html), [ListDeployments](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ListDeployments.html).

{{< command >}}
$ awslocal deploy create-deployment \
    --application-name hello \
    --deployment-group-name hello-group \
    --revision '{"revisionType": "S3", "s3Location": {"bucket": "placeholder", "key": "placeholder", "bundleType": "tar"}}'
<disable-copy>
{
    "deploymentId": "d-TU3TNCSTO"
}
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal deploy list-deployments
<disable-copy>
{
    "deployments": [
        "d-TU3TNCSTO"
    ]
}
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal deploy get-deployment --deployment-id d-TU3TNCSTO
<disable-copy>
{
    "deploymentInfo": {
        "applicationName": "hello",
        "deploymentGroupName": "hello-group",
        "deploymentConfigName": "CodeDeployDefault.OneAtATime",
        "deploymentId": "d-TU3TNCSTO",
        "revision": {
            "revisionType": "S3",
            "s3Location": {
                "bucket": "placeholder",
                "key": "placeholder",
                "bundleType": "tar"
            }
        },
        "status": "Created",
        "createTime": 1747750522.133381,
        "creator": "user",
        "ignoreApplicationStopFailures": false,
        "updateOutdatedInstancesOnly": false,
        "deploymentStyle": {
            "deploymentType": "IN_PLACE",
            "deploymentOption": "WITHOUT_TRAFFIC_CONTROL"
        },
        "instanceTerminationWaitTimeStarted": false,
        "fileExistsBehavior": "DISALLOW",
        "deploymentStatusMessages": [],
        "computePlatform": "Server"
    }
}
</disable-copy>
{{< /command >}}

Furthermore, [ContinueDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_StopDeployment.html) and [StopDeployment](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_StopDeployment.html) can be used to control the deployment flows.

{{< command >}}
$ awslocal deploy continue-deployment --deployment-id d-TU3TNCSTO
{{< /command >}}

{{< command >}}
$ awslocal deploy stop-deployment --deployment-id d-TU3TNCSTO
<disable-copy>
{
    "status": "Succeeded",
    "statusMessage": "Mock deployment stopped"
}
</disable-copy>
{{< /command >}}

## Limitations

All CodeDeploy operations are currently mocked.
