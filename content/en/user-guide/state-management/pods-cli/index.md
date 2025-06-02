---
title: "CLI command reference"
weight: 5
description: >
  Reference guide for LocalStack Cloud Pods CLI commands and how to get started on using them!
aliases:
  - /user-guide/cloud-pods/pods-cli/
tags: ["Base"]
---

This reference provides descriptions and example commands for LocalStack Cloud Pods CLI (`pod`) commands.

## Syntax

Use the following syntax to run `localstack pod` commands from your terminal window:

{{< command >}}
$ localstack pod [OPTIONS] COMMAND [ARGS]...
{{< / command >}}

In the above syntax:
- `COMMAND` specifies the operation you want to perform with your Cloud Pods (`save` or `load`).
- `OPTIONS` specifies the optional flags.
- `ARGS` specifies the command arguments.

## Commands

The following section lists the available commands for the Cloud Pods CLI.
You can have an overview of these command by typing `localstack pod --help`:

{{< command >}}
<disable-copy>
Usage: pod [OPTIONS] COMMAND [ARGS]...

  Manage the state of your instance via Cloud Pods.

Options:
  --help  Show this message and exit.

Commands:
  delete    Delete a Cloud Pod
  inspect   Inspect the contents of a Cloud Pod This command shows the...
  list      List all available Cloud Pods
  load      Load the state of a Cloud Pod into the application runtime/...
  remote    Manage cloud pod remotes
  save      Create a new Cloud Pod
  versions  List all available versions for a Cloud Pod This command lists...
</disable-copy>
{{< / command >}}

### `save`

{{< command >}}
<disable-copy>
Usage: pod save [OPTIONS] NAME [REMOTE]

  Save the current state of the LocalStack container in a Cloud Pod.

  A Cloud Pod can be registered and saved with different storage options,
  called remotes.
  By default, Cloud Pods are hosted in the LocalStack
  platform.
  However, users can decide to store their Cloud Pods in other
  remotes, such as AWS S3 buckets or ORAS registries.

  An optional message can be attached to any Cloud Pod.
  Furthermore, one
  could decide to export only a subset of services with the optional
  --service option.

  To use the LocalStack platform for storage, the desired Cloud Pod's name will suffice, e.g.:

  localstack pod save <pod_name>

  Please be aware that each following save invocation with the same name
  will result in a new version being created.

  To save a local copy of your state, you can use the 'localstack state export' command.

Options:
  -m, --message TEXT             Add a comment describing this Cloud Pod's
                                 version

  -s, --services TEXT            Comma-delimited list of services to push in
                                 the Cloud Pod (all by default)

  --visibility [public|private]  Set the visibility of the Cloud Pod [`public`
                                 or `private`].
  Does not create a new version

  -f, --format [json]            The formatting style for the save command
                                 output.

  --help                         Show this message and exit.
</disable-copy>
{{< / command >}}

The `save` command allows you to save a new version of a Cloud Pod targeting a specific remote.
To save and load the state locally, you can use the command in the `localstack state` group.

{{< command >}}
$ localstack pod save my-pod
{{< / command >}}

The above command generates a new version of `my-pod` and uploads it on the LocalStack platform.
When pushing an already existing pod, a new version is created and subsequently uploaded to the platform.

Users also have the option to select a specific subset of AWS services they want to include in the new Cloud Pod version using the `--services` option.

Users who want to make a Cloud Pod accessible outside their organization can mark it as **public** with the following command:

{{< command >}}
$ localstack pod save --name my-pod --visibility public
{{< / command >}}

The above command does not create a new version and requires a version already registered with the platform.
The CLI manual for the `save` command is as follows:

### `load`

