---
title: "Elastic Compute Cloud (EC2)"
linkTitle: "Elastic Compute Cloud (EC2)"
categories: ["LocalStack Pro"]
description: Get started with Amazon Elastic Compute Cloud (Amazon EC2) on LocalStack
aliases:
  - /aws/elastic-compute-cloud/
---

## Introduction

EC2 (Elastic Compute Cloud) is a fundamental service within Amazon Web Services (AWS) that provides scalable and flexible virtual computing resources.
EC2 enables users to effortlessly launch and manage virtual servers, commonly referred to as instances.
Users can create diverse computing environments tailored to specific needs by encompassing a wide array of configurations, enabling users to select the desired combination of computing power, memory, storage, and networking capabilities.

LocalStack supports a mock implementation of EC2 via the Community offering while a fully-emulated implementation is available in the Pro/Team offering, allowing you to use the EC2 APIs in your local environment to create and manage your EC2 instances.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_ec2/), which provides information on the extent of EC2's integration with LocalStack.

## Getting started

This guide is designed for users new to EC2 and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an EC2 instance that runs a simple Python web server on port 8000 with the AWS CLI.

{{< alert title="Note" >}}
Docker Desktop on macOS does not expose the bridge network hence SSH access to the instance is not possible.
You can however follow the steps below to test the setup of the EC2 instance.
You also need to use LocalStack Pro/Team to test the setup of the EC2 instance, since it uses [Docker backend](#docker-backend) to emulate EC2 instances.
{{< /alert >}}

### Create a Key Pair

To create a key pair, you can use the [`CreateKeyPair`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateKeyPair.html) API.
Run the following command to create the key pair and pipe the output to a file named `key.pem`:

{{< command >}}
$ awslocal ec2 create-key-pair \
    --key-name foobar \
    --query 'KeyMaterial' \
    --output text | tee key.pem
{{< /command >}}

You can assign necessary permissions to the key pair file using the following command:

{{< command >}}
$ chmod 400 key.pem
{{< /command >}}

### Add rules to your security group

Currently, LocalStack only supports the `default` security group.
You can add rules to the security group using the [`AuthorizeSecurityGroupIngress`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html) API.
Run the following command to add a rule to allow inbound traffic on port 8000:

{{< command >}}
$ awslocal ec2 authorize-security-group-ingress \
    --group-id default \
    --protocol tcp \
    --port 8000 \
    --cidr 0.0.0.0/0
{{< /command >}}

The above command will enable rules in the security group to allow incoming traffic from your local machine on port 8000 of an emulated EC2 instance.

### Run an EC2 instance

You can fetch the Security Group ID using the [`DescribeSecurityGroups`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html) API.
Run the following command to fetch the Security Group ID:

{{< command >}}
$ awslocal ec2 describe-security-groups
{{< /command >}}

You should see the following output:

```bash
{
    "SecurityGroups": [
        {
            "Description": "default VPC security group",
            "GroupName": "default",
            ...
            "OwnerId": "000000000000",
            "GroupId": "sg-0372ee3c519883079",
            ...
        }
    ]
}
```

To start your Python Web Server in your locally emulated EC2 instance, you can use the following user script by saving it to a file named `user_script.sh`:

```bash
#!/bin/bash -xeu

apt update
apt install python3 -y
python3 -m http.server 8000
```

You can now run an EC2 instance using the [`RunInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API.
Run the following command to run an EC2 instance by adding the appropriate Security Group ID that we fetched in the previous step:

{{< command >}}
$ awslocal ec2 run-instances \
    --image-id ami-ff0fea8310f3 \
    --count 1 \
    --instance-type t3.nano \
    --key-name foobar \
    --security-group-ids '<SECURITY_GROUP_ID>' \
    --user-data file://./user_script.sh
{{< /command >}}

### Test the Python Web Server

You can now open the LocalStack logs to find the IP address of the locally emulated EC2 instance.
Run the following command to open the LocalStack logs:

{{< command >}}
$ localstack logs
{{< /command >}}

You should see the following output:

```bash
2023-08-16T17:18:29.702  INFO --- [   asgi_gw_0] l.s.ec2.vmmanager.docker   : Instance i-b07acefd77a3c415f will be accessible via SSH at: 127.0.0.1:12862, 172.17.0.4:22
2023-08-16T17:18:29.702  INFO --- [   asgi_gw_0] l.s.ec2.vmmanager.docker   : Instance i-b07acefd77a3c415f port mappings (container -> host): {'8000/tcp': 29043, '22/tcp': 12862}
```

You can now use the IP address to test the Python Web Server.
Run the following command to test the Python Web Server:

{{< command >}}
$ curl 172.17.0.4:8000
{{< /command >}}

You should see the following output:

```bash
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Directory listing for /</title>
...
```

{{< alert title="Note" >}}
Similar to the setup in production AWS, the user data content is stored at `/var/lib/cloud/instances/<instance_id>/user-data.txt` within the instance.
Any execution of this data is recorded in the `/var/log/cloud-init-output.log` file.
{{< /alert >}}

### Connecting via SSH

You can also set up an SSH connection to the locally emulated EC2 instance using the instance IP address.

First, we need to create or import an SSH keypair. For example, you can use an existing SSH public key in your home directory under `~/.ssh/id_rsa.pub`:
{{< command >}}
$ awslocal ec2 import-key-pair --key-name my-key --public-key-material file://~/.ssh/id_rsa.pub
{{< /command >}}

When running the EC2 instance, make sure to pass the `--key-name` parameter to the command:
{{< command >}}
$ awslocal ec2 run-instances --key-name my-key ...
{{< /command >}}

Once the instance is up and running, we can use the `ssh` command to set up an SSH connection. Assuming the instance is available under `127.0.0.1:12862` (as per the LocalStack log output), use this command:
{{< command >}}
$ ssh -p 12862 -i ~/.ssh/id_rsa root@127.0.0.1
{{< /command >}}

## Docker backend

LocalStack Pro supports the Docker backend, enabling the execution of emulated EC2 instances.
The Docker backend employs the [Docker Engine](https://docs.docker.com/engine/) to simulate EC2 instances.
All restrictions associated with containers are also applicable to EC2 instances managed by the Docker manager.


These restrictions encompass elements like root access and networking.
In order for LocalStack to function seamlessly, access to the Docker socket is essential, which can be facilitated by attaching the socket file during the launch process.

Instances encompass the mounted Docker socket (`/var/run/docker.sock`), which facilitates scenarios involving Docker-in-Docker.
This setup makes it feasible to engage in use cases that require interactions with Docker within the instances themselves.

### Operations

The Docker backend supports the following operations:

| Operation       | Notes                                                                                        |
|:----------------|:---------------------------------------------------------------------------------------------|
| `CreateImage`   | Utilizes Docker commit to capture a snapshot of a running instance into a new AMI          |
| `DescribeImages`| Retrieves a list of Docker images available for use within LocalStack                        |
| `DescribeInstances`| Provides information about both 'mock' instances and Docker-backed instances. Docker-backed instances are marked with the resource tag `ec2_vm_manager:docker` |
| `RunInstances`  | Initiates the start of a container                                                          |
| `StopInstances` | Initiates the pause of a container                                                          |
| `StartInstances`| Initiates the resumption of a paused container                                               |
| `TerminateInstances`| Initiates the termination of a container                                                 |

### Base Images

LocalStack utilizes a specific naming convention for recognition and management of its associated containers and images.
Containers are designated with the name format `localstack-ec2.<InstanceId>`, while images are tagged using the format `localstack-ec2/<AmiName>:<AmiId>`.

Within the Docker backend, Docker images following the aforementioned naming pattern are treated as Amazon Machine Images (AMIs).
For instance, you can associate the Ubuntu Focal image as `ami-000001` using the command below:

{{< command >}}
$ docker tag ubuntu:focal localstack-ec2/ubuntu-focal-ami:ami-000001
{{< /command >}}

Such Docker-backed AMIs bear the resource tag `ec2_vm_manager:docker` and can be listed using the subsequent command:

{{< command >}}
$ awslocal ec2 describe-images --filters Name=tag:ec2_vm_manager,Values=docker
{{< /command >}}

It's important to note that all other AMIs are mocked and originate from the community edition of LocalStack.
Attempting to launch Dockerized instances using these specific AMIs will result in an `InvalidAMIID.NotFound` error.

### Configuration

You can also use the [`EC2_DOCKER_FLAGS`]({{< ref "configuration#ec2" >}}) LocalStack configuration variable to convey supplementary flags to Docker during the initiation of containerized instances.
This allows for adjustments such as commencing the container in privileged mode using `--privileged` or specifying an alternate CPU platform with `--platform`, and more.
Keep in mind that these modifications apply to all instances launched within the LocalStack session.

## Networking

{{< alert title="Note" >}}
LocalStack daemon is deprecated and will be removed in an upcoming major release.
{{< /alert >}}

LocalStack allocates distinct private IP addresses to Dockerized instances.
To make use of this feature, it's essential to run the LocalStack daemon process on the host.
This daemon process is responsible for handling the creation and administration of networking on the host system.

Before using this command, ensure you've logged in to your `localstack` CLI (using `localstack login`) via your LocalStack Web Application credentials.
To confirm, execute `localstack --help` and check if `daemons` is among the available commands.

{{< command >}}
$ pip install localstack[runtime]
$ export LOCALSTACK_API_KEY=...
$ localstack daemons start
{{< /command >}}

The SSH access address for the instance is displayed in the logs during the instance initialization process.:

```bash
2022-03-21T14:46:49.540  INFO  Instance i-1d6327abf04e31be6 will be accessible via SSH at: 127.0.0.1:55705, 172.17.0.4:22
```

The LocalStack daemon is supported on Linux and macOS operating systems.
If the LocalStack daemon is inactive, the instance can only be accessed at `127.0.0.1` along with an available port on the host.

To make additional ports available to the host system, you can modify the default security group and incorporate the needed ingress ports.
It's important to note that security group ingress rules are applied only during the creation of the Dockerized instance.
Modifying a security group will not open any ports for a running instance.

The system supports up to 32 ingress ports.
This constraint is in place to prevent the host from exhausting available ports.

{{< command >}}
$ awslocal ec2 authorize-security-group-ingress \
  --group-id default \
  --protocol tcp \
  --port 8080
$ awslocal ec2 describe-security-groups \
  --group-names default
{{< /command >}}

The port mapping details are provided in the logs during the instance initialization process.

```bash
2022-12-20T19:43:44.544  INFO  Instance i-1d6327abf04e31be6 port mappings (container -> host): {'8080/tcp': 51747, '22/tcp': 55705}
```

## Attaching EBS Block Devices to EC2 Instances

A common use case is to attach an EBS block device to an EC2 instance, which can then be used to create a custom filesystem for additional storage. This section illustrates how this functionality can be achieved with EC2 Docker instances in LocalStack.

{{< alert title="Note" >}}
This feature is disabled by default, please configure `EC2_MOUNT_BLOCK_DEVICES=1` in your LocalStack environment to enable it.
{{< /alert >}}

First, we create a user data script `init.sh` which creates an ext3 file system on the block device `/ebs-dev/sda1` and mounts it under `/ebs-mounted`:
{{< command >}}
$ cat > init.sh <<EOF
#!/bin/bash
set -eo
mkdir -p /ebs-mounted
mkfs -t ext3 /ebs-dev/sda1
mount -o loop /ebs-dev/sda1 /ebs-mounted
touch /ebs-mounted/my-test-file
EOF
{{< /command >}}

We can then start an EC2 instance, specifying a block device mapping under the device name `/ebs-dev/sda1`, and pointing to our `init.sh` user data script:
{{< command >}}
$ awslocal ec2 run-instances --image-id ami-ff0fea8310f3 --count 1 --instance-type t3.nano \
    --block-device-mapping '{"DeviceName":"/ebs-dev/sda1","Ebs":{"VolumeSize":10}}' \
    --user-data file://init.sh
{{< /command >}}

Please note that, whereas real AWS uses GB for volume sizes, we use MB as the unit for `VolumeSize` in the command above (to avoid creating huge files locally). Also, by default block device images are limited to 1GB in size, but this can be customized by setting the `EC2_EBS_MAX_VOLUME_SIZE` config variable (defaults to `1000`).

Once the instance is successfully started and initialized, we can first determine the container ID via `docker ps`, and then list the contents of the mounted filesystem `/ebs-mounted`, which should contain our test file named `my-test-file`:
{{< command >}}
$ docker ps
CONTAINER ID   IMAGE                  PORTS           NAMES
5c60cf72d84a   ...:ami-ff0fea8310f3   19419->22/tcp   localstack-ec2...
$ docker exec 5c60cf72d84a ls /ebs-mounted
my-test-file
{{< /command >}}

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing EC2 instances.
You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **EC2** under the **Compute** section.

<img src="ec2-resource-browser.png" alt="EC2 Resource Browser" title="EC2 Resource Browser" width="900" />
<br>
<br>

The Resource Browser allows you to perform the following actions:
- **Create Instance**: Create a new EC2 instance by clicking the **Launch Instance** button and specifying the AMI ID, instance type, and other parameters.
- **View Instance**: View the details of an EC2 instance by clicking on the Instance ID.
- **Terminate Instance**: Terminate an EC2 instance by selecting the Instance ID, and clicking on the **ACTIONS** button followed by clicking on **Terminate Selected**.
- **Start Instance**: Start a stopped EC2 instance by selecting the Instance ID, and clicking on the **ACTIONS** button followed by clicking on **Start Selected**.
- **Stop Instance**: Stop a running EC2 instance by selecting the Instance ID, and clicking on the **ACTIONS** button followed by clicking on **Stop Selected**.
