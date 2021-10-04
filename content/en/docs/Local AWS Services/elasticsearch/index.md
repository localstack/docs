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
**Note**: The first time you create a cluster, the Elasticsearch binary is downloaded, which may take a while to download.
{{< /alert >}}


{{< alert >}}
**Note**: The default Elasticsearch version used is 7.7.
{{< /alert >}}

```bash
$ awslocal es create-elasticsearch-domain --domain-name foobar
{
    "DomainStatus": {
        "DomainId": "000000000000/foobar",
        "DomainName": "foobar",
        "ARN": "arn:aws:es:us-east-1:000000000000:domain/foobar",
        "Created": false,
        "Deleted": false,
        "Endpoint": "http://localhost:4571",
        "Processing": false,
        "ElasticsearchVersion": "7.7",
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
```

In the LocalStack log you will see something like

```
2021-10-01T21:12:47:INFO:localstack.services.es.es_api: starting <class 'localstack.services.es.cluster.ProxiedElasticsearchCluster'> on localhost:4571
2021-10-01T21:12:47:INFO:localstack.services.install: Downloading and installing local Elasticsearch (7.7.0) server. This may take some time.
[2021-10-01 21:12:47 +0200] [16518] [INFO] Running on http://0.0.0.0:4571 (CTRL + C to quit)
2021-10-01T21:12:47:INFO:hypercorn.error: Running on http://0.0.0.0:4571 (CTRL + C to quit)
2021-10-01T21:13:32:INFO:localstack.services.install: Installing Elasticsearch plugin analysis-icu
2021-10-01T21:13:41:INFO:localstack.services.install: Installing Elasticsearch plugin ingest-attachment
2021-10-01T21:13:54:INFO:localstack.services.install: Installing Elasticsearch plugin analysis-kuromoji
2021-10-01T21:14:01:INFO:localstack.services.install: Installing Elasticsearch plugin mapper-murmur3
2021-10-01T21:14:07:INFO:localstack.services.install: Installing Elasticsearch plugin mapper-size
2021-10-01T21:14:14:INFO:localstack.services.install: Installing Elasticsearch plugin analysis-phonetic
2021-10-01T21:14:21:INFO:localstack.services.install: Installing Elasticsearch plugin analysis-smartcn
2021-10-01T21:14:27:INFO:localstack.services.install: Installing Elasticsearch plugin analysis-stempel
2021-10-01T21:14:45:INFO:localstack.services.install: Installing Elasticsearch plugin analysis-ukrainian
2021-10-01T21:15:01:INFO:localstack.services.es.cluster: starting elasticsearch: /opt/code/localstack/localstack/infra/elasticsearch/bin/elasticsearch -E http.port=59237 -E http.publish_port=59237 -E transport.port=0 -E network.host=127.0.0.1 -E http.compression=false -E path.data="/opt/code/localstack/localstack/infra/elasticsearch/data" -E path.repo="/tmp/localstack/es_backup" -E xpack.ml.enabled=false with env {'ES_JAVA_OPTS': '-Xms200m -Xmx600m', 'ES_TMPDIR': '/opt/code/localstack/localstack/infra/elasticsearch/tmp'}

```

and after some time, you should see that the `Created` state of the domain is set to `true`:

```bash
$ awslocal es describe-elasticsearch-domain --domain-name foobar | jq ".DomainStatus.Created"
true
```

## Interact with the cluster

You can now interact with the cluster at the cluster API endpoint `http://localhost:4571`.

{{< alert >}}
**Note**: Only one Elasticsearch cluster instance is created locally.
Additional domains share the same Elasticsearch cluster.
{{< /alert >}}

For example:

```bash
$ curl http://localhost:4571
{
  "name" : "om",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "z8n5oqE1SAmmhg3bR9jd2A",
  "version" : {
    "number" : "7.7.0",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "81a1e9eda8e6183f5237786246f6dced26a10eaf",
    "build_date" : "2020-05-12T02:01:37.602180Z",
    "build_snapshot" : false,
    "lucene_version" : "8.5.1",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
```

Or the health endpoint:

```bash
curl -s http://localhost:4571/_cluster/health | jq .
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
```
