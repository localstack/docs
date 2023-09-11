---
title: "Neptune"
linkTitle: "Neptune"
categories: ["LocalStack Pro"]
description: >
  Get started with Amazon Neptune on LocalStack
aliases:
  - /aws/neptune/
---

## Introduction

The Neptune API provides a graph database to store nodes and edges. 
It allows to build and navigate relationships.
General use cases include social networking, recommendations, or fraud detection. 
Neptune can be queried using Apache TinkerPop Gremlin queries.

LocalStack supports Neptune via the Pro/Team offering, allowing you to use the Neptune APIs in your local environment. 
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_neptune/), which provides information on the extent of Neptune's integration with LocalStack.

## Getting started

This guide is designed for users new to Neptune and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

For example, you can create a Neptune cluster like this:

{{< command >}}
$ awslocal neptune create-db-cluster \
    --engine neptune \
    --db-cluster-identifier my-neptune-db
{{< / command >}}

You should see the following output:

```json
{
    "DBCluster": {
        ...
        "Endpoint": "localhost:4510",
        "Port": 4510,  # may vary
        "DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:my-neptune-db",
        ...
    }
}
```

To add an instance you can run the following command:

{{< command >}}
$ awslocal neptune create-db-instance \
    --db-cluster-identifier my-neptune-db \
    --db-instance-identifier my-neptune-instance \
    --engine neptune \
    --db-instance-class db.t3.medium
{{< / command >}}

In LocalStack the `Endpoint` for the `DBCluster` and the `Endpoint.Address` of the `DBInstance` will be the same and can be used to connect to the graph database.


To start a connection you have to use the `ws` protocol.

Here is an example that uses python and [gremlinpython](https://pypi.org/project/gremlinpython/) to connect to the database:

```python
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import Bindings, T, gt

ENDPOINT = "localhost:4510" # TODO change to your endpoint
DATABASE_URL = f"ws://{ENDPOINT}/gremlin"


if __name__ == '__main__':
    conn = DriverRemoteConnection(
        DATABASE_URL,
        "g",
        pool_size=1,
    )

    g = traversal().withRemote(conn)

    # add some nodes
    v1 = g.addV("person").property(T.id, "1").property("name", "marko").property("age", 29).next()
    v2 = g.addV("person").property(T.id, "2").property("name", "stephen").property("age", 33).next()
    v3 = g.addV("person").property(T.id, "3").property("name", "mia").property("age", 30).next()

    # add edges/relation
    g.V(Bindings.of("id", v1)).addE("knows").to(v2).property("weight", 0.75).iterate()
    g.V(Bindings.of("id", v1)).addE("knows").to(v3).property("weight", 0.85).iterate()

    # retrieve all names
    names = g.V().values("name").to_list()

    # list all names of persons that know "marko"
    marko_knows = g.V("1").outE("knows").inV().values("name").order().to_list()

    # all persons that "marko" know that are older than 30
    marko_knows_older_30 = g.V("1").out("knows").has("age", gt(30)).values("name").to_list()

    # reset everything
    g.V().drop().iterate()

    result = {
        "names": names,
        "marko_knows": marko_knows,
        "marko_knows_older_30": marko_knows_older_30,
    }
    print(result)
```

## Examples 

The following code snippets and sample applications provide practical examples of how to use ACM in LocalStack for various use cases:

- [Neptune Graph Database Demo](hhttps://github.com/localstack/localstack-pro-samples/tree/master/neptune-graph-db)
