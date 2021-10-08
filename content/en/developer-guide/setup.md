---
title: "Setup and requirements"
weight: 4
description: >
  Set up your development environment for developing LocalStack.
---


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

Here are very basic installation instructions for the dependencies you will need.

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

### Tips


* Python 3.9+ currently does not work. Use pyenv (<https://github.com/pyenv/pyenv>) to manage python versions. Quick start:`pyenv install 3.8.10 && pyenv global 3.8.10`
* If virtualenv chooses system python installations before your pyenv installations, manually initialize virtualenv before running `make install` like this: `virtualenv -p ~/.pyenv/shims/python3.8 .venv` .
* Terraform needs version <0.14 to work currently. Use tfenv (<https://github.com/tfutils/tfenv>) to manage terraform versions comfortable. Quick start: `tfenv install 0.13.7 && tfenv use 0.13.7`
* Set env variable LS_LOG='trace' to print every http request sent to localstack and their responses. Useful for debugging certain issues.
* As per dev guide, it requires `libsasl2-dev`. Arch based Distro equivalent: `libsasl`
