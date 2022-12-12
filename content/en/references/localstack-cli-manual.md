---
title: "LocalStack CLI manual"
weight: 2
description: >
  The reference guide for LocalStack CLI commands and how to get started on using them!
---

The LocalStack command-line interface (CLI) is a tool for starting, managing, and configuring your LocalStack container. It provides convenience features that make it easier to use LocalStack, and use LocalStack tools like Cloud Pods, Extensions, and more. The `localstack` CLI syntax is:

```bash
$ localstack [OPTIONS] COMMAND [ARGS]...
```

## `login`

The `login` command is used to authenticate with the LocalStack Platform. It is required to use advanced features like Cloud Pods and Extensions.

{{< command >}}
$ localstack login [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The options available for the `login` command are:

| Name, Shorthand          | Default | Description                  |
| ------------------------ | ------- | ---------------------------- |
| `--password`, `-p`       |         | Password                     |
| `--username`, `-u`       |         | Username                     |
| `--password-stdin`, `-s` |         | Take the password from stdin |

## `update`

The `update` command is used to update the LocalStack CLI to the latest version.

{{< command >}}
$ localstack update [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `update` command are:

| Name             | Description                          |
| ---------------- | ------------------------------------ |
| `all`            | Updates all LocalStack components    |
| `docker-images`  | Updates the LocalStack Docker images |
| `localstack-cli` | Updates the LocalStack CLI           |

## `config`

The `config` command is used to inspect your LocalStack configuration.

{{< command >}}
$ localstack config [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `config` command are:

| Name       | Description                                   |
| ---------- | --------------------------------------------- |
| `show`     | Shows the LocalStack configuration values     |
| `validate` | Validates the LocalStack configuration values |

## `start`

The `start` command is used to start your LocalStack container.

{{< command >}}
$ localstack start [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The options available for the `start` command are:

| Name, Shorthand    | Default | Description                                      |
| ------------------ | ------- | ------------------------------------------------ |
| `--detached`, `-d` |         | Run the LocalStack container in detached mode    |
| `--docker`         |         | Start LocalStack in a Docker container (default) |
| `--host`           |         | Start LocalStack directly on the host machine    |
| `--no-banner`      |         | Disable the LocalStack banner                     |

## `stop`

The `stop` command is used to stop your LocalStack container.

{{< command >}}
$ localstack stop [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

## `wait`

The `wait` command is used to wait for your LocalStack container to be ready.

{{< command >}}
$ localstack wait [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The options available for the `wait` command are:

| Name, Shorthand   | Default | Description                                           |
| ----------------- | ------- | ----------------------------------------------------- |
| `--timeout`, `-t` |         | Timeout in seconds to wait for LocalStack to be ready |
