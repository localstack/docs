---
title: "Managed Streaming for Kafka (MSK)"
linkTitle: "Managed Streaming for Kafka (MSK)"
categories: ["LocalStack Pro"]
description: >
  Managed Streaming for Kafka (MSK)
---

LocalStack supports a basic version of [Managed Streaming for Kafka (MSK)](https://aws.amazon.com/msk/) for testing. This allows you to spin up Kafka clusters on the local machine, create topics for exchanging messages, and define event source mappings that trigger Lambda functions when messages are received on a certain topic.

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
        "ZookeeperConnectString": "localhost:4515"
    }
}
{{< / command >}}