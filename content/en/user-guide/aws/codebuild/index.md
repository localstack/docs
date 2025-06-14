---
title: CodeBuild
linkTitle: CodeBuild
description: >
  Get started with CodeBuild on LocalStack
tags: ["Base"]
---

## Introduction

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy.
It is part of the [AWS Developer Tools suite](https://aws.amazon.com/products/developer-tools/) and integrates with other AWS services to provide an end-to-end development pipeline.

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
`MessageUtil.java` contains the entire logic of this small application.
It does nothing more than print a salutation message.
Create a `MessageUtil.java` file and save it into the `src/main/java` directory.

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

Every build needs to be tested.
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

In this file we can observe how the build will be executed.
First, we define a runtime version.
Then, we run a `mvn install` command in the build phase which does both the compilation and the testing.
The pre and post build phases do not do much in this example, but can be used for various things, like install some software needed for the build itself.

A full specification of a `buildspec` file can be found in the [AWS CodeBuild docs](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html).

### Create input and output buckets

Now we have to create two S3 buckets:
- one bucket that stores the source we just created, that will be the source of the AWS CodeBuild build
- one bucket where the output of the build, i.e., the JAR file, will be stored.

Create the buckets with the following commands:

{{< command >}}
$ awslocal s3 mb s3://codebuild-demo-input
<disable-copy>
make_bucket: codebuild-demo-input
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal s3 mb s3://codebuild-demo-output
<disable-copy>
make_bucket: codebuild-demo-output
{{< /command >}}

Finally, zip the content of the source code directory and upload it to the created source bucket.
With a UNIX system, you can simply use the `zip` utility:
{{< command >}}
$ zip -r MessageUtil.zip <source-directory>
{{< /command >}}

Then, upload `MessageUtil.zip` to the `codebuild-demo-input` bucket with the following command:

{{< command >}}
$ awslocal s3 cp MessageUtil.zip s3://codebuild-demo-input
{{< /command >}}

### Configuring IAM

To properly work, AWS CodeBuild needs access to other AWS services, e.g., to retrieve the source code from a S3 bucket.
Create a `create-role.json` file with following content:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "codebuild.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Then, run the following command to create the necessary IAM role:
{{< command >}}
$ awslocal iam create-role --role-name CodeBuildServiceRole --assume-role-policy-document file://create-role.json
{{< /command >}}

From the command's response, keep note of the role ARN:
it will be needed to create the CodeBuild project later on.

Let us now define a policy for the created role.
Create a `put-role-policy.json` file with the following content:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CloudWatchLogsPolicy",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CodeCommitPolicy",
      "Effect": "Allow",
      "Action": [
        "codecommit:GitPull"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3GetObjectPolicy",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3PutObjectPolicy",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3BucketIdentity",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketAcl",
        "s3:GetBucketLocation"
      ],
      "Resource": "*"
    }
  ]
}
```

Finally, assign the policy to the role with the following command:

{{< command >}}
$ awslocal put-role-policy --role-name CodeBuildServiceRole --policy-name CodeBuildServiceRolePolicy --policy-document file://put-role-policy.json
{{< /command >}}

### Create the build project

We now need to create a build project, containing all the information about how to run a build, where to get the source code, and where to place the output.

You can use the CLI to generate the skeleton of the `CreateBuild` request, which you can later modify.
Save the output of the following command to a file named `create-project.json`.

{{< command >}}
$ awslocal codebuild create-project --generate-cli-skeleton
{{< /command >}}

From the generated file, change the source and the artifact location to match the S3 bucket names you just created.
Similarly, fill in the ARN of the CodeBuild service role.

```json {hl_lines=[5,9,16]}
{
  "name": "codebuild-demo-project",
  "source": {
    "type": "S3",
    "location": "codebuild-demo-input"
  },
  "artifacts": {
    "type": "S3",
    "location": "codebuild-demo-output"
  },
  "environment": {
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/standard:5.0",
    "computeType": "BUILD_GENERAL1_SMALL"
  },
  "serviceRole": "service-role-arn"
}
```

Now create the project with the following command:

{{< command >}}
$ awslocal codebuild create-project --cli-input-json file://create-project.json
{{< /command >}}

You have now created a CodeBuild project called `codebuild-demo-project` that uses the S3 buckets you just created as source and artifact.

{{< callout >}}
By default, LocalStack runs the all the builds in a Amazon Linux Container, ignoring the image provided in the `environment` parameter.
See the [Build Environments](#build-environments) section for more details.
{{< /callout >}}

### Run the build

In this final step, you can now execute your build with the following command:

{{< command >}}
$ awslocal codebuild start-build --project-name codebuild-demo-project
{{< /command >}}

Make note of the `id` information given in output, since it can be used to query the status of the build.
If you inspect the running containers (e.g., with the `docker ps -a` command), you will notice a container with the `localstack-codebuild` prefix (followed by the build ID), which CodeBuild started to execute the build.
This container will be responsible to start a Docker compose stack that executes the actual build.

As said, you can inspect the status of the build with the following command:

{{< command >}}
$ awslocal codebuild batch-get-builds --ids <build-id>
{{< /command >}}

The command returns a list of builds.
A build has a `buildStatus` attribute that will be set to `SUCCEEDED` if the build correctly terminates.

{{< callout >}}
Each build goes through different phases, each of them having a start and end time, as well as a status.
LocalStack does not provided such granular information.
Currently, it reports only the final status of the build.
{{< /callout >}}

Once the build is completed, you can verify that the JAR artifact has been uploaded to the correct S3 bucket with the following command:

{{< command >}}
$ awslocal s3 ls://codebuild-demo-output
{{< /command >}}

## Build Environments

LocalStack does not offer out-of-the-box all the build environments provided by AWS CodeBuild.
By default, all the builds are executed in a Amazon Linux 2023 image (`public.ecr.aws/codebuild/amazonlinux-x86_64-standard:5.0` and `public.ecr.aws/codebuild/amazonlinux-aarch64-standard:3.0` for x86 and ARM, respectively).
You can overcome this limitation by activating the `CODEBUILD_ENABLE_CUSTOM_IMAGES` environment variable.

AWS shares the Dockerfiles of official AWS CodeBuild curated Docker images in a dedicated [GitHub repository](https://github.com/aws/aws-codebuild-docker-images).
For instance, let us assume you want to run your builds on the Ubuntu `7.0` standard image.

First, you have to build the image as follows:
{{< command >}}
$ git clone https://github.com/aws/aws-codebuild-docker-images.git
$ cd aws-codebuild-docker-images
$ cd ubuntu/standard/7.0
$ docker build -t aws/codebuild/standard:7.0 .
{{< /command >}}

Then, start LocalStack with `CODEBUILD_ENABLE_CUSTOM_IMAGES=1`.
Finally, you can use the create image name, i.e., `aws/codebuild/standard:7.0` in the environment reference when you create you CodeBuild project.

## Limitations

- CodeBuild currently only supports S3, NO_SOURCE, and CODEPIPELINE as [project source](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ProjectSource.html).
- Custom build environments needs to have `bash` installed to properly work in LocalStack.
- Environment variables in the `buildspec` are currently not supported.
- Communication with the LocalStack container within the build environment is possible only via the host network, by using the Gateway IP address (typically 172.17.0.1) or `host.docker.internal` if running on MacOS.
