---
title: "Extensions Reference"
linkTitle: "Extensions"
weight: 50
description: >
  References for using and building LocalStack extensions.
aliases:
  /references/localstack-extensions/
---

Extensions are a powerful system to extend and customize LocalStack with additional features, emulators, or custom functionality.

## Using extensions

Find a user-oriented guide on extensions [here]({{< ref "/user-guide/extensions" >}}).
* [Managing extensions]({{< ref "managing-extensions" >}})
* [Developing extensions]({{< ref "developing-extensions" >}})
* [List of official extensions]({{< ref "official-extensions" >}})

## Extensions API reference

* [Extension interface to implement](https://github.com/localstack/localstack-extensions#the-extensions-api)
* [Extension API in our core codebase](https://github.com/localstack/localstack/tree/master/localstack/extensions/api)

## Extension configuration

### Environment variables

| Environment Variable   | Description                                                                                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EXTENSION_DEV_MODE     | Enable/disable developer mode for extensions. Developer mode will mount local extension sources automatically into the container. See our user guide on [developing extensions]({{<ref "developing-extensions" >}}) |
| EXTENSION_AUTO_INSTALL | A comma-separated list of extensions that will be installed automatically as the container starts up                                                                                                                |


### Paths in the container

* `/etc/localstack/conf.d/extensions.txt`: a file following the [pip requirements file format](https://pip.pypa.io/en/stable/reference/requirements-file-format/) that will automatically be installed on container startup.
  This file can contain a list of extensions.


## How extensions are managed

Extensions are Python distributions managed in their own virtual environment within the [LocalStack Volume]({{< ref "filesystem" >}}).
Specifically, within the "variable packages folder `/var/lib/localstack/lib`", the volume management system creates a folder `extensions` and a virtual environment `python_venv`, where all extensions and their dependencies live.
LocalStack's own virtual environment is linked so it resolves all transitive dependencies of extensions.

Here's an example what the default LocalStack volume looks like after installing the MailHog extension:

```console
thomas@om ~/.cache/localstack/volume
 % tree -L 4
.
├── cache
│   ├── ...
├── lib
│   ├── extensions
│   │   └── python_venv
│   │       ├── bin
│   │       ├── include
│   │       ├── lib
│   │       ├── lib64 -> lib
│   │       └── pyvenv.cfg
│   └── mailhog
│       └── v1.0.1
│           └── MailHog_linux_amd64
├── logs
└── tmp
    └── state
```
