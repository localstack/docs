---
title: "Elastic Compute Cloud (EC2)"
linkTitle: "Elastic Compute Cloud (EC2)"
categories: ["LocalStack Pro"]
description: Elastic Compute Cloud (EC2)
---

LocalStack has basic support for two backend managers for running instances locally: `virtualbox` (default) and `docker`.
The manager can be configured by using the `EC2_VM_MANAGER` environment variable.

### VirtualBox

The VirtualBox backend requires the [Oracle VM VirtualBox](https://www.virtualbox.org/) installed on your system.

<!-- Where is the stuff about EC2 local daemon documented? Link it here? -->

### Docker

The Docker backend uses the [Docker Engine](https://docs.docker.com/engine/) to simulate instances.
All limitations that apply to containers apply to EC2 instances backed by the Docker manager, including root access and networking.
Access to the Docker socket is required which can be made available to LocalStack by mounting the socket file during launch.

{{< alert >}}**Note**:
The Docker backend manager for EC2 is under active development.
Please report any bugs and issues you may encounter.
{{< /alert >}}

LocalStack uses a naming scheme to recognise and manage the containers and images associated with it.
Containers are named `localstack-ec2.<InstanceId>`, while images are tagged `localstack-ec2/<AmiName>:<AmiId>`.

AWS EC2 provides a default set of AMIs from which new AMIs can be created.
By tagging an existing Docker image with a compatible name, this can be replicated within LocalStack, for example:

{{< command >}}
docker tag ubuntu:focal localstack-ec2/ubuntu-focal-ami:ami-000001
{{< /command >}}

The AMI `ami-000001` will then be available for use.

The Docker backend supports following operations:

| Operation | Notes |
|:----------|:------|
| CreateImage | Uses Docker commit to take a snapshot of a running instance into a new AMI |
| DescribeImages | Retrieve a list of Docker images available for use within LocalStack |
| DescribeInstances | Supports the `InstanceId.N` request parameter |
| RunInstances | Supports the `ImageId` and `MaxCount` request parameter |
| StopInstances | Corresponds to pausing a container. Supports the `InstanceId.N` request parameter |
| StartInstances | Corresponds to unpausing a container. Supports the `InstanceId.N` request parameter |
| TerminateInstances | Corresponds to stopping a container. Supports the `InstanceId.N` request parameter |
