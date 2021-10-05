---
title: "Getting Started"
linkTitle: "🚀 Getting Started"
weight: 2
description: >
  How to get up to speed with LocalStack.
---

[LocalStack](https://localstack.cloud) is a cloud service emulator that runs in a single container on your laptop or in your CI environment.
With LocalStack, you can run your AWS applications or Lambdas entirely on your local machine without connecting to a remote cloud provider!
Whether you are testing complex CDK applications or Terraform configurations, or just beginning to learn about AWS services,
LocalStack helps speed up and simplify your testing and development workflow.

LocalStack supports a growing number of [AWS services]({{< ref "Local AWS Services" >}}), like AWS Lambda, [S3]({{< ref "s3" >}}), DynamoDB, [Kinesis]({{< ref "kinesis" >}}), [SQS]({{< ref "sqs" >}}), SNS, and **many** more!
The [**Pro version** of LocalStack](https://localstack.cloud/pricing) supports additional APIs and advanced features.
You can find a comprehensive list of supported APIs on our [⭐ Feature Coverage]({{< ref "feature-coverage" >}}) page.

LocalStack also provides additional features to make your life as a cloud developer easier!
Check out LocalStack's [Cloud Developer Tools]({{< ref "LocalStack Tools" >}}).

## Get LocalStack Up and Running
The first thing when getting started with LocalStack is to choose your preferred way of starting and managing your LocalStack instance.\
LocalStack currently provides the following options:
- [LocalStack CLI]({{< ref "#localstack-cli" >}})\
  The easiest way to start and manage LocalStack - either on your machine, in a Docker container on your machine, or even on a remote Docker host.

- [Docker]({{< ref "#docker" >}})\
  Use the `docker` CLI to manually start the LocalStack Docker container.

- [Docker-Compose]({{< ref "#docker-compose" >}})\
  Use `docker-compose` to configure and start your LocalStack Docker container.

- [Helm]({{< ref "#helm" >}})\
  Use `helm` to create a LocalStack deployment in a Kubernetes cluster.


### LocalStack CLI
The LocalStack CLI aims to simplify starting and managing LocalStack.
It provides convenience features to start LocalStack on your local machine, as a Docker container on your machine, or even on a remote Docker host.
In addition you can easily check the status or open a shell in your LocalStack instance if you want to take a deep-dive.

#### Prerequisites
Please make sure to install the following tools on your machine before moving on:
- [`python`](https://docs.python.org/3/using/index.html) (Python 3.6 up to 3.9 is supported)
- [`pip`](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- [`docker`](https://docs.docker.com/get-docker/)

#### Installation
The easiest way to install the LocalStack CLI is via `pip`:

```sh
python3 -m pip install localstack
```

{{< alert >}}
**Note**: Please do **not** use `sudo` or the `root` user - LocalStack should be installed and started entirely under a local non-root user. 
If you have problems with permissions in MacOS X Sierra, install with `python3 -m pip install --user localstack`.
{{< /alert >}}

Afterwards you should be able to use the LocalStack CLI in your terminal:
```
$ localstack --help
Usage: localstack [OPTIONS] COMMAND [ARGS]...

  The LocalStack Command Line Interface (CLI)

Options:
...
```

#### Troubleshooting
##### The installation is successful, but I cannot execute `localstack` on my terminal.
If you can successfully install LocalStack using `pip` but you cannot use it in your terminal, you most likely haven't set up your operating system's / terminal's `PATH` variable (in order to tell them where to find programs installed via `pip`).
- If you are using Windows, you can enable the `PATH` configuration when installing Python, [as described in the official docs of Python](https://docs.python.org/3/using/windows.html#finding-the-python-executable).
- If you are using a MacOS or Linux operating system, please make sure that the `PATH` is correctly set up - either system wide, or in your terminal.

As a workaround you can call the LocalStack CLI python module directly:
```sh
python3 -m localstack.cli.main
```

#### Starting LocalStack with the LocalStack CLI
By default, LocalStack is started inside a Docker container by running:

```sh
localstack start
```

{{< alert title="Notes" >}}
- This command starts all services provided by LocalStack.
  You can limit the services to a subset by setting the environment variable `SERVICES` (for example with `SERVICES="dynamodb,s3" localstack start`).

- By default, LocalStack uses the image tagged `latest` that is cached on your machine, and will **not** pull the latest image automatically from Docker Hub (i.e., the image needs to be pulled manually if needed).

- On MacOS you may have to run `TMPDIR=/private$TMPDIR localstack start --docker` if `$TMPDIR` contains a symbolic link that cannot be mounted by Docker.

- From 2020-07-11 onwards, the default image `localstack/localstack` in Docker Hub refers to the "light version", which has some large dependency files like Elasticsearch removed (and lazily downloads them, if required). (Note that the `localstack/localstack-light` image alias may get removed in the future). In case you need the full set of dependencies, the `localstack/localstack-full` image can be used instead. Please also refer to the [`USE_LIGHT_IMAGE` environment variable]({{< ref "configuration#core" >}}).

- Although we strongly recommend to use Docker, the infrastructure can also be spun up directly on the host machine using the `--host` startup flag. Note that this will require [additional dependencies]({{< ref "#developing" >}}), and is not supported on some operating systems, including Windows.
{{< /alert >}}

### Docker
If you do not want to use the [LocalStack CLI]({{< ref "#localstack-cli" >}}), you can also decide to manually start the LocalStack Docker container.

#### Prerequisites
Please make sure that you have a working [`docker` environment](https://docs.docker.com/get-docker/) on your machine before moving on.
You can check if `docker` is correctly configured on your machine by executing `docker info` in your terminal. If it does not report an error (but shows information on your Docker system), you're good to go.

#### Starting LocalStack with Docker
You can start the Docker container simply by executing the following `docker run` command:
```
docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack
```

{{< alert title="Notes" >}}
- This command pulls the current nighty build from the `master` branch (if you don't have the image locally) and **not** the latest supported version.
  If you want to use a specific version, use the appropriate tag (for example `localstack/localstack:0.12.18`).

- This command reuses the image if it's already on your machine, i.e. it will **not** pull the latest image automatically from Docker Hub.

- This command does not bind all ports which are potentially used by LocalStack, nor does it mount any volumes.
  When using Docker to manually start LocalStack, you will have to configure the container on your own.
  This could be seen as the "expert mode" of starting LocalStack.
  If you are looking for a simpler method of starting LocalStack, please use the [LocalStack CLI]({{< ref "#localstack-cli" >}}).

- This command starts all services provided by LocalStack.
  You can limit the services to a subset by setting the environment variable `SERVICES` (for example with `-e "SERVICES=dynamodb,s3"`).

- To facilitate interoperability, configuration variables can be prefixed with `LOCALSTACK_` in docker. For instance, setting `LOCALSTACK_SERVICES=s3` is equivalent to `SERVICES=s3`.
{{< /alert >}}

### Docker-Compose
If you want to manually manage your Docker container, it's usually a good idea to use [`docker-compose`](https://docs.docker.com/compose/reference/) in order to simplify your container configuration.

#### Prerequisites
- [`docker`](https://docs.docker.com/get-docker/)
- [`docker-compose`](https://docs.docker.com/compose/install/) (version 1.9.0+)

#### Starting LocalStack with Docker-Compose
You can use the [`docker-compose.yml` file from the official LocalStack repository](https://github.com/localstack/localstack/blob/master/docker-compose.yml) and use this command (currently requires `docker-compose` version 1.9.0+):

```
docker-compose up
```

{{< alert title="Notes" >}}
- This command pulls the current nighty build from the `master` branch (if you don't have the image locally) and **not** the latest supported version.
  If you want to use a specific version, use the appropriate tag (for example `localstack/localstack:0.12.18`).

- This command reuses the image if it's already on your machine, i.e. it will **not** pull the latest image automatically from Docker Hub.

- On MacOS you may have to run `TMPDIR=/private$TMPDIR docker-compose up` if `$TMPDIR` contains a symbolic link that cannot be mounted by Docker.

- To facilitate interoperability, configuration variables can be prefixed with `LOCALSTACK_` in docker. For instance, setting `LOCALSTACK_SERVICES=s3` is equivalent to `SERVICES=s3`.
{{< /alert >}}

### Helm
If you want to deply LocalStack in your [Kubernetes](https://kubernetes.io) cluster, you can use [Helm](https://helm.sh).

#### Prerequisites
- [Kubernetes](https://kubernetes.io)
- [Helm](https://helm.sh/docs/intro/install/)

#### Deploy LocalStack using Helm
You can deploy LocalStack in a Kubernetes cluster by running these commands:
```sh
helm repo add localstack-repo https://helm.localstack.cloud
helm upgrade --install localstack localstack-repo/localstack
```

The Helm charts are not maintained in the main repository, but in a [separate one](https://github.com/localstack/helm-charts).

## Ran into trouble?
We strive to make it as easy as possible for you to use LocalStack, and we are very grateful for any feedback.
If you run into any issues or problems with this guide, please [submit an issue](https://github.com/localstack/docs/issues). 

## What's next?
Now that you have LocalStack up and running, the following resources might be useful for your next steps:
- [Use the LocalStack integrations]({{< ref "integrations" >}}) to interact with LocalStack and other integrated tools, for example:
  - Use `awslocal` to use the AWS CLI against your local cloud!
  - Use the Serverless Framework with LocalStack!
  - And many more!
- [Find out how to configure LocalStack]({{< ref "configuration" >}}) such that it perfectly fits your need.
- [Use LocalStack in your CI environment]({{< ref "LocalStack in CI" >}}) to increase your code quality.
- [Checkout LocalStack's Cloud Developer Tools]({{< ref "LocalStack Tools" >}}) to further increase your development efficiency with LocalStack.