---
title: "Managing extensions"
weight: 2
description: >
  How to manage LocalStack extensions in your LocalStack environment
tags: ["Pro image"]
---

You have different options to install and manage your LocalStack extensions depending on your environment and work style.

Extensions are managed through the LocalStack container, but stored in the [LocalStack volume]({{< ref "/references/filesystem#localstack-volume" >}}) on your host.
The next time you start up LocalStack, your extensions will still be there!

## Using the extensions manager in our App

The easiest way to manage official extensions is through our webapp and our [Extension Manager App](https://app.localstack.cloud/inst/default/extensions/manage).
Simply install and remove extensions from your specific LocalStack instance directly from the App.

If you have multiple instances of LocalStack, each instance has its own set of extensions,
and our App allows you to manage extensions for each instance individually.

{{< callout "tip" >}}
When you install or uninstall extensions, LocalStack needs to be restarted.
LocalStack will do this automatically for you!
It re-starts the process inside the running container, not the container itself.
However, you may lose LocalStack state if you do not use persistence.
{{</callout>}}


{{< figure src="extensions-manager.png" >}}

## Using the extensions CLI

If you use LocalStack with the CLI, you can also use our `localstack extensions` CLI command suite.
To get a list of all available commands in LocalStack Extensions, run:

{{< command >}}
$ localstack extensions --help

Usage: localstack extensions [OPTIONS] COMMAND [ARGS]...

Manage LocalStack extensions (preview)

Options:
-v, --verbose  Print more output
-h, --help     Show this message and exit

Commands:
dev        Developer tools for developing LocalStack extensions
init       Initialize the LocalStack extensions environment
install    Install a LocalStack extension
list       List installed extension
uninstall  Remove a LocalStack extension
{{< / command >}}

To install an extension, specify the name of the `pip` dependency that contains the extension. For example, for the official Stripe extension, you can either use the package distributed on PyPI:

{{< command >}}
$ localstack extensions install localstack-extension-httpbin
{{< / command >}}

Extensions are just Python pip packages, and the `install` command will accept anything that resolves to a valid pip package.
For example, you can install the latest development version directly from our Git repository using the `git+https` directive.

{{< command >}}
$ localstack extensions install "git+https://github.com/localstack/localstack-extensions/#egg=localstack-extension-httpbin&subdirectory=httpbin"
{{< / command >}}

If you have Python distribution as files on your local machine, for instance pip wheels or source distributions, then you can also install those via the `file://` directive
The file will be automatically mounted into the container and installed from there.

{{< command >}}
pip install file://./my-extensions/dist/my-extension-0.0.1.dev0.tar.gz
{{< / command >}}

### Specify the `LOCALSTACK_VOLUME_DIR`

Extensions should be installed in the `LOCALSTACK_VOLUME_DIR`. The default directory on your host is currently `~/.cache/localstack`. If you decide to mount a different directory to `/var/lib/localstack` in your docker-compose file, as shown below, you must specify the `LOCALSTACK_VOLUME_DIR` before installing extensions.

```yaml
volumes:
    - "/tmp/volume:/var/lib/localstack" # LOCALSTACK_VOLUME_DIR mount
    - "/var/run/docker.sock:/var/run/docker.sock"
```

Here's how you can use `LOCALSTACK_VOLUME_DIR` in your commands:

{{< command >}}
export LOCALSTACK_VOLUME_DIR=/tmp/volume
localstack extensions install file:///tmp/my_files/my-extension-1.0.0.tar.gz
{{< / command >}}

## Automating extensions installation

When you are working in CI or with docker-compose, you may want to automate extension management.
LocalStack provides two ways to do this:

### Environment variable

The `EXTENSION_AUTO_INSTALL` variable is interpreted by LocalStack at startup,
to ensure that the extensions set in the variable value are installed when the container starts up.

The value is a comma-separated list of extensions directives that can also be specified in `localstack extensions install`.
If you want to use the `file://` directive, the distribution file needs to be mounted into the container.

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
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?}
      - DEBUG=1
      - EXTENSION_AUTO_INSTALL=localstack-extension-mailhog,localstack-extension-httpbin
    volumes:
      - "./volume:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
```

### Configuration file

LocalStack also supports configuration files to automatically install extensions.

Inside the container, LocalStack will resolve the file `/etc/localstack/conf.d/extensions.txt`, and will install all extensions defined in this list.
Since LocalStack extensions are essentially just Python pip packages, the `extensions.txt` has the same format as a [pip requirements file](https://pip.pypa.io/en/stable/reference/requirements-file-format/).

An example project could look something like this:

* `extensions.txt`
  ```
  localstack-extension-mailhog
  git+https://github.com/localstack/localstack-extensions/#egg=localstack-extension-aws-replicator&subdirectory=aws-replicator
  ```
*  Project layout:
    ```console
    extension-install
    ├── conf.d
    │   └── extensions.txt
    └── docker-compose.yml
    ```
* `docker-compose.yaml`
    ```yaml
    version: "3.8"

    services:
      localstack:
        ...
        volumes:
          - "./volume:/var/lib/localstack"
          - "conf.d:/etc/localstack/conf.d"
          - "/var/run/docker.sock:/var/run/docker.sock"
    ```

When LocalStack starts up, you should see it tries to install the extensions and all their dependencies.

## Extension Management within LocalStack

Extensions in LocalStack are Python distributions that operate within their dedicated virtual environment, residing in the [LocalStack Volume]({{< ref "filesystem" >}}). This involves the creation of a"variable packages folder `/var/lib/localstack/lib`," where the volume management system establishes both an `extensions` folder and a virtual environment named `python_venv`. Within this environment, all extensions and their dependencies are managed. LocalStack integrates its virtual environment, ensuring the resolution of all transitive dependencies associated with extensions.

Here's an example what the default LocalStack volume looks like after installing the MailHog extension:

```bash
$ pwd
~/.cache/localstack/volume
$ tree -L 4
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
