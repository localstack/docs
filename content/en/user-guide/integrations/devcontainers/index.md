---
title: "DevContainers"
linkTitle: "DevContainers"
description: >
  Use DevContainers with LocalStack
---

## Overview

[DevContainers](https://containers.dev/) is a local tool to create a self-contained, reproducible and containerized development environment that you can setup to encapsulate your project with all its libraries and dependencies.

In this guide, you will learn how to use [DevContainers](https://containers.dev/) with LocalStack.
You can use the following two approaches to set up LocalStack with DevContainers:

* [LocalStack templates](#localstack-templates)
* [LocalStack feature](#localstack-feature)

## LocalStack Templates

LocalStack provides two different approaches for [Templates](https://github.com/localstack/devcontainer-template) which can be used via [supporting tools](https://containers.dev/supporting).

| **Type**                     | **Advantages**                                                                                      | **Disadvantages**                                                                                                                                                                         |
|------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Docker-in-Docker**         | • Strict separation from host Docker service<br>• Control LocalStack with LocalStack CLI<br>• All-in-one container      | • Resources are limited as all resources spawned by LocalStack are encapsulated within the container<br>• LocalStack volume directory must exist beforehand<br>• Larger container size<br>• Cannot use existing images on host system |
| **Docker-outside-of-Docker** | • Easy addition of external services managed by Docker Compose<br>• DNS service for custom domains | • Host's Docker socket mounted into containers, raising security concerns<br>• Limited LocalStack CLI usage<br>• LocalStack volume directory must exist beforehand                        |

### Docker-in-Docker

* [Dev Container CLI](#dev-container-cli)
* [VS Code](#vscode)
* [Reference file](#reference-file)

#### Dev Container CLI

You can use the DevContainer CLI to create a `devcontainer.json` file from the LocalStack template.
Before you start, ensure that you have the [DevContainer CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli) installed.

Create a JSON file called `options.json` with the desired options in it.

```json
{
    "imageVariant": "bullseye",
    "awslocal": "true",
    "logLevel": "debug",
    "debug": "true",
    "startup": "true"
}
```

Use the command below to generate your `devcontainer.json` from the template.
Include additional features with the `--features` option if needed.

{{< command >}}
$ devcontainer templates apply \
    --template-id ghcr.io/localstack/devcontainer-template/localstack-dind \
    --template-args "$(cat ./options.json)" \
    --features '[{"id":"ghcr.io/devcontainers/features/aws-cli:1"}]'
{{< /command >}}

Start your container using the following command.

{{< command >}}
$ devcontainer up --id-label project=localstack --workspace-folder .
{{< /command >}}

Connect to it using the `id-label`.

{{< command >}}
$ devcontainer exec --id-label project=localstack /bin/bash
{{< /command >}}

Check that the LocalStack CLI is installed by executing:

{{< command >}}
vscode ➜ ~ $ localstack --version
3.6.0
vscode ➜ ~ $
{{< /command >}}

To remove the container, run this cleanup script since the Dev Container CLI cannot currently do it.

{{< command >}}
$ for container in $(docker ps -q); do \
    [[ "$(docker inspect --format '{{ index .Config.Labels "project"}}' $container)" = "localstack" ]] && \
    docker rm -f $container; \
done
{{< /command >}}

#### VSCode

{{< callout >}}
The DevContainer extension is currently reporting issues & bugs.
Follow the [issue](https://github.com/microsoft/vscode-remote-release/issues/10180) for details.
{{< /callout >}}

To get started with LocalStack and DevContainers in VS Code, follow these steps:

* Open VS Code with the DevContainers extension installed.
* From the Command Palette, select **Dev Containers: Add Dev Container configuration file**.
  <br><br>
  <img alt="Add Dev Container configuration file" src="01_add_devcontainer_conf.png" width="800px" />
  <br><br>

* Choose **Add configuration to workspace**; alternatively, select **Add configuration to user data folder** for general usage.
  <br><br>
  <img alt="Add configuration to workspace" src="02_add_conf_workspace.png" width="800px" />
  <br><br>

* Select **Show All Definitions...** to view community templates.
  <br><br>
  <img alt="Show all Template definitions" src="03_show_all_definitions.png" width="800px" />
  <br><br>

* Filter by typing "localstack" in the search bar and select the **LocalStack Docker-in-Docker** template.
  <br><br>
  <img alt="Select official LocalStack Template (DinD)" src="04a_select_template_dind.png" width="800px" />
  <br><br>

* Proceed through the configuration by selecting or entering values.
  Pressing **Enter** through the options will apply default settings, which include:
  <br><br>
  * Select the image variant (only Debian-based images are supported).
    <br><br>
    <img alt="Image variant option" src="05_option_1.png" width="800px" />
    <br><br>
  * Select the log level.
    <br><br>
    <img alt="Log level option" src="06_option_2.png" width="800px" />
    <br><br>
  * Select the LocalStack version.
    <br><br>
    <img alt="LocalStack version option" src="07_option_3.png" width="800px" />
    <br><br>

* Relative paths are acceptable for the volume path, but the specified mount folder must be created prior to building the container.
  <br><br>
  <img alt="Volume path option" src="08_volume_option.png" width="800px" />
  <br><br>
  <img alt="Volume folder exists" src="09_volume_folder.png" />
  <br><br>

* Select various tools and configuration options from the checklist.
  For local tools, either select the appropriate SDK or tool feature, or install it manually.
  The template and LocalStack CLI feature do not manage these installations.
  <br><br>
  <img alt="List of options (DinD)" src="10a_options_list_dind.png" width="800px" />
  <br><br>

* You can also add additional features.
  <br><br>
  <img alt="Additional Features" src="11_additional_features.png" width="800px" />
  <br><br>

* This results in the following folder structure in your workspace.
  <br><br>
  <img alt="Generated folder structure (DinD)" src="12a_folder_structure_dind.png" width="800px" />
  <br><br>

#### Reference file

The `devcontainer.json` will look similar to the following:

```json
{
 "name": "LocalStack DinD setup",
 "image": "mcr.microsoft.com/devcontainers/base:bullseye",

 "remoteEnv": {
  // Activate LocalStack Pro: https://docs.localstack.cloud/getting-started/auth-token/
  "LOCALSTACK_AUTH_TOKEN": "${localEnv:LOCALSTACK_AUTH_TOKEN}",  // required for Pro, not processed via template due to security reasons
  "LOCALSTACK_API_KEY": "${localEnv:LOCALSTACK_API_KEY}",
  // LocalStack configuration: https://docs.localstack.cloud/references/configuration/
  "ACTIVATE_PRO": false,
  "DEBUG": true,
  "LS_LOG": "debug",
  "PERSISTENCE": false,
  "AWS_ENDPOINT_URL": "http://localhost.localstack.cloud:4566",
  "AUTO_LOAD_POD": " ",
  "ENFORCE_IAM": false,
  "AWS_REGION": "us-east-1",
  "AWS_DEFAULT_REGION": "us-east-1",
  "IMAGE_NAME": "localstack/localstack-pro:latest",
  "LOCALSTACK_VOLUME_DIR": "/data"
 },

 // 👇 Features to add to the Dev Container.
 // More info: https://containers.dev/implementors/features.
 "features": {
  "ghcr.io/devcontainers/features/docker-in-docker:2": {},
  "ghcr.io/localstack/devcontainer-feature/localstack-cli:latest": {
   "version": "latest",
   "awslocal": true,  // if true, add in features manually: ghcr.io/devcontainers/features/aws-cli
   "cdklocal": false,  // if true, add in features manually: ghcr.io/devcontainers-contrib/features/aws-cdk
   "pulumilocal": false,  // if true, add in features manually: ghcr.io/devcontainers-contrib/features/pulumi
   "samlocal": false,  // if true, add in features manually: ghcr.io/customink/codespaces-features/sam-cli
   "tflocal": false  // if true, add in features manually: ghcr.io/devcontainers-contrib/features/terraform-asdf
  },
  "ghcr.io/devcontainers/features/aws-cli:1": {}
 },

 // 👇 Use 'postCreateCommand' to run commands after the container is created.
 "postCreateCommand": "type localstack; true && localstack start -d || true",
 "mounts": [
  {
   // to persist build data and images
   "source": "dind-var-lib-docker",
   "target": "/var/lib/docker",
   "type": "volume"
  },
  {
   "source": "./.volume",
   "target": "/data",
   "type": "bind",
   "consistency": "cached"
  }
 ]
}
```

### Docker-outside-of-Docker

* [Dev Container CLI](#dev-container-cli)
* [VS Code](#vscode)
* [Reference files](#reference-files)

#### Dev Container CLI

You can use the DevContainer CLI to create a  `devcontainer.json`  file from the LocalStack template.
Before you start, ensure that you have the  [DevContainer CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli)  installed.

Create a JSON file called  `options.json`  with the desired options in it.

```json
{
    "imageVariant": "bookworm",
    "awslocal": "true",
    "logLevel": "debug",
    "debug": "true",
    "networkName": "localstack-network",
    "networkCidr": "192.168.9.0/24",
    "ipAddress": "192.168.9.13"
}
```

Use the command below to generate your  `devcontainer.json`  from the template.
Include additional features with the  `--features`  option if needed.

{{< command >}}
$ devcontainer templates apply \
    --template-id ghcr.io/localstack/devcontainer-template/localstack-dood \
    --template-args "$(cat ./options.json)" \
    --features '[{"id":"ghcr.io/devcontainers/features/aws-cli:1"}]'
{{< /command >}}

Start your container using the following command.

{{< command >}}
$ devcontainer up --id-label project=localstack --workspace-folder .
{{< /command >}}

Connect to it using the `id-label`.

{{< command >}}
$ devcontainer exec --id-label project=localstack /bin/bash
{{< /command >}}

Check that the LocalStack CLI is installed by executing:

{{< command >}}
vscode ➜ ~ $ localstack --version
3.6.0
vscode ➜ ~ $
{{< /command >}}

To remove the container, run this cleanup script since the Dev Container CLI cannot currently do it.

{{< command >}}
$ docker compose \
  --project-name "$(basename $PWD)_devcontainer" \
  -f ./.devcontainer/docker-compose.yml down
{{< /command >}}

#### VSCode

{{< callout >}}
The DevContainer extension is currently reporting issues & bugs.
Follow the [issue](https://github.com/microsoft/vscode-remote-release/issues/10180) for details.
{{< /callout >}}

To get started with LocalStack and DevContainers in VS Code, follow these steps:

* Open VSCode with the DevContainers extension installed.
* From the Command Palette, choose **Dev Containers: Add Dev Container configuration file**.
  <br><br>
  <img alt="Add Dev Container configuration file" src="01_add_devcontainer_conf.png" width="800px" />
  <br><br>

* Choose the **Add configuration to workspace** option; alternatively, select **Add configuration to user data folder** for general usage.
  <br><br>
  <img alt="Add configuration to workspace" src="02_add_conf_workspace.png" width="800px" />
  <br><br>

* Select **Show All Definitions...** to view community templates.
  <br><br>
  <img alt="Show all Template definitions" src="03_show_all_definitions.png" width="800px" />
  <br><br>

* Start typing "localstack" in the search bar to filter the official LocalStack templates and choose **LocalStack Docker-outside-of-Docker**.
  <br><br>
  <img alt="Select official LocalStack Template (DooD)" src="04b_select_template_dood.png" width="800px" />
  <br><br>

* Navigate through the configuration inputs by either selecting or typing in values.
  The defaults provided in the template are sufficient; navigating through the options by hitting Enter will result in a valid configuration.
  These options include:
  <br><br>
  * The image variant (currently only Debian-based images are supported).
    <br><br>
    <img alt="Image variant option" src="05_option_1.png" width="800px" />
    <br><br>
  * The log level.
    <br><br>
    <img alt="Log level option" src="06_option_2.png" width="800px" />
    <br><br>
  * The LocalStack version.
    <br><br>
    <img alt="LocalStack version option" src="07_option_3.png" width="800px" />
    <br><br>

* Note that LocalStack's IP address must be within the defined CIDR range.
  The network CIDR defaults to `10.0.2.0/24`, with the container IP set to `10.0.2.20`.
  <br><br>

* For the volume path, relative paths are accepted, but you must create the specified mount's folder before successfully building the container.
  The default is `./.volume`.
  <br><br>
  <img alt="Volume path option" src="08_volume_option.png" width="800px" />
  <br><br>
  <img alt="Volume folder exists" src="09_volume_folder.png" />
  <br><br>

* Select multiple tools and configuration options from the checklist.
  For local tools, you must select the appropriate SDK or tool feature, or install it manually.
  The template and the underlying LocalStack CLI Feature do not manage these installations.
  <br><br>
  <img alt="List of options (DooD)" src="10b_options_list_dood.png" width="800px" />
  <br><br>

* You can also add additional features.
  <br><br>
  <img alt="Additional Features" src="11_additional_features.png" width="800px" />
  <br><br>

* As a result, you will end up with the folder structure shown below.
  <br><br>
  <img alt="Folder structure (DooD)" src="12b_folder_structure_dood.png" width="800px" />
  <br><br>

###### Reference files

{{< tabpane lang="json" >}}
{{< tab header="devcontainer.json" lang="json" >}}
{
 "name": "LocalStack DooD setup",
 "dockerComposeFile": "docker-compose.yml",
 "service": "app",
 "workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}",

 // 👇 Features to add to the Dev Container.
 // More info: https://containers.dev/implementors/features.
 "features": {
  "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {},
  "ghcr.io/localstack/devcontainer-feature/localstack-cli:latest": {
   "version": "latest",
   "awslocal": true,  // if true, add in features manually: ghcr.io/devcontainers/features/aws-cli
   "cdklocal": false,  // if true, add in features manually: ghcr.io/devcontainers-contrib/features/aws-cdk
   "pulumilocal": false,  // if true, add in features manually: ghcr.io/devcontainers-contrib/features/pulumi
   "samlocal": false,  // if true, add in features manually: ghcr.io/customink/codespaces-features/sam-cli
   "tflocal": false  // if true, add in features manually: ghcr.io/devcontainers-contrib/features/terraform-asdf
  },
  "ghcr.io/devcontainers/features/aws-cli:1": {}
 }
}
{{< /tab >}}

{{< tab header="docker-compose.yml" lang="yaml" >}}
services:
  localstack:
    container_name: "localstack-main"
    image: localstack/localstack-pro:latest  # required for Pro
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
      - "127.0.0.1:443:443"              # LocalStack HTTPS Gateway (Pro)
    env_file:
      - .env
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "./.volume:/var/lib/localstack"
    networks:
      ls:
        # Set the container IP address in the 10.0.2.0/24 subnet
        ipv4_address: 10.0.2.20
  
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - ../..:/workspaces:cached
    # Overrides default command so things don't shut down after the process ends.
    command: sleep infinity
    init: true
    env_file:
      - .env
    dns:
      # Set the DNS server to be the LocalStack container
      - 10.0.2.20
    networks:
      - ls

networks:
  ls:
    ipam:
      config:
        # Specify the subnet range for IP address allocation
        - subnet: 10.0.2.0/24
{{< /tab >}}

{{< tab header="Dockerfile" lang="dockerfile" >}}
FROM mcr.microsoft.com/devcontainers/base:bookworm
{{< /tab >}}
{{< tab header=".env" lang="bash" >}}
# Activate LocalStack Pro: https://docs.localstack.cloud/getting-started/auth-token/
LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:-}  # required for Pro, not processed via template due to security reasons
LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY:-}
# LocalStack configuration: https://docs.localstack.cloud/references/configuration/
ACTIVATE_PRO=false
DEBUG=true
LS_LOG=debug
PERSISTENCE=false
AWS_ENDPOINT_URL=http://localhost.localstack.cloud:4566
LOCALSTACK_HOST=localhost.localstack.cloud:4566
AUTO_LOAD_POD=
ENFORCE_IAM=false
AWS_REGION=us-east-1
AWS_DEFAULT_REGION=us-east-1
IMAGE_NAME=localstack/localstack-pro:latest
{{< /tab >}}
{{< /tabpane >}}

## LocalStack Feature

Add the following minimal [Feature](https://github.com/localstack/devcontainer-feature) snippet to your DevContainer config.

```json
...
 "features": {
    "ghcr.io/localstack/devcontainer-feature/localstack-cli:latest": {}
  }
...
```

That's it.
By building your container the LocalStack CLI and any of the enabled local-tools (currently these are `awslocal`, `cdklocal`, `pulumilocal`, `samlocal` and `tflocal`) will be installed.

{{< callout >}}
The LocalStack Feature does not manage the installation of underlying tools (e.g., for awslocal, aws-cli is not installed).
For more information on dependencies, please refer to the [Feature documentation](https://github.com/localstack/devcontainer-feature).
{{< /callout >}}
