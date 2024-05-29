---
title: "MemoryDB for Redis"
linkTitle: "MemoryDB for Redis"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS MemoryDB on LocalStack
aliases:
  - /aws/memorydb/
---

## Introduction

MemoryDB is a fully managed, Redis-compatible, in-memory database tailored for workloads demanding ultra-fast, primary database functionality.
It streamlines the deployment and management of in-memory databases within the AWS cloud environment, acting as a replacement for using a cache in front of a database for improved durability and performance.

LocalStack's Pro offering contains support for the main MemoryDB APIs surrounding cluster creation, allowing developers to utilize the MemoryDB functionalities in their local development environment. The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_memorydb/), which provides information on the extent of MemoryDB's integration with LocalStack.

## Getting started

This guide is designed for users new to MemoryDB and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a MemoryDB cluster and connect to it.

### Basic cluster creation

You can create a MemoryDB cluster using the [`CreateCluster`](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateCluster.html) API. Run the following command to create a cluster:

{{< command >}}
$ awslocal memorydb create-cluster \
  --cluster-name my-redis-cluster \
  --node-type db.t4g.small \
  --acl-name open-access 
{{< /command>}}

Once it becomes available, you will be able to use the cluster endpoint for Redis operations. Run the following command to retrieve the cluster endpoint using the [`DescribeClusters`](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html) API:

{{< command >}}
$ awslocal memorydb describe-clusters --query "Clusters[0].ClusterEndpoint"
{
  "Address": "127.0.0.1",
  "Port": 36739
}
{{< /command >}}

The cache cluster uses a random port of the [external service port range]({{< ref "external-ports" >}}) in regular execution and a port between 36739 and 46738 in container mode.
Use this port number to connect to the Redis instance using the `redis-cli` command line tool:

{{< command >}}
$ redis-cli -p 4510 ping
PONG
$ redis-cli -p 4510 set foo bar
OK
$ redis-cli -p 4510 get foo
"bar"
{{< / command >}}

You can also check the cluster configuration using the [`cluster nodes`](https://redis.io/commands/cluster-nodes) command:

{{< command >}}
$ redis-cli -c -p 4510 cluster nodes
...
{{< / command >}}

## Container mode

To start Redis clusters of a specific version, enable container mode for Redis-based services in LocalStack. 
This approach directs LocalStack to launch Redis instances in distinct containers, utilizing your chosen image tag. 
Additionally, container mode is beneficial for independently examining the logs of each Redis instance. To activate this, set the `REDIS_CONTAINER_MODE` configuration variable to `1`.

## Current Limitations

LocalStack's emulation support for MemoryDB primarily focuses on the creation and termination of Redis servers in cluster mode. Essential resources for running a cluster, such as parameter groups, security groups, and subnet groups, are mocked but have no effect on the Redis servers' operation.

LocalStack currently doesn't support MemoryDB snapshots, failovers, users/passwords, service updates, replication scaling, SSL, migrations, service integration (like CloudWatch/Kinesis log delivery, SNS notifications) or tests.

At present, LocalStack does not support features such as:

- MemoryDB snapshots
- Failovers
- User/password management
- Service updates
- Replication scaling
- SSL
- Migrations
- Service integration (e.g., CloudWatch/Kinesis log delivery, SNS notifications) or facilitate related testing.
