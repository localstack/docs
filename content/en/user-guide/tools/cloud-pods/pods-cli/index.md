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

where `COMMAND` specifies the operation you want to perform with your Cloud Pods, e.g., `save` or `load`, `OPTIONS` specify the optional flags, and `ARGS` specifies the command arguments. Examples will follow.

## Commands

### save
The `save` command is used to create a new version of a Cloud Pod. Pro users have the option to dump the Cloud Pod locally or upload it to the LocalStack platform.
To dump the state locally, simply pass a local file URI as an argument to the `save` command. For instance, the following command:
```
localstack pod save file://<path_to_disk>/my-pod
```
will create a zip file named _my-pod_ to the specified location on the disk.
To use the Cloud Pods platform, simply specify the Cloud Pod's name as an argument, e.g.:
```
localstack pod save my-pod
```
This command creates a version of _my-pod_ and registers it to our platform.
Pushing already existing pod results in creating a new version of it and, eventually, uploading it to the platform.
Users can also select a subset of AWS services they wish to incorporate in a new Cloud Pod version with the `--services` option.

Users who want to make a Cloud Pod accessible outside their organization can mark it as *public* with the command `localstack pod push --name <pod_name> --visibility public`.
Please note that this command does not create a new version and requires a version to be already registered with the platform.

**Synopsis**
```
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

**Community Usage**
Community users have access to a restricted version of the `save` command. 
In particular, they can simply invoke the `save` command with a file URI as an argument.

### load

**Synopsis**
```
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

### delete

The `delete` command let users delete their remote or local Cloud Pods.

**Synopsis**
```
Delete a Cloud Pod.

Options:
  -n, --name TEXT  Name of the Cloud Pod.
  -l, --local      Delete only the local Cloud Pod, leaving the remote copy intact
```
### inject

The `inject` command let users inject a specific application state, previously saved, into the application runtime.
Please note that this is a local-only operation, i.e., the injecting state must be located on the host machine (usually under `~/.localstack/cloudpods/<pod_name>`).

By default, the injecting state updates the application runtime at a service level.
By using the `merge` injection strategy, the state of all services specified in the injecting state are reflected exactly in the application runtime, whilst all other active services remain unchanged.

The `--strategy` option can be used to change such default injection behaviour.
More specifically, the `overwrite` strategy will ensure the application runtime is an exact instance of the injecting state, and the `deep-merge` strategy will perform a fine-grain merge of the injecting state into the application runtime.

**Synopsis**
```
Inject the state from a locally available Cloud Pod version into the application runtime.

Options:
  -v, --version INTEGER  Version to inject (most recent one by default).
  -n, --name TEXT        Name of the cloud pod.
  -s, --strategy TEXT    Inject strategy (merge, overwrite, deep-merge).
```
### inspect

The `inspect` command simply lets the user inspect the content of a Cloud Pod.

**Synopsis**
```
Inspect the contents of a Cloud Pod.

Options:
  -n, --name TEXT    Name of the Cloud Pod.
  -f, --format TEXT  Format (curses, rich, json).
```

### status

The `status` command compiles a report of LocalStack current in-memory application runtime, or state, listing what Cloud Pod and Cloud Pod version have contributed to each AWS Service.
The set of active, or loaded, AWS Services is also given in this report so to distinguish which are not derivatives of Cloud Pod operations.

The `-v` option extends the default report to also include the sequence of state changing Cloud Pod operations, listing for each the type and affected AWS Services.

**Synopsis**
```
Lists what Cloud Pods have contributed to each service's current in-memory state.

Options:
  -v, --verbose      Include sequence of state changing Cloud Pod operations in the output.
  -f, --format TEXT  Format (curses, rich, json).
```


### list

The `list` command displays all the available Cloud Pods.
By default, it only shows the pods that have been uploaded to the platform.
The `-l` option will also show the locally available pods. 
The `-p` option will list all the available public Cloud Pods.

**Synopsis**

List all available Cloud Pods.
```
Options:
  -l, --local   List also locally available Cloud Pods
  -p, --public  List all public Cloud Pods.
```
### pull

The `pull` command retrieves the content of a Cloud Pod previously created and uploaded to the LocalStack platform and injects it into the application runtime.

By default, the fetched pod updates the application runtime at a service level, utilising a `merge` injection strategy.
Like the `inject` command, the `--strategy` option can change such default injection behaviour.

**Synopsis**
```
Incorporate the state of a Cloud Pod into the application runtime.

Options:
  -n, --name TEXT      Name of the cloud pod
  -s, --strategy TEXT  Inject strategy (merge, overwrite, deep-merge).
```
### push

The `push` command is used to create a new version of a Cloud Pods and upload it to the LocalStack platform.
A new version is created from the latest snapshot, e.g., taken with a previous `commit`.
A snapshot will be created at the moment of the push if no previous snapshot has been taken.
By default, a `push` operation will always retrieve the application state, create a Cloud Pod, and upload a version to the platform.
Users can use the `--local` flag if they wish to avoid the last step and keep the newly created pod on the host machine.
Users can also select a subset of AWS services they wish to incorporate in a new Cloud Pod version with the `--services` option.
Pushing an already existing pod results in creating a new version of it and, eventually, uploading it to the platform.

Users who want to make a Cloud Pod accessible outside their organization can mark it as *public* with the command `localstack pod push --name <pod_name> --visibility public`.
Please note that this command does not create a new version and requires a version to be already registered with the platform.

**Synopsis**
```
Create a new version of a Cloud Pod from the latest snapshot. A snapshot is created if it does not
exists yet.

Options:
  -l, --local            Create the Cloud Pod version only locally, without pushing to remote
  -m, --message TEXT     Add a comment describing the version.
  -n, --name TEXT        Name of the Cloud Pod.
  -s, --services TEXT    Comma-delimited list of services to push in the pods (all by default).
  --overwrite BOOLEAN    Overwrite a version with the content from the latest snapshot of the selected version.
  -v, --version INTEGER  Version to overwrite. Works with `--overwrite`.
  --visibility TEXT      Set the visibility of the Cloud Pod [`public` or `private`]. Does not create a new version.
```
### versions

The `versions` command simply lists all the available versions of a Cloud Pod.

**Synopsis**
```
List all available versions for a Cloud Pod.

Options:
  -n, --name TEXT  Name of the Cloud Pod.
```