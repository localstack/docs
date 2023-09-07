---
title: LocalStack CLI manual
weight: 3
description: The reference guide for LocalStack CLI commands and how to get started on using them!
---

The LocalStack command-line interface (CLI) is a tool for starting, managing, and configuring your LocalStack container.
It provides convenience features that make it easier to use LocalStack, and use LocalStack tools like Cloud Pods, Extensions, and more.

## Options

The following options are available for the `localstack` CLI.

### `auth`

(Beta) Authenticate with your LocalStack account.

```bash
Usage: localstack auth [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  set-token   Set your Localstack auth token to allow you to start LocalStack
              Pro
  show-token  Show the auth token in your configuration
```

### `aws`

Access additional functionality on LocalStack AWS Services.

```bash
Usage: localstack aws [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  iam  (Beta) Access LocalStack IAM features
```

### `completion`

CLI shell completion.

```bash
Usage: localstack completion [OPTIONS] {bash|zsh|fish}

   Print shell completion code for the specified shell (bash, zsh, or fish).
   The shell code must be evaluated to enable the interactive shell completion
   of LocalStack CLI commands.  This is usually done by sourcing it from the
   .bash_profile.

    Examples:
      # Bash
      ## Bash completion on Linux depends on the 'bash-completion' package.
      ## Write the LocalStack CLI completion code for bash to a file and source it from .bash_profile
      localstack completion bash > ~/.localstack/completion.bash.inc
      printf "
      # LocalStack CLI bash completion
      source '$HOME/.localstack/completion.bash.inc'
      " >> $HOME/.bash_profile
      source $HOME/.bash_profile
   
      # zsh
      ## Set the LocalStack completion code for zsh to autoload on startup:
      localstack completion zsh > "${fpath[1]}/_localstack"
   
      # fish
      ## Set the LocalStack completion code for fish to autoload on startup:
      localstack completion fish > ~/.config/fish/completions/localstack.fish

Options:
  -h, --help  Show this message and exit.
```

### `config`

Manage your LocalStack config.

```bash
Usage: localstack config [OPTIONS] COMMAND [ARGS]...

  Inspect and validate your LocalStack configuration.

Options:
  -h, --help  Show this message and exit.

Commands:
  show      Show your config
  validate  Validate your config
```

### `daemons`

(Deprecated) Manage local daemon processes.

```bash
Usage: localstack daemons [OPTIONS] COMMAND [ARGS]...

  (Deprecated)

Options:
  -h, --help  Show this message and exit.

Commands:
  log    (Deprecated) Show log of daemon process
  start  (Deprecated) Start local daemon processes
  stop   (Deprecated) Stop local daemon processes
```

### `dns`

Manage LocalStack DNS host config.

```bash
Usage: localstack dns [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  systemd-resolved  Manage LocalStack DNS in systemd-resolved
```

### `extensions`

(Beta) Manage LocalStack extensions.

```bash
Usage: localstack extensions [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  dev
  init
  install
  uninstall
```

### `infra`

(Deprecated) Manage LocalStack infrastructure.

```bash
Usage: localstack infra [OPTIONS] COMMAND [ARGS]...

  (Deprecated)  Manage LocalStack infrastructure

Options:
  -h, --help  Show this message and exit.

Commands:
  start  Start LocalStack
```

### `license`

(Beta) Manage and verify your LocalStack license.

```bash
Usage: localstack license [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  activate
  info
```

### `login`

Login to the LocalStack Platform.

```bash
Usage: localstack login [OPTIONS]

Options:
  -u, --username USER   Username for login
  -p, --password PWD    Password for login
  -s, --password-stdin  Read password from stdin
  -h, --help            Show this message and exit.
```

### `logout`

Log out from the LocalStack Platform.

```bash
Usage: localstack logout [OPTIONS]

Options:
  -h, --help  Show this message and exit.
```

### `logs`

