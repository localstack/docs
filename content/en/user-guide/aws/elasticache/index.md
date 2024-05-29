---
title: "ElastiCache"
linkTitle: "ElastiCache"
categories: ["LocalStack Pro"]
description: Get started with AWS ElastiCache on LocalStack
aliases:
- /aws/elasticache/
persistence: supported

---

## Introduction

Amazon ElastiCache is a managed in-memory caching service provided by Amazon Web Services (AWS).
It facilitates the deployment and operation of in-memory caches within the AWS cloud environment.
ElastiCache is designed to improve application performance and scalability by alleviating the workload on backend databases.
It supports popular open-source caching engines like Redis and Memcached (LocalStack currently supports Redis),
providing a means to efficiently store and retrieve frequently accessed data with minimal latency.

LocalStack supports ElastiCache via the Pro offering, allowing you to use the ElastiCache APIs in your local environment.
The supported APIs are available on our [API Coverage Page]{{< ref "coverage_elasticache" >}},
which provides information on the extent of ElastiCache integration with LocalStack.


## Getting started

This guide is designed for users new to ElastiCache and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.


### Single cache cluster

After starting LocalStack Pro, you can create a cluster with the following command.

{{< command >}}
$ awslocal elasticache create-cache-cluster \
  --cache-cluster-id my-redis-cluster \
  --cache-node-type cache.t2.micro \
  --engine redis \
  --num-cache-nodes 1
{{< /command>}}

Wait for it to be available, then you can use the cluster endpoint for Redis operations.

{{< command >}}
$ awslocal elasticache describe-cache-clusters --show-cache-node-info --query "CacheClusters[0].CacheNodes[0].Endpoint"
{
  "Address": "localhost.localstack.cloud",
  "Port": 4510
}
{{< /command >}}

The cache cluster uses a random port of the [external service port range]({{< ref "external-ports" >}}).
Use this port number to connect to the Redis instance like so:

{{< command >}}
$ redis-cli -p 4510 ping
PONG
$ redis-cli -p 4510 set foo bar
OK
$ redis-cli -p 4510 get foo
"bar"
{{< / command >}}


### Replication groups in non-cluster mode

{{< command >}}
$ awslocal elasticache create-replication-group \
  --replication-group-id my-redis-replication-group \
  --replication-group-description 'my replication group' \
  --engine redis \
  --cache-node-type cache.t2.micro \
  --num-cache-clusters 3
{{< /command >}}

Wait for it to be available. When running the following command, you should see one node group when running:

{{< command >}}
$ awslocal elasticache describe-replication-groups --replication-group-id my-redis-replication-group
{{< /command >}}

To retrieve the primary endpoint:

{{< command >}}
$ awslocal elasticache describe-replication-groups --replication-group-id my-redis-replication-group \
  --query "ReplicationGroups[0].NodeGroups[0].PrimaryEndpoint"
{{< /command >}}


### Replication groups in cluster mode

The cluster mode is enabled by using `--num-node-groups` and `--replicas-per-node-group`:

{{< command >}}
$ awslocal elasticache create-replication-group \
  --engine redis \
  --replication-group-id my-clustered-redis-replication-group \
  --replication-group-description 'my clustered replication group' \
  --cache-node-type cache.t2.micro \
  --num-node-groups 2 \
  --replicas-per-node-group 2
{{< /command >}}

Note that the group nodes do not have a primary endpoint. Instead they have a `ConfigurationEndpoint`, which you can connect to using `redis-cli -c` where `-c` is for cluster mode.

{{< command >}}
$ awslocal elasticache describe-replication-groups --replication-group-id my-clustered-redis-replication-group \
    --query "ReplicationGroups[0].ConfigurationEndpoint"
{{< /command >}}

## Container mode

In order to start Redis clusters of a specific version, you need to use the container mode for Redis-based services.
This instructs LocalStack to start Redis instances in a separate container using the specified image tag.
Another reason you might want to use the container mode is to check the logs of every Redis instance separately.

To do this, you can set the `REDIS_CONTAINER_MODE` configuration variable to `1`.

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


## Current Limitations

LocalStack currently supports Redis single-node and cluster mode, but not memcached.
Moreover, LocalStack emulation support for ElastiCache is mostly centered around starting/stopping Redis servers.

Resources necessary to operate a cluster, like parameter groups, security groups, subnets groups, etc. are mocked, but have no effect on the functioning of the Redis servers.

LocalStack currently doesn't support ElastiCache snapshots, failovers, users/passwords, service updates, replication scaling, SSL, migrations, service integration (like CloudWatch/Kinesis log delivery, SNS notifications) or tests.
