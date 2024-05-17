---
title: "Building a Java Notification app using AWS Java SDK, Simple Email Service (SES), and CloudFormation"
linkTitle: "Building a Java Notification app using AWS Java SDK, Simple Email Service (SES), and CloudFormation"
weight: 3
description: >
  Build a Java Spring Boot application to configure Simple Email Service (SES) to send messages using AWS Java SDK in LocalStack. Learn how to configure Simple Queue Service (SQS) & Simple Notification Service (SNS) using CloudFormation templates deployed locally.
type: tutorials
teaser: ""
services:
- ses
- sqs
- sns
- clf
platform:
- java
deployment:
- aws-java-sdk
- CloudFormation
tags:
- Java
- Spring Boot
- AWS Java SDK
- Simple Email Service
- Simple Queue Service
- Simple Notification Service
- CloudFormation
pro: true
leadimage: "java-notification-app-featured-image.png"
---

Java is a popular platform for cloud applications that use Amazon Web Services.
With the AWS Java SDK, Java developers can build applications that work with various AWS services, like Simple Email Service (SES), Simple Queue Service (SQS), Simple Notification Service (SNS), and more. Simple Email Service (SES) is a cloud-based email-sending service that enables developers to integrate email functionality into their applications running on AWS. SES allows developers to work without an on-prem Simple Mail Transfer Protocol (SMTP) system and send bulk emails to many recipients.