Show LocalStack logs.

```bash
Usage: localstack logs [OPTIONS]

  Show the logs of the current LocalStack runtime.

  This command shows the logs of the currently running LocalStack docker
  container. By default, this command looks for a container named
  `localstack_main` (which is the default container name used by the
  `localstack start` command). If your LocalStack container has a different
  name, set the config variable `MAIN_CONTAINER_NAME`.

Options:
  -f, --follow  Block the terminal and follow the log output
  -n, --tail N  Print only the last <N> lines of the log output
  -h, --help    Show this message and exit.
```

### `pod`

Manage the state of your instance via Cloud Pods..

```bash
Usage: localstack pod [OPTIONS] COMMAND [ARGS]...

  Manage the state of your instance via Cloud Pods.

Options:
  -h, --help  Show this message and exit.

Commands:
  delete    Delete a Cloud Pod
  inspect
  list      List all available Cloud Pods
  load
  remote    Manage cloud pod remotes
  remotes   Lists the available remotes
  save      Create a new Cloud Pod
  versions
```

### `ssh`

Obtain a shell in LocalStack.

```bash
Usage: localstack ssh [OPTIONS]

  Obtain a shell in the current LocalStack runtime.

  This command starts a new interactive shell in the currently running
  LocalStack container. By default, this command looks for a container named
  `localstack_main` (which is the default container name used by the
  `localstack start` command). If your LocalStack container has a different
  name, set the config variable `MAIN_CONTAINER_NAME`.

Options:
  -h, --help  Show this message and exit.
```

### `start`

Start LocalStack.

```bash
Usage: localstack start [OPTIONS]

  Start the LocalStack runtime.

  This command starts the LocalStack runtime with your current configuration.
  By default, it will start a new Docker container from the latest
  LocalStack(-Pro) Docker image with best-practice volume mounts and port
  mappings.

Options:
  --docker        Start LocalStack in a docker container [default]
  --host          Start LocalStack directly on the host
  --no-banner     Disable LocalStack banner
  -d, --detached  Start LocalStack in the background
  -h, --help      Show this message and exit.
```

### `state`

(Beta) Manage the persistence state of localstack.

```bash
Usage: localstack state [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  reset  Reset the state of LocalStack services
```

### `status`

Query status info.

```bash
Usage: localstack status [OPTIONS] COMMAND [ARGS]...

  Query status information about the currently running LocalStack instance.

Options:
  -h, --help  Show this message and exit.

Commands:
  docker    Query LocalStack Docker status
  services  Query LocalStack services status
```

### `stop`

Stop LocalStack.

```bash
Usage: localstack stop [OPTIONS]

  Stops the current LocalStack runtime.

  This command stops the currently running LocalStack docker container. By
  default, this command looks for a container named `localstack_main` (which
  is the default container name used by the `localstack start` command). If
  your LocalStack container has a different name, set the config variable
  `MAIN_CONTAINER_NAME`.

Options:
  -h, --help  Show this message and exit.
```

### `update`

Update LocalStack.

```bash
Usage: localstack update [OPTIONS] COMMAND [ARGS]...

  Update different LocalStack components.

Options:
  -h, --help  Show this message and exit.

Commands:
  all             Update all LocalStack components
  docker-images   Update docker images LocalStack depends on
  localstack-cli  Update LocalStack CLI
```

### `wait`

Wait for LocalStack.

```bash
Usage: localstack wait [OPTIONS]

  Wait for the LocalStack runtime to be up and running.

  This commands waits for a started LocalStack runtime to be up and running,
  ready to serve requests. By default, this command looks for a container
  named `localstack_main` (which is the default container name used by the
  `localstack start` command). If your LocalStack container has a different
  name, set the config variable `MAIN_CONTAINER_NAME`.

Options:
  -t, --timeout N  Only wait for <N> seconds before raising a timeout error
  -h, --help       Show this message and exit.
```

