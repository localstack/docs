---
title: "AWS Copilot CLI"
tags: ["continuous-delivery"]
weight: 5
description: >
  Build, Release and Operate Containerized Applications on AWS with AWS Copilot CLI
---

## Overview

The AWS Copilot CLI is a command line tool for developer, to release and operate containerized applications using the AWS services ECS, Fargate and App runner.
Copilot CLI makes it very simple to deploy your application, without the need for manual configuration of the mentioned services.

## Copilot Local

`copilotlocal` is a [fork of AWS Copilot CLI](https://github.com/localstack/copilot-cli-local), where the endpoints for all services are redirected to `http://localhost:4566`.
Using `copilotlocal` instead of `copilot` in your command line therefore ensures the deployment of your service against LocalStack instead of AWS.

### Download / Installation

{{< tabpane >}}
{{< tab header="Linux AMD64" lang="bash">}}
curl -Lo copilotlocal https://github.com/localstack/copilot-cli/raw/localstack-builds/build/linux-amd64/copilotlocal && chmod +x copilotlocal
# if you want to have copilotlocal in your $PATH, move the executable e.g. to /usr/local/bin/
sudo mv copilotlocal /usr/local/bin/
{{< /tab >}}
{{< tab header="Linux ARM64" lang="bash">}}
curl -Lo copilotlocal https://github.com/localstack/copilot-cli/raw/localstack-builds/build/linux-arm64/copilotlocal && chmod +x copilotlocal
# if you want to have copilotlocal in your $PATH, move the executable e.g. to /usr/local/bin/
sudo mv copilotlocal /usr/local/bin/
{{< /tab >}}
{{< tab header="Mac OS" lang="bash">}}
curl -Lo copilotlocal https://github.com/localstack/copilot-cli/raw/localstack-builds/build/macos-darwin/copilotlocal && chmod +x copilotlocal
# if you want to have copilotlocal in your $PATH, move the executable e.g. to /usr/local/bin/
sudo mv copilotlocal /usr/local/bin/
{{< /tab >}}
{{< tab header="Windows Powershell" lang="powershell">}}
Invoke-WebRequest -Uri https://github.com/localstack/copilot-cli/raw/localstack-builds/build/windows/copilotlocal.exe -OutFile copilotlocal.exe 
{{< /tab >}}
{{< /tabpane >}}

### Configuration

* `LOCALSTACK_HOSTNAME`: Target hostname under which LocalStack endpoints are available (default: `localhost`)
* `EDGE_PORT`: Target port under which LocalStack endpoints are available (default: `4566`)
* `LOCALSTACK_DISABLE`: Optional flag to disable the local endpoints and use the default behavior of `copilot` (set to `1` or `true` to enable)

### Usage

`copilotlocal` can be used as a drop-in replacement for `copilot`.
You can execute any `copilot` command as `copilotlocal` to run your intended action against LocalStack instead of AWS.

To deploy your init your copilot environment, execute the following command in your project folder:

```bash
copilotlocal init
```

For more information about how to use the AWS Copilot CLI, checkout the [copilot documentation](https://aws.github.io/copilot-cli/docs/overview/).
Just remember to replace `copilot` with `copilotlocal`.