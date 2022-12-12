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

## Options

### `--version`

The `--version` option is used to display the version of the LocalStack CLI.

{{< command >}}
$ localstack --version
{{< /command >}}

### `--debug`

The `--debug` option is used to enable debug mode for the LocalStack CLI.

{{< command >}}
$ localstack --debug
{{< /command >}}

### `--help`

The `--help` option is used to display the help message for the LocalStack CLI.

{{< command >}}
$ localstack --help
{{< /command >}}

### `--profile`

The `--profile` option is used to specify the configuration profile to use for the LocalStack CLI.

{{< command >}}
$ localstack --profile <PROFILE>
{{< /command >}}

## Commands

The following commands are available for the `localstack` CLI.

### `login`

The `login` command is used to authenticate with the LocalStack Platform. It is required to use advanced features like Cloud Pods and Extensions.

{{< command >}}
$ localstack login [OPTIONS]
{{< /command >}}

The options available for the `login` command are:

| Name, Shorthand          | Default | Description                  |
| ------------------------ | ------- | ---------------------------- |
| `--password`, `-p`       |         | Password                     |
| `--username`, `-u`       |         | Username                     |
| `--password-stdin`, `-s` |         | Take the password from stdin |

## `logout`

The `logout` command is used to log out of the LocalStack Platform.

{{< command >}}
$ localstack logout
{{< /command >}}

### `update`

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

### `config`

The `config` command is used to inspect your LocalStack configuration.

{{< command >}}
$ localstack config [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `config` command are:

| Name       | Description                                   |
| ---------- | --------------------------------------------- |
| `show`     | Shows the LocalStack configuration values     |
| `validate` | Validates the LocalStack configuration values |

### `start`

The `start` command is used to start your LocalStack container.

{{< command >}}
$ localstack start [OPTIONS]
{{< /command >}}

The options available for the `start` command are:

| Name, Shorthand    | Default | Description                                      |
| ------------------ | ------- | ------------------------------------------------ |
| `--detached`, `-d` |         | Run the LocalStack container in detached mode    |
| `--docker`         |         | Start LocalStack in a Docker container (default) |
| `--host`           |         | Start LocalStack directly on the host machine    |
| `--no-banner`      |         | Disable the LocalStack banner                     |

### `stop`

The `stop` command is used to stop your LocalStack container.

{{< command >}}
$ localstack stop [OPTIONS]
{{< /command >}}

### `wait`

The `wait` command is used to wait for your LocalStack container to be ready.

{{< command >}}
$ localstack wait [OPTIONS]
{{< /command >}}

The options available for the `wait` command are:

| Name, Shorthand   | Default | Description                                           |
| ----------------- | ------- | ----------------------------------------------------- |
| `--timeout`, `-t` |         | Timeout in seconds to wait for LocalStack to be ready |

### `status`

The `status` command is used to check the status of your LocalStack container and print status information.

{{< command >}}
$ localstack status [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `status` command are:

| Name       | Description                                                          |
| ---------- | -------------------------------------------------------------------- |
| `docker`   | Query information about the LocalStack Docker image and runtime      |
| `services` | Query information about running services in the LocalStack container |

### `daemons`

The `daemons` command is used to manage LocalStack daemon processes.

{{< command >}}
$ localstack daemons [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `daemons` command are:

| Name    | Description                  |
| ------- | ---------------------------- |
| `log`   | Show log of daemon process   |
| `start` | Start local daemon processes |
| `stop`  | Stop local daemon processes  |

### `dns`

The `dns` command is used to manage the DNS settings of your host.

{{< command >}}
$ localstack dns [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `dns` command are:

| Name               | Description                             |
| ------------------ | --------------------------------------- |
| `systemd-resolved` | Manage DNS settings of systemd-resolved |

### `extensions`

LocalStack Extensions allow developers to extend and customize LocalStack. Extensions are a LocalStack Pro feature. To use and install extensions, use the CLI to first log in to your account.

{{< command >}}
$ localstack extensions [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `extensions` command are:

| Name        | Description                                          |
| ----------- | ---------------------------------------------------- |
| `install`   | Install an extension                                 |
| `uninstall` | Uninstall an extension                               |
| `init`      | Initialize an extension                              |
| `dev`       | Developer tools for developing LocalStack extensions |

### `pod`

The `pod` command is used to manage Cloud Pods. Cloud Pods is a LocalStack Pro feature. To use Cloud Pods, use the CLI to first log in to your account.

{{< command >}}
$ localstack pod [OPTIONS] COMMAND [ARGS]...
{{< /command >}}

The commands available for the `pod` command are:

| Name       | Description                                                           |
| ---------- | --------------------------------------------------------------------- |
| `save`     | Create a new Cloud Pod                                                |
| `load`     | Load a Cloud Pod from a file or URL into running LocalStack container |
| `list`     | List all Cloud Pods in your account                                   |
| `delete`   | Delete a Cloud Pod from your account                                  |
| `inpsect`  | Inspect the contents of a Cloud Pod                                   |
| `versions` | List all available versions of a Cloud Pod                            |

An extended CLI manual for Cloud Pods is available on the [Cloud Pods CLI manual]({{< ref "user-guide/tools/cloud-pods/pods-cli" >}}).

### `reset`

The `reset` command is used to reset the service states of the running LocalStack container.

{{< command >}}
$ localstack reset [OPTIONS]
{{< /command >}}

The options available for the `reset` command are:

| Name, Shorthand       | Default | Description                                                                  |
| --------------------- | ------- | ---------------------------------------------------------------------------- |
| `--persistence`, `-p` |         | Reset the persistence directory (set with `PERSISTENCE=1`)                   |
| `--services`, `-s`    |         | Comma-delimited list of services to reset. By default, it resets everything. |

### `ssh`

The `ssh` command is used to connect to the obtain a shell in the running LocalStack container.

{{< command >}}
$ localstack ssh [OPTIONS]
{{< /command >}}

### `infra`

The `infra` command is used to manipulate the infrastructure of your LocalStack container. It is a legacy command and will be removed in a future release.

{{< command >}}
$ localstack infra [OPTIONS] COMMAND [ARGS]...
{{< /command >}}
