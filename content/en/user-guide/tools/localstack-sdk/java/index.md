---
title: "Java"
weight: 1
description: Use the LocalStack SDK for Java
---

## Introduction

You can use the LocalStack SDK for Java to develop Java applications that interact with the LocalStack platform and internal developer endpoints.
The SDK extends the REST API, offering an object-oriented interface for easier use.

The LocalStack SDK for Java currently supports these features:

- Save, list, load, and delete Cloud Pods.
- Manage fault configurations for the Chaos API.

{{< callout >}}
This SDK is still in a preview phase, and will be subject to fast and breaking changes.
{{< /callout >}}

## Installation

The best way to use the LocalStack SDK for Java in your project is to consume it from Maven Central.
You can use Maven to import the entire SDK into your project.

```xml
<dependency>
    <groupId>cloud.localstack</groupId>
    <artifactId>localstack-sdk</artifactId>
    <version>0.0.1</version>
</dependency>
```

Similarly, you can copy the following line in the dependencies block of your `build.gradle(.kts)` file, if you are using Gradle as a build tool.

```kotlin
implementation("cloud.localstack:localstack-sdk:0.0.1")
```

## Quick Start

Currently, the LocalStack SDK for Java only supports Chaos and Cloud Pods APIs.
Both these features have a client that can be instantiated from the `cloud.localstack.sdk.chaos` and
`cloud.localstack.sdk.pods` package, respectively.

The clients accept requests built by using the [builder pattern](https://en.wikipedia.org/wiki/Builder_pattern).
For instance, let us imagine the case in which you want to add a fault rule for S3 on the `us-east-1` region.
You first need to use the `FaultRuleRequest` class to build a fault rule request.
Then, you need to pass such a request object to the `addFaultRules` method of a created `ChaosClient`.

```java
import cloud.localstack.sdk.chaos.ChaosClient;
import cloud.localstack.sdk.chaos.requests.FaultRuleRequest;

var client = new ChaosClient();
var faultRuleRequest = new FaultRuleRequest.Builder().faultRule("s3", "us-east-1").build();
var addedRules = client.addFaultRules(request);
```

As a second example, let us look at the necessary code to save and load a Cloud Pod.
Similarly to the `ChaosClient`, the `PodsClient` exposes two functions, `savePod` and `loadPod`, which expect a `SavePodRequest` and a `LoadPodRequest`, respectively.
The resulting code is the following:

```java
import cloud.localstack.sdk.pods.PodsClient;
import cloud.localstack.sdk.pods.requests.LoadPodRequest;
import cloud.localstack.sdk.pods.requests.SavePodRequest;

var podsClient = new PodsClient();
// save a cloud pod
var saveRequest = new SavePodRequest.Builder().podName(POD_NAME).build();
podsClient.savePod(saveRequest);

//load a cloud pod
var loadRequest = new LoadPodRequest.Builder().podName(POD_NAME).build();
podsClient.loadPod(loadRequest);
```
