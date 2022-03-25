---
title: "Setup and requirements"
weight: 4
description: >
  Set up your development environment for developing LocalStack.
---

{{% alert %}}
**Note:** We have recently added a couple of refactorings and enhancements in the core framework and application architecture, hence this page is no longer fully up to date. We're planning to publish an updated version soon.
{{% /alert %}}

## Development requirements

You will need the following tools for local development of LocalStack.

* Python 3.7+
* Sasl
* Pip
* Virtualenv
* OpenJDK
* Node & npm
* Maven
* Gradle
* Terraform
* Docker
* Docker-Compose


### Installation instructions

Below are some basic installation instructions for the dependencies you will need (assuming you're on Debian/Ubuntu Linux).

* Python 3.7+
  ```bash
  update-alternatives --install /usr/bin/python python /usr/bin/python3.8 2
  ```
* Sasl
  ```bash
  apt install libsasl2-dev
  ```
* Pip
  ```bash
  apt-get install python3-pip
  update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 2
  ```
* Virtualenv
  ```bash
    pip install virtualenv
  ```
* OpenJDK
  ```bash
    apt-get install openjdk-11-jdk
  ```
* Node
  ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    apt-get install -y nodejs
  ```
* Maven
  ```bash
  wget https://mirrors.estointernet.in/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.zip -O /opt/apache-maven-3.6.3-bin.zip
  unzip /opt/apache-maven-3.6.3-bin.zip -d /opt/
  ```
* Gradle
  ```bash
  wget https://services.gradle.org/distributions/gradle-6.7-bin.zip -O /opt/gradle-6.7-bin.zip
  unzip /opt/gradle-6.7-bin.zip -d /opt/
  ```
* Terraform
  ```bash
  curl -L -o /opt/terraform/terraform.zip https://releases.hashicorp.com/terraform/0.13.4/terraform_0.13.4_linux_amd64.zip
  (cd /opt/terraform && unzip -q /opt/terraform/terraform.zip && rm /opt/terraform/terraform.zip)
  ```
* Adding Environment variable
  ```bash
  echo "PATH=$PATH:/opt/apache-maven-3.6.3/bin:/opt/gradle-6.7/bin:/opt/terraform" >> ~/.bashrc && source ~/.bashrc
  ```
* Docker
  ```bash
  curl -sSLk https://get.docker.com | bash -
  ```
* Docker-Compose
  ```bash
  sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
  ```

### Development Environment

If you pull the repo in order to extend/modify LocalStack, run this command to install all the dependencies:

```
make install
```

This will install the required pip dependencies in a local Python virtualenv directory `.venv` (your global python packages will remain untouched), as well as some node modules in `./localstack/node_modules/`. Depending on your system, some pip/npm modules may require additional native libs installed.

The Makefile contains a start command to conveniently start:

```
make start
```

### Building the Docker image for Development

Please note that there are a few commands we need to run on the host to prepare the local environment for the Docker build - specifically, downloading some dependencies like the StepFunctions local binary. Therefore, simply running `docker build .` in a fresh clone of the repo may not work.

We generally recommend using this command to build the Docker image locally (works on Linux/MacOS):

```
make docker-build
```

### Tips


* Python 3.9+ currently does not work. Use pyenv (<https://github.com/pyenv/pyenv>) to manage python versions. Quick start:`pyenv install 3.8.10 && pyenv global 3.8.10`
* If virtualenv chooses system python installations before your pyenv installations, manually initialize virtualenv before running `make install` like this: `virtualenv -p ~/.pyenv/shims/python3.8 .venv` .
* Terraform needs version <0.14 to work currently. Use tfenv (<https://github.com/tfutils/tfenv>) to manage terraform versions comfortable. Quick start: `tfenv install 0.13.7 && tfenv use 0.13.7`
* Set env variable LS_LOG='trace' to print every http request sent to localstack and their responses. Useful for debugging certain issues.
* As per dev guide, it requires `libsasl2-dev`. Arch based Distro equivalent: `libsasl`
