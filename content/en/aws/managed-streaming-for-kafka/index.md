---
title: "Managed Streaming for Kafka (MSK)"
linkTitle: "Managed Streaming for Kafka (MSK)"
categories: ["LocalStack Pro"]
description: >
  Managed Streaming for Kafka (MSK)
---

LocalStack supports a basic version of [Managed Streaming for Kafka (MSK)](https://aws.amazon.com/msk/) for testing. This allows you to spin up Kafka clusters on the local machine, create topics for exchanging messages, and define event source mappings that trigger Lambda functions when messages are received on a certain topic.

# Create a local MSK Cluster

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
The output of the command looks as follows:
{{< command >}}
{
    "ClusterArn": "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster",
    "ClusterName": "EventsCluster",
    "State": "CREATING"
}
{{< / command >}}

Describing the MSK cluster can be as simple as running the following command with the ClusterArn displayed after the creation of the cluser

{{< command >}}
awslocal kafka describe-cluster --cluster-arn "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster"
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
        "ClusterArn": "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster",
        "ClusterName": "EventsCluster",
        "CurrentBrokerSoftwareInfo": {
            "KafkaVersion": "2.5.0"
        },
        "NumberOfBrokerNodes": 3,
        "State": "ACTIVE",
        "ZookeeperConnectString": "localhost:4513"
    }
}
{{< / command >}}

In this step of Getting Started Using LocalStack MSK, you create a client machine. You use this client machine to create a topic that produces and consumes data.

First, Install Java on the client machine by running the following command:

{{< command >}}
sudo yum install java-1.8.0
{{< / command >}}

Run the following command to download Apache Kafka.

{{< command >}}
wget https://archive.apache.org/dist/kafka/2.2.1/kafka_2.12-2.2.1.tgz
{{< / command >}}

Run the following command in the directory where you downloaded the TAR file in the previous step.

{{< command >}}
tar -xzf kafka_2.12-2.2.1.tgz
{{< / command >}}

Now, **Go to the kafka_2.12-2.2.1 directory.**

Cluster creation can take a few minutes. To find out whether the cluster you created is ready, run the following command, replacing ```ClusterArn``` with the Amazon Resource Name (ARN) that you obtained above when you created then Cluster.

{{< command >}}
awslocal kafka describe-cluster --cluster-arn "arn:aws:kafka:us-east-1:000000000000:cluster/EventsCluster"
{{< / command >}}

Run the following command, replacing ```ZookeeperConnectString``` with the value that you saved after you ran the describe-cluster command.

{{< command >}}
bin/kafka-topics.sh --create --zookeeper localhost:4513 --replication-factor 1 --partitions 1 --topic LocalStackMSKTopic
{{< / command >}}

Your output should be similar to this one

{{< command >}}
Created topic LocalStackMSKTopic.
{{< / command >}}

