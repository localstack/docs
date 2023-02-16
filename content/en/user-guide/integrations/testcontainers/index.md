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

<img src="testcontainers-logo.svg" width="600px" alt="Testcontainers logo">

## Overview

[Testcontainers](https://www.testcontainers.com/) is a library that helps you to run your
tests against real dependencies.

In this guide, you will learn how to use [Testcontainers](https://www.testcontainers.com/)
with LocalStack.

## Covered Topics

* [Installing the Localstack module](#installing-the-localstack-module)
* [Obtaining a LocalStack container](#obtaining-a-localstack-container)
* [Configuring the AWS client](#configuring-the-aws-client)
* [Useful Links](#useful-links)

### Installing the Localstack module

{{< tabpane >}}
{{< tab header="Go" lang="go">}}
go get github.com/testcontainers/testcontainers-go/modules/localstack
{{< /tab >}}
{{< tab header="Java (Maven)" lang="xml">}}
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>localstack</artifactId>
    <version>1.17.6</version>
    <scope>test</scope>
</dependency>
{{< /tab >}}
{{< tab header="Java (Gradle)" lang="gradle">}}
testImplementation 'org.testcontainers:localstack:1.17.6'
{{< /tab >}}
{{< tab header="NuGet" lang="shell">}}
dotnet add package Testcontainers --version 2.4.0
{{< /tab >}}
{{< /tabpane >}}

### Obtaining a LocalStack container

{{< tabpane >}}
{{< tab header="Go" lang="go">}}
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
{{< /tab >}}
{{< tab header="Java" lang="java">}}
LocalStackContainer localstack = new LocalStackContainer("localstack/localstack:1.4.0")
    .withServices(LocalStackContainer.Service.S3);
{{< /tab >}}
{{< tab header=".NET" lang="csharp">}}

/* The current released version of Testcontainers for .NET does not include a
LocalStack module. However, developers who want to use Testcontainers with
LocalStack should not be discouraged, as the Testcontainers team has already
developed a LocalStack module that will be included in the next release. In the
meantime, developers can still use Testcontainers' generic builder to create a
LocalStack container. */

const string localStackImage = "localstack/localstack:1.4.0";

const ushort localStackPort = 4566

var localStackContainer = new ContainerBuilder()
    .WithImage(localStackImage)
    .WithPortBinding(localStackPort, true)
    .WithWaitStrategy(Wait.ForUnixContainer().UntilHttpRequestIsSucceeded(request =>
        request.ForPath("/_localstack/health").ForPort(localStackPort)))
    .Build();

await localStackContainer.StartAsync()
    .ConfigureAwait(false);
{{< /tab >}}
{{< /tabpane >}}

## Configuring the AWS client

{{< tabpane >}}
{{< tab header="Go" lang="go">}}
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
{{< /tab >}}
{{< tab header="Java" lang="java">}}
S3Client s3 = S3Client.builder()
    .endpointOverride(localstack.getEndpointOverride(LocalStackContainer.Service.S3))
    .credentialsProvider(StaticCredentialsProvider.create(AwsBasicCredentials.create(localstack.getAccessKey(), localstack.getSecretKey())))
    .region(Region.of(localstack.getRegion()))
    .build();
{{< /tab >}}
{{< tab header=".NET" lang="csharp">}}
var config = new AmazonS3Config();
config.ServiceURL = _localStackContainer.GetConnectionString();
using var client = new AmazonS3Client(config);
{{< /tab >}}
{{< /tabpane >}}

## Useful Links

* https://www.testcontainers.com (Java, .NET, Go, Python, Ruby, Node.js)
* https://www.testcontainers.org (Java)
* https://www.testcontainers.org/modules/localstack (Java)
* https://golang.testcontainers.org (Go)
* https://golang.testcontainers.org/modules/localstack (Go)
