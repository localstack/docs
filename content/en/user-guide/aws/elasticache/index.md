---
title: "ElastiCache"
linkTitle: "ElastiCache"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS ElastiCache on LocalStack
aliases:
  - /aws/elasticache/
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

## Getting started

This guide is designed for users new to ElastiCache and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

### Create a single-node Redis cluster

After starting LocalStack Pro, you can create a cluster with the following command.

{{< command >}}
$ awslocal elasticache create-cache-cluster \
  --cache-cluster-id my-redis-cluster \
  --cache-node-type cache.t2.micro \
  --engine redis \
  --num-cache-nodes 1
{{< /command>}}

You should see LocalStack responding with something like:
```json
{
    "CacheCluster": {
        "CacheClusterId": "my-redis-cluster",
        "ConfigurationEndpoint": {
            "Address": "localhost",
            "Port": 4510
        },
        ...
}
```

### Interact with the cache cluster

By default, the cache cluster (in this case the Redis server) is exposed on a random port of the [external service port range]({{< ref "external-ports" >}}).
You can see the port in the ``ConfigurationEndpoint`` directive returned by the `create-cache-cluster` command.
You can also get the port by calling `awslocal elasticache describe-cache-clusters`.

Use the returned port number (in this case `4510` - but it will be a random port within the range) to connect to the Redis instance:
{{< command >}}
$ redis-cli -p 4510 ping
PONG
$ redis-cli -p 4510 set foo bar
OK
$ redis-cli -p 4510 get foo
"bar"
{{< / command >}}

### Replication group

We also support the `create-replication-group` API which supports the replication groups in ElastiCache clusters.
With the API, you can now have a Redis cluster, a Redis replication group with cluster mode disabled, and a Redis replication group with cluster mode enabled.

You can create a replication group as follows:

{{< command >}}
$ awslocal elasticache create-replication-group \
  --engine redis \
  --replication-group-id my-redis-replication-group \
  --primary-cluster-id my-primary-redis-cluster \
  --automatic-failover-enabled \
  --cache-node-type cache.m5.large \
  --num-cache-clusters 2 \
  --replication-group-description 'my replication group'
{{< / command >}}

In the LocalStack log output, you should be able to see that Redis starts in the cluster mode (`Running mode=cluster`):
```
2023-09-11T15:19:20.527  INFO --- [functhread27] l.s.elasticache.redis      : 813:M 11 Sep 2023 15:19:20.527 * Running mode=cluster, port=4511.
```

{{< alert title="Note">}}
Redis requires at least three or more nodes to form a Redis replication group with cluster mode enabled.
Hence, if the user requests only two node groups, we transparently upgrade to three nodes automatically to avoid raising an error.
{{< /alert >}}

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

LocalStack currently supports Redis single-node and cluster mode, but not memcached.
Moreover, LocalStack emulation support for ElastiCache is mostly centered around starting/stopping Redis servers.
Resource necessary to operate a cluster, like parameter groups, security groups, subnets groups, etc. are mocked, but have no effect on the functioning of the Redis servers.
LocalStack currently doesn't support ElastiCache snapshots, users, user groups, service updates, global replication groups, migrations or tests.
You can find a detailed list of covered API methods on the [ElastiCache coverage page]({{< ref "coverage_elasticache" >}}).