[LocalStack Pro](https://app.localstack.cloud/) supports SES along with a simple user interface to inspect email accounts and sent messages. LocalStack also supports sending SES messages through an actual SMTP email server. We will use SQS and SNS to process the emails. We would further employ a CloudFormation stack to configure the infrastructure and configure SNS & SQS subscriptions. AWS Java SDK would be employed to receive these SQS messages and to send these messages through SES further.

In this tutorial, we will build a Java Spring Boot application that uses locally emulated AWS infrastructure on LocalStack provisioned by CloudFormation, and that uses the Java AWS SDK to send SES, SQS, and SNS messages. We will further use [MailHog](https://github.com/mailhog/MailHog), a local SMTP server, to inspect the emails sent through SES via an intuitive user interface.

## Prerequisites

For this tutorial, you will need:

- [LocalStack Pro](https://localstack.cloud/pricing/) to emulate the AWS services (SNS, SQS, SES, etc) locally
  - Don't worry, if you don't have a subscription yet, you can just get a trial license for free.
- [awslocal]({{< ref "aws-cli#localstack-aws-cli-awslocal" >}})
- [Docker](https://docker.io/)
- Java 11+
- Maven 3+

## Project setup

To get started, we will set up our Spring Boot project by implementing a single module named `example` that will house our application code. The module will contain the code required to set up our AWS configuration, notification service, and message application. We will have another directory called `resources` that will house our CloudFormation stack required to set up an SNS topic and an SQS queue. The project directory would look like this:

```bash
├── pom.xml
├── src
│   └── main
│       ├── java
│       │   └── com
│       │       └── example
│       │           ├── AwsConfiguration.java
│       │           ├── MessageApplication.java
│       │           ├── Notification.java
│       │           ├── NotificationController.java
│       │           └── ReceiveSendNotifications.java
│       └── resources
│           └── email-infra.yml
```

In our root POM configuration, we will add the following dependencies:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>cloud.localstack.samples</groupId>
  <artifactId>java-notification-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.2.5.RELEASE</version>
    <relativePath/> <!-- lookup parent from repository -->
  </parent>
  <properties>
    <java.version>11</java.version>
    <awsjavasdk.version>2.17.189</awsjavasdk.version>
  </properties>
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>bom</artifactId>
        <version>2.17.189</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>
  <dependencies>

    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>ses</artifactId>
    </dependency>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>sns</artifactId>
    </dependency>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>sqs</artifactId>
    </dependency>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>cloudformation</artifactId>
    </dependency>

    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-test</artifactId>
      <scope>test</scope>
      <exclusions>
        <exclusion>
          <groupId>org.junit.vintage</groupId>
          <artifactId>junit-vintage-engine</artifactId>
        </exclusion>
      </exclusions>
    </dependency>

  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
      </plugin>
    </plugins>
  </build>
</project>
```

In the above POM file, we have added the AWS Java SDK dependencies for SES, SNS, SQS, and CloudFormation. We have also added the Spring Boot dependencies for our application. We can move on to the next step with the initial setup complete.

## Setting up AWS configuration

To get started, we will setup the AWS configuration, to be defined in `AwsConfiguration.java`, required for our Spring Boot application. We will create a configuration class to use the Spring Bean annotation to create two beans: `SesClient` and a `SqsClient`, to connect to the SES and SQS clients respectively. We will then create a bean to retrieve the `queueUrl` for the `email-notification-queue`:

```java
package com.example;

import java.net.URI;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import software.amazon.awssdk.auth.credentials.EnvironmentVariableCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ses.SesClient;
import software.amazon.awssdk.services.sqs.SqsClient;

@Configuration
public class AwsConfiguration {

    private static final String ENDPOINT_URL = "http://localhost:4566";
    private static final Region DEFAULT_REGION = Region.US_EAST_1;

    @Bean
    public SqsClient sqsClient() {
        return SqsClient.builder()
                .region(DEFAULT_REGION)
                .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
                .applyMutation(builder -> {
                    builder.endpointOverride(URI.create(ENDPOINT_URL));
                })
                .build();
    }

    @Bean
    public SesClient sesClient() {
        return SesClient.builder()
                .region(DEFAULT_REGION)
                .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
                .applyMutation(builder -> {
                    builder.endpointOverride(URI.create(ENDPOINT_URL));
                })
                .build();
    }

    @Bean
    @Autowired
    public String notificationQueueUrl(SqsClient sqsClient) {
        return sqsClient.getQueueUrl(builder -> {
            builder.queueName("email-notification-queue");
        }).queueUrl();
    }
}
```

In the above code, we have used the `@Autowired` annotation to autowrire the dependencies that are required for the application (`SqsClient` `SesClient`, and `notificationQueueUrl` in this case). Now that we have got the URL of the queue created in the previous step, we can move on to the next step.

{{< callout "note" >}}
You can also use the pre-defined clients from the [localstack-utils](https://mvnrepository.com/artifact/cloud.localstack/localstack-utils) Maven project, as an alternative to creating the AWS SDK clients with endpoint overrides manually.
{{< /callout >}}

## Creating a Notification Service

To get started with creating a Notification Service, we would need to create a `Notification` class to define the structure of the notification that we would be sending to the SQS queue. We will create a `Notification` class in the `Notification.java` file:

```java
package com.example;

public class Notification {
    private String address;
    private String subject;
    private String body;

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
}
```

In the above code, we have defined three instance variables: `address`, `subject`, and `body`. We have also defined the getters and setters for the instance variables. Let's now create a `@Component` class to listen to a queue, receive and transform the notifications into emails, and send the emails transactionally:

```java
package com.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import software.amazon.awssdk.services.ses.SesClient;
import software.amazon.awssdk.services.ses.model.SendEmailRequest;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.Message;
import software.amazon.awssdk.services.sqs.model.ReceiveMessageRequest;
import software.amazon.awssdk.services.sqs.model.ReceiveMessageResponse;

@Component
public class ReceiveSendNotifications {

    private static final Logger LOG = LoggerFactory.getLogger(ReceiveSendNotifications.class);

    private static final String SOURCE_EMAIL = "no-reply@localstack.cloud";

    @Autowired
    private SqsClient sqsClient;

    @Autowired
    private SesClient sesClient;

    @Autowired
    private String notificationQueueUrl;

    private final ObjectMapper objectMapper = new ObjectMapper();

    public List<String> processNotifications() {
        // receive messages from queue
        ReceiveMessageResponse receiveMessageResponse = sqsClient.receiveMessage(
                request -> request.queueUrl(notificationQueueUrl).maxNumberOfMessages(10)
        );

        if (!receiveMessageResponse.hasMessages()) {
            return Collections.emptyList();
        }

        // transform notifications
        List<Message> messages = receiveMessageResponse.messages();
        List<Notification> notificationsToSend = new ArrayList<>(messages.size());
        List<String> notificationReceipts = new ArrayList<>(messages.size());
        for (Message message : messages) {
            String body = message.body();

            try {
                // extract SNS event
                HashMap snsEvent = objectMapper.readValue(body, HashMap.class);
                LOG.info("processing snsEvent {}", snsEvent);

                // Notification is expected to be wrapped in the SNS message body
                String notificationString = snsEvent.get("Message").toString();
                Notification notification = objectMapper.readValue(notificationString, Notification.class);
                notificationsToSend.add(notification);
                notificationReceipts.add(message.receiptHandle());
            } catch (JsonProcessingException e) {
                LOG.error("error processing message body {}", body, e);
            }
        }

        // send notifications transactional
        List<String> sentMessages = new ArrayList<>();
        for (int i = 0; i < notificationsToSend.size(); i++) {
            Notification notification = notificationsToSend.get(i);
            String receiptHandle = notificationReceipts.get(i);

            try {
                String messageId = sendNotificationAsEmail(notification);
                LOG.info("successfully sent notification as email, message id = {}", messageId);
                sentMessages.add(messageId);
            } catch (Exception e) {
                LOG.error("could not send notification as email {}", notification, e);
                continue;
            }

            sqsClient.deleteMessage(builder -> {
                builder.queueUrl(notificationQueueUrl).receiptHandle(receiptHandle);
            });
        }

        return sentMessages;
    }

    public String sendNotificationAsEmail(Notification notification) {
        return sesClient.sendEmail(notificationToEmail(notification)).messageId();
    }

    public SendEmailRequest notificationToEmail(Notification notification) {
        return SendEmailRequest.builder().applyMutation(email -> {
            email.message(msg -> {
                msg.body(body -> {
                    body.text(text -> {
                        text.data(notification.getBody());
                    });
                }).subject(subject -> {
                    subject.data(notification.getSubject());
                });
            }).destination(dest -> {
                dest.toAddresses(notification.getAddress());
            }).source(SOURCE_EMAIL);
        }).build();
    }

    public List<HashMap<String, String>> listMessages() {
        ReceiveMessageRequest receiveRequest = ReceiveMessageRequest.builder()
                .queueUrl(notificationQueueUrl)
                .visibilityTimeout(0)
                .maxNumberOfMessages(10)
                .build();

        ReceiveMessageResponse receiveMessageResponse = sqsClient.receiveMessage(receiveRequest);
        if (!receiveMessageResponse.hasMessages()) {
            return Collections.emptyList();
        }
        return receiveMessageResponse.messages().stream().map(Message::body).map(str -> {
            try {
                return (HashMap<String, String>) objectMapper.readValue(str, HashMap.class);
            } catch (JsonProcessingException e) {
                LOG.error("error processing message body {}", str, e);
                HashMap<String, String> map = new HashMap<>();
                map.put("body", str);
                return map;
            }
        }).collect(Collectors.toList());
    }

    public void purgeQueue() {
        sqsClient.purgeQueue(builder -> {
            builder.queueUrl(notificationQueueUrl);
        });
    }

}
```

Let us now create a Notification Controller to:

- Send emails from all parseable notifications in the queue (using the `/process` endpoint)
- List all the message bodies (using the `/list` endpoint)
- Purge the messages from the queue (using the `/purge` endpoint)

Let's create a controller class to define the endpoints for the Notification Service:

```java
package com.example;

import java.util.HashMap;
import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class NotificationController {

    @Autowired
    ReceiveSendNotifications msgService;

    // Send emails for all parseable notifications
    @RequestMapping(value = "/process", method = RequestMethod.GET)
    @ResponseBody
    List<String> processNotifications(HttpServletRequest request, HttpServletResponse response) {
        return msgService.processNotifications();
    }


    //  Lists all message bodies
    @RequestMapping(value = "/list", method = RequestMethod.GET)
    @ResponseBody
    List<HashMap<String, String>> listMessages(HttpServletRequest request, HttpServletResponse response) {
        return msgService.listMessages();
    }


    //  Purge the message queue
    @RequestMapping(value = "/purge", method = RequestMethod.GET)
    @ResponseBody
    void purgeQueue(HttpServletRequest request, HttpServletResponse response) {
        msgService.purgeQueue();
    }

}
```

## Setup the Spring Boot application & infrastructure

Now that we have the code ready, let us setup the Spring Boot application using the `SpringApplication` Class to bootstrap and launch our Spring application from the `main` method.

```java
package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MessageApplication {

    public static void main(String[] args) {
        SpringApplication.run(MessageApplication.class, args);
    }

}
```

You can now build the application using the following command:

{{< command >}}
$ mvn clean install
{{< / command >}}

If the build is successful, you will notice a `BUILD SUCCESS` message. Now that we have the application ready, let us setup the infrastructure using CloudFormation. Create a new file in ``src/main/resources` called `email-infra.yml` and add the following content:

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  EmailQueue:
    Type: AWS::SQS::Queue
    Properties:
      QueueName: email-notification-queue
  EmailTopic:
    Type: AWS::SNS::Topic
    Properties:
      TopicName: email-notifications

  SnsSubscription:
    Type: AWS::SNS::Subscription
    Properties:
      Protocol: sqs
      Endpoint: !GetAtt EmailQueue.Arn
      TopicArn: !GetAtt EmailTopic.TopicArn
```

In the above code, we have created a queue called `email-notification-queue` and a topic called `email-notifications`. We have also created a subscription between the queue and the topic, allowing any message published to the topic to be sent to the queue.

## Creating the infrastructure

Now that the initial coding is done, we can give it a try. Let's start LocalStack using a custom `docker-compose` setup, which includes MailHog to capture the emails sent by SES:

```yaml
version: "3.8"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4510-4559:4510-4559"  # external service port range
      - "127.0.0.1:4566:4566"            # LocalStack Edge Proxy
    environment:
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?}
      - DEBUG=1
      - HOST_TMP_FOLDER=${TMPDIR:-/tmp/}localstack
      - SMTP_HOST=smtp:1025
    volumes:
      - "${TMPDIR:-/tmp}/localstack:/tmp/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"

  smtp:
    image: mailhog/mailhog
    ports:
      - "1025"
      - "8025:8025"
```

The above `docker-compose` file will start LocalStack and pull the MailHog image to start the SMTP server (if it doesn't exist yet!) on port `8025`. You can start LocalStack using the following command:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<your-auth-token> docker-compose up -d
{{< / command >}}

Once LocalStack is started, we can deploy the CloudFormation stack (which might take a few moments):

{{< command >}}
$ awslocal cloudformation deploy \
    --template-file src/main/resources/email-infra.yml \
    --stack-name email-infra
{{< / command >}}

With our infrastructure ready, we can now start the Spring Boot application. We will set dummy AWS access credentials as environment variables in the command:

{{< command >}}
$ AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test mvn spring-boot:run
{{< / command >}}

## Testing the application

To get started, we will an add email address to the list of identities for our mocked SES account to verify the email address:

{{< command >}}
$ awslocal ses verify-email-identity --email-address no-reply@localstack.cloud
{{< / command >}}

Let us now send a message to the topic:

{{< command >}}
$ awslocal sns publish \
    --topic arn:aws:sns:us-east-1:000000000000:email-notifications \
    --message '{"subject":"hello", "address": "alice@example.com", "body": "hello world"}'
{{< / command >}}

In the above command, we have published a message to the topic `email-notifications` with a generic message body. The output of the command should look like this:

```json
{
    "MessageId": "<MESSAGE-ID>"
}
```

You can now use cURL to send a request to the `/list` endpoint for the queued messages:

{{< command >}}
$ curl -s localhost:8080/list | jq .
{{< / command >}}

You will see an output similar to the following:

```json
[
  {
    "SignatureVersion": "1",
    "Type": "Notification",
    "TopicArn": "arn:aws:sns:us-east-1:000000000000:email-notifications",
    "Message": "{\"subject\":\"hello\", \"address\": \"alice@example.com\", \"body\": \"hello world\"}",
    "UnsubscribeURL": "http://localhost:4566/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:000000000000:email-notifications:<ID>",
    "Signature": "EXAMPLEpH+..",
    "Timestamp": "<TIMESTAMP>",
    "SigningCertURL": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-0000000000000000000000.pem",
    "MessageId": "<MESSAGE-ID>",
  }
]
```

You can now run the `/process` endpoint to send the queued notifications as emails:

{{< command >}}
$ curl -s localhost:8080/process
{{< / command >}}

To check whether the email has been sent, you can query the LocalStack internal SES endpoint using the following command:

{{< command >}}
$ curl -s localhost:4566/_aws/ses | jq .
{{< / command >}}

You will see an output similar to the following:

```json
{
  "messages": [
    {
      "Id": "<ID>",
      "Timestamp": "<TIMESTAMP>",
      "Region": "us-east-1",
      "Source": "no-reply@localstack.cloud",
      "Destination": {
        "ToAddresses": [
          "alice@example.com"
        ]
      },
      "Subject": "hello",
      "Body": {
        "text_part": "hello world",
        "html_part": null
      }
    }
  ]
}
```

You can also navigate to the MailHog via the user-interface: [`localhost:8025`](http://localhost:8025/) to check out the email.

## Conclusion

In this tutorial, we have demonstrated, how you can:

- Use CloudFormation to provision infrastructure for SNS & SQS subscriptions on LocalStack
- Use the AWS Java SDK and Spring Boot to build an application that sends SQS and SES messages.

Using [LocalStack Pro](https://app.localstack.cloud), you can use our Web user interface to view the email messages sent by SES. The code for this tutorial can be found in our [LocalStack Pro samples over GitHub](https://github.com/localstack/localstack-pro-samples/tree/master/java-notification-app).
