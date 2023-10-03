---
title: "Cloud Pods CLI command reference"
weight: 5
description: >
  Reference guide for LocalStack Cloud Pods CLI commands and how to get started on using them!
---

This reference provides descriptions and example commands for LocalStack Cloud Pods CLI (`pod`) commands.

## Syntax

Use the following syntax to run `localstack pod` commands from your terminal window:

{{< command >}}
$ localstack pod [OPTIONS] COMMAND [ARGS]
{{< / command >}}

In the above syntax:
- `COMMAND` specifies the operation you want to perform with your Cloud Pods (`save` or `load`).
- `OPTIONS` specifies the optional flags.
- `ARGS` specifies the command arguments.

## Commands

The following section lists the available commands for the Cloud Pods CLI.

### `save`

The `save` command allows you to save a new version of a Cloud Pod. For licensed users, it provides the option to either save the Cloud Pod locally or upload it to the LocalStack platform. 

To save the state locally, simply provide a local file URI as an argument when using the `save` command. Running the following command will create a file named `my-pod` in the specified location on the disk:

{{< command >}}
$ localstack pod save file://<path_to_disk>/my-pod
{{< / command >}}

The command mentioned above will produce a zip file named `my-pod` and save it to the designated location on your disk. If you intend to utilize the Cloud Pods platform, you should specify the Cloud Pod's name as an argument, as shown below:

{{< command >}}
$ localstack pod save my-pod
{{< / command >}}

The above command generates a new version of `my-pod` and uploads it on the LocalStack platform. When pushing an already existing pod, a new version is created and subsequently uploaded to the platform. 

Users also have the option to select a specific subset of AWS services they want to include in the new Cloud Pod version using the `--services` option.

Users who want to make a Cloud Pod accessible outside their organization can mark it as **public** with the following command:

{{< command >}}
$ localstack pod save --name my-pod --visibility public
{{< / command >}}

The above command does not create a new version and requires a version already registered with the platform. The CLI manual for the `save` command is as follows:

{{< command >}}
$ localstack pod save --help
<disable-copy>
Usage: localstack pod save [OPTIONS] URL_OR_NAME [REMOTE]

Options:
  -m, --message TEXT             Add a comment describing this Cloud Pod's version
  -s, --services TEXT            Comma-delimited list of services to push in the Cloud Pod
                                 (all by default)
  --visibility [public|private]  Set the visibility of the Cloud Pod [`public` or `private`].
                                 Does not create a new version
  -f, --format [json]            The formatting style for the save command output.
  -h, --help                     Show this message and exit.
</disable-copy>
{{< / command >}}

### `load`

The `load` command is the inverse operation of `save`. It retrieves the content of a previously stored Cloud Pod from the local file system or the LocalStack platform and injects it into the LocalStack container.

The `load` command takes an argument that can either be a URI or a Cloud Pods name. By default, the injecting state updates the container state at a service level. The CLI manual for the `load` command is as follows:

{{< command >}}
$ localstack pod save --help
<disable-copy>
Usage: localstack pod load [OPTIONS] URL_OR_NAME [REMOTE]

Options:
  --merge [overwrite|merge]  The merge strategy to adopt when loading the Cloud Pod  [default:
                             merge]
  -h, --help                 Show this message and exit.
</disable-copy>
{{< / command >}}

### `delete`

The `delete` command let users delete a Cloud Pod stored in the remote platform. The CLI manual for the `delete` command is as follows:

{{< command >}}
$ localstack pod delete --help
<disable-copy>
Usage: localstack pod delete [OPTIONS] NAME

Options:
  -h, --help  Show this message and exit.
</disable-copy>
{{< / command >}}

### `inspect`

The `inspect` command simply lets the user inspect the content of a Cloud Pod. The CLI manual for the `inspect` command is as follows:

{{< command >}}
$ localstack pod delete --help
<disable-copy>
Usage: localstack pod inspect [OPTIONS] NAME

Options:
  -f, --format [curses|rich|json]
                                  The formatting style for the inspect command output.
                                  [default: curses]
  -h, --help                      Show this message and exit.
</disable-copy>
{{< / command >}}

### list

The `list` command lists all of the available Cloud Pods. It shows all the pods available for a single user and its organization by default. The CLI manual for the `list` command is as follows:

{{< command >}}
$ localstack pod list --help
<disable-copy>
Usage: localstack pod list [OPTIONS] [REMOTE]

Options:
  -p, --public               List all the available public Cloud Pods
  -f, --format [table|json]  The formatting style for the list pods command output.  [default:
                             table]
  -h, --help                 Show this message and exit.
</disable-copy>
{{< / command >}}

### versions

The `versions` command lists all the available versions of a Cloud Pod. The CLI manual for the `version` command is as follows:

{{< command >}}
$ localstack pod versions --help
<disable-copy>
Usage: localstack pod versions [OPTIONS] NAME

Options:
  -f, --format [table|json]  The formatting style for the version command output.  [default:
                             table]
  -h, --help                 Show this message and exit.
</disable-copy>
{{< / command >}}
