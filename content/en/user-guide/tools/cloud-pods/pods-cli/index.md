---
title: "Cloud Pods CLI command reference"
weight: 5
categories: ["LocalStack Pro", "Tools", "Persistence", "CLI"]
description: >
  The reference guide for LocalStack Cloud Pods CLI commands and how to get started on using them!
aliases:
  - /tools/cloud-pods/pods-cli/
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

The `save` command creates a new version of a Cloud Pod. Pro users can dump the Cloud Pod locally or upload it to the LocalStack platform. To dump the state locally, pass a local file URI as an argument to the `save` command. For instance, the following command:

{{< command >}}
$ localstack pod save file://<path_to_disk>/my-pod
{{< / command >}}

The above command will create a zip file named `my-pod` to the specified location on the disk. To use the Cloud Pods platform, specify the Cloud Pod's name as an argument, for example:

{{< command >}}
$ localstack pod save my-pod
{{< / command >}}

The above command creates a version of `my-pod` and registers it to our platform. Pushing already existing pod results in creating a new version and, eventually, uploading it to the platform. Users can also select a subset of AWS services they wish to incorporate in a new Cloud Pod version with the `--services` option.

Users who want to make a Cloud Pod accessible outside their organization can mark it as **public** with the following command:

{{< command >}}
$ localstack pod push --name <pod_name> --visibility public
{{< / command >}}

The above command does not create a new version and requires a version already registered with the platform. The CLI manual for the `save` command is as follows:

```bash
Usage: python -m localstack.cli.main pod save [OPTIONS] URL_OR_NAME

  Save the current state of the LocalStack container in a Cloud Pod. A Cloud Pod can be exported
  locally or registered within the LocalStack Pod's platform (with a Pro license). An optional
  message can be attached to any Cloud Pod. Furthermore, one could decide to export only a subset
  of services with the optional --service option.

  To export on a local path run the following command:
  localstack pod save file://<path_on_disk>/<pod_name>

  The output will be a <pod_name> zip file in the specified directory. This Cloud Pod instance can
  be restored at any point in time with the load command.

  To use the LocalStack Pod's platform, the desired Pod's name only will suffice, e,g.:

  localstack pod save <pod_name>

  Please be aware that each following save invocation with the same name will result in a new
  version being created.

Options:
  -m, --message TEXT   Add a comment describing this Cloud Pod's version
  -s, --services TEXT  Comma-delimited list of services to push in the Cloud Pod (all by default)
  --visibility TEXT    Set the visibility of the Cloud Pod [`public` or `private`]. Does not
                       create a new version
  --help               Show this message and exit.
```

{{% alert %}}
Community users have access to a restricted version of the `save` command.  In particular, they can simply invoke the `save` command with a file URI as an argument.
{{% /alert %}}

### `load`

The `load` command is the inverse operation of `save`. It retrieves the content of a previously stored Cloud Pod from the local file system or the Cloud Pod's platform and injects it into the application runtime.

The `load` command takes an argument that can either be a URI or a Cloud Pods name. While the first option is available to all users, the second is valid only for licensed ones.

By default, the injecting state updates the application runtime at a service level. Using the merge injection strategy, the state of all services specified in the injecting state is reflected precisely in the application runtime, while all other active services remain unchanged.

The `--strategy` option can be used to change such default injection behavior. More specifically, the overwrite strategy will ensure the application runtime is an exact instance of the injecting state. The deep-merge strategy will perform a fine-grain merge of the injecting state into the application runtime.

The CLI manual for the `load` command is as follows:

```shell
Usage: python -m localstack.cli.main pod load [OPTIONS] URL_OR_NAME

  Load a Cloud Pod into the running LocalStack container. Users can import Pods different sources:
  community users can store and retrieve Pods from local storage or any provided HTTP URL;
  licensed users can take advantage of the LocalStack Pod's platform to ease the storage,
  versioning, and retrieval of Pods.

  The --source option specifies a URI scheme that point to the Cloud Pod's resources to import.

  We support the following protocols:
  localstack pod load file://<path_to_disk>
  localstack pod load https://<some_url>
  localstack pod load git://<user>/<repo>/<local_repo_path>

  The latter option is merely a shortcut for --source
  https://raw.githubusercontent.com/<user>/<repo>/<branch>/<path>

  Importing via a provided --source is available for all users. Licensed users can omit this
  option and simply provide a name for their Cloud Pods.

Options:
  -s, --strategy TEXT  Inject strategy (merge, overwrite, deep-merge).
  --help               Show this message and exit.
```

{{% alert %}}
Similar to the `save` command, the usage of the Cloud Pod's platform is restricted to licensed users. Community users can load a Cloud Pod from a local URI file, URL, or public GitHub repository. However, they have no access to Cloud Pods versioning.
{{% /alert %}}

### `delete`

The `delete` command let users delete a Cloud Pod stored in the remote platform. The CLI manual for the `delete` command is as follows:

```shell
Usage: python -m localstack.cli.main pod delete [OPTIONS]

  Delete a Cloud Pod register on the remove LocalStack Pod's platform. This command will cancel
  all the versions of a created Pod and won't be reversible.

Options:
  -n, --name TEXT  Name of the Cloud Pod  [required]
  --help           Show this message and exit.
```

### `inspect`

The `inspect` command simply lets the user inspect the content of a Cloud Pod. The CLI manual for the `inspect` command is as follows:

```shell
Usage: python -m localstack.cli.main pod inspect [OPTIONS]

  Inspect the contents of a Cloud Pod

Options:
  -n, --name TEXT    Name of the Cloud Pod  [required]
  -f, --format TEXT  Format (curses, rich, json).
  --help             Show this message and exit.
```

### list

The `list` command lists all of the available Cloud Pods. It shows all the pods available for a single user and its organization by default. If the `--public option is passed to the commands, it shows only the Cloud Pods marked as public and are, therefore, available to all licensed users. The CLI manual for the `list` command is as follows:

```shell
Usage: python -m localstack.cli.main pod list [OPTIONS]

  List all the Cloud Pods available for a single user, or for an entire organization, if the user
  is part of one.

  With the --public flag, it lists the all the available public Cloud Pods. A public Cloud Pod is
  available across the boundary of a user ond/or organization. In other words, any public Cloud
  Pod can be injected by any other user holding a LocalStack Pro (or above) license.

Options:
  -p, --public  List all the available public Cloud Pods
  --help        Show this message and exit.
```

### versions

The `versions` command simply lists all the available versions of a Cloud Pod. The CLI manual for the `version` command is as follows:

```shell
Usage: python -m localstack.cli.main pod versions [OPTIONS]

  List the versions available for a Cloud Pod. Each invocation of the save command is going to
  create a new version for a named Cloud Pod, is a Pod with such name already does exist in the
  LocalStack Pods platform.

Options:
  -n, --name TEXT  Name of the Cloud Pod  [required]
  --help           Show this message and exit.
```
