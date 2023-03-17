---
title: ".NET"
categories: []
tags: ["sdk"]
description: >
  How to use the .NET AWS SDK with LocalStack.
aliases:
  - /integrations/sdks/dotnet/
---

## Overview

The [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/), like other AWS SDKs, lets you set the endpoint when creating resource clients,
which is the preferred way of integrating the .NET SDK with LocalStack.

## Example

Here is an example of how to create an `LambdaClient` with the endpoint set to LocalStack.

```csharp
var lambdaClient = new AmazonLambdaClient(new AmazonLambdaConfig(
    {
        ServiceURL = "http://localhost:4566"
    }
);
```

If you want to specify a region and credentials when creating the client, please set them as `AuthenticationRegion` and `BasicAWSCredentials`, like in this example:

```csharp
var lambdaClient = new AmazonLambdaClient(new BasicAWSCredentials("test", "test"), new AmazonLambdaConfig(
    {
        ServiceURL = "http://localhost:4566",
        AuthenticationRegion = "eu-west-1"
    }
);
```

{{< alert title="Note">}}
Make sure you are setting the `AuthenticationRegion` and not the `RegionEndpoint`.
Setting the `RegionEndpoint` to a constant like `RegionEndpoint.EUWest1` will override the ServiceURL, and your request will end up against AWS.
{{< /alert >}}

### S3 specific endpoint

```csharp
var config = new AmazonS3Config({ ServiceURL = "http://s3.localhost.localstack.cloud:4566" });
var s3client = new AmazonS3Client(config);
```

{{< alert title="Note">}}
In case of issues resolving this DNS record, we can fallback to http://localhost:4566 in combination with the provider setting `ForcePathStyle = true`. The S3 service endpoint is slightly different from the other service endpoints, because AWS is deprecating path-style based access for hosting buckets.
{{< /alert >}}

```csharp
var config = new AmazonS3Config(
    {
        ServiceURL = "http://localhost:4566",
        ForcePathStyle = true
    }
);
var s3client = new AmazonS3Client(config);
```

## Resources

* [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/)
* [Official repository of the AWS SDK for .NET](https://github.com/aws/aws-sdk-net)
