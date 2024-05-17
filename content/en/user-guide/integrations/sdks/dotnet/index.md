---
title: ".NET"
categories: []
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

{{< callout >}}
Make sure you are setting the `AuthenticationRegion` and not the `RegionEndpoint`.
Setting the `RegionEndpoint` to a constant like `RegionEndpoint.EUWest1` will override the ServiceURL, and your request will end up against AWS.
{{< /callout >}}

### S3 specific endpoint

Here is another example, this time with an `S3Client` and its specific endpoint.

```csharp
var config = new AmazonS3Config({ ServiceURL = "http://s3.localhost.localstack.cloud:4566" });
var s3client = new AmazonS3Client(config);
```

{{< callout >}}
In case of issues resolving this DNS record, we can fallback to <http://localhost:4566> in combination with the provider setting `ForcePathStyle = true`. The S3 service endpoint is slightly different from the other service endpoints, because AWS is deprecating path-style based access for hosting buckets.
{{< /callout >}}

```csharp
var config = new AmazonS3Config(
    {
        ServiceURL = "http://localhost:4566",
        ForcePathStyle = true
    }
);
var s3client = new AmazonS3Client(config);
```

## Alternative: Using LocalStack.NET

If you're working with .NET and LocalStack, you have a few options. In addition to the AWS SDK for .NET, there's an alternative client library, `LocalStack.NET`, which facilitates integration with LocalStack.

### Overview

`LocalStack.NET` is a .NET client library developed to simplify the connection between .NET applications and LocalStack. It wraps around the AWS SDK for .NET and offers an alternative setup for creating LocalStack clients.

**LocalStack.NET Documentation:** Comprehensive guide and examples [here](https://github.com/localstack-dotnet/localstack-dotnet-client).

### How it Works

Instead of manually setting the endpoint configurations when initializing a client, `LocalStack.NET` offers methods that handle these details. The library aims to reduce the boilerplate required to set up LocalStack clients in .NET.

### Example Usage

#### Dependency Injection Approach

```csharp
public void ConfigureServices(IServiceCollection services)
{
    // Add framework services.
    services.AddMvc();

    services.AddLocalStack(Configuration)
    services.AddDefaultAWSOptions(Configuration.GetAWSOptions());
    services.AddAwsService<IAmazonS3>();
}

...

var amazonS3Client = serviceProvider.GetRequiredService<IAmazonS3>();
```

#### Standalone Approach

```csharp
var sessionOptions = new SessionOptions();
var configOptions = new ConfigOptions();

ISession session = SessionStandalone.Init()
    .WithSessionOptions(sessionOptions)
    .WithConfigurationOptions(configOptions).Create();

var amazonS3Client = session.CreateClientByImplementation<AmazonS3Client>();
```

### Benefits

- **Consistent Client Configuration:** `LocalStack.NET` provides a standardized approach to initialize clients, eliminating the need for manual endpoint configurations.
- **Tailored for .NET Developers:** The library offers functionalities specifically developed to streamline integration of LocalStack with .NET applications.
- **Adaptable Environment Transition:** Switching between LocalStack and actual AWS services can be achieved with minimal configuration changes when leveraging `LocalStack.NET`.
- **Versatile .NET Compatibility:** Supports a broad spectrum of .NET versions, from .NET Framework 4.6.1 and .NET Standard 2.0, up to recent .NET iterations such as .NET 7.0.

### Considerations:

- Both the standard AWS SDK method and `LocalStack.NET` provide ways to integrate with LocalStack using .NET. The choice depends on developer preferences and specific project needs.
- `LocalStack.NET` works alongside the AWS SDK, using it as a base and providing a more focused API for LocalStack interactions.

## Resources

- [AWS SDK for .NET](https://aws.amazon.com/sdk-for-net/)
- [Official repository of the AWS SDK for .NET](https://github.com/aws/aws-sdk-net)
- [LocalStack.NET Documentation](https://github.com/localstack-dotnet/localstack-dotnet-client)
