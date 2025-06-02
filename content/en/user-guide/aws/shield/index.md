---
title: "Shield"
linkTitle: "Shield"
description: Get started with Shield on LocalStack
tags: ["Ultimate"]
---

## Introduction

Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS.
Shield provides always-on detection and inline mitigations that minimize application downtime and latency, by protecting users from L4, L7 and most common L3, L4 network and transport layer DDoS attacks.
Shield detection and mitigation is designed to protect against threats, including ones that are not known to the service at the time of detection.

LocalStack allows you to use the Shield APIs in your local environment, and provides a simple way to mock and test the Shield service locally.
The supported APIs are available on our [API coverage page]({{< ref "coverage_shield" >}}), which provides information on the extent of Shield's integration with LocalStack.

## Getting Started

This guide is designed for users new to Shield and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Shield protection, list all protections, and delete a protection with the AWS CLI.

### Create a Shield Protection

To create a Shield protection, use the [`CreateProtection`](https://docs.aws.amazon.com/cli/latest/reference/shield/create-protection.html) API.
The following command creates a Shield protection for a resource:

{{< command >}}
$ awslocal shield create-protection \
  --name "my-protection" \
  --resource-arn "arn:aws:elasticloadbalancing:us-east-1:000000000000:loadbalancer/app/my-alb/1234567890"
{{< /command >}}

The output should look similar to the following:

```bash
{
    "ProtectionId": "67908d33-16c0-443d-820a-31c02c4d5976"
}
```

### List all Protections

To list all Shield protections, use the [`ListProtections`](https://docs.aws.amazon.com/cli/latest/reference/shield/list-protections.html) API.
The following command lists all Shield protections:

{{< command >}}
$ awslocal shield list-protections
{{< /command >}}

The output should look similar to the following:

```bash
{
    "Protections": [
        {
            "Id": "67908d33-16c0-443d-820a-31c02c4d5976",
            "Name": "my-protection",
            "ResourceArn": "arn:aws:elasticloadbalancing:us-east-1:000000000000:loadbalancer/app/my-alb/1234567890",
            "ProtectionArn": "arn:aws:shield::000000000000:protection/67908d33-16c0-443d-820a-31c02c4d5976"
        }
    ]
}
```

### Describe a Protection

To describe a Shield protection, use the [`DescribeProtection`](https://docs.aws.amazon.com/cli/latest/reference/shield/describe-protection.html) API.
The following command describes a Shield protection:

{{< command >}}
$ awslocal shield describe-protection \
  --protection-id "67908d33-16c0-443d-820a-31c02c4d5976"
{{< /command >}}

Replace the protection ID with the ID of the protection you want to describe.
The output should look similar to the following:

```bash
{
    "Protection": {
        "Id": "67908d33-16c0-443d-820a-31c02c4d5976",
        "Name": "my-protection",
        "ResourceArn": "arn:aws:elasticloadbalancing:us-east-1:000000000000:loadbalancer/app/my-alb/1234567890",
        "ProtectionArn": "arn:aws:shield::000000000000:protection/67908d33-16c0-443d-820a-31c02c4d5976"
    }
}
```

### Delete a Protection

To delete a Shield protection, use the [`DeleteProtection`](https://docs.aws.amazon.com/cli/latest/reference/shield/delete-protection.html) API.
The following command deletes a Shield protection:

{{< command >}}
$ awslocal shield delete-protection \
  --protection-id "67908d33-16c0-443d-820a-31c02c4d5976"
{{< /command >}}

## Current Limitations

Shield Config is currently mocked in LocalStack.
You can create, read, update, and delete Shield protections & subscriptions, but the actual protection or subscription is not applied to any resources.
If you need this feature, please consider opening a [feature request on GitHub](https://github.com/localstack/localstack/issues/new).