{{< command >}}
<disable-copy>
Usage: pod load [OPTIONS] NAME [REMOTE]

  Load the state of a Cloud Pod into the application runtime/ Users can
  import Cloud Pods from different remotes, with the LocalStack platform
  being the default one.

  Loading the state of a Cloud Pod into LocalStack might cause some
  conflicts with the current state of the container.
  By default, LocalStack
  will attempt a best-effort merging strategy between the current state and
  the one from the Cloud Pod.
  For a service X present in both the current
  state and the Cloud Pod, we will attempt to merge states across different
  accounts and regions.
  If the service X has a state for the same account
  and region both in the running container and the Cloud Pod, the latter
  will be used.
  If a service Y is present in the running container but not
  in the Cloud Pod, it will be left untouched.
  With `--merge overwrite`, the
  state of the Cloud Pod will completely replace the state of the running
  container.

  To load a local copy of a LocalStack state, you can use the 'localstack state import' command.

Options:
  --merge [overwrite|merge]  The merge strategy to adopt when loading the
                             Cloud Pod

  -y, --yes                  Automatic yes to prompts.
  Assume a positive
                             answer to all prompts and run non-interactively

  --help                     Show this message and exit.
</disable-copy>
{{< / command >}}

The `load` command is the inverse operation of `save`.
It retrieves the content of a previously stored Cloud Pod a remote (by default, theLocalStack platform) and injects it into the LocalStack container.

### `delete`

{{< command >}}
<disable-copy>
Usage: pod delete [OPTIONS] NAME

  Delete a Cloud Pod registered on the remote LocalStack platform.

  This command will remove all the versions of a Cloud Pod, and the
  operation is not reversible.

Options:
  --help  Show this message and exit.
</disable-copy>
{{< / command >}}

The `delete` command let users delete a Cloud Pod stored in the remote platform.
The CLI manual for the `delete` command is as follows:

### `inspect`

{{< command >}}
<disable-copy>
Usage: pod inspect [OPTIONS] NAME

  Inspect the contents of a Cloud Pod

  This command shows the content of a Cloud Pod.
  By default, it starts a
  curses interface which allows an interactive inspection of the contents in
  the Cloud Pod.

Options:
  -f, --format [curses|rich|json]
                                  The formatting style for the inspect command
                                  output.

  --help                          Show this message and exit.
</disable-copy>
{{< / command >}}

The `inspect` command simply lets the user inspect the content of a Cloud Pod.

### `list`

{{< command >}}
<disable-copy>
Usage: pod list [OPTIONS] [REMOTE]

  List all the Cloud Pods available for a single user, or for an entire
  organization, if the user is part of one.

  With the --public flag, it lists the all the available public Cloud Pods.
  A public Cloud Pod is available across the boundary of a user one/or
  organization.
  In other words, any public Cloud Pod can be injected by any
  other user holding a LocalStack Pro (or above) license.

Options:
  -p, --public               List all the available public Cloud Pods
  -f, --format [table|json]  The formatting style for the list pods command
                             output.

  --help                     Show this message and exit.
</disable-copy>
{{< / command >}}

The `list` command lists all of the available Cloud Pods.
It shows all the pods available for a single user and its organization by default.

### `versions`

{{< command >}}
<disable-copy>
Usage: pod versions [OPTIONS] NAME

  List all available versions for a Cloud Pod

  This command lists the versions available for a Cloud Pod.
  Each invocation
  of the save command is going to create a new version for a named Cloud
  Pod, if a Pod with such name already does exist in the LocalStack
  platform.

Options:
  -f, --format [table|json]  The formatting style for the version command
                             output.

  --help                     Show this message and exit.
</disable-copy>
{{< / command >}}

The `versions` command lists all the available versions of a Cloud Pod.
The CLI manual for the `version` command is as follows:

### `remote`

The `remote` command group lets you manage custom Cloud Pod remotes, to enable alternative storage backends in addition to the default LocalStack managed platform.
It offers 3 commands: `add`, `delete`, and `list`.

For more info about remote usage, check our [documentation]({{< ref "/user-guide/state-management/pods-cli/#remote" >}}).

{{< command >}}
<disable-copy>
Usage: pod remote [OPTIONS] COMMAND [ARGS]...

  Manage cloud pod remotes

Options:
  --help  Show this message and exit.

Commands:
  add     Add a remote
  delete  Delete a remote
  list    Lists the available remotes
