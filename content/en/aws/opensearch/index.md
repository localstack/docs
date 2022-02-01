---
title: "OpenSearch Service"
linkTitle: "OpenSearch Service"
categories: ["LocalStack Community"]
description: >
  Amazon OpenSearch Service (successor to Amazon Elasticsearch Service)
---

The OpenSearch Service in LocalStack lets you create one or more single-node OpenSearch clusters that behave like the [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/).
This service is, like its AWS counterpart, heavily linked with the [Elasticsearch Service](../elasticsearch).
Any cluster created with the OpenSearch Service will show up in the Elasticsearch Service and vice versa.


## Creating an OpenSearch cluster

You can go ahead and use [awslocal]({{< ref "aws-cli.md#localstack-aws-cli-awslocal" >}}) to create a new OpenSearch domain via the `aws opensearch create-domain` command.

{{< alert >}}
**Note**: Everytime when you create a cluster with a version of OpenSearch you haven't used before, the OpenSearch binary for the respective version needs to be downloaded, which may take a while.
{{< /alert >}}

{{< alert >}}
**Note**: The default OpenSearch version used is 1.1.0.
{{< /alert >}}

{{< command >}}
$ awslocal opensearch create-domain --domain-name my-domain
{
    "DomainStatus": {
        "DomainId": "000000000000/my-domain",
        "DomainName": "my-domain",
        "ARN": "arn:aws:es:us-east-1:000000000000:domain/my-domain",
        "Created": true,
        "Deleted": false,
        "Endpoint": "my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566",
        "Processing": true,
        "UpgradeProcessing": false,
        "EngineVersion": "OpenSearch_1.1",
        "ClusterConfig": {
            "InstanceType": "m3.medium.search",
            "InstanceCount": 1,
            "DedicatedMasterEnabled": true,
            "ZoneAwarenessEnabled": false,
            "DedicatedMasterType": "m3.medium.search",
            "DedicatedMasterCount": 1,
            "WarmEnabled": false,
            "ColdStorageOptions": {
                "Enabled": false
            }
        },
        "EBSOptions": {
            "EBSEnabled": true,
            "VolumeType": "gp2",
            "VolumeSize": 10,
            "Iops": 0
        },
        "AccessPolicies": "",
        "SnapshotOptions": {
            "AutomatedSnapshotStartHour": 0
        },
        "CognitoOptions": {
            "Enabled": false
        },
        "EncryptionAtRestOptions": {
            "Enabled": false
        },
        "NodeToNodeEncryptionOptions": {
            "Enabled": false
        },
        "AdvancedOptions": {
            "override_main_response_version": "false",
            "rest.action.multi.allow_explicit_index": "true"
        },
        "ServiceSoftwareOptions": {
            "CurrentVersion": "",
            "NewVersion": "",
            "UpdateAvailable": false,
            "Cancellable": false,
            "UpdateStatus": "COMPLETED",
            "Description": "There is no software update available for this domain.",
            "AutomatedUpdateDate": 0.0,
            "OptionalDeployment": true
        },
        "DomainEndpointOptions": {
            "EnforceHTTPS": false,
            "TLSSecurityPolicy": "Policy-Min-TLS-1-0-2019-07",
            "CustomEndpointEnabled": false
        },
        "AdvancedSecurityOptions": {
            "Enabled": false,
            "InternalUserDatabaseEnabled": false
        },
        "AutoTuneOptions": {
            "State": "ENABLE_IN_PROGRESS"
        }
    }
}

{{< / command >}}

In the LocalStack log you will see something like, where you can see the cluster starting up in the background.

