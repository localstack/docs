---
title: "Podman"
weight: 30
description: >
  Describes how to run LocalStack inside Podman.
tags: ["podman", "docker"]
---

Usually, LocalStack CLI runs the emulation layer inside Docker container, but there is a way to run LocalStack container inside [Podman](https://podman.io/getting-started/) instead of Docker.

From Podman docs:
> Podman is a daemonless, open source, Linux native tool designed to make it easy to find, run, build, share and deploy applications using Open Containers Initiative (OCI) Containers and Container Images. Podman provides a command line interface (CLI) familiar to anyone who has used the Docker Container Engine. Most users can simply alias Docker to Podman (`alias docker=podman`) without any problems.


To run `localstack`, just alias `alias docker=podman` is not enough
- `localstack` is using [docker-py](https://pypi.org/project/docker/) which requires connection to `/var/run/docker.sock`
- `LAMBDA_EXECUTOR=docker` requires mounting `/var/run/docker.sock` as well

## podman-docker
There is package `podman-docker` that emulates Docker CLI using podman, it creates links
- `/usr/bin/docker ->  /usr/bin/podman`
- `/var/run/docker.sock -> /run/podman/podman.sock`

This package is available for some distros:
- https://archlinux.org/packages/community/x86_64/podman-docker/
- https://packages.ubuntu.com/impish/podman-docker
- https://packages.debian.org/sid/podman-docker

## Rootfull Podman with podman-docker
The simplest option is to run `localstack` using `podman` by having `podman-docker` and running `localstack start` as root
```sh
# you have to start podman socket first
sudo systemctl start podman

# then
sudo sh -c 'DEBUG=1 localstack start'
```

## Rootfull Podman without podman-docker
```sh
# you still have to start podman socket first
sudo systemctl start podman

# you have to pass a bunch of env variables
sudo sh -c 'DEBUG=1 DOCKER_CMD=podman DOCKER_HOST=unix://run/podman/podman.sock DOCKER_SOCK=/run/podman/podman.sock localstack start'
```

## Rootless Podman
You have to prepare your environment first:
- https://wiki.archlinux.org/title/Podman#Rootless_Podman
- https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md
- https://www.redhat.com/sysadmin/rootless-podman

```sh
# again, you have to start podman socket first
systemctl --user start podman.service

# and then localstack
DEBUG=1 DOCKER_CMD="podman" DOCKER_SOCK=$XDG_RUNTIME_DIR/podman/podman.sock DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock localstack start
```

If you have problems with [subuid and subgid](https://wiki.archlinux.org/title/Podman#Set_subuid_and_subgid) you could try use [overlay.ignore_chown_errors option](https://www.redhat.com/sysadmin/controlling-access-rootless-podman-users)
```sh
DEBUG=1 DOCKER_CMD="podman --storage-opt overlay.ignore_chown_errors=true" DOCKER_SOCK=$XDG_RUNTIME_DIR/podman/podman.sock DOCKER_HOST=unix://$XDG_RUNTIME_DIR/podman/podman.sock localstack start
```
