---
title: "LocalStack Testing Tools"
weight: 5
categories: ["LocalStack Community", "LocalStack Pro"]
description: >
  Tools to simplify application testing
---

## Covered Topics

* [JVM Testing Utils](#jvm-testing-utils)

## JVM Testing Utils

LocalStack provides [Java Utils library](https://github.com/localstack/localstack-java-utils)
that integrates with JUnit and provides LocalStack-targeted AWS Clients.

### Installation

{{< tabpane >}}
{{< tab header="Maven" lang="xml" >}}
<dependency>
    <groupId>cloud.localstack</groupId>
    <artifactId>localstack-utils</artifactId>
    <version>0.2.15</version>
    <scope>test</scope>
</dependency>
{{< /tab >}}
{{< tab header="Gradle" lang="gradle" >}}
testImplementation group: 'cloud.localstack', name: 'localstack-utils', version: '0.2.15'
{{< /tab >}}
{{< /tabpane >}}

### Usage

{{< tabpane >}}
{{< tab header="Java" lang="java" >}}
...
import cloud.localstack.LocalstackTestRunner;
import cloud.localstack.ServiceName;
import cloud.localstack.TestUtils;
import cloud.localstack.docker.annotation.LocalstackDockerProperties;

@RunWith(LocalstackTestRunner.class)
@LocalstackDockerProperties(services = { ServiceName.S3, "sqs", "kinesis" })
public class MyCloudAppTest {

  @Test
  public void testLocalS3API() {
    AmazonS3 s3 = TestUtils.getClientS3()
    List<Bucket> buckets = s3.listBuckets();
    ...
  }

}
{{< /tab >}}
{{< tab header="Kotlin" lang="kotlin" >}}
...
import cloud.localstack.LocalstackTestRunner
import cloud.localstack.ServiceName
import cloud.localstack.TestUtils
import cloud.localstack.docker.annotation.LocalstackDockerProperties

@RunWith(LocalstackTestRunner::class)
@LocalstackDockerProperties(services = [ServiceName.S3, "sqs", "kinesis"])
public class MyCloudAppTest {

  @Test
  fun testLocalS3API() {
    val s3 = TestUtils.getClientS3()
    val buckets = s3.listBuckets();
    ...
  }

}
{{< /tab >}}
{{< /tabpane >}}

#### Powermock

You can use the PowerMock Library to call the builders default method and still get LocalStack version of the AWS clients.

```java
...
@RunWith(PowerMockRunner.class)
@PowerMockRunnerDelegate(LocalstackTestRunner.class)
@LocalstackDockerProperties(services = { "ses" })
@PrepareForTest({ AmazonSimpleEmailServiceClientBuilder.class, AmazonSimpleEmailServiceAsyncClientBuilder.class })
@PowerMockIgnore({"javax.crypto.*", "org.hamcrest.*", "javax.net.ssl.*", "com.sun.org.apache.xerces.*", "javax.xml.*", "org.xml.*", "javax.management.*", "javax.security.*", "org.w3c.*"})
public class SESMessagingTest {
....
    @Before
    public void mockSES() {
        AmazonSimpleEmailService mockSes = TestUtils.getClientSES();
        PowerMockito.mockStatic(AmazonSimpleEmailServiceClientBuilder.class);
        when(AmazonSimpleEmailServiceClientBuilder.defaultClient()).thenReturn(mockSes);
    }
    @Test
    public void testSendEmail() throws Exception {
        AmazonSimpleEmailService client = amazonSimpleEmailServiceClientBuilder.defaultClient();
    ....
```

#### PowerMockLocalStack Utility

This utility makes easier to use PowerMock with Localstack.

```java
...
public class PowerMockLocalStackExampleTest extends PowerMockLocalStack{
    private static final String TOPIC = "topic";
    @Before
    public void mock() {
        PowerMockLocalStack.mockSNS();
    }

    @Test
    public void testSendMessage() throws JMSException {
        final AmazonSNS clientSNS = AmazonSNSClientBuilder.defaultClient();
        ...
    }
}
```