```
2022-01-13T10:36:29.436:INFO:localstack.services.opensearch.cluster: starting opensearch: /tmp/localstack/var_libs/opensearch/1.1.0/bin/opensearch -E http.port=35403 -E http.publish_port=35403 -E transport.port=0 -E network.host=127.0.0.1 -E http.compression=false -E path.data="/tmp/localstack/opensearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/data" -E path.repo="/tmp/localstack/opensearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/backup" -E plugins.security.disabled=true with env {'OPENSEARCH_JAVA_OPTS': '-Xms200m -Xmx600m', 'OPENSEARCH_TMPDIR': '/tmp/localstack/opensearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/tmp'}
2022-01-13T10:36:29.437:INFO:localstack.services.opensearch.cluster: registering an endpoint proxy for http://my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566 => http://127.0.0.1:35403
2022-01-13T10:36:32.803:INFO:localstack.services.opensearch.cluster: [2022-01-13T10:36:32,800][INFO ][o.o.n.Node               ] [host-pc] version[1.1.0], pid[231895], build[tar/15e9f137622d878b79103df8f82d78d782b686a1/2021-10-04T21:29:03.079792Z], OS[Linux/5.11.0-46-generic/amd64], JVM[AdoptOpenJDK/OpenJDK 64-Bit Server VM/15.0.1/15.0.1+9]
2022-01-13T10:36:32.805:INFO:localstack.services.opensearch.cluster: [2022-01-13T10:36:32,805][INFO ][o.o.n.Node               ] [host-pc] JVM home [/tmp/localstack/var_libs/opensearch/1.1.0/jdk], using bundled JDK [true]
2022-01-13T10:36:32.806:INFO:localstack.services.opensearch.cluster: [2022-01-13T10:36:32,805][INFO ][o.o.n.Node               ] [host-pc] JVM arguments [-Xshare:auto, -Dopensearch.networkaddress.cache.ttl=60, -Dopensearch.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -XX:+ShowCodeDetailsInExceptionMessages, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dio.netty.allocator.numDirectArenas=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Djava.locale.providers=SPI,COMPAT, -XX:+UseG1GC, -XX:G1ReservePercent=25, -XX:InitiatingHeapOccupancyPercent=30, -Djava.io.tmpdir=/tmp/localstack/opensearch/arn:aws:es:us-east-1:000000000000:domain/my-domain/tmp, -XX:+HeapDumpOnOutOfMemoryError, -XX:HeapDumpPath=data, -XX:ErrorFile=logs/hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=logs/gc.log:utctime,pid,tags:filecount=32,filesize=64m, -Xms200m, -Xmx600m, -XX:MaxDirectMemorySize=314572800, -Dopensearch.path.home=/tmp/localstack/var_libs/opensearch/1.1.0, -Dopensearch.path.conf=/tmp/localstack/var_libs/opensearch/1.1.0/config, -Dopensearch.distribution.type=tar, -Dopensearch.bundled_jdk=true]
...
```

and after some time, you should see that the `Processing` state of the domain is set to `false`:

{{< command >}}
$ awslocal opensearch describe-domain --domain-name my-domain | jq ".DomainStatus.Processing"
false
{{< / command >}}

### Creating an Elasticsearch cluster

Like in AWS, the OpenSearch service can create Elasticsearch clusters and manage them.
To do so, you can use [awslocal]({{< ref "aws-cli.md#localstack-aws-cli-awslocal" >}}) and select an Elasticsearch version with the `--engine-version` parameter of the `awslocal opensearch create-domain` command.
For an overview of existing Elasticsearch versions you can use `awslocal opensearch list-versions`.

## Interact with the cluster

You can now interact with the cluster at the cluster API endpoint for the domain, in this case `http://my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566`.

For example:

