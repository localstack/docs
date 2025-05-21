---
title: CodeBuild
linkTitle: CodeBuild
description: >
  Get started with CodeBuild on LocalStack
tags: ["Pro image"]
---

## Introduction

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.
It's part of the AWS Developer Tools suite and integrates with other AWS services to provide an end-to-end development pipeline.

LocalStack supports the emulation of most of the CodeBuild operations.
The supported operations are listed on the [API coverage page]({{< ref "coverage_codebuild" >}}).

AWS CodeBuild emulation is powered by the [AWS CodeBuild agent](https://docs.aws.amazon.com/codebuild/latest/userguide/use-codebuild-agent.html).

## Getting Started

This tutorial will show you how to use AWS CodeBuild to test and build a deployable version of a Java executable.

It assumes basic knowledge of the [`awslocal`](https://github.com/localstack/awscli-local) wrapper, Apache Maven, and Java.

### Create the source code

In the first step, we have to create the project that we want to build with AWS CodeBuild.

In an empty directory, we need to re-create the following structure:

```bash
root-directory-name
├── pom.xml
└── src
    ├── main
    │   └── java
    │       └── MessageUtil.java
    └── test
        └── java
            └── TestMessageUtil.java
```

Let us walk through these files.
`MessageUtil.java` is the file implementing the logic of this small application.
It does nothing more than print a salutation message.
Copy the following content into the `src/main/java` directory.

```java
public class MessageUtil {
  private String message;

  public MessageUtil(String message) {
    this.message = message;
  }

  public String printMessage() {
    System.out.println(message);
    return message;
  }

  public String salutationMessage() {
    message = "Hi!" + message;
    System.out.println(message);
    return message;
  }
}
```

Every build needs some testing!
Therefore, create the `TestMessageUtil.java` file in the `src/test/java` directory.

```java
import org.junit.Test;
import org.junit.Ignore;
import static org.junit.Assert.assertEquals;

public class TestMessageUtil {

  String message = "Robert";    
  MessageUtil messageUtil = new MessageUtil(message);

  @Test
  public void testPrintMessage() {      
    System.out.println("Inside testPrintMessage()");
    assertEquals(message,messageUtil.printMessage());
  }

  @Test
  public void testSalutationMessage() {
    System.out.println("Inside testSalutationMessage()");
    message = "Hi!" + "Robert";
    assertEquals(message,messageUtil.salutationMessage());
  }
}
```

This small suite simply verifies that the greeting message is built correctly.

Finally, we need a `pom.xml` file to instruct Maven about what to build and which artifact needs to be produced.
Create this file at the root of your directory.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.example</groupId>
  <artifactId>messageUtil</artifactId>
  <version>1.0</version>
  <packaging>jar</packaging>
  <name>Message Utility Java Sample App</name>
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.0</version>
      </plugin>
    </plugins>
  </build>
</project>
```

With the following configuration, Maven will compile the `java` files into a executable jar and run the specified tests.

### Create the buildspec file

Now that we have our project set up, we need to create a `buildspec` file.
A `buildspec` file is a collection of settings and commands, specified in YAML format, that tells AWS CodeBuild how to run a build.

Create this `buildspec.yml` file in the root directory.

```yaml
version: 0.2

phases:
  install:
    runtime-versions:
      java: corretto11
  pre_build:
    commands:
      - echo Nothing to do in the pre_build phase...
  build:
    commands:
      - echo Build started on `date`
      - mvn install
  post_build:
    commands:
      - echo Build completed on `date`
artifacts:
  files:
    - target/messageUtil-1.0.jar
```

### Create input and output buckets

Now we have to create two S3 buckets:
- one bucket that stores the source we just created, that will be the source of the AWS CodeBuild build;
- one bucket where the output of the build, i.e., the JAR file, will be stored.

Create the buckets with the following commands:

{{< command >}}
$ awslocal s3 mb s3://codebuild-demo-input
<disable-copy>
make_bucket: codebuild-demo-input
{{< /command >}}

{{< command >}}
$ awslocal s3 mb s3://codebuild-demo-output
<disable-copy>
make_bucket: codebuild-demo-output
{{< /command >}}

Finally, zip the content of the source code directory and upload it to the created source bucket.
With a UNIX system, you can use the `zip` utility:
{{< command >}}
$ zip -r MessageUtil.zip <source-directory>
{{< /command >}}

Then, upload `MessageUtil.zip` to the `codebuild-demo-input` bucket with the following command:

{{< command >}}
$ awslocal s3 cp MessageUtil.zip s3://codebuild-demo-input
{{< /command >}}

## Limitations

- CodeBuild currently only supports S3 as a code source.
You can use AWS CodePipeline to integrate CodeBuild with a source code repository provider via CodeStarSourceConnection.
- We only use one build
- Talk to the host (pass via the host network)
