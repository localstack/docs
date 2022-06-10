---
title: ".NET"
categories: []
tags: ["sdk"]
description: >
  How to use the .NET AWS SDK with LocalStack.
---

## Overview

The [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/), like other AWS SDKs, lets you set the endpoint when creating resource clients,
which is the preferred way of integrating the .NET SDK with LocalStack.

## Example

Here is an example of how to create an `LambdaClient` with the endpoint set to LocalStack.

```csharp
var lambdaClient = new AmazonLambdaClient(new AmazonLambdaConfig()
    {
        ServiceURL = "http://localhost:4566"
    });
```

If you want to specify a region and credentials when creating the client, please set them as `AuthenticationRegion` and `BasicAWSCredentials`, like in this example:

```csharp
var lambdaClient = new AmazonLambdaClient(new BasicAWSCredentials("temp", "temp"), new AmazonLambdaConfig()
    {
        ServiceURL = "http://localhost:4566",
        AuthenticationRegion = "eu-west-1"
    });
```

{{< alert >}}
Make sure you are setting the `AuthenticationRegion` and not the `RegionEndpoint`. Setting the `RegionEndpoint` to a constant like `RegionEndpoint.EUWest1` will override the ServiceURL, and your request will end up against AWS.
{{< /alert >}}


## Resources

* [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/)
* [Official repository of the AWS SDK for .NET](https://github.com/aws/aws-sdk-net)
