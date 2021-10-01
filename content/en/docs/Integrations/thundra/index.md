---
title: "Thundra"
tags: ["thundra", "tracing", "observability"]
weight: 6
description: >
  Monitor and debug your AWS Lambda functions with LocalStack and [Thundra](https://thundra.io).
---

This guide describes how you can monitor and debug your AWS Lambda functions with [Thundra](https://thundra.io).


## Integrating Thundra with LocalStack

{{% alert title="Supported languages" color="info" %}}
Currently only **Node.js**, **Python** and **Java** Lambdas are supported in this integration - support for other runtimes (.NET, Go) is coming soon.
{{% /alert %}}

LocalStack comes with out-of-the-box support for Thundra. Simply obtain a Thundra API key [here](https://console.thundra.io/onboarding/serverless) and add it to your Lambda function's environment variables (`THUNDRA_APIKEY`):

{{< tabpane >}}
{{< tab header="AWS SAM" lang="yaml" >}}
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      // other function properties
      Environment:
        Variables:
          // other environment variables
          THUNDRA_APIKEY: <YOUR-THUNDRA-API-KEY>{{< /tab >}}
{{< tab header="AWS CDK" lang="js" >}}
const myFunction = new Function(this, "MyFunction", {
    ..., // other function properties
    environment: {
        ..., // other environment variables
        THUNDRA_APIKEY: <MY-THUNDRA-API-KEY>
    }
});{{< /tab >}}
{{< tab header="Serverless Framework" lang="yaml" >}}
functions:
  MyFunction:
    // other function properties
    environment:
      // other environment variables
      THUNDRA_APIKEY: <YOUR-THUNDRA-API-KEY>{{< /tab >}}
{{< /tabpane >}}

After invoking your AWS Lambda function, you can inspect the invocations and traces in the [Thundra Console](https://console.thundra.io). You can find more details in the [Thundra documentation](https://apm.docs.thundra.io).

## Further Reading

For a complete example, you may check our blog post "[Test Monitoring for LocalStack Apps with Thundra](https://localstack.cloud/blog/2021-09-16-test-monitoring-for-localstack-apps)" and take a look at the example project [here](https://github.com/thundra-io/thundra-demo-localstack-java).