---
title: "Managed Streaming for Kafka (MSK)"
linkTitle: "Managed Streaming for Kafka (MSK)"
categories: ["LocalStack Pro"]
description: >
  Managed Streaming for Kafka (MSK)
---

LocalStack supports a basic version of [Managed Streaming for Kafka (MSK)](https://aws.amazon.com/msk/) for testing. This allows you to spin up Kafka clusters on the local machine, create topics for exchanging messages, and define event source mappings that trigger Lambda functions when messages are received on a certain topic.

## Create a local MSK Cluster

### Prerequisites

- Java 8

To create a local MSK cluster, the following create-cluster example creates an MSK cluster named EventsCluster with three broker nodes. A JSON file named `brokernodegroupinfo.json` specifies the three subnets over which you want yout local Amazon MSK to distribute the broker nodes. This example doesn't specify the monitoring level, so the cluster gets the DEFAULT level.

{{< command >}}
$ awslocal kafka create-cluster \
    --cluster-name "EventsCluster" \
    --broker-node-group-info file://brokernodegroupinfo.json \
    --kafka-version "2.2.1" \
    --number-of-broker-nodes 3
{{< / command >}}

The brokernodegroupinfo.json contains the following info:
{{< command >}}
{
    "InstanceType": "kafka.m5.xlarge",
    "BrokerAZDistribution": "DEFAULT",
    "ClientSubnets": [
        "subnet-01",
        "subnet-02",
        "subnet-03"
    ]
}
{{< / command >}}
The output of the command looks similar to this:
{{< command >}}
{
    "ClusterArn": "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster/b154d18a-8ecb-4691-96b2-50348357fc2f-25",
    "ClusterName": "EventsCluster",
    "State": "CREATING"
}
{{< / command >}}

Describing the MSK cluster can be achieved by running the following command. Replace the ClusterArn with your own.

{{< command >}}
awslocal kafka describe-cluster --cluster-arn "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster/b154d18a-8ecb-4691-96b2-50348357fc2f-25"
{{< / command >}}

The expected output is something like the following

{{< command >}}
{
    "ClusterInfo": {
        "BrokerNodeGroupInfo": {
            "BrokerAZDistribution": "DEFAULT",
            "ClientSubnets": [
                "subnet-01",
                "subnet-02",
                "subnet-03"
            ],
            "InstanceType": "kafka.m5.xlarge"
        },
        "ClusterArn": "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster/b154d18a-8ecb-4691-96b2-50348357fc2f-25",
        "ClusterName": "EventsCluster",
        "CreationTime": "2022-06-29T02:45:16.848000Z",
        "CurrentBrokerSoftwareInfo": {
            "KafkaVersion": "2.5.0"
        },
        "CurrentVersion": "K5OWSPKW0IK7LM",
        "NumberOfBrokerNodes": 3,
        "State": "ACTIVE",
        "ZookeeperConnectString": "localhost:4510"
    }
}

{{< / command >}}

## Create a kafka topic

In this step of using LocalStack MSK, we'll download and use the Kafka command line interface (CLI) to create a topic that produces and consumes data.

Run the following command to download Apache Kafka.

{{< command >}}
wget https://archive.apache.org/dist/kafka/2.2.1/kafka_2.12-2.2.1.tgz
tar -xzf kafka_2.12-2.2.1.tgz
{{< / command >}}


Now, **Go to the kafka_2.12-2.2.1 directory.**

The cluster creation can take a few minutes. To find out whether the cluster you created is ready, run the following command, replacing `ClusterArn` with the Amazon Resource Name (ARN) that you obtained above when you created then Cluster.

{{< command >}}
awslocal kafka describe-cluster --cluster-arn "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster"
{{< / command >}}

Run the following command, replacing ```ZookeeperConnectString``` with the value that you saved after you ran the describe-cluster command.

{{< command >}}
bin/kafka-topics.sh --create --zookeeper localhost:4510 --replication-factor 1 --partitions 1 --topic LocalMSKTopic
{{< / command >}}

Your output should be similar to this one

{{< command >}}
Created topic LocalMSKTopic.
{{< / command >}}

## Interacting with the topic

In this example we use the JVM truststore to talk to the MSK cluster. To do this, first create a folder named `/tmp` on the client machine. Then, go to the bin folder of the Apache Kafka installation and run the following command, replacing ```java_home``` with the path of your ```java_home```. In this instance, the ```java_home``` is ``` /Library/Internet\ Plug-Ins/JavaAppletPlugin.plugin/Contents/Home```.

> **Note**: The following step is optional and may not be required, depending on the operating system environment being used.

{{< command >}}
cp java_home/lib/security/cacerts /tmp/kafka.client.truststore.jks
{{< / command >}}

While still in the bin folder of the Apache Kafka installation on the client machine, create a text file named `client.properties` with the following contents.

{{< command >}}
ssl.truststore.location=/tmp/kafka.client.truststore.jks
{{< / command >}}

Run the following command, replacing ```ClusterArn``` with the Amazon Resource Name (ARN).


{{< command >}}
awslocal kafka get-bootstrap-brokers --cluster-arn ClusterArn
{{< / command >}}

From the JSON result of the command, save the value associated with the string named "`BootstrapBrokerStringTls`" because you need it in the following commands.

{{< command >}}
{
    "BootstrapBrokerString": "localhost:4511"
}
{{< / command >}}

Run the following command in the bin folder, replacing `BootstrapBrokerStringTls` with the value that you obtained when you ran the previous command.

{{< command >}}
./kafka-console-producer.sh --broker-list BootstrapBrokerStringTls --producer.config client.properties --topic LocalMSKTopic
{{< / command >}}

Enter any message that you want, and press Enter. Repeat this step two or three times. Every time you enter a line and press Enter, that line is sent to your Apache Kafka cluster as a separate message.

Keep the connection to the client machine open, and then open a second, separate connection to that machine in a new window.

In the following command, replace ```BootstrapBrokerStringTls``` with the value that you saved earlier. Then, go to the bin folder and run the command using your second connection to the client machine.

{{< command >}}
./kafka-console-consumer.sh --bootstrap-server BootstrapBrokerStringTls --consumer.config client.properties --topic LocalMSKTopic --from-beginning
{{< / command >}}

You start seeing the messages you entered earlier when you used the console producer command. These messages are TLS encrypted in transit.

Enter more messages in the producer window, and watch them appear in the consumer window.


## Local MSK and Lambdas

### Adding a local MSK trigger 

The following example uses the Lambda Event Source Mapping API to map a Lambda function named my-kafka-function to a Kafka topic named LocalMSKTopic. The topic's starting position is set to LATEST.

{{< command >}}
awslocal lambda create-event-source-mapping \
  --event-source-arn arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster \
  --topics LocalMSKTopic \
  --starting-position LATEST \
  --function-name my-kafka-function
{{< / command >}}

The following response is to be expected

{{< command >}}
{
    "UUID": "9c353a2b-bc1a-48b5-95a6-04baf67f01e4",
    "StartingPosition": "LATEST",
    "BatchSize": 100,
    "ParallelizationFactor": 1,
    "EventSourceArn": "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:my-kafka-function",
    "LastModified": "2021-11-21T20:55:49.438914+01:00",
    "LastProcessingResult": "OK",
    "State": "Enabled",
    "StateTransitionReason": "User action",
    "Topics": [
        "LocalMSKTopic"
    ]
}
{{< / command >}}

Using this event source mapping, LocalStack will automatically spawn Lambda functions for each message that gets published to the target Kafka topic. You can use the `kafka-console-producer.sh` client script (see above) to publish messages to the topic, and then observe the LocalStack log output to see how Lambda function are executed (in Docker containers) as new messages arrive.

## Delete the local MSK cluster

Run the following command to list your MSK clusters

{{< command >}}
awslocal kafka list-clusters --region us-east-1
{{< / command >}}

From the list of clusters, pick the ```ClusterARN``` of the cluster you want deleted and run the command

{{< command >}}
awslocal kafka delete-cluster --cluster-arn ClusterArn
{{< / command >}}

