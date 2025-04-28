---
title: "Testcontainers"
linkTitle: "Testcontainers"
description: >
  Use Testcontainers with LocalStack
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
* [Special Setup for using RDS](#special-setup-for-using-rds)
* [Useful Links](#useful-links)

### Installing the Localstack module

{{< tabpane >}}
{{< tab header="NuGet" lang="shell">}}
dotnet add package Testcontainers.LocalStack --version 3.0.0
{{< /tab >}}
{{< tab header="Go" lang="go">}}
go get github.com/testcontainers/testcontainers-go/modules/localstack
{{< /tab >}}
{{< tab header="Java (Maven)" lang="xml">}}
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>localstack</artifactId>
    <version>1.18.0</version>
    <scope>test</scope>
</dependency>
{{< /tab >}}
{{< tab header="Java (Gradle)" lang="gradle">}}
testImplementation 'org.testcontainers:localstack:1.18.0'
{{< /tab >}}
{{< tab header="NodeJS (npm)" lang="npm">}}
npm i @testcontainers/localstack
{{< /tab >}}
{{< /tabpane >}}

### Obtaining a LocalStack container

{{< tabpane >}}
{{< tab header=".NET" lang="csharp">}}
var localStackContainer = new LocalStackBuilder().Build();

await localStackContainer.StartAsync()
    .ConfigureAwait(false);
{{< /tab >}}
{{< tab header="Go" lang="go">}}
container, err := localstack.Run(ctx, "localstack/localstack:latest")
{{< /tab >}}
{{< tab header="Java" lang="java">}}
LocalStackContainer localstack = new LocalStackContainer(DockerImageName.parse("localstack/localstack:3"));
{{< /tab >}}
{{< tab header="NodeJS (typescript)" lang="typescript">}}
const localstack = new LocalstackContainer("localstack/localstack:3").start()
{{< /tab >}}
{{< /tabpane >}}

## Configuring the AWS client

{{< tabpane >}}
{{< tab header=".NET" lang="csharp">}}
var config = new AmazonS3Config();
config.ServiceURL = localStackContainer.GetConnectionString();
using var client = new AmazonS3Client(config);
{{< /tab >}}
{{< tab header="Go" lang="go">}}
type resolverV2 struct {
    // you could inject additional application context here as well
}

func (*resolverV2) ResolveEndpoint(ctx context.Context, params s3.EndpointParameters) (
    smithyendpoints.Endpoint, error,
) {
    // delegate back to the default v2 resolver otherwise
    return s3.NewDefaultEndpointResolverV2().ResolveEndpoint(ctx, params)
}

func s3Client(ctx context.Context, l *localstack.LocalStackContainer) (*s3.Client, error) {
    mappedPort, err := l.MappedPort(ctx, nat.Port("4566/tcp"))
    if err != nil {
        return nil, err
    }

    provider, err := testcontainers.NewDockerProvider()
    if err != nil {
        return nil, err
    }
    defer provider.Close()

    host, err := provider.DaemonHost(ctx)
    if err != nil {
        return nil, err
    }

    awsCfg, err := config.LoadDefaultConfig(context.TODO(),
        config.WithRegion(region),
        config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(accesskey, secretkey, token)),
    )
    if err != nil {
        return nil, err
    }

    // reference: https://aws.github.io/aws-sdk-go-v2/docs/configuring-sdk/endpoints/#with-both
    client := s3.NewFromConfig(awsCfg, func(o *s3.Options) {
        o.BaseEndpoint = aws.String("http://" + host + ":" + mappedPort.Port())
        o.EndpointResolverV2 = &resolverV2{}
        o.UsePathStyle = true
    })

    return client, nil
}
{{< /tab >}}
{{< tab header="Java" lang="java">}}
S3Client s3 = S3Client.builder()
    .endpointOverride(localstack.getEndpoint())
    .credentialsProvider(StaticCredentialsProvider.create(AwsBasicCredentials.create(localstack.getAccessKey(), localstack.getSecretKey())))
    .region(Region.of(localstack.getRegion()))
    .build();
{{< /tab >}}
{{< tab header="NodeJS (typescript)" lang="typescript">}}
const awsConfig = {
      endpoint: localstack.getConnectionUri(),
      credentials: {
        accessKeyId: "test",
        secretAccessKey: "test",
      },
      region: "eu-central-1",
    };
const s3 = S3Client(awsConfig);
{{< /tab >}}
{{< /tabpane >}}

## Special Setup for using RDS

Some services like RDS require additional setup so that the correct port is exposed and accessible for the tests.
The reserved ports on LocalStack are between `4510-4559`, depending on your use case you might need to expose several ports using `witExposedPorts`.

Check the [pro-sample on how to use RDS with Testcontainers for Java](https://github.com/localstack/localstack-pro-samples/tree/master/testcontainers-java-sample).

The Testcontainer can be created like this:

```java
/**
  * Start LocalStackContainer with exposed Ports. Those ports are used by services like RDS, where several databases can be started, running on different ports.
  * In this sample we only map 5 ports, however, depending on your use case you may need to map ports up to 4559
*/
@Rule
public LocalStackContainer localstack = new LocalStackContainer(DockerImageName("localstack/localstack:2.0.0"))
                                                    .withExposedPorts(4510, 4511, 4512, 4513, 4514) // the port can have any value between 4510-4559, but LS starts from 4510
                                                    .withEnv("LOCALSTACK_AUTH_TOKEN", auth_token); // add your Auth Token here

```

To find the exposed port which you can use to connect to the instance:

```java
// identify the port localstack provides for the instance
int localstack_port = response.dbInstance().endpoint().port();

// get the port it was mapped to, e.g. the one we can reach from host/the test
int mapped_port = localstack.getMappedPort(localstack_port);
```

## Useful Links

* https://www.testcontainers.com (Java, .NET, Go, Python, Ruby, Node.js)
* https://www.testcontainers.org (Java)
* https://www.testcontainers.org/modules/localstack (Java)
* https://golang.testcontainers.org (Go)
* https://golang.testcontainers.org/modules/localstack (Go)
* https://node.testcontainers.org (NodeJs)
* https://node.testcontainers.org/modules/localstack (NodeJs)
