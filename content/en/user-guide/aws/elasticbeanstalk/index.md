---
title: "Elastic Beanstalk"
linkTitle: "Elastic Beanstalk"
description: >
  Get started with Elastic Beanstalk (EB) on LocalStack
tags: ["Pro image"]
---

## Introduction

Elastic Beanstalk (EB) is a managed platform-as-a-service (PaaS) provided by Amazon Web Services (AWS) that simplifies the process of deploying, managing, and scaling web applications and services. Elastic Beanstalk orchestrates various AWS services, including EC2, S3, SNS, and Elastic Load Balancers. Elastic Beanstalk also supports various application environments, such as Java, .NET, Node.js, PHP, Python, Ruby, Go, and Docker.

LocalStack allows you to use the Elastic Beanstalk APIs in your local environment to create and manage applications, environments and versions. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_elasticbeanstalk/), which provides information on the extent of Elastic Beanstalk's integration with LocalStack.

## Getting started

This guide is designed for users new to Elastic Beanstalk and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to create an Elastic Beanstalk application and environment with the AWS CLI.

### Create an application

To create an Elastic Beanstalk application, you can use the [`CreateApplication`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplication.html) API. Run the following command to create an application named `my-app`:

{{< command >}}
$ awslocal elasticbeanstalk create-application \
    --application-name my-app
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Application": {
        "ApplicationArn": "arn:aws:elasticbeanstalk:us-east-1:000000000000:application/my-app",
        "ApplicationName": "my-app",
        "DateCreated": "2023-08-24T05:55:57.603443Z"
    }
}
```

You can also use the [`DescribeApplications`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplications.html) API to retrieve information about your application. Run the following command to retrieve information about the `my-app` application, we created earlier:

{{< command >}}
$ awslocal elasticbeanstalk describe-applications \
    --application-names my-app
{{< /command >}}

### Create an environment

To create an Elastic Beanstalk environment, you can use the [`CreateEnvironment`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateEnvironment.html) API. Run the following command to create an environment named `my-environment`:

{{< command >}}
$ awslocal elasticbeanstalk create-environment \
    --application-name my-app \
    --environment-name my-environment
{{< /command >}}

The following output would be retrieved:

```bash
{
    "EnvironmentName": "my-environment",
    "EnvironmentId": "4fcae3fb",
    "ApplicationName": "my-app",
    "DateCreated": "2023-08-24T05:57:59.889966Z",
    "EnvironmentArn": "arn:aws:elasticbeanstalk:us-east-1:000000000000:applicationversion/my-app/version"
}
```

You can also use the [`DescribeEnvironments`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html) API to retrieve information about your environment. Run the following command to retrieve information about the `my-environment` environment, we created earlier:

{{< command >}}
$ awslocal elasticbeanstalk describe-environments \
    --environment-names my-environment
{{< /command >}}

### Create an application version

To create an Elastic Beanstalk application version, you can use the [`CreateApplicationVersion`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplicationVersion.html) API. Run the following command to create an application version named `v1`:

{{< command >}}
$ awslocal elasticbeanstalk create-application-version \
    --application-name my-app \
    --version-label v1
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationVersion": {
        "ApplicationVersionArn": "arn:aws:elasticbeanstalk:us-east-1:000000000000:applicationversion/my-app/v1",
        "ApplicationName": "my-app",
        "VersionLabel": "v1",
        "DateCreated": "2023-08-24T05:59:58.166021Z"
    }
}
```

You can also use the [`DescribeApplicationVersions`](https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeApplicationVersions.html) API to retrieve information about your application version. Run the following command to retrieve information about the `v1` application version, we created earlier:

{{< command >}}
$ awslocal elasticbeanstalk describe-application-versions \
    --application-name my-app
{{< /command >}}

## Current Limitations

LocalStack's Elastic Beanstalk implementation is limited and lacks support for installing application and running it in a local Elastic Beanstalk environment. LocalStack also does not support the [`eb`](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) CLI tool. However, you can use other integrations, such as AWS CLI & Terraform, to mock the Elastic Beanstalk APIs and test your workflow locally.
