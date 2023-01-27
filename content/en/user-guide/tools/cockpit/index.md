---
title: "Cockpit"
weight: 6
categories: ["LocalStack Cockpit"]
description: >
  Manage your local LocalStack instance via the Cockpit Desktop UI.
aliases:
  - /get-started/cockpit/
---

LocalStack Cockpit is a desktop client that allows users to easily control and manage their LocalStack instance. With LocalStack Cockpit, users can start and stop their LocalStack instance with a single click, view the current status of their instance, and access quick links to LocalStack documentation and other resources. 
Cockpit also provides instant insights into the runtime and environment information, as well as the status of available services and log information. In addition, users can directly manage and use their LocalStack profiles through the app.

To get started with Cockpit, you can download the app for your operating system through [**localstack.cloud/products/cockpit**](https://localstack.cloud/products/cockpit).

To install LocalStack Cockpit, [**Docker**](https://www.docker.com) is the only prerequisite.

<p>
{{< img src="cockpit-screenshot.png" class="img-fluid shadow rounded" >}}
</p>

{{< alert title="Note" >}}
The Cockpit beta version is not yet verified on Windows and Mac app stores.
On [Windows](https://www.windowscentral.com/how-disable-smartscreen-trusted-app-windows-10) and [Mac](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac) you need to allow your OS to run untrusted code.
{{< /alert >}}

## Features

LocalStack Cockpit helps users to manage their LocalStack instance with a simple and intuitive UI. Some of the features of LocalStack Cockpit, include automated environment checks, profile configurations, instance management and quick log access.

### Automated environment checks

While starting Cockpit, it will automatically check your system environment to ensure that everything is ready to start LocalStack. It includes checking Docker version, pulling the official LocalStack Docker image, and checking for the presence of the LocalStack CLI and runtime status. In the absence of a Docker image, Cockpit will automatically pull the latest version of the LocalStack Docker image.

{{< alert title="Important" color="warning" >}}
Before starting LocalStack Cockpit, Docker should be already running.
{{< /alert >}}

<p>
{{< img src="cockpit-init-check.png" class="img-fluid shadow rounded" >}}
</p>

### Run configurations

Using Cockpit, you can manage and select LocalStack run configurations to start LocalStack with a particular configuration. Configurations allow you to save your LocalStack Pro API key, or a particular set of environment variables into a run configuration.

<p>
{{< img src="cockpit-runconfig-edit.png" class="img-fluid shadow rounded" >}}
</p>

### Manage your LocalStack instance

You can easily start and stop your LocalStack instance with a single click. Cockpit also provides you with the status of your LocalStack instance, including the number of running services and the runtime information.

### Quick log access

Cockpit provides quick access to your LocalStack logs for instant insights. Currently, the beta version of Cockpit does not have auto-follow cockpit, so you need to click "Refresh" and "Scroll to end" to view the latest logs.

<p>
{{< img src="cockpit-logs.png" class="img-fluid shadow rounded" >}}
</p>

## Known issues

- Mac OS X 10.0 and lower are not supported yet.
- There may be `glibc` issues on older Linux versions.

While installing Cockpit on Mac M1, macOS may prevent the software from running because of issues with code signing. To fix it, you can run `xattr -rc` in the terminal on the binary file and then run the application again. You can visit the [Apple Developer Forum thread](https://developer.apple.com/forums/thread/692774) for more information.

## Report issues

Support for LocalStack Cockpit is provided on a best-effort basis. To help us improve the product, please report any issues you encounter on [GitHub](https://github.com/localstack/cockpit/issues) and share your log files, so that we can investigate into your problem more easily. The logs are available in the following locations, depending on your operating system.:

- Linux: `~/.config/localstack-cockpit/logs/`
- macOS: `~/Library/Logs/localstack-cockpit/`
- Windows: `%USERPROFILE%\AppData\Roaming\localstack-cockpit\logs\`
