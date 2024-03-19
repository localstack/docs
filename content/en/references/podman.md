---
title: "Podman"
weight: 50
description: >
  Running LocalStack inside Podman
---

## Overview

By default, the LocalStack CLI starts the LocalStack runtime inside a Docker container.
Docker may not be available on your system, and a popular alternative is [Podman](https://podman.io/getting-started/) which you can use to run LocalStack.
Podman support is still experimental, and the following docs give you an overview of the current state.

From the Podman docs:

> Podman is a daemonless, open source, Linux native tool designed to make it easy to find, run, build, share and deploy applications using Open Containers Initiative (OCI) Containers and Container Images. Podman provides a command line interface (CLI) familiar to anyone who has used the Docker Container Engine. Most users can simply alias Docker to Podman (`alias docker=podman`) without any problems.

## Options

To run `localstack`, simply aliasing `alias docker=podman` is not enough, for the following reasons:
- `localstack` is using [docker-py](https://pypi.org/project/docker/) which requires a connection to `/var/run/docker.sock`
- Lambda requires mounting the Docker socket `/var/run/docker.sock` into the container (see [Lambda providers]({{< ref "user-guide/aws/lambda" >}})).

Here are several options on running LocalStack using podman:

### podman-docker
The package `podman-docker` emulates the Docker CLI using podman. It creates the following links:
- `/usr/bin/docker ->  /usr/bin/podman`
- `/var/run/docker.sock -> /run/podman/podman.sock`

This package is available for some distros:
- https://archlinux.org/packages/community/x86_64/podman-docker/
- https://packages.ubuntu.com/impish/podman-docker
- https://packages.debian.org/sid/podman-docker

### Rootfull Podman with podman-docker
The simplest option is to run `localstack` using `podman` by having `podman-docker` and running `localstack start` as root
```sh
# you have to start the podman socket first
sudo systemctl start podman

# then
sudo sh -c 'DEBUG=1 localstack start'
```

### Rootfull Podman without podman-docker
```sh
# you still have to start the podman socket first
sudo systemctl start podman

# you have to pass a bunch of env variables
sudo sh -c 'DEBUG=1 DOCKER_CMD=podman DOCKER_HOST=unix://run/podman/podman.sock DOCKER_SOCK=/run/podman/podman.sock localstack start'
```

### Rootless Podman
You have to prepare your environment first:
- https://wiki.archlinux.org/title/Podman#Rootless_Podman
- https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md
- https://www.redhat.com/sysadmin/rootless-podman

```sh
# again, you have to start the podman socket first
systemctl --user start podman.service

# and then localstack
DEBUG=1 DOCKER_CMD="podman" DOCKER_SOCK=$XDG_RUNTIME_DIR/podman/podman.sock DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock localstack start
```

If you have problems with [subuid and subgid](https://wiki.archlinux.org/title/Podman#Set_subuid_and_subgid), you could try to use [overlay.ignore_chown_errors option](https://www.redhat.com/sysadmin/controlling-access-rootless-podman-users)
```sh
DEBUG=1 DOCKER_CMD="podman --storage-opt overlay.ignore_chown_errors=true" DOCKER_SOCK=$XDG_RUNTIME_DIR/podman/podman.sock DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock localstack start
```
