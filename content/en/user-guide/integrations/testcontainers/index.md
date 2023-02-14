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

### Testcontainers for Java

Testcontainers provides a [LocalStack module](https://www.testcontainers.org/modules/localstack/)
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
