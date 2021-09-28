---
title: "ElastiCache"
linkTitle: "ElastiCache"
date: 2021-09-28
weight: 5
categories: ["LocalStack Pro"]
description: >
  ElastiCache
---

A basic version of [ElastiCache](https://aws.amazon.com/elasticache/) is provided. By default, the API is started on http://localhost:4598 and supports running a local Redis instance (Memcached support coming soon).

After starting LocalStack Pro, you can test the following commands:
```
$ awslocal elasticache create-cache-cluster --cache-cluster-id i1
{
    "CacheCluster": {
        "CacheClusterId": "i1",
        "ConfigurationEndpoint": {
            "Address": "localhost",
            "Port": 4530
        }
    }
}
```

Then use the returned port number (`4530`) to connect to the Redis instance:
```
$ redis-cli -p 4530 ping
PONG
$ redis-cli -p 4530 set foo bar
OK
$ redis-cli -p 4530 get foo
"bar"
```
