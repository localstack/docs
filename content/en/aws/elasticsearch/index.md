---
title: "Elasticsearch Service"
linkTitle: "Elasticsearch Service"
categories: ["LocalStack Community"]
description: >
  Amazon Elasticsearch Service
---

The Elasticsearch Service in LocalStack lets you create a single node Elasticsearch cluster that behaves like the [Amazon Elasticsearch Service](https://aws.amazon.com/opensearch-service/the-elk-stack/what-is-elasticsearch/).


## Creating an Elasticsearch cluster

You can go ahead and use [awslocal]({{< ref "aws-cli.md#localstack-aws-cli-awslocal" >}}) to create a new elasticsearch domain via the `aws es create-elasticsearch-domain` command.

{{< alert >}}
**Note**: Unless you use the Elasticsearch default version, the first time you create a cluster with a specific version, the Elasticsearch binary is downloaded, which may take a while to download.
{{< /alert >}}

{{< alert >}}
**Note**: The default Elasticsearch version used is 7.10.0.
{{< /alert >}}

{{< command >}}
$ awslocal es create-elasticsearch-domain --domain-name my-domain
{
    "DomainStatus": {
        "DomainId": "000000000000/my-domain",
        "DomainName": "my-domain",
        "ARN": "arn:aws:es:us-east-1:000000000000:domain/my-domain",
        "Created": true,
        "Deleted": false,
        "Endpoint": "my-domain.us-east-1.es.localhost.localstack.cloud:4566",
        "Processing": true,
        "ElasticsearchVersion": "7.10.0",
        "ElasticsearchClusterConfig": {
            "InstanceType": "m3.medium.elasticsearch",
            "InstanceCount": 1,
            "DedicatedMasterEnabled": true,
            "ZoneAwarenessEnabled": false,
            "DedicatedMasterType": "m3.medium.elasticsearch",
            "DedicatedMasterCount": 1
        },
        "EBSOptions": {
            "EBSEnabled": true,
            "VolumeType": "gp2",
            "VolumeSize": 10,
            "Iops": 0
        },
        "CognitoOptions": {
            "Enabled": false
        }
    }
}
{{< / command >}}

In the LocalStack log you will see something like, where you can see the cluster starting up in the background.

```
2021-11-08T16:29:28:INFO:localstack.services.es.cluster: starting elasticsearch: /opt/code/localstack/localstack/localstack/infra/elasticsearch/bin/elasticsearch -E http.port=57705 -E http.publish_port=57705 -E transport.port=0 -E network.host=127.0.0.1 -E http.compression=false -E path.data="/tmp/localstack/elasticsearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/data" -E path.repo="/tmp/localstack/elasticsearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/backup" -E xpack.ml.enabled=false with env {'ES_JAVA_OPTS': '-Xms200m -Xmx600m', 'ES_TMPDIR': '/tmp/localstack/elasticsearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/tmp'}
2021-11-08T16:29:28:INFO:localstack.services.es.cluster: registering an endpoint proxy for http://my-domain.us-east-1.es.localhost.localstack.cloud:4566 => http://127.0.0.1:57705
2021-11-08T16:29:30:INFO:localstack.services.es.cluster: OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.
2021-11-08T16:29:32:INFO:localstack.services.es.cluster: [2021-11-08T16:29:32,502][INFO ][o.e.n.Node               ] [noctua] version[7.10.0], pid[22403], build[default/tar/51e9d6f22758d0374a0f3f5c6e8f3a7997850f96/2020-11-09T21:30:33.964949Z], OS[Linux/5.4.0-89-generic/amd64], JVM[Ubuntu/OpenJDK 64-Bit Server VM/11.0.11/11.0.11+9-Ubuntu-0ubuntu2.20.04]
2021-11-08T16:29:32:INFO:localstack.services.es.cluster: [2021-11-08T16:29:32,510][INFO ][o.e.n.Node               ] [noctua] JVM home [/usr/lib/jvm/java-11-openjdk-amd64], using bundled JDK [false]
2021-11-08T16:29:32:INFO:localstack.services.es.cluster: [2021-11-08T16:29:32,511][INFO ][o.e.n.Node               ] [noctua] JVM arguments [-Xshare:auto, -Des.networkaddress.cache.ttl=60, -Des.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dio.netty.allocator.numDirectArenas=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Djava.locale.providers=SPI,COMPAT, -XX:+UseConcMarkSweepGC, -XX:CMSInitiatingOccupancyFraction=75, -XX:+UseCMSInitiatingOccupancyOnly, -Djava.io.tmpdir=/tmp/localstack/elasticsearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/tmp, -XX:+HeapDumpOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Xms200m, -Xmx600m, -XX:MaxDirectMemorySize=314572800, -Des.path.home=/opt/code/localstack/localstack/localstack/infra/elasticsearch, -Des.path.conf=/opt/code/localstack/localstack/localstack/infra/elasticsearch/config, -Des.distribution.flavor=default, -Des.distribution.type=tar, -Des.bundled_jdk=true]
2021-11-08T16:29:36:INFO:localstack.services.es.cluster: [2021-11-08T16:29:36,258][INFO ][o.e.p.PluginsService     ] [noctua] loaded module [aggs-matrix-stats]
2021-11-08T16:29:36:INFO:localstack.services.es.cluster: [2021-11-08T16:29:36,259][INFO ][o.e.p.PluginsService     ] [noctua] loaded module [analysis-common]
2021-11-08T16:29:36:INFO:localstack.services.es.cluster: [2021-11-08T16:29:36,260][INFO ][o.e.p.PluginsService     ] [noctua] loaded module [constant-keyword]
...
```

and after some time, you should see that the `Processing` state of the domain is set to `false`:

{{< command >}}
$ awslocal es describe-elasticsearch-domain --domain-name my-domain | jq ".DomainStatus.Processing"
false
{{< / command >}}

## Interact with the cluster

You can now interact with the cluster at the cluster API endpoint for the domain,
in this case `http://my-domain.us-east-1.es.localhost.localstack.cloud:4566`.

For example:

{{< command >}}
$ curl http://my-domain.us-east-1.es.localhost.localstack.cloud:4566
{
  "name" : "localstack",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "IC7E9daNSiepRBB9Ksul7w",
  "version" : {
    "number" : "7.10.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "51e9d6f22758d0374a0f3f5c6e8f3a7997850f96",
    "build_date" : "2020-11-09T21:30:33.964949Z",
    "build_snapshot" : false,
    "lucene_version" : "8.7.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
{{< / command >}}

Or the health endpoint:

{{< command >}}
$ curl -s http://my-domain.us-east-1.es.localhost.localstack.cloud:4566/_cluster/health | jq .
{
  "cluster_name": "elasticsearch",
  "status": "green",
  "timed_out": false,
  "number_of_nodes": 1,
  "number_of_data_nodes": 1,
  "active_primary_shards": 0,
  "active_shards": 0,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 0,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks": 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 100
}
{{< / command >}}


## Advanced topics

### Endpoints

There are three configurable strategies that govern how domain endpoints are created, and can be configured via the `ES_ENDPOINT_STRATEGY` environment variable.

| Value | Format | Description |
| - | - | - |
| `domain` | `<domain-name>.<region>.es.localhost.localstack.cloud:4566` | This is the default strategy that uses the `localhost.localstack.cloud` domain to route to your localhost |
| `path` | `localhost:4566/es/<region>/<domain-name>` | An alternative that can be useful if you cannot resolve LocalStack's localhost domain |
| `off` | `http://localhost:4571` | Exposes the default cluster directly on the given endpoint (only works with `ES_MULTI_CLUSTER=0`) |


#### Custom Endpoints

LocalStack allows you to set arbitrary custom endpoints for your clusters in the domain endpoint options.
This can be used to overwrite the behavior of the endpoint strategies described above.
You can also choose custom domains, however it is important to add the edge port (`80`/`443` or by default `4566`).

{{< command >}}
awslocal es create-elasticsearch-domain --domain-name my-domain \
    --elasticsearch-version 7.10 \
    --domain-endpoint-options '{ "CustomEndpoint": "http://localhost:4566/my-custom-endpoint", "CustomEndpointEnabled": true }'
{{< / command >}}

Once the domain processing is complete, you can access the cluster:

{{< command >}}
curl http://localhost:4566/my-custom-endpoint/_cluster/health
{{< / command >}}


### Re-using a single cluster instance

In some cases, you may not want to create a new cluster instance for each domain,
for example when you are only interested in testing API interactions instead of actual Elasticsearch functionality.
In this case, you can set `ES_MULTI_CLUSTER=0`, which will multiplex all domains to the same cluster.
This can however lead to unexpected behavior when persisting data into Elastichsearch, or creating clusters with different versions, so we do not recommend it.


### Storage Layout

Elasticsearch will be organized in your `DATA_DIR`, or the temporary directory (e.g., `/tmp/localstack`), as follows:

```
localstack@machine /tmp/localstack % tree -L 4
.
├── elasticsearch
│   └── arn:aws:es:us-east-1:000000000000:domain
│       ├── my-cluster-1
│       │   ├── backup
│       │   ├── data
│       │   └── tmp
│       ├── my-cluster-2
│       │   ├── backup
│       │   ├── data
│       │   └── tmp
```

## Differences to AWS

* By default, AWS only sets the `Endpoint` attribute of the cluster status once the cluster is up.
  LocalStack will return the endpoint immediately, but keep `Processing = "true"` until the cluster has been started.
* The `CustomEndpointOptions` allows arbitrary endpoint URLs, which is not allowed in AWS
