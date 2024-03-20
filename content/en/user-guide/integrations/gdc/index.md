---
title: "Generic Development Container"
linkTitle: "Generic Development Container"
description: >
  Use the Generic Development Container to develop in a containerized environment with LocalStack.
---

## Introduction

[Generic Development Container (GDC)](https://github.com/devxpod/GDC) allows you to manage diverse development environments. GDC works across Windows, macOS, and Linux, supporting various programming languages like Node, Java, and Python. GDC simplifies cloud identity management in AWS and uses Docker to provide ready-to-use development setups.

GDC offers first-class support and integration with LocalStack. You can use GDC to develop and test your application locally with LocalStack, and pre-configure various dependencies like AWS CLI, AWS CDK, Terraform, Pulumi, and more. GDC's internal configuration enables shared DNS between LocalStack and the Development Container, which will use LocalStack's DNS server. In addition, you can customize how LocalStack is started and configured.

## Configuration

GDC allows users to work with their preferred IDE or shell on their workstation, known as the **host**. Containers connect on a virtual network and are run next to each other, not within each other. Development containers can forward internal ports to the host, allowing the use of tools and browsers directly on the host machine to interact with services inside the containers.

To use LocalStack with GDC, install Generic Development Container on your workstation. You can find installation instructions in the [GDC documentation](https://github.com/devxpod/GDC?tab=readme-ov-file#install-required-tools).

Create a new file named `.env-gdc` in the root of your project direct. Add the following content to the file:

```bash
export AWS_REGION=us-east-1
export GDC_NAME=lappc
export LS_VERSION=latest
export LS_IMAGE=localstack/localstack-pro # use localstack/localstack if you are using LocalStack Community
export USE_LOCALSTACK=yes
export USE_LOCALSTACK_HOST=yes
export USE_LOCALSTACK_PERSISTENCE=no
export USE_LOCALSTACK_DNS=yes # Configure the dev container to use LocalStack for DNS
export LOCALSTACK_HOST_DNS_PORT="" # this makes LocalStack not map port 53 the host
export USE_PRECOMMIT=no
```

If you're using LocalStack Pro, create a file called `.env-gdc-local` and put your `LOCALSTACK_API_KEY` or `LOCALSTACK_AUTH_TOKEN` in it:

```bash
export LOCALSTACK_API_KEY="<your real key>"
# or
export LOCALSTACK_AUTH_TOKEN="<your real token>"
```

You can run your development container with the following command:

{{< command >}}
$ run-dev-container.sh
{{< /command >}}

## Aliases & Commands

You can use `awsl` to run AWS CLI commands against LocalStack. For example, to list all S3 buckets, run:

{{< command >}}
$ awsl s3 ls
{{< /command >}}

You have the following commands available to interact with LocalStack in the development container:

| Script        | Option          | Description                                                             |
| ------------- | --------------- | ----------------------------------------------------------------------- |
| `start-ls.sh` | `-h`, `host`, `internal` | Start LocalStack container in specified mode. Autodetects if not specified. |
| `stop-ls.sh`  | `-h`, `host`, `internal` | Stops LocalStack container in specified mode. Autodetects if not specified.  |

## Environment Variables

| Key                           | Description                                                                                                             | Example Values |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------- |
| `USE_LOCALSTACK`              | Enables LocalStack helpers.                                                                                  | yes            |
| `USE_LOCALSTACK_PRO`          | Enables LocalStack Pro API Keys / Auth tokens.                                                                             | yes            |
| `USE_LOCALSTACK_PERSISTENCE`  | Toggle persistent storage for LocalStack defaults to persistence disabled.                                         | no             |
| `LOCALSTACK_VOLUME_DIR`       |            Lorem                                                                                |    `$HOST_PROJECT_PATH/ls_volume`            |
| `LOCALSTACK_API_KEY`          | Specify the LocalStack API Key                                                                                       |                |
| `LOCALSTACK_AUTH_TOKEN`       | Specify the LocalStack Auth Token                                                                           |                |
| `LS_IMAGE`                    | Specify the LocalStack image |    `localstack/localstack`. If `LOCALSTACK_API_KEY` or `LOCALSTACK_AUTH_TOKEN` is specified, it defaults to `localstack/localstack-pro`.   |
| `LS_VERSION`                  | Starts a LocalStack container running specified version.                                                              |    `3.0.0`            |
| `USE_LOCALSTACK_HOST`         | Forwards LocalStack ports to host if `LS_VERSION` is set.                                                           | yes            |
| `USE_LOCALSTACK_SHARED`       | Mount GDC shared volume in LocalStack container under /shared.                                                     | no             |
| `USE_LOCALSTACK_DNS`          | Assigns static IP to LocalStack container and sets GDC to use its DNS.                                             | no             |
| `LOCALSTACK_STATIC_IP`        | Sets a static IP for LocalStack container if set. This will be auto set if not specified and `USE_LOCALSTACK_DNS=yes` is configured.      |                |
| `LOCALSTACK_HOST_DNS_PORT`    | When LocalStack is running in host mode, forward this port from host to LocalStack. Set to blank string to disable LocalStack DNS forward. | 53             |
