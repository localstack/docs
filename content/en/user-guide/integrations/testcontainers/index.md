---
title: "Testcontainers"
tags: [
  "testcontainers",
  "test",
  "java",
  "jvm",
  "kotlin",
  "go",
  "dotnet"
]
categories: ["LocalStack Community", "LocalStack Pro"]
date: 2023-02-11
weight: 5
description: >
  Use Testcontainers with LocalStack
aliases:
  - /integrations/testcontainers/
---

<img src="testcontainers-logo.svg" width="600px" alt="Testcontainers logo"><br />

## Overview

[Testcontainers](https://www.testcontainers.com/) is a library that helps you to run your
tests against real dependencies.

In this guide, you will learn how to use [Testcontainers](https://www.testcontainers.com/) 
with LocalStack.

## Covered Topics

* [Testcontainers for .NET](#testcontainers-for-net)
* [Testcontainers for Go](#testcontainers-for-go)
* [Testcontainers for Java](#testcontainers-for-java)

### Testcontainers for .NET

### Testcontainers for Go

Testcontainers for Go provides a [LocalStack module](https://golang.testcontainers.org/modules/localstack/)
which allows you to run LocalStack in a Docker container and use it in your tests.

Install it into your project:

{{< command >}}
$ go get github.com/testcontainers/testcontainers-go/modules/localstack
{{< / command >}}

In order to use LocalStack in your tests, you need to create a container instance:

```go
container, err := localstack.StartContainer(
    ctx,
    localstack.OverrideContainerRequest(testcontainers.ContainerRequest{
        Env: map[string]string{
            "AWS_ACCESS_KEY_ID":     accesskey,
            "AWS_SECRET_ACCESS_KEY": secretkey,
            "AWS_SESSION_TOKEN":     token,
            "AWS_DEFAULT_REGION":    region,
            "SERVICES":              "s3,sqs,cloudwatchlogs,kms",
        }},
    ),
)
```

Configure the client to use the LocalStack endpoint:

```go
func s3Client(ctx context.Context, l *localstack.LocalStackContainer) (*s3.Client, error) {
    // the Testcontainers Docker provider is used to get the host of the Docker daemon
    provider, err := testcontainers.NewDockerProvider()
    if err != nil {
        return nil, err
    }

    host, err := provider.DaemonHost(ctx)
    if err != nil {
        return nil, err
    }

    mappedPort, err := l.MappedPort(ctx, nat.Port("4566/tcp"))
    if err != nil {
        return nil, err
    }

    customResolver := aws.EndpointResolverWithOptionsFunc(
        func(service, region string, opts ...interface{}) (aws.Endpoint, error) {
            return aws.Endpoint{
                PartitionID:   "aws",
                URL:           fmt.Sprintf("http://%s:%d", host, mappedPort.Int()),
                SigningRegion: region,
            }, nil
        })

    awsCfg, err := config.LoadDefaultConfig(context.TODO(),
        config.WithRegion(region),
        config.WithEndpointResolverWithOptions(customResolver),
        config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(accesskey, secretkey, token)),
    )
    if err != nil {
        return nil, err
    }

    client := s3.NewFromConfig(awsCfg, func(o *s3.Options) {
        o.UsePathStyle = true
    })

    return client, nil
}

```

### Testcontainers for Java

Testcontainers for Java provides a [LocalStack module](https://www.testcontainers.org/modules/localstack/)
which allows you to run LocalStack in a Docker container and use it in your tests.

With Maven:

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>localstack</artifactId>
    <version>1.17.6</version>
    <scope>test</scope>
</dependency>
```

With Gradle:

```gradle
testImplementation 'org.testcontainers:localstack:1.17.6'
 ```

In order to use LocalStack in your tests, you need to create a `LocalStackContainer` instance

```java
LocalStackContainer localstack = new LocalStackContainer("localstack/localstack:1.4.0")
    .withServices(LocalStackContainer.Service.S3);
```

Configure the client to use the LocalStack endpoint:

```java
S3Client s3 = S3Client.builder()
    .endpointOverride(localstack.getEndpointOverride(LocalStackContainer.Service.S3))
    .credentialsProvider(StaticCredentialsProvider.create(AwsBasicCredentials.create(localstack.getAccessKey(), localstack.getSecretKey())))
    .region(Region.of(localstack.getRegion()))
    .build();
```

## Useful Links

* https://www.testcontainers.org/
* https://www.testcontainers.org/modules/localstack/
