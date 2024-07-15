---
title: "Auto Scaling"
linkTitle: "Auto Scaling"
description: Get started with Auto Scaling" on LocalStack
tags: ["Pro image"]
---

## Introduction

Auto Scaling helps you maintain application availability and allows you to automatically add or remove EC2 instances according to the demand. You can use Auto Scaling to ensure that you are running your desired number of instances.

LocalStack allows you to use the Auto Scaling APIs locally to create and manage Auto Scaling groups locally. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_autoscaling/), which provides information on the extent of Auto Scaling's integration with LocalStack.

## Getting started

This guide is designed for users new to Auto Scaling and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a launch template, an Auto Scaling group, and attach an instance to the Auto Scaling group using the AWS CLI.

### Create a launch template

You can create a launch template that defines the launch configuration for the instances in the Auto Scaling group using the [`CreateLaunchTemplate`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API. Run the following command to create a launch template:

{{< command >}}
$ awslocal ec2 create-launch-template \
    --launch-template-name my-template-for-auto-scaling \
    --version-description version1 \
    --launch-template-data '{"ImageId":"ami-ff0fea8310f3","InstanceType":"t2.micro"}'
{{< /command >}}

The following output is displayed:

```json
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-5ccdf1a84f178ba44",
        "LaunchTemplateName": "my-template-for-auto-scaling",
        "CreateTime": "2024-07-12T07:59:08+00:00",
        "CreatedBy": "arn:aws:iam::000000000000:root",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1,
        "Tags": []
    }
}
```

### Create an Auto Scaling group

Before creating an Auto Scaling group, you need to fetch the subnet ID. Run the following command to describe the subnets:

{{< command >}}
$ awslocal ec2 describe-subnets
{{< /command >}}

Copy the subnet ID from the output and use it to create the Auto Scaling group. Run the following command to create an Auto Scaling group using the [`CreateAutoScalingGroup`](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CreateAutoScalingGroup.html) API:

{{< command >}}
$ awslocal autoscaling create-auto-scaling-group \
    --auto-scaling-group-name my-asg \
    --launch-template LaunchTemplateId=lt-5ccdf1a84f178ba44 \
    --min-size 1 \
    --max-size 5 \
    --vpc-zone-identifier 'subnet-d4d16268'
{{< /command >}}

### Describe the Auto Scaling group

You can describe the Auto Scaling group using the [`DescribeAutoScalingGroups`](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html) API. Run the following command to describe the Auto Scaling group:

{{< command >}}
$ awslocal autoscaling describe-auto-scaling-groups
{{< /command >}}

The following output is displayed:

```json
{
    "AutoScalingGroups": [
        {
            "AutoScalingGroupName": "my-asg",
            "AutoScalingGroupARN": "arn:aws:autoscaling:us-east-1:000000000000:autoScalingGroup:74b4ffac-4588-4a7c-86b1-9fa992f49c8e:autoScalingGroupName/my-asg",
            "LaunchTemplate": {
                "LaunchTemplateId": "lt-5ccdf1a84f178ba44",
                "LaunchTemplateName": "my-template-for-auto-scaling"
            },
            "MinSize": 1,
            "MaxSize": 5,
            ...
            "Instances": [
                {
                    "InstanceId": "i-fc01551d496fc363f",
                    "InstanceType": "t2.micro",
                    "AvailabilityZone": "us-east-1a",
                    ...
                }
            ],
            ...
            "TerminationPolicies": [
                "Default"
            ],
            ...
            "CapacityRebalance": false
        }
    ]
}
```

### Attach an instance to the Auto Scaling group

You can attach an instance to the Auto Scaling group using the [`AttachInstances`](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachInstances.html) API.

Before that, create an EC2 instance using the [`RunInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API. Run the following commands to create an EC2 instance locally:

{{< command >}}
$ docker pull ubuntu:focal
$ docker tag ubuntu:focal localstack-ec2/ubuntu-focal-docker-ami:ami-00a001
$ awslocal ec2 run-instances \
    --image-id ami-00a001 --count 1
{{< /command >}}

Fetch the instance ID from the output and use it to attach the instance to the Auto Scaling group. Run the following command to attach the instance to the Auto Scaling group:

{{< command >}}
$ awslocal autoscaling attach-instances \
    --instance-ids i-0d678c4ecf6018dde \
    --auto-scaling-group-name my-asg
{{< /command >}}

Replace `i-0d678c4ecf6018dde` with the instance ID that you fetched from the output.
