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

Amazon ElastiCache is a managed in-memory caching service provided by Amazon Web Services (AWS).
It facilitates the deployment and operation of in-memory caches within the AWS cloud environment.
ElastiCache is designed to improve application performance and scalability by alleviating the workload on backend databases.
It supports popular open-source caching engines like Redis and Memcached (LocalStack currently supports Redis),
providing a means to efficiently store and retrieve frequently accessed data with minimal latency.

LocalStack supports ElastiCache via the Pro offering, allowing you to use the ElastiCache APIs in your local environment.
The supported APIs are available on our API Coverage Page,
which provides information on the extent of ElastiCache integration with LocalStack.

Amazon MemoryDB is a fully managed, Redis-compatible, in-memory database service offered by Amazon Web Services (AWS).
It is designed to simplify the deployment and management of in-memory databases in the AWS cloud environment.

MemoryDB plays a crucial role in enhancing application performance and scalability by efficiently handling data stored in-memory, thus reducing the burden on backend databases.
With its Redis compatibility, it seamlessly integrates with applications that leverage Redis for caching, session storage, and real-time analytics.

LocalStack's Pro offering contains support for MemoryDB APIs, allowing developers to utilize the MemoryDB functionalities in their local development environment.
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



## Resource browser

The LocalStack Web Application provides a Resource Browser for managing ElastiCache resources.
You can access the Resource Browser by opening the LocalStack Web Application in your browser and navigating to the Resources section, then clicking on ElastiCache.

In the ElastiCache resource browser you can:

* List and remove existing cache clusters
  {{< img src="elasticache-resource-browser-list.png" alt="Create a ElastiCache cluster in the resource browser" >}}
* View details of cache clusters
  {{< img src="elasticache-resource-browser-show.png" alt="Create a ElastiCache cluster in the resource browser" >}}
* Create new cache clusters
  {{< img src="elasticache-resource-browser-create.png" alt="Create a ElastiCache cluster in the resource browser" >}}


## Limitations

LocalStack emulation support for MemoryDB is mostly centered around starting/stopping Redis servers in cluster mode.
Resources necessary to operate a cluster, like parameter groups, security groups, subnets groups, etc. are mocked, but have no effect on the functioning of the Redis servers.

LocalStack currently doesn't support MemoryDB snapshots, failovers, users/passwords, service updates, replication scaling, SSL, migrations, service integration (like CloudWatch/Kinesis log delivery, SNS notifications) or tests.

You can find a detailed list of covered API methods on the [MemoryDB coverage page]({{< ref "coverage_memorydb" >}}).
