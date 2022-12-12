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
$ localstack login
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
$ localstack update
{{< /command >}}

The commands available for the `update` command are:

| Name             | Description                          |
| ---------------- | ------------------------------------ |
| `all`            | Updates all LocalStack components    |
| `docker-images`  | Updates the LocalStack Docker images |
| `localstack-cli` | Updates the LocalStack CLI           |