</disable-copy>
{{< / command >}}

#### `remote add`

{{< command >}}
<disable-copy>
Usage: pod remote add [OPTIONS] NAME URL

  Add a new remote for Cloud Pods.

  A remote is the place where your Cloud Pods are stored.
  By default, Cloud
  Pods are store in the LocalStack platform.

Options:
  --help  Show this message and exit.
</disable-copy>
{{< / command >}}

#### `remote delete`

{{< command >}}
<disable-copy>
Usage: pod remote delete [OPTIONS] NAME

  Remove a remote for Cloud Pods.

Options:
  --help  Show this message and exit.
</disable-copy>
{{< / command >}}

#### `remote list`

{{< command >}}
<disable-copy>
Usage: pod remote list [OPTIONS]

Options:
  -f, --format [table|json]  The formatting style for the remotes command
                             output.

  --help                     Show this message and exit.
</disable-copy>
{{< / command >}}

---

# Local Commands

In addition to the commands in the `pod` group, we also offer a simple alternative to save and load the LocalStack state.
The `state` group offers two commands to export and import the state of the LocalStack container to/from a zip file from the host machine.

## `state` syntax

{{< command >}}
<disable-copy>
Usage: state [OPTIONS] COMMAND [ARGS]...

  (Preview) Manage and manipulate the localstack state.

  The state command group allows you to interact with LocalStack's state
  backend.

  Read more: https://docs.localstack.cloud/references/persistence-mechanism/#snapshot-based-persistence

Options:
  --help  Show this message and exit.

Commands:
  export  Export the state of LocalStack services
  import  Import the state of LocalStack services
  reset   Reset the state of LocalStack services

</disable-copy>
{{< / command >}}

### `state export`

{{< command >}}
<disable-copy>
Usage: state export [OPTIONS] [DESTINATION]

  Save the current state of the LocalStack container to a file on the local
  disk.
  This file can be restored at any point in time using the `localstack
  state import` command.
  Please be aware that this might not be possible
  when importing the state with a different version of LocalStack.

  If you are looking for a managed solution to handle the state of your
  LocalStack container, please check out the Cloud Pods feature:
  https://docs.localstack.cloud/user-guide/tools/cloud-pods/

  Use the DESTINATION argument to specify an absolute path for the exported
  file or a filename in current working directory.
  If no destination is
  specified, a file named `ls-state-export` will be saved in the current
  working directory.

  Examples:
      localstack state export my-state
      localstack state export /home/johndoe/my-state

  You can also specify a subset of services to export.
  By default, the state
  of all running services is exported.

Options:
  -s, --services TEXT  Comma-delimited list of services to reset.
By default,
                       the state of all running services is exported.

  -f, --format [json]  The formatting style for the save command output.
  --help               Show this message and exit.
</disable-copy>
{{< / command >}}

### `state import`

{{< command >}}
<disable-copy>
Usage: state import [OPTIONS] SOURCE

  Load the state of LocalStack from a file into the running container.
  The
  SOURCE file must have been generated from a previous `localstack state
  export` command.
  Please be aware that it might not be possible to import a
  state generated from a different version of LocalStack.

  Examples:
      localstack state import my-state
      localstack state import /home/johndoe/my-state

Options:
  --help  Show this message and exit.
</disable-copy>
{{< / command >}}

### `state reset`

{{< command >}}
<disable-copy>
Usage: state reset [OPTIONS]

  Reset the service states of the current LocalStack runtime.

  This command invokes a reset of services in the currently running
  LocalStack container.
  By default, all services are rest.
  The `services`
  options allows to select a subset of services which should be reset.

  This command tries to automatically discover the running LocalStack
  instance.
  If LocalStack has not been started with `localstack start` (and
  is not automatically discoverable), please set `LOCALSTACK_HOST`.

Options:
  -s, --services TEXT  Comma-delimited list of services to reset.
By default,
                       the state of all running services is reset.

  --help               Show this message and exit.
</disable-copy>
{{< / command >}}
