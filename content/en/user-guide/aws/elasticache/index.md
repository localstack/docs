---
title: "ElastiCache"
linkTitle: "ElastiCache"
categories: ["LocalStack Pro"]
description: >
  ElastiCache
---

A basic version of [ElastiCache](https://aws.amazon.com/elasticache/) is provided. By default, the API is started on http://localhost:4598 and supports running a local Redis instance (Memcached support coming soon).

After starting LocalStack Pro, you can test the following commands:
{{< command >}}
$ awslocal elasticache create-cache-cluster --cache-cluster-id i1
{
    "CacheCluster": {
        "CacheClusterId": "i1",
        "ConfigurationEndpoint": {
            "Address": "localhost",
            "Port": 4510
        }

        ...

    }
}
{{< / command >}}

Then use the returned port number (`4510`) to connect to the Redis instance:
{{< command >}}
$ redis-cli -p 4510 ping
PONG
$ redis-cli -p 4510 set foo bar
OK
$ redis-cli -p 4510 get foo
"bar"
{{< / command >}}

We also support the `create-replication-group` API which supports the replication groups in ElastiCache clusters. With the API, you can now have a Redis cluster, a Redis replication group with cluster mode disabled, and a Redis replication group with cluster mode enabled.

{{< alert >}}**Note**:
Redis requires at least 3+ nodes to form a Redis replication group with cluster mode enabled. Hence, if the user requests only 2 node groups, we transparently upgrade to 3 nodes behind the scenes, to avoid raising an error.
{{< /alert >}}
