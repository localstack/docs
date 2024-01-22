---
title: "MemoryDB for Redis"
linkTitle: "MemoryDB"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS MemoryDB on LocalStack
aliases:
  - /aws/memorydb/
---

## Introduction

Amazon MemoryDB is a fully managed, Redis-compatible, in-memory database tailored for workloads demanding ultra-fast, primary database functionality.
It streamlines the deployment and management of in-memory databases within the AWS cloud environment, acting as a replacement for using a cache in front of a database for improved durability and performance.

MemoryDB is a good fit for your use case if you want to build an application using Redis data structures and APIs with a primary, durable database.
It seamlessly integrates with applications relying on Redis for its remarkable ultra-fast performance, offering microsecond read times and single-digit millisecond write latencies.
This makes MemoryDB a compelling choice for applications that prioritize speed and responsiveness.

LocalStack's Pro offering contains support for the main MemoryDB APIs surrounding cluster creation, allowing developers to utilize the MemoryDB functionalities in their local development environment.
For detailed information on the supported MemoryDB APIs and the extent of integration with LocalStack, please refer to our API Coverage Page.
This resource outlines the comprehensive support for MemoryDB, enabling developers to simulate and test their applications effectively before deploying them to the AWS cloud.

## Getting started

This guide is designed for users new to MemoryDB and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

### Basic cluster creation

After starting LocalStack Pro, you can create a cluster with the following command.

{{< command >}}
$ awslocal memorydb create-cluster \
  --cluster-name my-redis-cluster \
  --cache-node-type db.t4g.small \
  --acl-name open-access 
{{< /command>}}

Wait for it to be available, then you can use the cluster endpoint for Redis operations.

{{< command >}}
$ awslocal memorydb describe-clusters --query "Clusters[0].ClusterEndpoint"
{
  "Address": "127.0.0.1",
  "Port": 36739
}
{{< /command >}}

The cache cluster uses a random port of the [external service port range]({{< ref "external-ports" >}}) in regular execution and a port between 36739 and 46738 in container mode.
Use this port number to connect to the Redis instance like so:

{{< command >}}
$ redis-cli -p 4510 ping
PONG
$ redis-cli -p 4510 set foo bar
OK
$ redis-cli -p 4510 get foo
"bar"
{{< / command >}}

You can also check the cluster configuration like so:

{{< command >}}
$ redis-cli -c -p 4510 cluster nodes
...
{{< / command >}}



## Container mode

In order to start Redis clusters of a specific version, you need to use the container mode for Redis-based services.
This instructs LocalStack to start Redis instances in a separate container using the specified image tag.
Another reason you might want to use the container mode is to check the logs of every Redis instance separately.

To do this, you can set the `REDIS_CONTAINER_MODE` configuration variable to `1`.

## Limitations

LocalStack emulation support for MemoryDB is mostly centered around starting/stopping Redis servers in cluster mode.
Resources necessary to operate a cluster, like parameter groups, security groups, subnets groups, etc. are mocked, but have no effect on the functioning of the Redis servers.

LocalStack currently doesn't support MemoryDB snapshots, failovers, users/passwords, service updates, replication scaling, SSL, migrations, service integration (like CloudWatch/Kinesis log delivery, SNS notifications) or tests.

