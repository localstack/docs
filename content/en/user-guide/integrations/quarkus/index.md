---
title: "Quarkus"
linkTitle: "Quarkus"
description: >
  Use the Quarkus framework with LocalStack
---

## Introduction

Quarkus is a Java framework optimized for cloud, serverless, and containerized environments. Quarkus leverages a Kubernetes Native Java stack tailored for GraalVM & OpenJDK HotSpot, which further builds on various Java libraries and standards.

Localstack is supported by Quarkus as a Dev service for Amazon Services. Quarkus Amazon Services automatically starts a LocalStack container in development mode and when running tests, and the extension client is configured automatically.

## Getting started

In this guide, we will demonstrate how you can create a service client for creating and managing Lambdas on LocalStack. The Lambda extension is based on [AWS Java SDK 2.x](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/welcome.html).

### Prerequisites

- [LocalStack](https://docs.localstack.cloud/getting-started/installation) installed and running
- [JDK 17+](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) with `JAVA_HOME` configured properly
- [Maven 3.8.1+](https://maven.apache.org/download.cgi)
- [Docker](https://docs.docker.com/get-docker/)

### Create a Maven project

Create a new project with the following command:

{{< command >}}
$ mvn io.quarkus.platform:quarkus-maven-plugin:3.6.3:create \
    -DprojectGroupId=org.acme \
    -DprojectArtifactId=amazon-lambda-quickstart \
    -DclassName="org.acme.lambda.QuarkusLambdaSyncResource" \
    -Dpath="/sync" \
    -Dextensions="resteasy-reactive-jackson,amazon-lambda"
$ cd amazon-lambda-quickstart
{{< /command >}}

The above command generates a Maven project structure with imports for RESTEasy Reactive/JAX-RS and Amazon Lambda Client extensions.

### Configure Lambda Client

Both Lambda clients (sync and async) can be configured through the `application.properties` file, which should be located in the `src/main/resources` directory. Additionally, ensure that a suitable implementation of the sync client is added to the `classpath`. By default, the extension employs the URL connection HTTP client, so it's necessary to include a URL connection client dependency in the `pom.xml` file:

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>url-connection-client</artifactId>
</dependency>
```

If you want to use Apache HTTP client instead, configure it as follows in `application.properties`:

```xml
quarkus.lambda.sync-client.type=apache
```

Add the following dependencies to the `pom.xml` file:

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>apache-client</artifactId>
</dependency>
````

To configure LocalStack, add the following properties to the `application.properties` file:

```bash
quarkus.lambda.endpoint-override=http://localhost:4566 

quarkus.lambda.aws.region=us-east-1 
quarkus.lambda.aws.credentials.type=static 
quarkus.lambda.aws.credentials.static-provider.access-key-id=test-key
quarkus.lambda.aws.credentials.static-provider.secret-access-key=test-secret
```

### Package the application

You can package the application with the following command:

{{< command >}}
$ ./mvnw clean package
{{< /command >}}

You can further run the application in dev mode with the following command:

{{< command >}}
$ java -Dparameters.path=/quarkus/is/awesome/ -jar target/quarkus-app/quarkus-run.jar
{{< /command >}}

{{< callout "tip" >}}
With GraalVM installed, you can also create a native executable binary using the following command:
{{< command >}}
$ ./mvnw clean package -Dnative.
{{< /command >}}
{{< /callout >}}

{{< callout >}}
Dev Services for Amazon Services is automatically enabled for each extension added to the `pom.xml`, except in the following scenarios:

-   When `quarkus.devservices.enabled` is set to false.
-   When `devservices.enabled` is set to false per extension (e.g., `quarkus.s3.devservices.enabled=false`).
-   When the `endpoint-override` is configured (e.g., `quarkus.s3.endpoint-override=http://localhost:4566`).
{{< /callout >}}

## Supported extensions

- [Lambda](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-lambda.html)
- [S3](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-s3.html)
- [SSM](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-ssm.html)
- [SQS](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-sqs.html)
- [SNS](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-sns.html)
- [SES](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-ses.html)
- [Secrets Manager](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-secretsmanager.html)
- [KMS](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-kms.html)
- [IAM](https://docs.quarkiverse.io/quarkus-amazon-services/dev/amazon-iam.html)

## Configuration

The following configuration properties are fixed at build time. All the other configuration properties can be overridden at runtime.

| Property                                   | Type                   | Default                              |
|----------------------------------------------------------|------------------------|--------------------------------------|
| `quarkus.aws.devservices.localstack.image-name`           | string                 | `localstack/localstack:3.0.1`            |
| `quarkus.aws.devservices.localstack.init-scripts-folder`  | string                 |                                      |
| `quarkus.aws.devservices.localstack.init-scripts-classpath`| string                 |                                      |
| `quarkus.aws.devservices.localstack.init-completion-msg`  | string                 |                                      |
| `quarkus.aws.devservices.localstack.container-properties` | `Map<String,String>`  |                                      |
| `quarkus.aws.devservices.localstack.additional-services."additional-services".enabled` | boolean                |                                      |
| `quarkus.aws.devservices.localstack.additional-services."additional-services".shared`  | boolean                | `false`                              |
| `quarkus.aws.devservices.localstack.additional-services."additional-services".service-name` | string                 | `localstack`                         |
| `quarkus.aws.devservices.localstack.additional-services."additional-services".container-properties` | `Map<String,String>`  |                                      |

{{< callout >}}
- If `quarkus.aws.devservices.localstack.additional-services."additional-services".enabled` is set to `true` and the endpoint-override is not configured, LocalStack will be started and utilized instead of the provided configuration. For all services excluding Cognito, LocalStack will function as the core cloud emulator.  In the case of Cognito, the emulation/mocking will be done by Moto.
- The `quarkus.aws.devservices.localstack.additional-services."additional-services".shared` indicates whether the LocalStack container managed by Dev Services is shared. In shared mode, Quarkus utilizes label-based service discovery, specifically the `quarkus-dev-service-localstack` label, to identify running containers. If a matching container is found, it is used. Otherwise, Dev Services initiates a new container. It's important to note that sharing is not supported for the Cognito extension.
- In `quarkus.aws.devservices.localstack.additional-services."additional-services".service-name`, the value of the `quarkus-dev-service-localstack` label is attached to the initiated container. In dev mode, when the shared flag is true, Dev Services checks for a container with the `quarkus-dev-service-localstack` label set to the configured value before starting a new one. If found, it utilizes the existing container. Otherwise, it creates a new container with the `quarkus-dev-service-localstack` label set to the specified value. In test mode, Dev Services groups services with the same service-name value into a single container instance. This property is useful when there's a requirement for multiple shared LocalStack instances.
{{< /callout >}}

### Specific configuration

Dev Services can support specific configurations passed to the LocalStack container. These configurations can be globally applied to all containers or specified individually per service.

```bash
quarkus.aws.devservices.localstack.image-name=localstack/localstack:3.0.3
quarkus.dynamodb.devservices.container-properties.DYNAMODB_HEAP_SIZE=1G
```

### Additional services

To start additional services for which a Quarkus extension does not exist or is not imported in the project, use the `additional-services` property:

```bash
quarkus.aws.devservices.localstack.additional-services."kinesis".enabled=true
quarkus.aws.devservices.localstack.additional-services."redshift".enabled=true
```
