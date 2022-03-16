---
title: "Elastic Compute Cloud (EC2)"
linkTitle: "Elastic Compute Cloud (EC2)"
categories: ["LocalStack Pro"]
description: AWS Elastic Compute Cloud (EC2)
---

LocalStack supports two backends for running instances locally: `virtualbox` (default) and `docker`.
Backends can be configured by setting the `EC2_VM_MANAGER` environment variable.

### VirtualBox

The VirtualBox backend requires the [Oracle VM VirtualBox](https://www.virtualbox.org/) installed on your system.

To leverage the full functionality of the EC2 VirtualBox emulation, it is necessary to run a local daemon process on the host which takes care of creating and managing the VirtualBox VM instances.
You can use the LocalStack command-line interface to start up the daemon:

{{< command >}}
$ export LOCALSTACK_API_KEY=...
$ localstack daemons start
{{< /command >}}

Depending on your host operating system, you may be asked to enter your `sudo` password.
This is required to create virtual network interfaces on the local machine with IP addresses that allow to easily SSH into the created VirtualBox instances.

The VirtualBox backend supports following operations:

| Operation | Notes |
|:----------|:------|
| RunInstances | Creates and launches a virtual machine |

### Docker

The Docker backend uses the [Docker Engine](https://docs.docker.com/engine/) to emulate EC2 instances.
All limitations that apply to containers apply to EC2 instances backed by the Docker manager, including root access and networking.
Access to the Docker socket is required which can be made available to LocalStack by mounting the socket file during launch.

Instances have the Docker socket mounted inside them, making Docker-in-Docker usecases possible.

LocalStack uses a naming scheme to recognise and manage the containers and images associated with it.
Containers are named `localstack-ec2.<InstanceId>`, while images are tagged `localstack-ec2/<AmiName>:<AmiId>`.

AWS EC2 provides a default set of AMIs from which new AMIs can be created.
This can be replicated within LocalStack by tagging an existing Docker image with a compatible name, for example:

{{< command >}}
$ docker tag ubuntu:focal localstack-ec2/ubuntu-focal-ami:ami-000001
{{< /command >}}

The AMI `ami-000001` will then be available for use.

When the LocalStack local daemon is running on the host system, LocalStack creates the necessary network configuration to allow SSH access to the container.
TODO

The Docker backend supports following operations:

| Operation | Notes |
|:----------|:------|
| CreateImage | Uses Docker commit to take a snapshot of a running instance into a new AMI |
| DescribeImages | Retrieve a list of Docker images available for use within LocalStack |
| DescribeInstances | Supports the `InstanceId.N` request parameter |
| RunInstances | Supports `ImageId`, `MaxCount`, `KeyPair` and `UserData` request parameters |
| StopInstances | Corresponds to pausing a container. Supports the `InstanceId.N` request parameter |
| StartInstances | Corresponds to unpausing a container. Supports the `InstanceId.N` request parameter |
| TerminateInstances | Corresponds to stopping a container. Supports the `InstanceId.N` request parameter |
