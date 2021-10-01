---
title: "AWS Command Line Interface"
weight: 2
description: >
  How to use the AWS Command Line Interface (CLI) with LocalStack.
---

## Overview

The [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/) is a unified tool to manage AWS services from the command line.
All CLI commands that access [services that are implemented in LocalStack]({{< ref "feature-coverage" >}}) can be run against LocalStack.

There are two ways to use the CLI:

* Use our `awslocal` drop-in replacement:
  ```
  awslocal kinesis list-streams
  ```
* Configure AWS test environment variables and add the `--endpoint-url=<localstack-url>` flag to your `aws` CLI invocations.
  For example:
  ```
  export AWS_ACCESS_KEY_ID="test"
  export AWS_SECRET_ACCESS_KEY="test"
  export AWS_DEFAULT_REGION="us-east-1"

  aws --endpoint-url=http://localhost:4566 kinesis list-streams
  ```

## LocalStack AWS CLI (awslocal)

`awslocal` is a thin wrapper and a drop-in replacement for the `aws` command.
The source code can be found on GitHub: https://github.com/localstack/awscli-local


### Installation

You can install the `awslocal` command via `pip`:

```
pip install awscli-local[ver1]
```

Note that the command above also installs the latest version of the underlying AWS CLI version 1 (`awscli`) package. Use this command if you prefer to manage your own version of `awscli` (e.g., `v1`/`v2`) and install the wrapper script only:
```
pip install awscli-local
```

{{< alert >}}
**Note:** Automatic installation of AWS CLI version 2 is currently not supported yet (at the time of writing there is no official pypi package for `v2` available), but the `awslocal` technically also works with AWS CLI v2 (see [this section](#limitations) for more details).
{{< /alert >}}

### Usage

The `awslocal` command has the same usage as the `aws` command.
For detailed usage, please refer to the man pages of `aws help`.


### Configurations

You can use the following environment variables for configuration:

| Variable | Description |
| -------- | ----------- |
| `LOCALSTACK_HOST` | Set the hostname for the localstack instance. Useful when you have localstack is bound to another interface (i.e. docker-machine). |
| `USE_SSL` | Whether to use `https` endpoint URLs (required if LocalStack has been started with `USE_SSL=true` enabled). Defaults to `false`. |
| `DEFAULT_REGION` | Set the default region. Overrides `AWS_DEFAULT_REGION` environment variable. |

### Limitations

Please note that there is a known limitation for using the `cloudformation package ...` command with the AWS CLI v2.
The problem is that the AWS CLI v2 is [not available as a package on pypi.org](https://github.com/aws/aws-cli/issues/4947), but is instead shipped as a binary package that cannot be easily patched from `awslocal`.
To work around this issue, you have 2 options:
- Downgrade to the v1 AWS CLI (this is the recommended approach)
- There is an inofficial way to install AWS CLI v2 from sources.
  We do not recommend this, but it is technically possible.
  Also, you should install these libraries in a Python virtualenv, to avoid version clashes with other libraries on your system:

```bash
virtualenv .venv
. .venv/bin/activate
pip install https://github.com/boto/botocore/archive/v2.zip https://github.com/aws/aws-cli/archive/v2.zip
```

### AWS CLI v2

Automatic installation of AWS CLI version 2 is currently not supported yet (at the time of writing there is no official pypi package for v2 available), but the awslocal technically also works with AWS CLI v2 (see this section for more details).