{{< command >}}
$ curl http://my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566
{
  "name" : "host-pc",
  "cluster_name" : "opensearch",
  "cluster_uuid" : "DMN-2TlwRkuhMH4aRRqrkA",
  "version" : {
    "distribution" : "opensearch",
    "number" : "1.1.0",
    "build_type" : "tar",
    "build_hash" : "15e9f137622d878b79103df8f82d78d782b686a1",
    "build_date" : "2021-10-04T21:29:03.079792Z",
    "build_snapshot" : false,
    "lucene_version" : "8.9.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "The OpenSearch Project: https://opensearch.org/"
}
{{< / command >}}

Or the health endpoint:

{{< command >}}
$ curl -s http://my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566/_cluster/health | jq .
{
  "cluster_name": "opensearch",
  "status": "green",
  "timed_out": false,
  "number_of_nodes": 1,
  "number_of_data_nodes": 1,
  "discovered_master": true,
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

There are two configurable strategies that govern how domain endpoints are created. The strategy can be configured via the `OPENSEARCH_ENDPOINT_STRATEGY` environment variable.

| Value | Format | Description |
| - | - | - |
| `domain` | `<domain-name>.<region>.<engine-type>.localhost.localstack.cloud:4566` | This is the default strategy that uses the `localhost.localstack.cloud` domain to route to your localhost |
| `path` | `localhost:4566/<engine-type>/<region>/<domain-name>` | An alternative that can be useful if you cannot resolve LocalStack's localhost domain |
| `port` | `localhost:<port-from-range>` | Exposes the cluster(s) directly with ports from [the external service port range]({{< ref "external-ports" >}})|

Regardless of the service from which the clusters were created, the domain of the cluster always corresponds to the engine type (OpenSearch or Elasticsearch) of the cluster.
OpenSearch cluster therefore have `opensearch` in their domain (e.g. `my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566`) and Elasticsearch clusters have `es` in their domain (e.g. `my-domain.us-east-1.es.localhost.localstack.cloud:4566`)

#### Custom Endpoints

LocalStack allows you to set arbitrary custom endpoints for your clusters in the domain endpoint options.
This can be used to overwrite the behavior of the endpoint strategies described above.
You can also choose custom domains, however it is important to add the edge port (`80`/`443` or by default `4566`).

{{< command >}}
$ awslocal opensearch create-domain --domain-name my-domain \
      --domain-endpoint-options '{ "CustomEndpoint": "http://localhost:4566/my-custom-endpoint", "CustomEndpointEnabled": true }'
{{< / command >}}

Once the domain processing is complete, you can access the cluster:

{{< command >}}
$ curl http://localhost:4566/my-custom-endpoint/_cluster/health
{{< / command >}}


### Re-using a single cluster instance

In some cases, you may not want to create a new cluster instance for each domain,
for example when you are only interested in testing API interactions instead of actual OpenSearch functionality.
In this case, you can set `OPENSEARCH_MULTI_CLUSTER=0`, which will multiplex all domains to the same cluster.
This can however lead to unexpected behavior when persisting data into OpenSearch, or creating clusters with different versions, so we do not recommend it.


### Storage Layout

OpenSearch will be organized in your `DATA_DIR`, or the temporary directory (e.g., `/tmp/localstack/data`), as follows:

```
localstack@machine /tmp/localstack/data % tree -L 4
.
├── opensearch
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

## Custom OpenSearch backends

LocalStack downloads OpenSearch asynchronously the first time you run the `aws opensearch create-domain`, so you will get the response from LocalStack first and then (after download/install) you will have your OpenSearch cluster running locally.
You may not want this, and instead use your already running OpenSearch cluster.
This can also be useful when you want to run a cluster with a custom configuration that LocalStack does not support.

To customize the OpenSearch backend, you can start your own OpenSearch cluster locally and point LocalStack to it using the `OPENSEARCH_CUSTOM_BACKEND` environment variable.
Note that only a single backend can be configured, meaning that you will get a similar behavior as when you  [re-use a single cluster instance](#re-using-a-single-cluster-instance).

### Example

The following shows a sample `docker-compose.yaml` file that contains a single-node OpenSearch cluster and a basic LocalStack setup.

```yaml
version: "3.9"

services:
  opensearch:
    container_name: opensearch
    image: opensearchproject/opensearch:1.1.0
    network_mode: bridge
    environment:
      - node.name=opensearch
      - cluster.name=opensearch-docker-cluster
      - discovery.type=single-node
      - bootstrap.memory_lock=true
      - "OPENSEARCH_JAVA_OPTS=-Xms512m -Xmx512m"
      - "DISABLE_SECURITY_PLUGIN=true"
    ports:
      - "9200:9200"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/opensearch/data

  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME-localstack_main}"
    image: localstack/localstack
    network_mode: bridge
    ports:
      - "4566:4566"
    depends_on:
      - opensearch
    environment:
      - OPENSEARCH_CUSTOM_BACKEND=http://opensearch:9200
      - DEBUG=${DEBUG- }
      - DATA_DIR=${DATA_DIR- }
      - DOCKER_HOST=unix:///var/run/docker.sock
      - HOST_TMP_FOLDER=${TMPDIR}
    volumes:
      - "${TMPDIR:-/tmp/localstack}:/tmp/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
    links:
      - opensearch

volumes:
  data01:
    driver: local
```

1. Run docker compose:
{{< command >}}
$ docker-compose up -d
{{< /command >}}

2. Create the OpenSearch domain:
{{< command >}}
$ awslocal opensearch create-domain --domain-name my-cluster
{
    "DomainStatus": {
        "DomainId": "000000000000/my-domain",
        "DomainName": "my-domain",
        "ARN": "arn:aws:es:us-east-1:000000000000:domain/my-domain",
        "Created": true,
        "Deleted": false,
        "Endpoint": "my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566",
        "Processing": false,
        "UpgradeProcessing": false,
        "EngineVersion": "OpenSearch_1.1",
        "ClusterConfig": {
            "InstanceType": "m3.medium.search",
            "InstanceCount": 1,
            "DedicatedMasterEnabled": true,
            "ZoneAwarenessEnabled": false,
            "DedicatedMasterType": "m3.medium.search",
            "DedicatedMasterCount": 1,
            "WarmEnabled": false,
            "ColdStorageOptions": {
                "Enabled": false
            }
        },
        "EBSOptions": {
            "EBSEnabled": true,
            "VolumeType": "gp2",
            "VolumeSize": 10,
            "Iops": 0
        },
        "AccessPolicies": "",
        "SnapshotOptions": {
            "AutomatedSnapshotStartHour": 0
        },
        "CognitoOptions": {
            "Enabled": false
        },
        "EncryptionAtRestOptions": {
            "Enabled": false
        },
        "NodeToNodeEncryptionOptions": {
            "Enabled": false
        },
        "AdvancedOptions": {
            "override_main_response_version": "false",
            "rest.action.multi.allow_explicit_index": "true"
        },
        "ServiceSoftwareOptions": {
            "CurrentVersion": "",
            "NewVersion": "",
            "UpdateAvailable": false,
            "Cancellable": false,
            "UpdateStatus": "COMPLETED",
            "Description": "There is no software update available for this domain.",
            "AutomatedUpdateDate": 0.0,
            "OptionalDeployment": true
        },
        "DomainEndpointOptions": {
            "EnforceHTTPS": false,
            "TLSSecurityPolicy": "Policy-Min-TLS-1-0-2019-07",
            "CustomEndpointEnabled": false
        },
        "AdvancedSecurityOptions": {
            "Enabled": false,
            "InternalUserDatabaseEnabled": false
        },
        "AutoTuneOptions": {
            "State": "ENABLE_IN_PROGRESS"
        }
    }
}
{{< /command >}}

3. If the `Processing` status is `true`, it means that the cluster is not yet healthy. You can run `decribe-domain` to receive the status:
{{< command >}}
$ awslocal opensearch describe-domain --domain-name my-domain
{{< /command >}}

4. Check the cluster health endpoint and create indices:
{{< command >}}
$ curl my-domain.us-east-1.opensearch.localhost.localstack.cloud:4566/_cluster/health | jq
{
  "name": "host-pc",
  "cluster_name": "opensearch",
  "cluster_uuid": "DMN-2TlwRkuhMH4aRRqrkA",
  "version": {
    "distribution": "opensearch",
    "number": "1.1.0",
    "build_type": "tar",
    "build_hash": "15e9f137622d878b79103df8f82d78d782b686a1",
    "build_date": "2021-10-04T21:29:03.079792Z",
    "build_snapshot": false,
    "lucene_version": "8.9.0",
    "minimum_wire_compatibility_version": "6.8.0",
    "minimum_index_compatibility_version": "6.0.0-beta1"
  },
  "tagline": "The OpenSearch Project: https://opensearch.org/"
}
{{< /command >}}

5. Create an example index:
{{< command >}}
$ curl -X PUT my-domain.us-east-1.es.localhost.localstack.cloud:4566/my-index
{"acknowledged":true,"shards_acknowledged":true,"index":"my-index"}
{{< /command >}}


## Differences to AWS

* By default, AWS only sets the `Endpoint` attribute of the cluster status once the cluster is up.
  LocalStack will return the endpoint immediately, but keep `Processing = "true"` until the cluster has been started.
* The `CustomEndpointOptions` allows arbitrary endpoint URLs, which is not allowed in AWS.


## Troubleshooting

If you are using the `OPENSEARCH_ENDPOINT_STRATEGY=domain` (which is the default) and are having issues with resolving the subdomains, [please check if your DNS blocks rebind queries]({{< ref "limitations#dns-rebind-protection" >}}).