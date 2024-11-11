---
title: "Starting LocalStack"
weight: 20
hide_readingtime: true
description: >
  Basic installation guide to get started with LocalStack on your local machine.
cascade:
  type: docs
---
## Install LocalStack CLI

The quickest way get started with LocalStack is by using the LocalStack CLI.
It allows you to start LocalStack from your command line.
Please make sure that you have a working [Docker installation](https://docs.docker.com/get-docker/) on your machine before moving on.

The CLI starts and manages the LocalStack Docker container.
For alternative methods of managing the LocalStack container, see our [alternative installation instructions]({{< ref "#alternatives" >}}).

{{< tabpane text=true >}}

<!--
Linux
-->

{{< tab header="**Linux**" >}}

<p>
You can download the pre-built binary for your architecture using the link below:
</p>

<p>
{{< cli-binary-download os="linux" >}}
</p>

<p>
or use the curl commands below:
</p>

<p>
For x86-64:
{{< command >}}
$ curl --output localstack-cli-{{< localstack-latest-version >}}-linux-amd64-onefile.tar.gz \
    --location https://github.com/localstack/localstack-cli/releases/download/v{{< localstack-latest-version >}}/localstack-cli-{{< localstack-latest-version >}}-linux-amd64-onefile.tar.gz
{{< / command >}}
</p>

<p>
For ARM64:
{{< command >}}
$ curl --output localstack-cli-{{< localstack-latest-version >}}-linux-arm64-onefile.tar.gz \
    --location https://github.com/localstack/localstack-cli/releases/download/v{{< localstack-latest-version >}}/localstack-cli-{{< localstack-latest-version >}}-linux-arm64-onefile.tar.gz
{{< / command >}}
</p>

<p>
Then extract the LocalStack CLI from the terminal:
{{< command >}}
$ sudo tar xvzf localstack-cli-{{< localstack-latest-version >}}-linux-*-onefile.tar.gz -C /usr/local/bin
{{< / command >}}
</p>

<details>
<summary><b>Alternative: Homebrew on Linux</b></summary>

<p>
If you are using <a href="https://docs.brew.sh/Homebrew-on-Linux">Homebrew for Linux</a>, you can install the LocalStack CLI directly from our official LocalStack tap:
{{< command >}}
$ brew install localstack/tap/localstack-cli
{{< / command >}}
</p>

</details>

{{< /tab >}}

<!--
MacOS
-->

{{< tab header="**MacOS**" >}}

<p>
You can install the LocalStack CLI using Brew directly from our official LocalStack tap:
{{< command >}}
$ brew install localstack/tap/localstack-cli
{{< / command >}}
</p>

<details>
<summary><b>Alternative: Binary Download</b></summary>

<p>
You may download the binary for your architecture using the link below:
</p>

<p>
{{< cli-binary-download os="macos" >}}
</p>

<p>
or use the following curl command:
{{< command >}}
$ curl --output localstack-cli-{{< localstack-latest-version >}}-darwin-amd64-onefile.tar.gz \
    --location https://github.com/localstack/localstack-cli/releases/download/v{{< localstack-latest-version >}}/localstack-cli-{{< localstack-latest-version >}}-darwin-amd64-onefile.tar.gz
{{< / command >}}
</p>

<p>
Then extract the LocalStack CLI from the terminal:
{{< command >}}
$ sudo tar xvzf localstack-cli-{{< localstack-latest-version >}}-darwin-*-onefile.tar.gz -C /usr/local/bin
{{< / command >}}
</p>
</details>
{{< /tab >}}

<!--
Windows
-->

{{< tab header="**Windows**" >}}
<p>
You can download the pre-built binary for your architecture using the link below:
</p>

<p>
{{< cli-binary-download os="windows" >}}
</p>

<p>
Then extract the archive and execute the binary in Powershell.
</p>
</details>
{{< /tab >}}

<!--
Python
-->

{{< tab header="**Other/Python**" >}}
<p>
If you cannot use the binary releases of LocalStack, you can install the Python distribution.
</p>

<p>
Please make sure to install the following before moving ahead:
{{% markdown %}}
- [Python](https://docs.python.org/3/using/index.html) (versions 3.7 to 3.11)
- [pip](https://pip.pypa.io/en/stable/installation/)
{{% /markdown %}}
</p>

<p>
Next install the LocalStack CLI in your Python environment by running:
{{< command >}}
$ python3 -m pip install --upgrade localstack
{{< / command >}}
</p>

{{< callout "note" >}}
To download a specific version of LocalStack, replace `<version>` with the required version from [release page](https://github.com/localstack/localstack/releases).

{{< command >}}
$ python3 -m pip install localstack==<version>
{{< /command >}}
{{< /callout >}}

{{< callout "tip" >}}
If you have problems with permissions in MacOS X Sierra, install with:
{{< command >}}
$ python3 -m pip install --user localstack
{{< /command >}}

{{< /callout >}}
{{< callout "warning" >}}
Do not use `sudo` or the `root` user when starting LocalStack.
It should be installed and started entirely under a local non-root user.
{{< /callout >}}

{{< /tab >}}
{{< /tabpane >}}

To verify that the LocalStack CLI was installed correctly, you can check the version in your terminal:
{{< command >}}
$ localstack --version
{{< localstack-latest-version >}}
{{< / command >}}

You are all set!

### Start LocalStack via the CLI

Now that the CLI is installed you can use it to quickly start LocalStack!
{{< command >}}
$ localstack auth set-token <YOUR_AUTH_TOKEN> # only needed once
$ localstack start # use -d flag to start localstack in background (detached)
{{< localstack-latest-version >}}
{{< / command >}}

## What's next?

Now that you have LocalStack up and running, the following resources might be useful for your next steps:
- Check out our [Quickstart guide]({{< ref "quickstart" >}}) if you are a new user to get started with LocalStack quickly.
- [Use the LocalStack integrations]({{< ref "integrations" >}}) to interact with LocalStack and other integrated tools, for example:
  - Use `awslocal` to use the AWS CLI against your local cloud!
  - Use the Serverless Framework with LocalStack!
  - And many more!
- [Find out how to configure LocalStack]({{< ref "configuration" >}}) such that it perfectly fits your need.
- [Use LocalStack in your CI environment]({{< ref "user-guide/ci" >}}) to increase your code quality.
- [Checkout LocalStack's Cloud Developer Tools]({{< ref "user-guide/tools" >}}) to further increase your development efficiency with LocalStack.
- Find out about the ways you can [configure LocalStack]({{< ref "configuration" >}}).



## Alternative ways to start LocalStack

Besides using the CLI, there are other ways of starting and managing your LocalStack instance:

- [LocalStack Desktop]({{< ref "#localstack-desktop" >}})\
  Get a desktop experience and work with your local LocalStack instance via the UI.

- [LocalStack Docker Extension]({{< ref "#localstack-docker-extension" >}})\
  Use the LocalStack extension for Docker Desktop to work with your LocalStack instance.

- [Docker-Compose]({{< ref "#docker-compose" >}})\
  Use Docker Compose to configure and start your LocalStack Docker container.

- [Docker]({{< ref "#docker" >}})\
  Use the Docker CLI to manually start the LocalStack Docker container.

- [Helm]({{< ref "#helm" >}})\
  Use Helm to create a LocalStack deployment in a Kubernetes cluster.

LocalStack runs inside a Docker container, and the above options are different ways to start and manage the LocalStack Docker container.

The localstack emulator is released and made available vie docker hub in two editions: The Community Edition `localstack/localstack` and the the Pro Edition `localstack/localstack-pro`.
To use advanced features and access additional emulated services in LocalStack, the use of the `localstack/localstack-pro` image is required.

For a comprehensive overview of the LocalStack images, check out our [Docker images documentation]({{< ref "docker-images" >}}).

### LocalStack Desktop

Learn more about our desktop client at [LocalStack Desktop]({{< ref "localstack-desktop" >}}) and download it [here](https://app.localstack.cloud/download).

### LocalStack Docker Extension

Install our [official Docker Desktop extension](https://hub.docker.com/extensions/localstack/localstack-docker-desktop) to manage LocalStack.
See [LocalStack Docker Extension]({{< ref "localstack-docker-extension" >}}) for more information.

### Docker-Compose

To use LocalStack without the [LocalStack CLI]({{< ref "#localstack-cli" >}}), you have the option of running the LocalStack Docker container by yourself.
If you want to manually manage your Docker container, it's usually a good idea to use [Docker Compose](https://docs.docker.com/compose/reference/) in order to simplify your container configuration.

#### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (version 1.9.0+)

#### Starting LocalStack with Docker-Compose

You can start LocalStack with [Docker Compose](https://docs.docker.com/compose/) by configuring a `docker-compose.yml` file.
Docker Compose v1.9.0 and above is supported.

{{< tabpane lang="yml" >}}
{{< tab header="Pro" lang="yml" >}}
services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack-pro  # required for Pro
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
      - "127.0.0.1:443:443"              # LocalStack HTTPS Gateway (Pro)
    environment:
      # Activate LocalStack Pro: https://docs.localstack.cloud/getting-started/auth-token/
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?}  # required for Pro
      # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
      - DEBUG=${DEBUG:-0}
      - PERSISTENCE=${PERSISTENCE:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
{{< /tab >}}
{{< tab header="Community" lang="yml" >}}
services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
    environment:
      # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
      - DEBUG=${DEBUG:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
{{< /tab >}}
{{< /tabpane >}}

Start the container by running the following command:

{{< command >}}
$ docker-compose up
{{< / command >}}

{{< callout "note" >}}
- This command pulls the current nightly build from the `master` branch (if you don't have the image locally) and **not** the latest supported version.
  If you want to use a specific version, set the appropriate LocalStack image tag at `services.localstack.image` in the `docker-compose.yml` file (for example `localstack/localstack:<version>`).

- If you are using LocalStack with an [Auth Token]({{< ref "auth-token" >}}), you need to specify the image tag as `localstack/localstack-pro` in the `docker-compose.yml` file.
  Going forward, `localstack/localstack-pro` image will contain our Pro-supported services and APIs.

- This command reuses the image if it's already on your machine, i.e. it will **not** pull the latest image automatically from Docker Hub.

- Mounting the Docker socket `/var/run/docker.sock` as a volume is required for some services that use Docker to provide the emulation, such as AWS Lambda.
  Check out the [Lambda providers]({{< ref "user-guide/aws/lambda" >}}) documentation for more information.

- To facilitate interoperability, configuration variables can be prefixed with `LOCALSTACK_` in docker.
  For instance, setting `LOCALSTACK_PERSISTENCE=1` is equivalent to `PERSISTENCE=1`.

- If using the Docker default bridge network using `network_mode: bridge`, container name resolution will not work inside your containers.
  Please consider removing it, if this functionality is needed.

- To configure an Auth Token, refer to the [Auth Token]({{< ref "auth-token" >}}) documentation.
{{< /callout >}}

Please note that there are a few pitfalls when configuring your stack manually via docker-compose (e.g., required container name, Docker network, volume mounts, and environment variables).
We recommend using the LocalStack CLI to validate your configuration, which will print warning messages in case it detects any potential misconfigurations:

{{< command >}}
$ localstack config validate
...
{{< / command >}}

### Docker

You can also directly start the LocalStack container using the Docker CLI instead of [Docker-Compose]({{< ref "#docker-compose" >}}).
This method requires more manual steps and configuration, but it gives you more control over the container settings.

#### Prerequisites

Please make sure that you have a working [Docker installation](https://docs.docker.com/get-docker/) on your machine before moving on.
You can check if Docker is correctly configured on your machine by executing `docker info` in your terminal.
If it does not report an error (but shows information on your Docker system), you're good to go.

#### Starting LocalStack with Docker

You can start the Docker container simply by executing the following `docker run` command:

{{< tabpane text=true >}}

{{< tab header="Community" >}}
{{< command >}}
$ docker run \
  --rm -it \
  -p 127.0.0.1:4566:4566 \
  -p 127.0.0.1:4510-4559:4510-4559 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  localstack/localstack
{{< /command >}}
{{< /tab >}}

{{< tab header="Pro" >}}
{{< command >}}
$ docker run \
  --rm -it \
  -p 127.0.0.1:4566:4566 \
  -p 127.0.0.1:4510-4559:4510-4559 \
  -p 127.0.0.1:443:443 \
  -e LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?} \
  -v /var/run/docker.sock:/var/run/docker.sock \
  localstack/localstack-pro{{< /tab >}}
{{< /command >}}
{{< /tabpane >}}

{{< callout "note" >}}
- This command pulls the current nightly build from the `master` branch (if you don't have the image locally) and **not** the latest supported version.
  If you want to use a specific version of LocalStack, use the appropriate tag: `docker run --rm -it -p 4566:4566 -p 4510-4559:4510-4559 localstack/localstack:<tag>`.
  Check-out the [LocalStack releases](https://github.com/localstack/localstack/releases) to know more about specific LocalStack versions.

- If you are using LocalStack with an [Auth Tsoken]({{< ref "auth-token" >}}), you need to specify the image tag as `localstack/localstack-pro` in your Docker setup.
  Going forward, `localstack/localstack-pro` image will contain our Pro-supported services and APIs.

- This command reuses the image if it's already on your machine, i.e. it will **not** pull the latest image automatically from Docker Hub.

- Mounting the Docker socket `/var/run/docker.sock` as a volume is required for some services that use Docker to provide the emulation, such as AWS Lambda.
  Check out the [Lambda providers]({{< ref "user-guide/aws/lambda" >}}) documentation for more information.

- When using Docker to manually start LocalStack, you will have to configure the container on your own (see [docker-compose-pro.yml](https://github.com/localstack/localstack/blob/master/docker-compose-pro.yml) and [Configuration]({{< ref "configuration" >}})).
  This could be seen as the "expert mode" of starting LocalStack.
  If you are looking for a simpler method of starting LocalStack, please use the [LocalStack CLI]({{< ref "#localstack-cli" >}}).

- To facilitate interoperability, configuration variables can be prefixed with `LOCALSTACK_` in docker.
  For instance, setting `LOCALSTACK_PERSISTENCE=1` is equivalent to `PERSISTENCE=1`.

- To configure an Auth Token, refer to the [Auth Token]({{< ref "auth-token" >}}) documentation.
{{< /callout >}}

### Helm

If you want to deploy LocalStack in your [Kubernetes](https://kubernetes.io) cluster, you can use [Helm](https://helm.sh).

#### Prerequisites

- [Kubernetes](https://kubernetes.io)
- [Helm](https://helm.sh/docs/intro/install/)

#### Deploy LocalStack using Helm

You can deploy LocalStack in a Kubernetes cluster by running these commands:
{{< command >}}
$ helm repo add localstack-repo https://helm.localstack.cloud
$ helm upgrade --install localstack localstack-repo/localstack
{{< / command >}}

The Helm charts are not maintained in the main repository, but in a [separate one](https://github.com/localstack/helm-charts).

## Updating

The LocalStack CLI allows you to easily update the different components of LocalStack.
To check the various options available for updating, run:
{{< command >}}
$ localstack update --help
Usage: localstack update [OPTIONS] COMMAND [ARGS]...

  Update different LocalStack components.

Options:
  -h, --help  Show this message and exit.

Commands:
  all             Update all LocalStack components
  docker-images   Update docker images LocalStack depends on
  localstack-cli  Update LocalStack CLI
{{< / command >}}

{{< callout >}}
Updating the LocalStack CLI using `localstack update localstack-cli` and `localstack update all` will work only if it was installed from the Python distribution.
If it was installed using the pre-built binary or via Brew, please run the installation steps again to update to the latest version.
{{< /callout >}}

## Troubleshooting

### The LocalStack CLI installation is successful, but I cannot execute `localstack`

If you can successfully install LocalStack using `pip` but you cannot use it in your terminal, you most likely haven't set up your operating system's / terminal's `PATH` variable (in order to tell them where to find programs installed via `pip`).
- If you are using Windows, you can enable the `PATH` configuration when installing Python, [as described in the official docs of Python](https://docs.python.org/3/using/windows.html#finding-the-python-executable).
- If you are using a MacOS or Linux operating system, please make sure that the `PATH` is correctly set up - either system wide, or in your terminal.

As a workaround you can call the LocalStack CLI python module directly:
{{< command >}}
$ python3 -m localstack.cli.main
{{< / command >}}

### The `localstack` CLI does not start the LocalStack container

If you are using the `localstack` CLI to start LocalStack, but the container is not starting, please check the following:
- Uncheck the **Use kernel networking for UDP** option in Docker Desktop (**Settings** → **Resources** → **Network**) or follow the steps in our [documentation](https://docs.localstack.cloud/user-guide/tools/dns-server/#system-dns-configuration) to disable it.
- Start LocalStack with a specific DNS address:
{{< command >}}
$ DNS_ADDRESS=0 localstack start
{{< / command >}}
- Remove port 53 as indicated in our [standard `docker-compose.yml`  file](https://github.com/localstack/localstack/blob/master/docker-compose-pro.yml).

### How should I access the LocalStack logs on my local machine?

You can now avail logging output and error reporting using LocalStack logs.
To access the logs, run the following command:

{{< command >}}
$ localstack logs
{{< / command >}}

AWS requests are now logged uniformly in the INFO log level (set by default or when `DEBUG=0`).
The format is:

```text
AWS <service>.<operation> => <http-status> (<error type>)
```

Requests to HTTP endpoints are logged in a similar way:

```text
2022-09-12T10:39:21.165  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.ListBuckets => 200
2022-09-12T10:39:41.315  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.CreateBucket => 200
2022-09-12T10:40:04.662  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.PutObject => 200
2022-09-12T11:01:55.799  INFO --- [   asgi_gw_0] localstack.request.http    : GET / => 200
```

### Common activation issues

Starting from version 2.0.0, the `localstack/localstack-pro` image in LocalStack demands a successful license activation for startup.
If the activation of the license is unsuccessful, LocalStack will exit and display error messages.

```bash
===============================================
License activation failed! 🔑❌

Reason: The credentials defined in your environment are invalid. lease make sure to set the
        ENV_LOCALSTACK_AUTH_TOKEN variable to a valid auth token. You can find your auth
        token in the LocalStack web app https://app.localstack.cloud."

Due to this error, Localstack has quit. LocalStack pro features can only be used with a valid license.

- Please check that your credentials are set up correctly and that you have an active license.
  You can find your credentials in our webapp at https://app.localstack.cloud.
- If you want to continue using LocalStack without pro features you can set `ACTIVATE_PRO=0`.
```

The activation of LocalStack may fail for several reasons, and the most common ones are listed below in this section.

#### Licensing-related configuration

To avoid logging any licensing-related error messages, set `LOG_LICENSE_ISSUES=0` in your environment.
Refer to our [configuration guide](https://docs.localstack.cloud/references/configuration/#localstack-pro) for more information.

#### Checking license activation

The simplest method to verify if LocalStack is active is by querying the health endpoint for a list of running services:

{{< tabpane text=true >}}
{{< tab header="macOS/Linux" lang="shell" >}}

{{< command >}}
$ curl http://localhost:4566/_localstack/info | jq
{{< / command >}}

{{< /tab >}}
{{< tab header="Windows" lang="powershell" >}}

{{< command >}}
$ Invoke-WebRequest -Uri http://localhost:4566/_localstack/info | ConvertFrom-Json
{{< / command >}}

{{< /tab >}}
{{< /tabpane >}}

The following output would be retrieved:

```bash
{
  "version": "3.0.0:6dd3f3d",
  "edition": "pro",
  "is_license_activated": true,
  "session_id": "7132da5f-a380-44ca-8897-6f0fdfd7b1c9",
  "machine_id": "0c49752c",
  "system": "linux",
  "is_docker": true,
  "server_time_utc": "2023-11-21T05:41:33",
  "uptime": 161
}
````

You can notice the `edition` field is set to `pro` and the `is_license_activated` field is set to `true`.
Another way to confirm this is by checking the logs of the LocalStack container for a message indicating successful license activation:

{{< command >}}
[...] Successfully activated license
{{< / command >}}


#### Missing Credentials

You need to provide an Auth Token to start the LocalStack Pro image successfully.
You can find your Auth Token on the [Auth Token page](https://app.localstack.cloud/workspace/auth-tokens) in the LocalStack Web App.

If you are using the `localstack` CLI, you can set the `LOCALSTACK_AUTH_TOKEN` environment variable to your Auth Token or use the following command to set it up:

{{< command >}}
$ localstack auth set-token <YOUR_AUTH_TOKEN>
{{< / command >}}

#### Invalid License

The issue may occur if there is no valid license linked to your account due to expiration or if the license has not been assigned.
You can check your license status in the LocalStack Web Application on the [My License page](https://app.localstack.cloud/workspace/my-license).

#### License Server Unreachable

LocalStack initiates offline activation when the license server is unreachable, requiring re-activation every 24 hours.
Log output may indicate issues with your machine resolving the LocalStack API domain, which can be verified using a tool like `dig`:

{{< command >}}
$ dig api.localstack.cloud
{{< / command >}}

If the result shows a status other than `status: NOERROR`, your machine is unable to resolve this domain.
Certain corporate DNS servers may filter requests to specific domains.
Kindly reach out to your network administrator to safelist `localstack.cloud` domain.

If you have any further problems concerning your license activation, or if the steps do not help, do not hesitate to [contact us](https://localstack.cloud/contact/).

### How should I share the LocalStack logs for troubleshooting?

You can share the LocalStack logs with us to help us identify issues.
To share the logs, call the diagnostic endpoint:

{{< command >}}
$ curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz
{{< / command >}}

Ensure that the diagnostic endpoint is run after you have tried reproducing the affected task.
After running the task, run the diagnostic endpoint and share the archive file with your team members or LocalStack Support.

### My application cannot reach LocalStack over the network

We have extensive network troubleshooting documentation available [here]({{< ref "references/network-troubleshooting" >}}).

If this does not solve your problem then please [reach out]({{< ref "help-and-support" >}}).

