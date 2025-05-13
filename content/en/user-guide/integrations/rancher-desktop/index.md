---
title: "Rancher Desktop"
linkTitle: "Rancher Desktop"
description: >
  Use Rancher Desktop with LocalStack
---

## Introduction

Rancher Desktop is a desktop application that provides a Kubernetes cluster on your local machine.
Rancher Desktop allows you to run Docker containers and Kubernetes clusters without relying on remote or cloud-based systems.
It utilizes `containerd` and `dockerd`, enabling users to easily switch between container runtimes.

By default, the LocalStack CLI launches the LocalStack runtime inside a Docker container.
However, if Docker is not available on your system, you can use Rancher Desktop as a popular alternative to run LocalStack.

## Getting started

To run LocalStack using Rancher Desktop, simply aliasing Docker commands to Rancher Desktop's `dockerd` service may not be sufficient for these reasons:

1. LocalStack depends on `docker-py`, which needs to connect to `/var/run/docker.sock`.
2. Lambda services in LocalStack require the Docker socket at `/var/run/docker.sock` to be mounted into the container.

Depending on your operating system, you may need to make additional configurations to ensure LocalStack runs smoothly with Rancher Desktop.

- [Linux/macOS](#linuxmacos)
  - [Rancher Desktop with dockerd](#rancher-desktop-with-dockerd)
  - [Rancher Desktop with containerd](#rancher-desktop-with-containerd)
- [Windows](#windows)

These setups enable LocalStack to run smoothly with Rancher Desktop across various operating systems, ensuring compatibility with Docker-based workflows.

### Linux/macOS

{{<alert type="info">}}
### Recommended Settings for Rancher Desktop on macOS

If you're using Rancher Desktop on macOS, particularly on Apple Silicon (M1, M2, etc.), it's crucial to adjust both the emulation engine and the volume-sharing method.
It is recommended to switch to the VZ virtualization engine and use VirtioFS for optimal performance and to avoid permission issues.
Without these adjustments, you may encounter permission issues with volume mounts in LocalStack.

#### Switching Emulation from QEMU to VZ (Apple Virtualization Framework)

For macOS users, Rancher Desktop allows switching from QEMU to the Apple Virtualization Framework (VZ) for virtualization.
Using VZ can enhance performance and resolve permission issues with volume mounts when running LocalStack.

Here’s how to switch from QEMU to VZ:

1. Open Rancher Desktop and navigate to **Settings**.
2. Go to the **Virtual Machine** section.
3. Find the **Virtualization Engine** option, which is set to QEMU by default.
4. Change the setting from `QEMU` to `VZ (Apple Virtualization)`.
5. Restart Rancher Desktop to apply the changes.

#### Changing Volume from Reverse-SSHFS to VirtioFS

By default, Rancher Desktop uses `reverse-sshfs` for mounting volumes inside the virtual machine.
However, you can switch to `VirtioFS` to improve performance and address permission issues.
VirtioFS is a faster and more reliable volume sharing method on macOS.

To switch the volume sharing method from reverse-SSHFS to VirtioFS:

1. Open Rancher Desktop and access the **Settings**.
2. Proceed to the **Virtual Machine** section, where you'll find the volume mount options.
3. Select the **File Sharing** setting and change it from `reverse-sshfs` to `VirtioFS`.
4. Restart Rancher Desktop to implement the changes.
{{</alert>}}

#### Rancher Desktop with dockerd

The simplest way to run LocalStack using Rancher Desktop involves making sure that Rancher Desktop's `dockerd` is active and properly configured.
Rancher Desktop typically places its Docker socket file somewhere under your user directory, such as `~/.rancher-desktop`.
LocalStack, however, expects the Docker socket to be at `/var/run/docker.sock`.
In this scenario, you need to create a symlink from the Rancher Desktop socket to the expected location.

Start Rancher Desktop and verify it is set to use the Docker runtime.
Link the Docker socket with the following command:

{{< command >}}
# 1. Make sure there is no existing socket at /var/run/docker.sock
sudo rm -f /var/run/docker.sock

# 2. Adjust the path if your Rancher Desktop socket is in a different location
$ sudo ln -s /var/run/rancher-desktop-lima/docker.sock /var/run/docker.sock
{{< /command >}}

Start LocalStack using this command:

{{< command >}}
$ DEBUG=1 localstack start --network rancher
{{< /command >}}

#### Rancher Desktop with containerd

If you are using the `containerd` runtime in Rancher Desktop, you'll need to make some additional configurations.
Ensure that the `docker` command is available through Rancher Desktop's setup, or alternatively, use the [`nerdctl` command line interface](https://github.com/containerd/nerdctl).

To start LocalStack with the `containerd` environment, use the following command:

{{< command >}}
$ DEBUG=1 DOCKER_CMD=nerdctl localstack start --network rancher
{{< /command >}}

### Windows

You can run Rancher Desktop on Windows using WSL2 (Windows Subsystem for Linux) with a Docker Compose setup for LocalStack.

Ensure Rancher Desktop is configured to use `dockerd`, and that the Docker socket is accessible in WSL2:

{{< command >}}
$ rancher-desktop settings set --docker
{{< /command >}}

Initialize and start Rancher Desktop:

{{< command >}}
$ rancher-desktop --start
{{< /command >}}

Modify your Docker Compose configuration to work with Rancher Desktop:

{{< tabpane lang="yml" >}}
{{< tab header="Community" lang="yml" >}}
services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"
      - "127.0.0.1:4510-4559:4510-4559"
    networks:
      - rancher
    environment:
      - DEBUG=${DEBUG:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
{{< /tab >}}
{{< tab header="Pro" lang="yml" >}}
services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack-pro
    ports:
      - "127.0.0.1:4566:4566"
      - "127.0.0.1:4510-4559:4510-4559"
      - "0.0.0.0:443:443"
    networks:
      - rancher
    environment:
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?}
      - DEBUG=${DEBUG:-0}
      - PERSISTENCE=${PERSISTENCE:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
{{< /tab >}}
{{< /tabpane >}}

Finally, start the services using `docker compose up` or `nerdctl compose up`, depending on your configuration.
This will launch your LocalStack instance configured to interact with Rancher Desktop.

### 📝 Note on Hot Reloading Lambdas in Windows (WSL2)

If you're using hot reloading for Lambda functions, make sure your Lambda handler paths are specified using **WSL2-compatible paths**.

For example, instead of using a Windows-style path like:

```bash
C:\Users\myuser\projects\lambda\handler.py
```

Use the corresponding WSL-style path:
```
/mnt/c/Users/myuser/projects/lambda/handler.py
```

This ensures that LocalStack can properly mount and watch your Lambda code inside the container when running under WSL2.
