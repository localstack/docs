---
title: "Neptune"
linkTitle: "Neptune"
description: >
  Get started with Neptune on LocalStack
---

## Introduction

Neptune is a fully managed, highly available, and scalable graph database service offered by AWS. 
It is designed for storing and querying highly connected data for applications that require complex relationship modeling, such as social networks, recommendation engines, and fraud detection.
Neptune supports popular graph query languages like Gremlin and SPARQL, making it compatible with a wide range of graph applications and tools.

LocalStack supports Neptune via the Pro/Team offering, allowing you to use the Neptune APIs in your local environment  to support both property graph and RDF graph models.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_neptune/), which provides information on the extent of Neptune's integration with LocalStack.

 The following versions of Neptune engine are supported by LocalStack:

| Engine Version | Tinkerpop Version |
|-----------------|---------------------|
| `1.1.0.0`       | `3.4.11`            |
| `1.1.1.0`       | `3.5.2`             |
| `1.2.0.0`       | `3.5.2`             |
| `1.2.0.1`       | `3.5.2`             |
| `1.2.0.2`       | `3.5.2`             |
| `1.2.1.0`       | `3.6.2`             |

## Getting started

This guide is designed for users new to Neptune and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script. 

Start your LocalStack container using your preferred method. We will demonstrate the following with AWS CLI & Python:

- Creating a Neptune cluster.
- Starting a connection to the Neptune cluster.
- Running a Python script to create nodes and edges and query the graph database.

### Create a Neptune cluster

To create a Neptune cluster you can use the [`CreateDBCluster`](https://docs.aws.amazon.com/neptune/latest/userguide/api-clusters.html#CreateDBCluster) API. 
Run the following command to create a Neptune cluster:

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
        "Endpoint": "localhost",
        "Port": 4510,  # may vary
        "DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:my-neptune-db",
        ...
    }
}
```

### Add an instance to the cluster

To add an instance you can use the [`CreateDBInstance`](https://docs.aws.amazon.com/neptune/latest/userguide/api-instances.html#CreateDBInstance) API. 
Run the following command to create a Neptune instance:

{{< command >}}
$ awslocal neptune create-db-instance \
    --db-cluster-identifier my-neptune-db \
    --db-instance-identifier my-neptune-instance \
    --engine neptune \
    --db-instance-class db.t3.medium
{{< / command >}}

In LocalStack the `Endpoint` for the `DBCluster` and the `Endpoint.Address` of the `DBInstance` will be the same and can be used to connect to the graph database.

### Start a connection

To start a connection you have to use the `ws` protocol.

Here is an example that uses Python and [`gremlinpython`](https://pypi.org/project/gremlinpython/) to connect to the database:

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

The following code snippets and sample applications provide practical examples of how to use Neptune in LocalStack for various use cases:

- [Neptune Graph Database Demo](https://github.com/localstack/localstack-pro-samples/tree/master/neptune-graph-db)
