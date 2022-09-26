---
title: "Development Environment Setup"
weight: 4
description: >
  Set up your development environment for developing LocalStack.
---

{{% alert %}}
**Note:** We have recently added a couple of refactorings and enhancements in the core framework and application architecture, hence this page is no longer fully up to date. We're planning to publish an updated version soon.
{{% /alert %}}

Before you get started with contributing to LocalStack, make sure you’ve familiarized yourself with LocalStack from the perspective of a user. You can follow our [getting started guide](https://docs.localstack.cloud/get-started/). Once LocalStack runs in your Docker environment and you’ve played around with the LocalStack and `awslocal` CLI, you can move forward to set up your developer environment.

## Development requirements

You will need the following tools for the local development of LocalStack.

* [Python 3.10+](https://www.python.org/downloads/)
* [Sasl](https://packages.debian.org/buster/libsasl2-2)
* `pip`
* [`virtualenv`](https://pypi.org/project/virtualenv/)
* [OpenJDK](https://openjdk.org/install/)
* [NodeJS & npm](https://nodejs.org/en/download/)
* [Maven](https://maven.apache.org/download.cgi)
* [Gradle](https://gradle.org/install/)
* [Terraform](https://www.terraform.io/downloads)
* [Docker](https://docs.docker.com/desktop/)
* [Docker-Compose](https://docs.docker.com/compose/install/)

We recommend you to individually install the above tools using your favorite package manager. For example, on macOS, you can use [Homebrew](https://brew.sh/) to install the above tools.

### Setting up Development Environment

To make contributions to LocalStack, you need to be able to run LocalStack in host mode from your IDE, and be able to attach a debugger to the running LocalStack instance. We have a basic tutorial to cover how you can do that.

The basic steps include:

*   Clone the localstack repository, and optionally our fork of `moto`:
    -   [https://github.com/localstack/localstack/](https://github.com/localstack/localstack/)
    -   [https://github.com/localstack/moto](https://github.com/localstack/moto)
*   Make sure you have `javac`, `node`, `npm`, and Python 3.10 installed.
*   Most of the contributors use the free community version [PyCharm](https://www.jetbrains.com/pycharm/).

{{< youtube XHLBy6VKuCM >}}

If you pull the repo in order to extend/modify LocalStack, run this command to install all the dependencies:

{{< command >}}
$ make install
{{< /command >}}

This will install the required pip dependencies in a local Python `virtualenv` directory `.venv` (your global python packages will remain untouched), as well as some node modules in `./localstack/node_modules/`. Depending on your system, some `pip`/`npm` modules may require additional native libs installed.

The Makefile contains a start command to conveniently start:

{{< command >}}
$ make start
{{< / command >}}

### Host mode

Although we strongly recommend to use Docker, the infrastructure can also be spun up directly on the host machine using the `--host` startup flag. Note that this will require additional dependencies, and is not supported on some operating systems, including Windows.

{{< command >}}
$ localstack start --host
{{< / command >}}

LocalStack will attempt to automatically fetch the missing dependencies when you first start it up in `host` mode; Alternatively, you can use the full profile to install all dependencies at `pip` installation time:

{{< command >}}
$ pip install "localstack[full]"
{{< / command >}}

### Building the Docker image for Development

Please note that there are a few commands we need to run on the host to prepare the local environment for the Docker build - specifically, downloading some dependencies like the StepFunctions local binary. Therefore, simply running `docker build .` in a fresh clone of the repo may not work.

We generally recommend using this command to build the Docker image locally (works on Linux/MacOS):

{{< command >}}
$ make docker-build
{{< / command >}}

### Tips

* If `virtualenv` chooses system python installations before your pyenv installations, manually initialize `virtualenv` before running `make install`: `virtualenv -p ~/.pyenv/shims/python3.10 .venv` .
* Terraform needs version <0.14 to work currently. Use `tfenv` (<https://github.com/tfutils/tfenv>) to manage terraform versions comfortable. Quick start: `tfenv install 0.13.7 && tfenv use 0.13.7`
* Set env variable `LS_LOG='trace'` to print every `http` request sent to localstack and their responses. It is useful for debugging certain issues.
* As per dev guide, it requires `libsasl2-dev`. The Arch based Distro equivalent is `libsasl`.
