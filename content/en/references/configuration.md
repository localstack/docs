---
title: "Configuration"
weight: 10
description: >
  Overview of configuration options in LocalStack
aliases:
  - /localstack/configuration/
---

LocalStack exposes various configuration options to control its behaviour.

These options can be passed to LocalStack as environment variables like so:

{{< command >}}
$ DEBUG=1 localstack start
{{< / command >}}

To facilitate interoperability, configuration variables can be prefixed with `LOCALSTACK_` in docker.
For instance, setting `LOCALSTACK_PERSISTENCE=1` is equivalent to `PERSISTENCE=1`.

You can also use [Profiles](#profiles).

Configurations marked as **Deprecated** will be removed in the next major version. You can find previously removed configuration variables under [Legacy](#legacy).

## Core

Options that affect the core LocalStack system.

| Variable | Example Values | Description |
| - | - | - |
| `DEBUG` | `0` (default) \|`1`| Flag to increase log level and print more verbose logs (useful for troubleshooting issues)|
| `IMAGE_NAME`| `localstack/localstack` (default), `localstack/localstack:0.11.0` | Specific name and tag of LocalStack Docker image to use.|
| `GATEWAY_LISTEN`| `0.0.0.0:4566` (default in Docker mode) `127.0.0.1:4566` (default in host mode) | Configures the bind addresses of LocalStack. It has the form `<ip address>:<port>(,<ip address>:<port>)*`. LocalStack Pro adds port `443`. |
| `LOCALSTACK_HOST`| `localhost.localstack.cloud:4566` (default) | This is interpolated into URLs and addresses that are returned by LocalStack. It has the form `<hostname>:<port>`. |
| `USE_SSL` | `0` (default) | Whether to return URLs using HTTP (`0`) or HTTPS (`1`). Changed with 3.0.0. In earlier versions this was toggling SSL support on or off. |
| `PERSISTENCE` | `0` (default) | Enable persistence. See [Persistence Mechanism]({{< ref "user-guide/state-management/persistence" >}}) and [Filesystem Layout]({{< ref "filesystem" >}}). |
| `MAIN_CONTAINER_NAME` | `localstack-main` (default) | Specify the main docker container name |
| `LS_LOG` | `trace`, `trace-internal`, `debug`, `info`, `warn`, `error`, `warning`| Specify the log level. Currently overrides the `DEBUG` configuration. `trace` for detailed request/response, `trace-internal` for internal calls, too. |
| `EXTERNAL_SERVICE_PORTS_START` | `4510` (default) | Start of the [External Service Port Range]({{< ref "external-ports" >}}) (inclusive). |
| `EXTERNAL_SERVICE_PORTS_END` | `4560` (default) | End of the [External Service Port Range]({{< ref "external-ports" >}}) (exclusive). |
| `EAGER_SERVICE_LOADING` | `0` (default) \|`1` | Boolean that toggles lazy loading of services. If eager loading is enabled, services are started at LocalStack startup rather than their first use. Be aware that eager loading increases the LocalStack startup time. |
| `SERVICES`| `s3,sqs` | A comma-delimited string of services. Check the [internal health endpoint]({{< ref "internal-endpoints/#localstack-endpoints" >}}) `/_localstack/health` for valid service names. If `SERVICES` is set LocalStack will only load the listed services. All other services will be disabled and cannot be used. |
| `ALLOW_NONSTANDARD_REGIONS` | `0` (default) | Allows the use of non-standard AWS regions. By default, LocalStack only accepts [standard AWS regions](https://docs.aws.amazon.com/general/latest/gr/rande.html). |
| `PARITY_AWS_ACCESS_KEY_ID` | `0` (default) | Enables the use production-like access key IDs. By default, LocalStack issues keys with `LSIA...` and `LKIA...` prefix, and will reject keys that start with `ASIA...` or `AKIA...`. |

[1]: http://docs.aws.amazon.com/cli/latest/reference/#available-services

## CLI

These options are applicable when using the CLI to start LocalStack.

| Variable | Example Values | Description |
| - | - | - |
| `LOCALSTACK_VOLUME_DIR` | `~/.cache/localstack/volume` (on Linux) | The location on the host of the LocalStack volume directory mount. See [Filesystem Layout]({{< ref "filesystem#using-the-cli" >}}) |
| `CONFIG_PROFILE` | | The configuration profile to load. See [Profiles]({{< ref "#profiles" >}}) |
| `CONFIG_DIR` | `~/.localstack` | The path where LocalStack can find configuration profiles and other CLI-specific configuration |

## Docker

Options to configure how LocalStack interacts with Docker.

| Variable | Example Values | Description |
| - | - | - |
| `DOCKER_FLAGS` | | Allows to pass custom flags (e.g., volume mounts) to "docker run" when running LocalStack in Docker. |
| `DOCKER_SOCK` | `/var/run/docker.sock` | Path to local Docker UNIX domain socket |
| `DOCKER_BRIDGE_IP` | `172.17.0.1` | IP of the docker bridge used to enable access between containers |
| `LEGACY_DOCKER_CLIENT` | `0`\|`1` | Whether LocalStack should use the command-line Docker client and subprocess execution to run Docker commands, rather than the Docker SDK. |
| `DOCKER_CMD` | `docker` (default), `sudo docker`| Shell command used to run Docker containers (only used in combination with `LEGACY_DOCKER_CLIENT`) |
| `FORCE_NONINTERACTIVE` | | When running with Docker, disables the `--interactive` and `--tty` flags. Useful when running headless. |

## Local AWS Services

This section covers configuration options that are specific to certain AWS services.

### AppSync

| Variable | Example Values | Description |
| - | - | - |
| `GRAPHQL_ENDPOINT_STRATEGY` | `legacy`\|`domain`\|`path` |  Governs how AppSync endpoints are created to access a GraphQL API (see [AppSync Endpoints]({{< ref "/tags/appsync#endpoints" >}})) |

### Batch

| Variable | Example Values | Description |
| - | - | - |
| `BATCH_DOCKER_FLAGS` | `-e TEST_ENV=1337` | Additional flags provided to the batch container. Same restrictions as `LAMBDA_DOCKER_FLAGS`. |

### BigData (EMR, Athena, Glue)

| Variable | Example Values | Description |
| - | - | - |
| `BIGDATA_DOCKER_NETWORK` | | Network the bigdata should be connected to. The LocalStack container has to be connected to that network as well. Per default, the bigdata container will be connected to a network LocalStack is also connected to.
| `BIGDATA_DOCKER_FLAGS` | | Additional flags for the bigdata container. Same restrictions as `LAMBDA_DOCKER_FLAGS`.

### CloudFormation
| Variable | Example Values | Description |
| - | - | - |
| `CFN_PER_RESOURCE_TIMEOUT` | `300` (default) | Set the timeout to deploy each individual CloudFormation resource.
| `CFN_VERBOSE_ERRORS` | `0` (default) | Show exceptions for CloudFormation deploy errors.

### CloudWatch

| Variable | Example Values | Description |
| - | - | - |
| `PROVIDER_OVERRIDE_CLOUDWATCH` | `v2` | Use the new CloudWatch provider. |

### DocumentDB

| Variable | Example Values | Description |
| - | - | - |
| `DOCDB_PROXY_CONTAINER` | `0` (default) \|`1` | Whether the DocumentDB starts the MongoDB container proxied over LocalStack container. When enabled lambda functions can use the `Endpoint` configuration of the DocDB cluster or instance to connect to the DocumentDB. By default the container starts without proxy as standalone container. |

### DynamoDB

| Variable | Example Values | Description |
| - | - | - |
| `DYNAMODB_ERROR_PROBABILITY` | Decimal value between `0.0`(default) and `1.0` | Randomly inject `ProvisionedThroughputExceededException` errors into DynamoDB API responses. |
| `DYNAMODB_HEAP_SIZE` | `256m` (default), `1G` | Sets the JAVA EE maximum memory size for DynamoDB; full table scans require more memory |
| `DYNAMODB_SHARE_DB` | `0`\|`1` | When activated, DynamodDB will use a single database instead of separate databases for each credential and region. |
| `DYNAMODB_IN_MEMORY` | `0` (default) \|`1` | When activated, DynamodDB will start in in-memory mode, which can have a faster throughput. If you use this options, both persistence and cloud pods will not work for DynamoDB |
| `DYNAMODB_OPTIMIZE_DB_BEFORE_STARTUP` | `0`\|`1` | Optimize the database tables in the store before starting |
| `DYNAMODB_DELAY_TRANSIENT_STATUSES` | `0`\|`1` | When activated, DynamoDB will introduce artificial delays in resource creation to simulate the actual cloud service more closely. Currently works only for CREATING and DELETING online index statuses. |
| `DYNAMODB_CORS` | `*` | Enable CORS support for specific allow-list list the domains separated by `,` use `*` for public access (default is `*`) |
| `DYNAMODB_REMOVE_EXPIRED_ITEMS` | `0`\|`1` | Enables [Time to Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) feature |

### ECR 

| Variable | Example Values | Description |
| - | - | - |
| `ECR_ENDPOINT_STRATEGY` | `domain` (default)\|`off`\| | Governs how the default ECR endpoints are returned |

### ECS

| Variable | Example Values | Description |
| - | - | - |
| `ECS_REMOVE_CONTAINERS` | `0`\|`1` (default) | Remove Docker containers associated with ECS tasks after execution. Disabling this and dumping container logs might help with troubleshooting failing ECS tasks. |
| `ECS_DOCKER_FLAGS` | `--privileged`, `--dns 1.2.3.4` | Additional flags passed to Docker when creating ECS task containers. Same restrictions as `LAMBDA_DOCKER_FLAGS`. |
| `ECS_DISABLE_AWS_ENDPOINT_URL` | `0` (default) \| `1` | Whether to disable injecting the environment variable `AWS_ENDPOINT_URL`, which automatically configures [supported AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html). |
| `ECS_TASK_EXECUTOR` | `kubernetes` | Whether to run  ECS tasks when LocalStack is deployed on Kubernetes. Tasks are added to ELB load balancer target groups. |

### EC2

| Variable | Example Values | Description |
| - | - | - |
| `EC2_DOCKER_FLAGS` | `--privileged` | Additional flags passed to Docker when launching containerized instances. Same restrictions as `LAMBDA_DOCKER_FLAGS`. |
| `EC2_DOWNLOAD_DEFAULT_IMAGES` | `0`\|`1` (default) | At startup, LocalStack Pro downloads latest Ubuntu images from Docker Hub for use as AMIs. This can be disabled for security reasons. |
| `EC2_EBS_MAX_VOLUME_SIZE` | `1000` (default) | Maximum size (in MiBs) of user-specified EBS block devices mounted into EC2 container instances. |
| `EC2_MOUNT_BLOCK_DEVICES` | `1`\|`0` (default) | Whether to create and mount user-specified EBS block devices into EC2 container instances. |
| `EC2_REMOVE_CONTAINERS` | `0`\|`1` (default) | Controls whether created Docker containers are removed at instance termination or LocalStack shuts down. Disable this if there is a need to examine the container filesystem for debugging. |
| `EC2_VM_MANAGER` | `docker`(default)\|`libvirt`|`mock` | Emulation method to use in LocalStack Pro. This option is not available in LocalStack community. |

### EKS

| Variable | Example Values | Description |
| - | - | - |
| `EKS_LOADBALANCER_PORT` | `8081` (default) | Local port on which the Kubernetes load balancer is exposed on the host. |
| `EKS_K3S_IMAGE_TAG` | `v1.22.6-k3s1` (default) | Custom tag of the `k8s/rancher` image used to spin up Kubernetes clusters locally. |

### ElastiCache

| Variable | Example Values | Description |
| - | - | - |
| `PROVIDER_OVERRIDE_ELASTICACHE` | `legacy` | Use the legacy ElastiCache provider. |
| `REDIS_CONTAINER_MODE` | `1`\|`0` (default) | Start ElastiCache cache nodes in separate containers instead of in the LocalStack container |


### Elasticsearch

{{< callout >}}
The OpenSearch configuration variables are used to manage both OpenSearch and ElasticSearch clusters.
See [here](#opensearch).
{{< /callout >}}

### IAM
| Variable | Example Values | Description |
| - | - | - |
| `ENFORCE_IAM` | `0` (default)\|`1` | Enable IAM policy evaluation and enforcement. If this is disabled (the default), IAM policies will have no effect to your requests. |
| `IAM_SOFT_MODE` | `0` (default)\|`1` | Enable IAM soft mode. This leads to policy evaluation without actually denying access. Needs `ENFORCE_IAM` enabled as well. For more information, see [Identity and Access Management]({{< ref "user-guide/aws/iam" >}}).|

### Kinesis

| Variable | Example Values | Description |
| - | - | - |
| `KINESIS_ERROR_PROBABILITY` | Decimal value between `0.0`(default) and `1.0` | Randomly inject `ProvisionedThroughputExceededException` errors into Kinesis API responses. |
| `KINESIS_SHARD_LIMIT` | `100` (default), `Infinity` (to disable) | Integer value , causing the Kinesis API to start throwing exceptions to mimic the default shard limit. |
| `KINESIS_ON_DEMAND_STREAM_COUNT_LIMIT` | `10` (default), `Infinity` (to disable) | Integer value , causing the Kinesis API to start throwing exceptions to mimic the default on demand stream count limit. |
| `KINESIS_LATENCY` | `500` (default), `0` (to disable)| Integer value of milliseconds, causing the Kinesis API to delay returning a response in order to mimic latency from a live AWS call. |

### Lambda

{{< callout >}}
The legacy [Lambda]({{< ref "user-guide/aws/lambda" >}}) implementation has been removed since LocalStack&nbsp;3.0 (Docker `latest` since 2023-11-09).
Please consult the [migration guide]({{< ref "user-guide/aws/lambda#migrating-to-lambda-v2" >}}) for more information.
{{< /callout >}}

| Variable| Example Values | Description |
| - | - | - |
| `BUCKET_MARKER_LOCAL` | `hot-reload` (default) | Magic S3 bucket name for [Hot Reloading]({{< ref "user-guide/lambda-tools/hot-reloading" >}}). The S3Key points to the source code on the local file system. |
| `HOSTNAME_FROM_LAMBDA` | `localstack` | Endpoint host under which APIs are accessible from Lambda containers (optional). This can be useful in docker-compose stacks to use the local container hostname if neither IP address nor container name of the main container are available (e.g., in CI). Often used in combination with `LAMBDA_DOCKER_NETWORK`.|
| `LAMBDA_DISABLE_AWS_ENDPOINT_URL` | `0` (default) \| `1` | Whether to disable injecting the environment variable `AWS_ENDPOINT_URL`, which automatically configures [supported AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html). |
| `LAMBDA_DOCKER_DNS` | `""` (default) | Optional custom DNS server for the container running your Lambda function. Overwrites the default LocalStack [DNS Server]({{< ref "dns-server" >}}). Hence, resolving `localhost.localstack.cloud` requires additional configuration. |
| `LAMBDA_DOCKER_FLAGS` | `-e KEY=VALUE`, `-v host:container`, `-p host:container`, `--add-host domain:ip` | Additional flags passed to Docker `run`\|`create` commands. Supports environment variables (also with `--env-file`, but the file has to be mounted into the LocalStack container), ports, volume mounts, extra hosts, networks, DNS servers, labels, ulimits, user, platform, and privileged mode. |
| `LAMBDA_DOCKER_NETWORK` | `bridge` (Docker default) | [Docker network driver](https://docs.docker.com/network/) for the Lambda and ECS containers. Needs to be set to the network the LocalStack container is connected to. Limitation: `host` mode currently not supported. |
| `LAMBDA_DOWNLOAD_AWS_LAYERS` | `1` (default, pro) | Whether to download public Lambda layers from AWS through a LocalStack proxy when creating or updating functions. |
| `LAMBDA_IGNORE_ARCHITECTURE` | `0` (default) | Whether to ignore the AWS architectures (x86_64 or arm64) configured for the lambda function. Set to `1` to run cross-platform compatible lambda functions natively (i.e., Docker selects architecture). |
| `LAMBDA_K8S_IMAGE_PREFIX` | `amazon/aws-lambda-` (default, pro) | Prefix for images that will be used to execute Lambda functions in Kubernetes. |
| `LAMBDA_KEEPALIVE_MS` | `600000` (default 10min) | Time in milliseconds until lambda shuts down the execution environment after the last invocation has been processed. Set to `0` to immediately shut down the execution environment after an invocation. |
| `LAMBDA_LIMITS_CONCURRENT_EXECUTIONS` | `1000` (default) | The maximum number of events that functions can process simultaneously in the current Region. See [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html) |
| `LAMBDA_LIMITS_CODE_SIZE_ZIPPED` | `52428800` (default) | The maximum zip file size in bytes for the [CreateFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html) operation. Raising this limit enables the creation of larger Lambda functions without the need to upload the code to an S3 deployment bucket. |
| `LAMBDA_LIMITS_CREATE_FUNCTION_REQUEST_SIZE` | `70167211` (default) | The maximum HTTP request size in bytes for the [CreateFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html) operation. Raising this limit enables larger HTTP requests including zipped file size. |
| `LAMBDA_REMOVE_CONTAINERS` | `1` (default) | Whether to remove any Lambda Docker containers. |
| `LAMBDA_RUNTIME_ENVIRONMENT_TIMEOUT` | `20` (default) | How many seconds Lambda will wait for the runtime environment to start up. Increase this timeout if I/O is slow or your Lambda deployments are large or contain many files. |
| `LAMBDA_RUNTIME_EXECUTOR` | `docker` (default) | Where Lambdas will be executed. |
| | `kubernetes` (pro) | Execute lambdas in a Kubernetes cluster. |
| `LAMBDA_RUNTIME_IMAGE_MAPPING` | [base images for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html) (default) | Customize the Docker image of Lambda runtimes, either by:<br> a) pattern with `<runtime>` placeholder, e.g. `custom-repo/lambda-<runtime>:2022` <br> b) json dict mapping the `<runtime>` to an image, e.g. `{"python3.9": "custom-repo/lambda-py:thon3.9"}` |
| `LAMBDA_SYNCHRONOUS_CREATE` | `0` (default) | Set to `1` to create lambda functions synchronously (not recommended). |
| `LAMBDA_TRUNCATE_STDOUT` | `2000` (default) | Allows increasing the default char limit for truncation of lambda log lines when printed in the console. This does not affect the logs processing in CloudWatch. |
| `LAMBDA_LIMITS_MAX_FUNCTION_ENVVAR_SIZE_BYTES` | `4096` (default) | The maximum size of the environment variables that you can use to configure your function. |

### MemoryDB

| Variable | Example Values | Description |
| - | - | - |
| `REDIS_CONTAINER_MODE` | `1`\|`0` (default) | Start MemoryDB cluster nodes in separate containers instead of in the LocalStack container |

### MWAA

| Variable | Example Values | Description |
| - | - | - |
| `MWAA_PIP_TRUSTED_HOSTS` | `pypi.org,files.pythonhosted.org` | Comma-separated list of hosts for which SSL verification is not performed when installing Python dependencies for MWAA environment. |

### Neptune

| Variable | Example Values | Description |
| - | - | - |
| `NEPTUNE_DB_TYPE` | `neo4j`\|`tinkerpop` (default) | Starts Neptune DB as traditional netpune with Tinkerpop/Gremlin (default) or in Neo4J mode. |
| `NEPTUNE_ENABLE_TRANSACTION` | `1`\|`0` (default) | Enables Gremlin transaction. This is an experimental feature, [see notes]({{< ref "neptune#gremlin-transactions" >}}) |
| `NEPTUNE_GREMLIN_DEBUG` | `1`\|`0` (default) | Enable Gremlin logs  |
| `NEPTUNE_USE_SSL` | `1`\|`0` (default) | Whether to start the Neptune server with SSL configuration, which will enable wss protocol. This setting is only valid for Tinkerpop/Gremlin. By default SSL is not enabled. |

### OpenSearch

| Variable | Example Values | Description |
| - | - | - |
| `OPENSEARCH_CUSTOM_BACKEND` | `http://opensearch:9200` | URL to a custom OpenSearch backend cluster. If this is set to a valid URL, then LocalStack will not create OpenSearch cluster instances, but instead forward all domains to the given backend (see [Custom Opensearch Backends]({{< ref "opensearch#custom-opensearch-backends" >}})). |
| `OPENSEARCH_MULTI_CLUSTER` | `1`\| `0` | When activated, LocalStack will spawn one OpenSearch cluster per domain. Otherwise all domains will share a single cluster instance. This is ignored if `OPENSEARCH_CUSTOM_BACKEND` is set. |
| `OPENSEARCH_ENDPOINT_STRATEGY` | `path`\|`domain`\|`port` | Governs how domain endpoints are created to access a cluster (see [Opensearch Endpoints]({{< ref "opensearch#endpoints" >}})). |
| `SKIP_INFRA_DOWNLOADS` | `1` \| `0` (default) | **Deprecated since 1.3.0** Whether to skip downloading additional infrastructure components (e.g., specific Elasticsearch versions) |

### RDS

| Variable | Example Values | Description |
| - | - | - |
| `RDS_CLUSTER_ENDPOINT_HOST_ONLY` | `1` (default) \| `0` | Whether the cluster endpoint returns the host only (which is AWS parity). If set to `0` it will return `<host>:<port>`. |
| `RDS_PG_CUSTOM_VERSIONS`         | `0` \| `1` (default) | Whether to install and use custom Postgres versions for RDS (or alternatively, use default version 11). |
| `RDS_MYSQL_DOCKER`               | `1` (default) \| `0` | Whether to disable MySQL engines (and use MariaDB instead). MySQL engine for cluster/instances will start in a new docker container. If you have troubles running MySQL in docker, you can disable the feature. |
| `MYSQL_IMAGE`                    | `mysql:8.0`       | Defines a specific MySQL image that should be used when spinning up the MySQL engine. Only available if `RDS_MYSQL_DOCKER` is enabled. |
| `MSSQL_IMAGE`                    | `mcr.microsoft.com/mssql/server:2022-latest` | Defines a specific image that should be used when spinning up a SQL server engine. |

### S3

| Variable | Example Values | Description |
| - | - | - |
| `S3_DIR` || **Deprecated since 3.0.0** This is only supported for the `legacy_v2` provider. Configure a global parent directory that contains all buckets as sub-directories (`S3_DIR=/path/to/root`) or an individual directory that will get mounted as special bucket names (`S3_DIR=/path/to/root/bucket1:bucket1`). Only available for Localstack Pro.
| `S3_SKIP_SIGNATURE_VALIDATION`| `0` \| `1` (default) | Used to toggle validation of S3 pre-signed URL request signature. Set to `0` to validate. Note that validation can only pass if the `AWS_SECRET_ACCESS_KEY` is set to `test` or if using credentials returned from `STS.AssumeRole`  |
| `S3_SKIP_KMS_KEY_VALIDATION` | `0` \| `1` (default) | Used to toggle validation of provided KMS key in S3 operations. |
| `PROVIDER_OVERRIDE_S3` | `legacy_v2` \| `v3` (default) | The new LocalStack-native S3 provider (v3) is active by default since LocalStack 3.0. |

### StepFunctions

| Variable | Example Values | Description |
| - | - | - |
| `PROVIDER_OVERRIDE_STEPFUNCTIONS` | `legacy` \| `v2` (default) | The new LocalStack-native StepFunctions provider (v2) is active by default since LocalStack 3.0. |
| `STEPFUNCTIONS_LAMBDA_ENDPOINT` | `default` | **Deprecated since 3.0.0** This is only supported for the `legacy` provider. URL to use as the Lambda service endpoint in Step Functions. By default this is the LocalStack Lambda endpoint. Use default to select the original AWS Lambda endpoint. <br> **Removed in new provider.** |

### SQS

| Variable | Example Values | Description |
| - | - | - |
| `SQS_DELAY_PURGE_RETRY` | `0` (default) | Used to toggle PurgeQueueInProgress errors when making more than one PurgeQueue call within 60 seconds. |
| `SQS_DELAY_RECENTLY_DELETED` | `0` (default) | Used to toggle QueueDeletedRecently errors when re-creating a queue within 60 seconds of deleting it. |
| `SQS_ENABLE_MESSAGE_RETENTION_PERIOD`| `0` (default) \| `1` | Used to toggle the MessageRetentionPeriod feature (see [Enabling `MessageRetentionPeriod`](https://docs.localstack.cloud/user-guide/aws/sqs/#enabling-messageretentionperiod) |
| `SQS_ENDPOINT_STRATEGY`| `standard` (default) \| `domain` \| `path` \| `off` | Configures the format of Queue URLs (see [SQS Queue URLs](https://docs.localstack.cloud/user-guide/aws/sqs/#queue-urls) |
| `SQS_DISABLE_CLOUDWATCH_METRICS` | `0` (default) | Disables the CloudWatch Metrics for SQS when set to `1` |
| `SQS_CLOUDWATCH_METRICS_REPORT_INTERVAL` | `60` (default) | Configures the report interval (in seconds) for `Approximate*` metrics that are sent to CloudWatch periodically. Sending will be disabled if `SQS_DISABLE_CLOUDWATCH_METRICS=1` |

## Security

{{< callout "warning" >}}
Please be aware that the following options may have severe security implications.
{{< /callout >}}

| Variable| Example Values | Description |
| - | - | - |
| `DISABLE_CORS_HEADERS` | `0` (default) | Whether to disable the returning of default CORS headers in API responses (disables access from https://app.localstack.cloud). |
| `DISABLE_CORS_CHECKS` | `0` (default) | Whether to disable all CSRF (server-side) mitigations. |
| `DISABLE_CUSTOM_CORS_S3` | `0` (default) | Whether to disable CORS override by S3. |
| `DISABLE_CUSTOM_CORS_APIGATEWAY` | `0` (default)| Whether to disable CORS override by apigateway. |
| `EXTRA_CORS_ALLOWED_ORIGINS` | | Comma-separated list of origins that are allowed to communicate with localstack. |
| `EXTRA_CORS_ALLOWED_HEADERS` | | Comma-separated list of header names to be be added to Access-Control-Allow-Headers CORS header. |
| `EXTRA_CORS_EXPOSE_HEADERS` | | Comma-separated list of header names to be be added to Access-Control-Expose-Headers CORS header. |
| `ENABLE_CONFIG_UPDATES` | `0` (default) | Whether to enable dynamic configuration updates at runtime. |


## Emails

Please check with your SMTP email service provider for the following settings.

| Variable | Example Values | Description |
| - | - | - |
| `SMTP_HOST` | `localhost:1025` | Hostname (and optionally the port) of the SMTP server. The port defaults to 25. |
| `SMTP_USER` |  | Login username for the SMTP server if required. |
| `SMTP_PASS` |  | Login password for the SMTP server if required. |
| `SMTP_EMAIL` | `sender@example.com` | Origin email address. Required for Cognito only. |

## Persistence

To learn more about these configuration options, see [Persistence]({{< ref "user-guide/state-management/persistence" >}}).

| Variable | Valid options | Description |
| - | - | - |
| `SNAPSHOT_SAVE_STRATEGY` | `ON_SHUTDOWN`\|`ON_REQUEST`\|`SCHEDULED`\|`MANUAL` | Strategy that governs when LocalStack should make state snapshots |
| `SNAPSHOT_LOAD_STRATEGY` | `ON_STARTUP`\|`ON_REQUEST`\|`MANUAL` | Strategy that governs when LocalStack restores state snapshots |
| `SNAPSHOT_FLUSH_INTERVAL` | 15 (default) | The interval (in seconds) between persistence snapshots. It only applies to a `SCHEDULED` save strategy (see [Persistence Mechanism]({{< ref "user-guide/state-management/persistence" >}}))|
| `AUTO_LOAD_POD` |  | Comma-separated list of Cloud Pods to be automatically loaded at startup time. This feature is disabled when snapshot persistence is set via the `PERSISTENCE` variable. |
| `POD_LOAD_CLI_TIMEOUT` | 60 (default) | Timeout in seconds to wait before returning from load operations on the Cloud Pods CLI |

## Miscellaneous

| Variable | Example Values | Description |
| - | - | - |
| `EVENT_RULE_ENGINE` | `python` (default) \| `java` (preview) | Engine for [event pattern matching](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.html) used in EventBridge, EventBridge Pipes, and Lambda Event Source Mapping. Set it `java` to use the AWS [event-ruler](https://github.com/aws/event-ruler) offering better parity. |
| `SKIP_SSL_CERT_DOWNLOAD` | | Whether to skip downloading the SSL certificate for localhost.localstack.cloud |
| `CUSTOM_SSL_CERT_PATH` | `/var/lib/localstack/custom/server.test.pem` | Defines the absolute path to a custom SSL certificate for localhost.localstack.cloud |
| `IGNORE_ES_DOWNLOAD_ERRORS` | | Whether to ignore errors (e.g., network/SSL) when downloading Elasticsearch plugins |
| `OVERRIDE_IN_DOCKER` | | Overrides the check whether LocalStack is executed within a docker container. If set to `true`, LocalStack assumes it runs in a docker container. Should not be set unless necessary. |
| `DISABLE_EVENTS` | `1` | Whether to disable publishing LocalStack events |
| `OUTBOUND_HTTP_PROXY` | `http://10.10.1.3` | HTTP Proxy used for downloads of runtime dependencies and connections outside LocalStack itself |
| `OUTBOUND_HTTPS_PROXY` | `https://10.10.1.3` | HTTPS Proxy used for downloads of runtime dependencies and connections outside LocalStack itself |
| `REQUESTS_CA_BUNDLE` | `/var/lib/localstack/lib/ca_bundle.pem` | CA Bundle to be used to verify HTTPS requests made by LocalStack |
| `DOCKER_HOST` | `unix:///var/run/docker.sock` (default) | Daemon socket to connect Docker. Used by the LocalStack dependency [Docker](https://docs.docker.com/engine/reference/commandline/cli/#environment-variables). |


## Debugging

| Variable | Example Values | Description |
| - | - | - |
| `DEVELOP` | | Starts a debugpy server before starting LocalStack services
| `DEVELOP_PORT` | | Port number for debugpy server
| `WAIT_FOR_DEBUGGER` | | Forces LocalStack to wait for a debugger to start the services


## DNS

To learn more about these configuration options, see [DNS Server]({{< ref "dns-server" >}}).

| Variable | Example Values | Description |
| - | - | - |
| `DNS_ADDRESS` | `0.0.0.0` (default) | Address the LocalStack should bind the DNS server on (port 53 tcp/udp). Value `0` to disable.
| `DNS_SERVER` | Default upstream DNS or `8.8.8.8` (default) | Fallback DNS server for queries not handled by LocalStack.
| `DNS_RESOLVE_IP` | `127.0.0.1` (default) | IP address the DNS server should return as A record for queries handled by LocalStack. If customized, this value will be returned in preference to the DNS server response.
| `DNS_NAME_PATTERNS_TO_RESOLVE_UPSTREAM` | `([^.]+\.)*(ecr\|lambda)\.[^.]+\.amazonaws\.com` (example) | List of domain names that should *NOT* be redirected by the LocalStack DNS to the LocalStack container, but instead always forwarded to the upstream resolver. This will *NOT* redirect requests made to LocalStack due to manual endpoint configuration. Comma-separated list of Python-flavored regex patterns. See [the DNS server documentation]({{< ref "user-guide/tools/dns-server#skip-localstack-dns-resolution" >}}) for more details.
| `DNS_LOCAL_NAME_PATTERNS` | `([^.]+\.)*(ecr\|lambda)\.[^.]+\.amazonaws\.com` (example) | **Deprecated since 3.0.2** List of domain names that should *NOT* be redirected by the LocalStack DNS to the LocalStack container, but instead always forwarded to the upstream resolver. This will *NOT* redirect requests made to LocalStack due to manual endpoint configuration. Comma-separated list of Python-flavored regex patterns. **Renamed to `DNS_NAME_PATTERNS_TO_RESOLVE_UPSTREAM`**

## Transparent Endpoint Injection

| Variable | Example Values | Description |
| - | - | - |
| `DISABLE_TRANSPARENT_ENDPOINT_INJECTION` | `0` (default in Pro) \| `1` | Whether to disable DNS resolution of AWS hostnames to the LocalStack container. Pro feature. (see [Transparent Endpoint Injection]({{< ref "user-guide/tools/transparent-endpoint-injection" >}}))

## LocalStack Pro

| Variable             | Example Values | Description |
|----------------------|----------------|-------------|
| `ACTIVATE_PRO`       | `0` \| `1`&nbsp;(default)    | Whether Pro should be activated or not. This is set to true by default if using the `localstack/localstack-pro` container image. If set to `1`, LocalStack will fail to start if the license key activation did not work. If set to `0`, an attempt is made to start LocalStack without Pro features. |
| `LOCALSTACK_AUTH_TOKEN` |             | [Auth token]({{< ref "auth-token" >}}) to activate LocalStack Pro. |
| `LOCALSTACK_API_KEY` |                | **Deprecated since 3.0.0** [API key]({{< ref "api-key" >}}) to activate LocalStack Pro.<br/> **Use the `LOCALSTACK_AUTH_TOKEN` instead (except for [CI environments]({{< ref "user-guide/ci/" >}})).** |
| `LOG_LICENSE_ISSUES` | `0` \| `1`&nbsp;(default)    | Whether to log issues with the license activation to the console. |


## Legacy

These configurations have already been removed and **won't have any effect** on newer versions of LocalStack.
**Please remove them from your configuration.**

<!-- Note on ordering: The list is ordered first by version (descending) and then by Variable name (ascending). -->

| Variable | Removed in | Example Values | Description |
| - | - | - | - |
| `<SERVICE>_BACKEND` | 3.0.0 | `http://localhost:7577` |  Custom endpoint URL to use for a specific service, where `<SERVICE>` is the uppercase service name. |
| `<SERVICE>_PORT_EXTERNAL` | 3.0.0 | `4567` | Port number to expose a specific service externally . `SQS_PORT_EXTERNAL`, e.g. , is used when returning queue URLs from the SQS service to the client. |
| `ACTIVATE_NEW_POD_CLIENT` | 3.0.0 | `0`\|`1` (default) |  Whether to use the new Cloud Pods client leveraging LocalStack container's APIs. |
| `BIGDATA_MONO_CONTAINER` | 3.0.0 |`0`\|`1` (default) | Whether to spin Big Data services inside the LocalStack main container. Glue jobs breaks when using `BIGDATA_MONO_CONTAINER=0`. | 
| `DEFAULT_REGION` | 3.0.0 | `us-east-1` (default) | AWS region to use when talking to the API (needs to be activated via `USE_SINGLE_REGION=1`). LocalStack now has full multi-region support. |
| `EDGE_BIND_HOST` | 3.0.0 | `127.0.0.1` (default), `0.0.0.0` (docker)| Address the edge service binds to. Use `GATEWAY_LISTEN` instead. |
| `EDGE_FORWARD_URL` | 3.0.0 | `http://10.0.10.5678` | Optional target URL to forward all edge requests to (e.g., for distributed deployments) |
| `EDGE_PORT` | 3.0.0 | `4566` (default)| Port number for the edge service, the main entry point for all API invocations. |
| `EDGE_PORT_HTTP` | 3.0.0 | `4566` (default)| Port number for the edge service, the main entry point for all API invocations. |
| `ES_CUSTOM_BACKEND` | 3.0.0 | `http://elasticsearch:9200` |  Use [`OPENSEARCH_CUSTOM_BACKEND`](#opensearch) instead. URL to a custom elasticsearch backend cluster. If this is set to a valid URL, then localstack will not create elasticsearch cluster instances, but instead forward all domains to the given backend (see [Custom Elasticsearch Backends]({{< ref "es#custom-elasticsearch-backends" >}})). |
| `ES_ENDPOINT_STRATEGY` | 3.0.0 | `path`\|`domain`\|`port` (formerly `off`) |  Use [`OPENSEARCH_ENDPOINT_STRATEGY`](#opensearch) instead. Governs how domain endpoints are created to access a cluster (see [Elasticsearch Endpoints]({{< ref "es#endpoints" >}})) |
| `ES_MULTI_CLUSTER` | 3.0.0 | `0`\|`1` |  Use [`OPENSEARCH_MULTI_CLUSTER`](#opensearch) instead. When activated, LocalStack will spawn one Elasticsearch cluster per domain. Otherwise all domains will share a single cluster instance. This is ignored if `ES_CUSTOM_BACKEND` is set. |
| `HOSTNAME_EXTERNAL` | 3.0.0 | `localhost` (default) |  Name of the host to expose the services externally. This host is used, e.g., when returning queue URLs from the SQS service to the client. Use `LOCALSTACK_HOST` instead.  |
| `KINESIS_INITIALIZE_STREAMS` | 3.0.0 | `"my-first-stream:1,my-other-stream:2:us-west-2,my-last-stream:1"` | A comma-delimited string of stream names, its corresponding shard count and an optional region to initialize during startup. If the region is not provided, the default region is used. Only works with the `kinesis-mock` `KINESIS_PROVIDER`. |
| `KINESIS_PROVIDER` | 3.0.0 | `kinesis-mock` (default) and `kinesalite` | |
| `KMS_PROVIDER` | 3.0.0 | `moto` (default), `local-kms` | `local-kms` has been removed. |
| `LAMBDA_CODE_EXTRACT_TIME` | 3.0.0 | `25` (default) | Time in seconds to wait at max while extracting Lambda code. By default, it is 25 seconds for limiting the execution time to avoid client/network timeout issues. <br> **Removed in new provider because function creation happens asynchronously.**|
| `LAMBDA_CONTAINER_REGISTRY` | 3.0.0 | `lambci/lambda` (default) | An alternative docker registry from where to pull lambda execution containers.<br> **Replaced by `LAMBDA_RUNTIME_IMAGE_MAPPING` in new provider.** |
| `LAMBDA_EXECUTOR` | 3.0.0 |  | Method to use for executing Lambda functions. For `docker` and `docker-reuse`, if LocalStack itself is started inside Docker, then the `docker` command needs to be available inside the container (usually requires to run the container in privileged mode). More information in Lambda Executor Modes.<br> **Removed in new provider. Mount the Docker socket or see [migration guide]({{< ref "user-guide/aws/lambda" >}}).** |
| | | `docker` (default) | Run each function invocation in a separate Docker container. |
| | | `local` (fallback) | Run Lambda functions in a temporary directory on the local machine. |
| | | `docker-reuse` | Create one Docker container per function and reuse it across invocations. |
| `LAMBDA_FALLBACK_URL` | 3.0.0 | | Fallback URL to use when a non-existing Lambda is invoked. Either records invocations in DynamoDB (value `dynamodb://<table_name>`) or forwards invocations as a POST request (value `http(s)://...`).<br> **Removed in new provider.** |
| `LAMBDA_FORWARD_URL` | 3.0.0 | | URL used to forward all Lambda invocations (useful to run Lambdas via an external service). <br> **Removed in new provider.** |
| `LAMBDA_JAVA_OPTS` | 3.0.0 | `-Xmx512M` | Allow passing custom JVM options to Java Lambdas executed in Docker. Use `_debug_port_` placeholder to configure the debug port, e.g., `-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=_debug_port_`.<br> **Currently not supported in new provider but possible via custom entrypoint.** |
| `LAMBDA_REMOTE_DOCKER` | 3.0.0 | | determines whether Lambda code is copied or mounted into containers.<br> **Removed in new provider because zip file copying is used by default and hot reloading automatically configures mounting.** |
| | | `true` (default) | your Lambda function definitions will be passed to the container by copying the zip file (potentially slower). It allows for remote execution, where the host and the client are not on the same machine.|
| | | `false` | your Lambda function definitions will be passed to the container by mounting a volume (potentially faster). This requires to have the Docker client and the Docker host on the same machine. |
| `LAMBDA_STAY_OPEN_MODE` | 3.0.0 | `1` (default) | Usage of the stay-open mode of Lambda containers. Only applicable if `LAMBDA_EXECUTOR=docker-reuse`. Set to `0` if you want to use [Hot Reloading]({{< ref "hot-reloading" >}}).<br> **Removed in new provider because stay-open mode is the default behavior. `LAMBDA_KEEPALIVE_MS` can be used to configure how long containers should be kept running in-between invocations.** |
| `LAMBDA_XRAY_INIT` | 3.0.0 | `1` \| `0` (default) | Whether to fully initialize XRay daemon for Lambda containers (may increase Lambda startup times).<br> **the X-Ray daemon is now always initialized.** |
| `LEGACY_EDGE_PROXY` | 3.0.0 | `1` \| `0` (default) | Whether to use the legacy edge proxy or the newer Gateway/HandlerChain framework.  |
| `LOCALSTACK_HOSTNAME` | 3.0.0 | `http://${LOCALSTACK_HOSTNAME}:4566` | Name of the host where LocalStack services are available. Use this hostname as endpoint in order to access the services from within your Lambda functions (e.g., to store an item to DynamoDB or S3 from a Lambda). This option is read-only. Use `LOCALSTACK_HOST` instead. |
| `MOCK_UNIMPLEMENTED` | 3.0.0 | `1` \| `0` (default)  |  Whether to return mocked success responses (instead of 501 errors) for currently unimplemented API methods |
| `PERSIST_ALL` | 3.0.0 | `true` (default) | Whether to persist all resources (including user code like Lambda functions), or only "light-weight" resources (e.g., SQS queues, or Cognito users). Can be set to `false` to reduce storage size of `DATA_DIR` folders or Cloud Pods. |
| `SYNCHRONOUS_KINESIS_EVENTS` | 3.0.0 | `1` (default) \| `0` | Whether or not to handle Kinesis Lambda event sources as synchronous invocations. |
| `USE_SINGLE_REGION` | 3.0.0 | `1` \| `0` (default) |  Whether to use the legacy single-region mode, defined via `DEFAULT_REGION`. |
| `DATA_DIR`| 2.0.0 | blank (disabled/default), `/tmp/localstack/data` |  Local directory for saving persistent data. Use `PERSISTENCE` instead. |
| `DISABLE_TERM_HANDLER` | 2.0.0 | `""` (default) \| `1` | Whether to disable signal passing to LocalStack when running in docker. Enabling this will prevent an orderly shutdown when running inside LS in docker. Setting this to anything else than an empty string will disable it.
| `HOST_TMP_FOLDER` | 2.0.0 | `/some/path` |  Temporary folder on the host that gets mounted as `$TMPDIR/localstack` into the LocalStack container. Required only for Lambda volume mounts when using `LAMBDA_REMOTE_DOCKER=false.` |
| `INIT_SCRIPTS_PATH` | 2.0.0 | `/some/path` | Before 1.0, this was used to configure the path to the initializing files with extensions `.sh` that were found in `/docker-entrypoint-initaws.d`. This has been replaced by the [init-hook system](https://docs.localstack.cloud/references/init-hooks/). |
| `LEGACY_DIRECTORIES` | 2.0.0 | `0` (default) | Use legacy method of managing internal filesystem layout. See [Filesystem Layout]({{< ref "filesystem" >}}). |
| `LEGACY_INIT_DIR` | 2.0.0 | `1` \| `0`(default) | Used with `INIT_SCRIPTS_PATH`. This has been replaced by the [init-hook system](https://docs.localstack.cloud/references/init-hooks/). |
| `MULTI_ACCOUNTS` | 2.0.0 | `0` (default) | Enable multi-accounts (preview) |
| `SQS_PROVIDER` | 2.0.0 |  `moto` (default) and `elasticmq` | |
| `SYNCHRONOUS_API_GATEWAY_EVENTS` | 2.0.0 | `1` (default) \| `0` | Whether or not to handle API Gateway Lambda event sources as synchronous invocations. |
| `SYNCHRONOUS_DYNAMODB_EVENTS` | 2.0.0 | `1` (default) \| `0` | Whether or not to handle DynamoDB Lambda event sources as synchronous invocations. |
| `SYNCHRONOUS_SQS_EVENTS` | 2.0.0 | `1`  \| `0` (default) | Whether or not to handle SQS Lambda event sources as synchronous invocations. |
| `SYNCHRONOUS_SNS_EVENTS` | 2.0.0 | `1`  \| `0` (default) | Whether or not to handle SNS Lambda event sources as synchronous invocations. |
| `TMPDIR`| 2.0.0 | `/tmp` (default) |  Temporary folder on the host running the CLI and inside the LocalStack container .|
| `USE_LIGHT_IMAGE` | 2.0.0 | `1` (default) | Whether to use the light-weight Docker image. Overwritten by `IMAGE_NAME`.|
| `LEGACY_PERSISTENCE` | 1.0.0 | `true` (default) | Whether to enable legacy persistence mechanism based on API calls record & replay. Only relevant for Community image, not relevant for advanced persistence mechanism in Pro. |
| `PERSISTENCE_SINGLE_FILE` | 1.0.0 | `true` (default)| Specify if persistence files should be combined (only relevant for legacy persistence in Community image, not relevant for advanced persistence in Pro version). |
| `PORT_WEB_UI` | 0.12.8 | `8080` (default) | Port for the legacy Web UI. Replaced by our [Web Application](https://app.localstack.cloud) |

## Profiles

LocalStack supports configuration profiles which are stored in the `~/.localstack` config directory.
A configuration profile is a set of environment variables stored in an `.env` file in the LocalStack config directory.

Here is an example of what configuration profiles might look like:

{{< command >}}
$ tree ~/.localstack
/home/username/.localstack
├── default.env
├── dev.env
└── pro.env
{{< / command >}}

Here is an example of what a specific environment profile looks like

{{< command >}}
$ cat ~/.localstack/pro-debug.env
LOCALSTACK_AUTH_TOKEN=XXXXX
DEBUG=1
DEVELOP=1
{{< / command >}}

You can load a profile by either setting the `env` variable `CONFIG_PROFILE=<profile>` or the `--profile=<profile>` CLI flag when using the CLI.
Let's take an example to load the `dev.env` profile file if it exists:

{{< command >}}
$ python -m localstack.cli.main --profile=dev start
{{< / command >}}

If no profile is specified, the `default.env` profile will be loaded.
While explicitly specified, the environment variables will always overwrite the profile.

To display the config environment variables, you can use the following command:

{{< command >}}
$ python -m localstack.cli.main --profile=dev config show
{{< / command >}}

{{< callout >}}
The `CONFIG_PROFILE` is a CLI feature and cannot be used with a Docker/Docker Compose setup.
You can look at [alternative means of setting environment variables](https://docs.docker.com/compose/environment-variables/set-environment-variables/) for your Docker Compose setups.
For Docker setups, we recommend passing the environment variables directly to the `docker run` command.
{{< /callout >}}
