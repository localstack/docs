---
title: "LocalStack Docker Extension"
weight: 8
description: >
  Getting started with LocalStack Extension for Docker Desktop
aliases:
  - /tools/docker-desktop-extension/
  - /user-guide/tools/docker-desktop-extension/
---

## Introduction

The LocalStack Extension for Docker Desktop enables developers working with LocalStack to operate their LocalStack container via Docker Desktop, including checking service status, container logs, and configuring profiles.
To install the LocalStack Extension for Docker Desktop, you need to have [Docker Desktop installed on your machine](https://www.docker.com/products/docker-desktop).

<img src="localstack-docker-extension.png" alt="LocalStack Extension for Docker Desktop" title="LocalStack Extension for Docker Desktop" width="800px"   />

## Installation

To utilize LocalStack's Docker Extension, it is necessary to have a recent version of Docker Desktop (v4.8 or higher) installed on the local machine.
To enable the extension, access the **Extensions** tab and select the **Enable Docker Extensions** and **Show Docker Extensions system containers** option.

<img src="localstack-docker-extension-preferences.png" title="Enable Docker Extensions in the Preferences within the Extensions tab" alt="Enable Docker Extensions in the Preferences within the Extensions tab" width="800px"   />
<br></br>

The LocalStack Extension for Docker Desktop has been validated and can be accessed on the Extensions Marketplace.
To begin using it, navigate to the **Extensions Marketplace**, search for **LocalStack**, and click the **Install** button to proceed with the installation.

<img src="localstack-docker-extension-marketplace.png" title="Discover the LocalStack Extension on the Docker Desktop Marketplace and install it!" width="800px" alt="Discover the LocalStack Extension on the Docker Desktop Marketplace and install it!" />
<br></br>

An alternative method for installing the LocalStack's Extension for Docker Desktop is pulling the [public Docker image](https://hub.docker.com/r/localstack/localstack-docker-desktop) from Docker Hub and installing it!

{{< command >}}
$ docker extension install localstack/localstack-docker-desktop:0.5.3
{{< /command >}}

After installation, you can access the LocalStack Extension for Docker Desktop from the **Extensions** tab.
Upon the initial launch of the extension, a prompt to select a mount point for the LocalStack container will appear.
Select your username from the drop-down menu.
Furthermore, you can modify this setting later by navigating to the **Configurations** tab and choosing a different mount point.

<img src="localstack-docker-extension-mount-point.png" title="Select the mount point upon the launch of LocalStack's Docker extension" alt="Select the mount point upon the launch of LocalStack's Docker extension" width="800px"  />

## Features

LocalStack's Docker Extension helps users to manage their LocalStack container with a simple and intuitive user interface through Docker Desktop.
The extension includes container management, configuration profile management, service status, and container logs!

### Container management

You can start, stop, and restart LocalStack from the Docker Desktop.
You can also see the current status of your LocalStack container and navigate to LocalStack Web Application.

<img src="localstack-docker-extension-start.png" title="Start and Stop your LocalStack container with a single click of a button with LocalStack's extension" alt="Start and Stop your LocalStack container with a single click of a button with LocalStack's extension" width="800px"  />

### Container logs

You can see the log information of the LocalStack container and all the available services and their status on the service page.

<img src="localstack-docker-extension-logs.png" title="Check the logs of your running LocalStack container through LocalStack's Docker extension" alt="Check the logs of your running LocalStack container through LocalStack's Docker extension" width="800px"  />

### Configuration management

You can manage and use your profiles via configurations and create new configurations for your LocalStack container.

<img src="localstack-docker-extension-configuration-profile.png" title="Create your configuration profiles within LocalStack's Extension to affect the state of LocalStack" alt="Create your configuration profiles within LocalStack's Extension to affect the state of LocalStack" width="800px" />

## Configure an Auth Token

To configure an Auth Token for the LocalStack Docker Extension, you need to create a new configuration profile.
Navigate to the **Configurations** tab and click the **New +** button.
Enter the configuration name and add the `LOCALSTACK_AUTH_TOKEN` environment variable with the desired value.

To start the LocalStack Pro container with the Auth Token, select the configuration profile from the drop-down menu and click the **Start** button.
