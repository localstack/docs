---
title: "Elastic Compute Cloud (EC2)"
linkTitle: "Elastic Compute Cloud (EC2)"
categories: ["LocalStack Pro"]
description: Get started with Amazon Elastic Compute Cloud (Amazon EC2) on LocalStack
aliases:
  - /aws/elastic-compute-cloud/
---

LocalStack Pro supports the Docker backend for running instances.

The Docker backend uses the [Docker Engine](https://docs.docker.com/engine/) to emulate EC2 instances.
All limitations that apply to containers apply to EC2 instances backed by the Docker manager, including root access and networking.
Access to the Docker socket is required which can be made available to LocalStack by mounting the socket file during launch.

Instances have the Docker socket (`/var/run/docker.sock`) mounted inside them, making Docker-in-Docker use cases possible.


## Base Images

LocalStack uses a naming scheme to recognise and manage the containers and images associated with it.
Containers are named `localstack-ec2.<InstanceId>`, while images are tagged `localstack-ec2/<AmiName>:<AmiId>`.

The Docker backend treats Docker images with the above naming scheme as AMIs.
For example, the following command can be used to associate the Ubuntu Focal image as `ami-000001`.

{{< command >}}
$ docker tag ubuntu:focal localstack-ec2/ubuntu-focal-ami:ami-000001
{{< /command >}}

These Docker-backed AMIs have the resource tag `ec2_vm_manager:docker` and can be listed with the following command:

{{< command >}}
$ awslocal ec2 describe-images --filters Name=tag:ec2_vm_manager,Values=docker
{{< /command >}}

All other AMIs are 'mocked' and are based off the community edition of LocalStack.
Attempting to launch Dockerised instances with these AMIs will return `InvalidAMIID.NotFound` error.


## Networking

LocalStack supports assignment of unique private IP addresses for Dockerised instances.
To leverage this feature, it is necessary to run the LocalStack daemon process on the host which takes care of creating and managing networking on the host system.

Make sure this command is available, by first logging in using `localstack login` with your Pro credentials (the same ones used for <https://app.localstack.cloud>).
To verify this, use `localstack --help` and check if `daemons` is part of the command list.

{{< command >}}
$ pip install localstack[runtime]
$ export LOCALSTACK_API_KEY=...
$ localstack daemons start
{{< /command >}}

The address for SSH access to the instance is printed in the logs when the instance is initialised.

```plaintext
2022-03-21T14:46:49.540  INFO  Instance i-1d6327abf04e31be6 will be accessible via SSH at: 127.0.0.1:55705, 172.17.0.4:22
```

The LocalStack daemon is supported on Linux and MacOS.

If the LocalStack daemon is not running, the instance will be only accessible at `127.0.0.1` and an available port on the host.

To expose additional ports to the host system, update the default security group and add the required ingress ports.
Security group ingress rules are only applied to the Dockerised instance at the time of creating.
Updating a security group will not open any ports of a running instance.

Up to 32 ingress ports are supported.
This limitation exists to prevent the host from running out of free ports.

{{< command >}}
$ awslocal ec2 authorize-security-group-ingress --group-id default --protocol tcp --port 8080
$ awslocal ec2 describe-security-groups --group-names default
{{< /command >}}

The port mapping is printed in the logs as when the instance is intialised.

```plaintext
2022-12-20T19:43:44.544  INFO  Instance i-1d6327abf04e31be6 port mappings (container -> host): {'8080/tcp': 51747, '22/tcp': 55705}
```


## Key pairs

You can specify a key pair at startup and LocalStack will copy it into the container and enable it for SSH authentication.

{{< command >}}
$ awslocal ec2 create-key-pair --key-name alice
$ awslocal ec2 run-instances --image-id ami-df5de72bdb3b --key-name alice
{{< /command >}}


## User data

It is possible to run commands on a instance at startup using [user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html).
The script can be passed to the `UserData` argument of `RunInstances` operation.

{{< command >}}
$ awslocal ec2 run-instances --image-id ami-df5de72bdb3b --user-data '#!/bin/bash
    whoami | tee /myname && echo localstack; echo "not printed">/dev/null;'
{{< /command >}}

Like production AWS, the contents of user data is saved at `/var/lib/cloud/instances/<instance_id>/user-data.txt` on the instance.
Its execution is logged at `/var/log/cloud-init-output.log`.


## Passing additional flags to Docker

Use the [`EC2_DOCKER_FLAGS`]({{< ref "configuration#ec2" >}}) LocalStack configuration variable to pass additional flags to Docker when starting containerised instances.
For example, this can be used to start the container in privileged mode with `--privileged`, or use a different CPU platform with `--platform`, etc.
Note that this affects all instances that are launched in the LocalStack session.


## Operations

The Docker backend supports following operations:

| Operation | Notes |
|:----------|:------|
| CreateImage | Uses Docker commit to take a snapshot of a running instance into a new AMI |
| DescribeImages | Retrieve a list of Docker images available for use within LocalStack |
| DescribeInstances | Describe 'mock' instances as well as Docker-backed instances. Docker-backed instances have the resource tag `ec2_vm_manager:docker` |
| RunInstances | Corresponds to starting a container |
| StopInstances | Corresponds to pausing a container |
| StartInstances | Corresponds to unpausing a container |
| TerminateInstances | Corresponds to stopping a container |
