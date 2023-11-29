---
title: "Auto-Load Cloud Pods"
weight: 99
description: >
  How to load automatically Cloud Pods in LocalStack environment
aliases:
  - /user-guide/cloud-pods/auto-load/
---

Apart from loading load Cloud Pods via either the [Command-Line Interface (CLI) Guide]({{< ref "pods-cli" >}}) or the web UI, you have the option to automatically load one or more Cloud Pods when the LocalStack container starts.

## Using environmental variables

The simplest way to load a Cloud Pod automatically when the LocalStack container starts is to use the `AUTO_LOAD_POD` [configuration variable](https://docs.localstack.cloud/references/configuration/).
For instance, to load a Cloud Pod named `foo-pod`, you can start LocalStack as follows:

{{< command >}}
$ AUTO_LOAD_POD=seed-pod localstack start
{{< / command >}}

`AUTO_LOAD_POD` accepts a comma-separated list of Cloud Pod names. 
Therefore, we support the auto-load of multiple Cloud Pods, e.g.;

{{< command >}}
$ AUTO_LOAD_POD=foo-pod,bar-pod localstack start
{{< / command >}}

Note that pods are loaded in the same order as given to `AUTO_LOAD_POD`.
When loading multiple Cloud Pods, the ones loaded last might overwrite the previous ones if they contain a state for the same service under the same account and region.

In a docker-compose file, this would look something like:
```yaml
version: "3.8"

services:
  localstack:
    container_name: "localstack-main"
    image: localstack/localstack-pro
    ports:
      - "127.0.0.1:4566:4566"
      - "127.0.0.1:4510-4559:4510-4559"
    environment:
      - DEBUG=1
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN-}
      - AUTO_LOAD_POD=foo-pod,bar-pod
    volumes:
      - "./volume:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

## Configuration file

LocalStack also supports configuration files to automatically load Cloud Pods at startup time.
//
Inside the container, LocalStack will iterate over the content of the `/etc/localstack/init-pod.d` folder looking for two kinds of files: 
`zip` files exported with the `localstack state export` command, 
`txt` files in which each line is the name of a Cloud Pod.

As example, let us assume the following project layout:

```console
.
├── docker-compose.yml
└── init-pods.d
    ├── pod-list.txt
    └── my-state.pod.zip
```

where the content of `pod-list.txt` is the following:

```text
foo-pod
bar-pod
```

The docker compose file will look something like this:

```yaml
version: "3.8"

services:
  localstack:
    container_name: "localstack-main"
    image: localstack/localstack-pro
    ports:
      - "127.0.0.1:4566:4566"
      - "127.0.0.1:4510-4559:4510-4559"
    environment:
      - DEBUG=1
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN-}
    volumes:
      - "./volume:/var/lib/localstack"
      - "./init-pods.d:/etc/localstack/init-pods.d"
```