---
title: "LocalSurf"
weight: 7
description: >
  Browser plugin to redirect AWS service calls to LocalStack
---

## Introduction

LocalSurf is a Chrome browser plugin to repoint AWS service calls to [LocalStack](https://localstack.cloud/).
While developing and testing AWS cloud Web applications locally with LocalStack, we need to make the browser connect to the local endpoint (`http://localhost:4566`) instead of the AWS production servers (`*.amazonaws.com`).
 LocalSurf enables you to use the production code without changes, and have the browser make requests to LocalStack instead of AWS directly by explicitly setting the [`endpoint`  attribute](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/specifying-endpoints.html) in the [AWS JavaScript SDK](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Endpoint.html).

> This plugin is experimental and still under active development.
> Please report any issues or feature requests on our [GitHub repository](https://github.com/localstack/local-surf).

## Installation

This extension is not yet available in the Chrome Web Store, but can be installed directly from source.
Clone the repository on your local machine to get started:

{{< command >}}
$ git clone git@github.com:localstack/local-surf.git
{{< /command >}}

Head over to `chrome://extensions/`  in Chrome, then select  `"Load unpacked"`  and point to the directory where the source code files are stored on the disk.

Once installed, a new icon should appear in the Chrome extensions bar.
When clicking on the icon, the plugin can be enabled/disabled by toggling the **Enable local mode** checkbox.

<p>
{{< img src="localsurf-extension.png" class="img-fluid shadow rounded" >}}
</p>

## Usage

To illustrate how the plugin works, we use the AWS [Serverlesspresso](https://github.com/aws-samples/serverless-coffee-workshop) sample application.
This app consists of various backend components (e.g., DynamoDB tables, Lambda functions, Cognito user pools, etc), as well as a hosted Web app user interface (UI) that can be used to interact with the backend components.

We can deploy the backend components to LocalStack directly, using the `samlocal` command line interface (CLI):

{{< command >}}
$ samlocal build
$ samlocal deploy
{{< /command >}}

Once deployed, the `samlocal` CLI will print out a display app URL which will look similar to the following:

```sh
Key                 DisplayAppURI
Description         The URL for the Display App
Value               https://workshop-display.serverlesscoffee.com/?region=us-east-1&userPoolId=us-east-1_43c9800e64c84467aa0abdb102e226ef&userPoolWebClientId=vr9aw2jr7iv36ezwaaqlzzkvbp&poolId=us-east-1:95dc88d0-1029-48fe-ba7b-1e6a9741bfc5&host=localhost.localstack.cloud&orderManagerEndpoint=https://fapencq0ue.execute-api.amazonaws.com:4566/Prod&APIGWEndpointValidatorService=https://psmdc7b1lv.execute-api.amazonaws.com:4566/Prod&APIGWEndpointConfigService=https://hw7yw61ba7.execute-api.amazonaws.com:4566/Prod
```

We can then open the URL in the browser and confirm the configurations in the form dialog:

<p>
{{< img src="serverlesspresso-config.png" class="img-fluid shadow rounded" >}}
</p>
<br>
Once confirmed, we are being forwarded to a signin screen, which uses an AWS Cognito user pool to manage authentication:

<p>
{{< img src="serverlesspresso-login.png" class="img-fluid shadow rounded" >}}
</p>
<br>
After clicking **Sign In** in this form, we can see that the browser makes a request to LocalStack (to  `localhost.localstack.cloud`, which is a domain name that resolves to `127.0.0.1`).
<br>
<p>
{{< img src="chrome-networking.png" class="img-fluid shadow rounded" >}}
</p>
<br>
This sample demonstrates how we can take an existing Web application, without any modification, and make it talk to the LocalStack APIs directly from the browser via the LocalSurf plugin.

## Note

Use this extension at your own risk - it is provided on an as-is basis,  **without**  warranties or conditions of **any** kind.
In particular, it is your obligation to ensure that the use of this extension is compliant with the user license agreement and the terms & conditions of Amazon Web Services (AWS) and their services.
