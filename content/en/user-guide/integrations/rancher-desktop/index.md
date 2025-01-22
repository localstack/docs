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

To address these issues, you can use the following options:

- [Switching Emulation and Volume Sharing](#switching-emulation-and-volume-sharing) (**only for macOS**)
  - [Switching Emulation from QEMU to VZ (Apple Virtualization Framework)](#switching-emulation-from-qemu-to-vz-apple-virtualization-framework)
  - [Changing Volume from Reverse-SSHFS to VirtioFS](#changing-volume-from-reverse-sshfs-to-virtiofs)
- [Rancher Desktop with Dockerd](#rancher-desktop-with-dockerd)
- [Rancher Desktop with containerd](#rancher-desktop-with-containerd)
- [Rancher Desktop with Windows](#rancher-desktop-with-windows)

These setups enable LocalStack to run smoothly with Rancher Desktop across various operating systems, ensuring compatibility with Docker-based workflows.
macOS users, particularly those with Apple Silicon, should switch to the VZ virtualization engine and use VirtioFS for optimal performance and to avoid permission issues.

### Switching Emulation and Volume Sharing

If you're using Rancher Desktop on macOS, particularly on Apple Silicon (M1, M2, etc.), it's crucial to adjust both the emulation engine and the volume-sharing method.
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

### Rancher Desktop with Dockerd

The simplest way to run LocalStack using Rancher Desktop involves making sure that Rancher Desktop's `dockerd` is active and properly configured.

Start Rancher Desktop and verify it is set to use the Docker runtime.
Link the Docker socket with the following command:

{{< command >}}
$ sudo ln -s /var/run/rancher-desktop-lima/docker.sock /var/run/docker.sock
{{< /command >}}

Start LocalStack using this command:

{{< command >}}
$ DEBUG=1 localstack start --network rancher
{{< /command >}}

### Rancher Desktop with containerd

If you are using the `containerd` runtime in Rancher Desktop, you'll need to make some additional configurations.
Ensure that the `docker` command is available through Rancher Desktop's setup, or alternatively, use the `nerdctl` command line interface.

To start LocalStack with the `containerd` environment, use the following command:

{{< command >}}
$ DEBUG=1 DOCKER_CMD=nerdctl localstack start --network rancher
{{< /command >}}

### Rancher Desktop with Windows

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
version: "3.8"
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
version: "3.8"
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
