---
title: "ARM64 Support"
weight: 50
description: >
  Running LocalStack on ARM64 CPUs
---

Since [version 0.13](https://github.com/localstack/localstack/releases/tag/v0.13.0), LocalStack officially publishes a [multi-architecture Docker manifest](https://hub.docker.com/r/localstack/localstack).
This manifest contains links to a Linux AMD64 as well as a Linux ARM64 image.

## Pulling the LocalStack image

With the multi-arch Docker manifest, your Docker client (and therefore the [LocalStack CLI]({{< ref "getting-started/#localstack-cli" >}})) now automatically selects the image according to your platform:
{{< command >}}
$ docker pull localstack/localstack
{{< / command >}}

You can check the architecture of the pulled image by using `docker inspect`:
{{< command >}}
$ docker inspect localstack/localstack | jq '.[0].Architecture'
"arm64"
{{< / command >}}

## Lambda multi-architecture support

Since LocalStack&nbsp;2.0, Lambda functions execute in Docker containers with the target platform `linux/amd64` or `linux/arm64`
depending on the [instruction set architecture](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html) configured for the function (`x86_64` by default or `arm64`).
This behavior can lead to errors if the host system, the Docker image, or the code/layer of the function do not support the target architecture.
If you prefer to execute Lambda functions natively, you can set the [configuration]({{< ref "configuration#lambda" >}}) variable `LAMBDA_IGNORE_ARCHITECTURE=1`.

Host systems with [multi-architecture support](https://docs.docker.com/build/building/multi-platform/) can run containers for different Linux architectures using emulation.
For example, an Apple Silicon MacBook can execute `linux/arm64` (`arm64`) Lambda functions natively or emulate them for `linux/arm64` (`x86_64`).
However, emulation through qemu is only best-effort and certain features such as [ptrace](https://github.com/docker/for-mac/issues/5191#issuecomment-834154431) for debugging might not work.

You can check the supported architectures on your host system with:
{{< command "hl_lines=3-7" >}}
$ docker run --privileged --rm tonistiigi/binfmt
{
  "supported": [
    "linux/amd64",
    "linux/arm64",
    "linux/386"
  ],
  "emulators": [
    "jar",
    "llvm-12-runtime.binfmt",
    "python3.10",
    "python3.9",
    "qemu-aarch64"
  ]
}
{{< / command >}}

If you want to execute Docker Lambda functions or binaries which have not been built for your architecture,
you might need to configure cross-platform emulation on your system.

You can do so by installing the `bin_fmt` emulator with the following command:

{{< callout "warning" >}}
The following command installs additional emulators on your host system.
{{< /callout >}}

{{< command >}}
$ docker run --privileged --rm tonistiigi/binfmt --install amd64
{{< / command >}}

## Troubleshooting

### Pulling images for other architectures

{{< callout "note" >}}
Please be aware that this workaround is not supported by LocalStack at all.
{{< /callout >}}

If you want to use a LocalStack image which has been built for another architecture than yours, you can instruct Docker to use another platform by setting the `DOCKER_DEFAULT_PLATFORM` environment variable:

{{< command >}}
$ export DOCKER_DEFAULT_PLATFORM=linux/amd64
{{< / command >}}

When using Docker Compose, you can use the `platform` element [as described in the specification](https://github.com/compose-spec/compose-spec/blob/master/spec.md#platform).

### Emulating AMD64 in host mode on Apple Silicon

{{< callout >}}
Please be aware that this workaround is not supported by LocalStack at all.
{{< /callout >}}

This advanced workaround is running the open source version of LocalStack in host mode (i.e., developer mode) using AMD64 emulation on an ARM64 machine.

First, you should enable "Rosetta" on your preferred terminal.
This way you'll be installing packages for `x86_64` platform.

![Rosetta](m1-trouble-1.png)

What we will be doing now is installing Java and Python executables using Homebrew, it should automatically resolve packages to proper architecture versions.

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install java11 and follow instructions
brew install java11

# Install jenv and follow instructions
brew install jenv

# Add Java11 to jenv and use it globally
jenv add /Library/Java/JavaVirtualMachines/openjdk-11.jdk/Contents/Home/
jenv global 11

# Install pyenv and follow instructions
brew install pyenv

# Install python and enable it globally (check localstack/.python-version)
pyenv install 3.11.9
pyenv global 3.11.9
```

Then clone LocalStack to your machine, run `make install` and then `make start`.


### Raspberry Pi
If you want to run LocalStack on your Raspberry Pi, make sure to use a 64bit operating system.
In our experience, it works best on a Raspberry Pi 4 8GB with [Ubuntu Server 20.04 64Bit for Raspberry Pi](https://ubuntu.com/download/raspberry-pi).

You can check if Docker is running and your architecture is ARM64 / aarch64 by using `docker info`:
{{< command "hl_lines=7-9" >}}
$ docker info
Client:
 ...

Server:
 ...
 Operating System: Ubuntu 20.04
 OSType: linux
 Architecture: aarch64
 ...
{{< / command >}}
