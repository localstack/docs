---
title: "Cloud Pods CLI"
weight: 5
categories: ["LocalStack Pro", "Tools", "Persistence", "CLI"]
description: >
  LocalStack provides a command line tool to manage the state of your instance via Cloud Pods.
---

## Syntax
Use the following syntax to run `localstack pod` commands from your terminal window:

```bash
localstack pod [command] [options]
```

where `command` specifies the operation you want to perform with your Cloud Pods, e.g., `pull` or `push`, and `options` specifies the optional flag.
For example, you can attach a specific message to a snapshot using the `-m` option while doing a `commit` operation.

## Configuration
The CRUD commands exposed with the Cloud Pods CLI expect a `--name <pod_name>` option to specify the pod's name.
Users can avoid specifying a pod name at every command by setting a global config with the `config` command.

For instance, the following command
```
localstack config --name my_pod
```
will implicitly pass a pod name to all subsequent CLI commands.
Such a configuration will be saved locally on the host machine in a JSON file (e.g., in `~/.localstack/cloudpods/pods-config.json`).

## Commands

### commit

The `commit` command creates a snapshot of your LocalStack running instance and locally saves it on the host machine.

**Synopsis**
```
Commit a snapshot of the LocalStack running instance.

Options:
  -m, --message TEXT   Add a comment describing the snapshot.
  -n, --name TEXT      Name of the Cloud Pod.
  -s, --services TEXT  Comma-delimited list of services to push in the pods (all, by default).
```

### config

The `config` command saves some configuration values that apply to all the subsequent CLI commands.
For instance with `localstack pod config --name <my_name>` users can avoid specifying a pod name for other commands like `pull` or `push`.
Users can specify a list of services with the following command:
```
localstack pod config --services sqs,sns
```
The following CRUD operation will only take into account the selected service and not the entire LocalStack application state.

**Synopsis**

```
Configure a set of parameters for all Cloud Pods commands.

Options:
  -n, --name TEXT      Name of the Cloud Pod.
  -s, --services TEXT  Comma-delimited list of services or `all` to enable all (default).
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

By default, the injecting state will replace the application runtime.
The `--merge` option, instead, will first merge the injecting state with the current runtime and then inject the result.

**Synopsis**
```
Inject the state from a locally available Cloud Pod version into the application runtime.

Options:
  --merge                Merge the injecting state with the current application runtime.
  -v, --version INTEGER  Version to inject (most recent one by default).
  -n, --name TEXT        Name of the cloud pod.
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
The set of active, or loaded, AWS Services is also given in this report so to distinguish which are not derivatives of CloudPod operations.

The `-v` option extends the default report to also include the sequence of state changing Cloud Pod operations, listing for each the type and affected AWS Services.

**Synopsis**
```
Lists what Cloud Pods have contributed to each service's current in-memory state.

Options:
  -v, --verbose      Include in the output the sequence of state changing CloudPod operations.
  -f, --format TEXT  Format (curses, rich, json).
```


### list

The `list` command displays all the available Cloud Pods.
By default, it only shows the pods that have been uploaded to the platform.
The `-l` option will also show the locally available pods.

**Synopsis**

List all available Cloud Pods.
```
Options:
  -l, --local  List also locally available Cloud Pods
```
### pull

The `pull` command retrieves the content of a Cloud Pod previously created and uploaded to the LocalStack platform and injects it into the application runtime.
By default, the fetched pod will always be injected.
The `--fetch` option will instead only trigger the download of the desired Cloud Pods to the host machine, without performing any additional operation.
Users could then, for instance, use the `--inject` command to inject the retrieved pods.
Similar to the `--inject` command, users can specify the `--merge` flag (off by default) if they wish to merge the current application state with the injecting one.

**Synopsis**
```
Incorporate the state of a Cloud Pod into the application runtime.

Options:
  -n, --name TEXT  Name of the cloud pod
  --merge          Merge the injecting state with the current application runtime.
  --fetch          Only fetch the Cloud Pod from the remote platform.
```
### push

The `push` command is used to create a new version of a Cloud Pods and upload it to the LocalStack platform.
A new version is created from the latest snapshot, e.g., taken with a previous `commit`.
A snapshot will be created at the moment of the push if no previous snapshot has been taken.
By default, a `push` operation will always retrieve the application state, create a Cloud Pod, and upload a version to the platform.
Users can use the `--local` flag if they wish to avoid the last step and keep the newly created pod on the host machine.
Users can also select a subset of AWS services they wish to incorporate in a new Cloud Pod version with the `--services` option.
Pushing an already existing pod results in creating a new version of it and, eventually, uploading it to the platform.

**Synopsis**
```
Create a new version of a Cloud Pod from the latest snapshot. A snapshot is created if it does not
exists yet.

Options:
  -l, --local            Create the Cloud Pod version only locally, without pushing to remote
  -m, --message TEXT     Add a comment describing the version.
  -n, --name TEXT        Name of the Cloud Pod.
  -s, --services TEXT    Comma-delimited list of services to push in the pods (all by default).
  --overwrite BOOLEAN    Overwrite a version with the content from the latest snapshot of the selected
                         version.
  -v, --version INTEGER  Version to overwrite. Works with `--overwrite`
```
### versions

The `versions` command simply lists all the available versions of a Cloud Pod.

**Synopsis**
```
List all available versions for a Cloud Pod.

Options:
  -n, --name TEXT  Name of the Cloud Pod.
```