---
title: "AWS Command Line Interface"
weight: 2
description: >
  How to use the AWS Command Line Interface (CLI) with LocalStack.
aliases:
  - /integrations/aws-cli/
---

## Overview

The [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/) is a unified tool to manage AWS services from the command line.
All CLI commands that access [services that are implemented in LocalStack]({{< ref "feature-coverage" >}}) can be run against LocalStack.

There are two CLI alternatives:

* [AWS CLI]({{<ref "#aws-cli" >}})
* [LocalStack AWS CLI]({{<ref "#localstack-aws-cli-awslocal">}})

## AWS CLI

Use the below command to install `aws`, if not installed already.

{{< command >}}
$ pip install awscli
{{< / command >}}

### Setting up local region and credentials to run LocalStack

Configure AWS test environment variables and add the `--endpoint-url=<localstack-url>` flag to your `aws` CLI invocations.
For example:
{{< command >}}
$ export AWS_ACCESS_KEY_ID="test"
$ export AWS_SECRET_ACCESS_KEY="test"
$ export AWS_DEFAULT_REGION="us-east-1"

$ aws --endpoint-url=http://localhost:4566 kinesis list-streams
{{< / command >}}

Create a configuration profile. The configuration file will be created under `~/.aws` directory and in the example below, using the `default` profile:

{{< command >}}
$ aws configure --profile default
{{< / command >}}

{{< alert title="Note">}}
Please use `test` as value for `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to make pre-signed URLs for S3 buckets work.
Our pre-signed URL signature verification algorithm validates the pre-signed URL and its expiration.
{{< /alert >}}

Verify the current configuration:

{{< command >}}
aws configure list
{{< / command >}}

## LocalStack AWS CLI (awslocal)

`awslocal` is a thin wrapper and a drop-in replacement for the `aws` command that runs commands directly against LocalStack (no need to specify `--endpoint-url` anymore).
The source code can be found on GitHub: https://github.com/localstack/awscli-local


### Installation

You can install the `awslocal` command via `pip`:

{{< command >}}
$ pip install awscli-local[ver1]
{{< / command >}}

Note that the command above also installs the latest version of the underlying AWS CLI version 1 (`awscli`) package. Use this command if you prefer to manage your own version of `awscli` (e.g., `v1`/`v2`) and install the wrapper script only:
{{< command >}}
$ pip install awscli-local
{{< / command >}}

{{< alert title="Note" >}}
Automatic installation of AWS CLI version 2 is currently not supported yet (at the time of writing there is no official pypi package for `v2` available), but the `awslocal` technically also works with AWS CLI v2 (see [this section]({{< ref "#limitations" >}}) for more details).
{{< /alert >}}

### Usage

The `awslocal` command has the same usage as the `aws` command.
For detailed usage, please refer to the man pages of `aws help`.

{{< command >}}
awslocal kinesis list-streams
{{< / command >}}

### Configurations

You can use the following environment variables for configuration:

| Variable | Description |
| -------- | ----------- |
| `LOCALSTACK_HOST` | Set the hostname for the localstack instance. Useful when you have localstack is bound to another interface (i.e. docker-machine). |
| `USE_SSL` | Whether to use `https` endpoint URLs (required if LocalStack has been started with `USE_SSL=true` enabled). Defaults to `false`. |
| `DEFAULT_REGION` | *Deprecated*. Set the default region. Overrides `AWS_DEFAULT_REGION` environment variable. |

Verify the current configuration:

{{< command >}}
awslocal configure list
{{< / command >}}


### Limitations

Please note that there is a known limitation for using the `cloudformation package ...` command with the AWS CLI v2.
The problem is that the AWS CLI v2 is [not available as a package on pypi.org](https://github.com/aws/aws-cli/issues/4947), but is instead shipped as a binary package that cannot be easily patched from `awslocal`.
To work around this issue, you have 2 options:
- Downgrade to the v1 AWS CLI (this is the recommended approach)
- There is an unofficial way to install AWS CLI v2 from sources.
  We do not recommend this, but it is technically possible.
  Also, you should install these libraries in a Python virtualenv, to avoid version clashes with other libraries on your system:

{{< command >}}
$ virtualenv .venv
$ . .venv/bin/activate
$ pip install https://github.com/boto/botocore/archive/v2.zip https://github.com/aws/aws-cli/archive/v2.zip
{{< / command >}}

Please also note there is a known limitation for issuing requests using
`--no-sign-request` with the AWS CLI. LocalStack's routing mechanism depends on
the signature of each request to identify the correct service for the request.
Thus, adding the flag `--no-sign-requests` provokes your request to reach the
wrong service. One possible way to address this is to use the `awslocal` CLI
instead of AWS CLI.

## AWS CLI v2

Automatic installation of AWS CLI version 2 is currently not supported (at the time of writing there is no official pypi package for v2 available), but the awslocal technically also works with AWS CLI v2 (see this section for more details).

### AWS CLI v2 with Docker and LocalStack

By default, the container running [amazon/aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-docker.html) is isolated from `0.0.0.0:4566` on the host machine, that means that aws-cli cannot reach localstack through your shell.

To ensure that the two docker containers can communicate create a network on the docker engine:

{{< command >}}
$ docker network create localstack
0c9cb3d37b0ea1bfeb6b77ade0ce5525e33c7929d69f49c3e5ed0af457bdf123
{{< / command >}}

Then modify the `docker-compose.yml` specifying the network to use:

```yaml
networks:
  default:
    external:
      name: "localstack"
```

Run AWS Cli v2 docker container using this network (example):

{{< command >}}
$ docker run --network localstack --rm -it amazon/aws-cli --endpoint-url=http://localstack:4566 lambda list-functions
{
    "Functions": []
}
{{< / command >}}

If you use AWS CLI v2 from a docker container often, create an alias:

{{< command >}}
$ alias laws='docker run --network localstack --rm -it amazon/aws-cli --endpoint-url=http://localstack:4566'
{{< / command >}}

So you can type:

{{< command >}}
$ laws lambda list-functions
{
    "Functions": []
}
{{< / command >}}
