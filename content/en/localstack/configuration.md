---
title: "Configuration"
weight: 5
description: >
  Environment variables which affect LocalStack.
---

LocalStack allows for many different configuration options.
You can pass these via environment variables, e.g., like the following:

{{< command >}}
$ SERVICES=kinesis,lambda,sqs,dynamodb DEBUG=1 localstack start
{{< / command >}}

## Core

| Variable | Example Values | Description |
| - | - | - |
| `SERVICES` | `kinesis,lambda,sqs`,`serverless`| Comma-separated list of [AWS CLI service names][1] or shorthands to start up. |
| `EDGE_BIND_HOST` | `127.0.0.1` (default), `0.0.0.0` (docker)| Address the edge service binds to.|
| `EDGE_PORT` | `4566` (default)| Port number for the edge service, the main entry point for all API invocations. |
| `HOSTNAME`| `localhost` (default) | Name of the host to expose the services internally. For framework-internal communication, e.g., services are started in different containers using docker-compose.|
| `HOSTNAME_EXTERNAL` | `localhost` (default) | Name of the host to expose the services externally. This host is used, e.g., when returning queue URLs from the SQS service to the client.|
| `DEBUG` | `0`\|`1`| Flag to increase log level and print more verbose logs (useful for troubleshooting issues)|
| `<SERVICE>_PORT_EXTERNAL` | `4567` | Port number to expose a specific service externally . `SQS_PORT_EXTERNAL`, e.g. , is used when returning queue URLs from the SQS service to the client. |
| `IMAGE_NAME`| `localstack/localstack` (default), `localstack/localstack:0.11.0` | Specific name and tag of LocalStack Docker image to use.|
| `USE_LIGHT_IMAGE` | `1` (default) | Whether to use the light-weight Docker image. Overwritten by `IMAGE_NAME`.|
| `TMPDIR`| `/tmp` (default)| Temporary folder on the host running the CLI and inside the LocalStack container .|
| `HOST_TMP_FOLDER` | `/some/path` | Temporary folder on the host that gets mounted as `$TMPDIR/localstack` into the LocalStack container. Required only for Lambda volume mounts when using `LAMBDA_REMOTE_DOCKER=false.` |
| `DATA_DIR`| blank (disabled/default), `/tmp/localstack/data` | Local directory for saving persistent data (see: TODO)|
| `PERSISTENCE_SINGLE_FILE` | `true` (default)| Specify if persistence files should be combined (deprecated - only relevant for legacy persistence in Community version, not relevant for advanced persistence in Pro version). |
| `PERSIST_ALL` | `true` (default) | Whether to persist all resources (including user code like Lambda functions), or only "light-weight" resources (e.g., SQS queues, Cognito users, etc). Can be set to `false` to reduce storage size of `DATA_DIR` folders or Cloud Pods. |
| `LEGACY_PERSISTENCE` | `true` (default) | Whether to enable legacy persistence mechanism based on API calls record&replay (deprecated). Only relevant for Community version, not relevant for advanced persistence mechanism in Pro. |
| `<SERVICE>_BACKEND` | | Custom endpoint URL to use for a specific service, where <SERVICE> is the uppercase service name. See (TODO) for supported services and (TODO) for examples for third-party integration |
| `MAIN_CONTAINER_NAME` | `localstack_main` (default) | Specify the main docker container name |
| `INIT_SCRIPTS_PATH` | `/some/path` | Specify the path to the initializing files with extensions `.sh` that are found default in `/docker-entrypoint-initaws.d`. |
| `LS_LOG` | `trace`, `trace-internal`, `debug`, `info`, `warn`, `error`, `warning`| Specify the log level. Currently overrides the `DEBUG` configuration. `trace` for detailed request/response, `trace-internal` for internal calls, too. |
| `EXTERNAL_SERVICE_PORTS_START` | `4510` (default) | Start of [the external service port range]({{< ref "external-ports" >}}) (included). |
| `EXTERNAL_SERVICE_PORTS_END` | `4560` (default) | End of [the external service port range]({{< ref "external-ports" >}}) (excluded). |
| `EAGER_SERVICE_LOADING` | | Boolean that toggles lazy loading of services. If eager loading is enabled, services are started at LocalStack startup rather than their first use. Eager loading significantly increases LocalStack startup time. |

[1]: http://docs.aws.amazon.com/cli/latest/reference/#available-services


### Docker

Docker is used extensively by LocalStack, and there are several configuration parameters for how LocalStack interacts with Docker.

| Variable | Example Values | Description |
| - | - | - |
| `DOCKER_FLAGS` | | Allows to pass custom flags (e.g., volume mounts) to "docker run" when running LocalStack in Docker. |
| `DOCKER_SOCK` | `/var/run/docker.sock` | Path to local Docker UNIX domain socket |
| `DOCKER_BRIDGE_IP` | `172.17.0.1` | IP of the docker bridge used to enable access between containers |
| `LEGACY_DOCKER_CLIENT` | `0`\|`1` | Whether LocalStack should use the command-line Docker client and subprocess execution to run Docker commands, rather than the Docker SDK. |
| `DOCKER_CMD` | `docker` (default), `sudo docker`| Shell command used to run Docker containers (only used in combination with `LEGACY_DOCKER_CLIENT`) |
| `FORCE_NONINTERACTIVE` | | When running with Docker, disables the `--interactive` and `--tty` flags. Useful when running headless. |

## Local AWS Services

This section covers configuration values that are specific to certain AWS services.

* [Batch]({{< ref "#batch" >}})
* [DynamoDB]({{< ref "#dynamodb" >}})
* [Elastic Kubernetes Service (EKS)]({{< ref "#eks" >}})
* [Elasticsearch]({{< ref "#elasticsearch" >}})
* [Kinesis]({{< ref "#kinesis" >}})
* [Lambda]({{< ref "#lambda" >}})
* [Stepfunctions]({{< ref "#stepfunctions" >}})

### Batch

| Variable | Example Values | Description |
| - | - | - |
| `BATCH_DOCKER_FLAGS` | `-e TEST_ENV=1337` | Additional flags provided to the batch container. Only flags for volumes, ports, environment variables and add-hosts are allowed. |

### DynamoDB

| Variable | Example Values | Description |
| - | - | - |
| `DYNAMODB_ERROR_PROBABILITY` | Decimal value between `0.0`(default) and `1.0` | Randomly inject `ProvisionedThroughputExceededException` errors into DynamoDB API responses. |
| `DYNAMODB_HEAP_SIZE` | `256m` (default), `1G` | Sets the JAVA EE maximum memory size for DynamoDB; full table scans require more memory |
| `DYNAMODB_SHARE_DB` | `0`\|`1` | When activated, DynamodDB will use a single database instead of separate databases for each credential and region. |
| `DYNAMODB_OPTIMIZE_DB_BEFORE_STARTUP` | `0`\|`1` | Optimize the database tables in the store before starting |
| `DYNAMODB_DELAY_TRANSIENT_STATUSES` | `0`\|`1` | When activated, DynamoDB will introduce artificial delays in resource creation to simulate the actual cloud service more closely. Currently works only for CREATING and DELETING online index statuses. |
| `DYNAMODB_CORS` | `*` | Enable CORS support for specific allow-list list the domains separated by `,` use `*` for public access (default is `*`) |

### EKS

| Variable | Example Values | Description |
| - | - | - |
| `EKS_LOADBALANCER_PORT` | `8081` (default) | Local port on which the Kubernetes load balancer is exposed on the host. |

### Elasticsearch

{{% alert title="Deprecated" color="warning" %}}
While the ElasticSearch API is actively maintained, the configuration variables for ElasticSearch have been deprecated. Please use the [OpenSearch configuration variables](#opensearch) instead. The OpenSearch configuration variables are used to manage both, OpenSearch and ElasticSearch clusters.
{{% /alert %}}

| Variable | Example Values | Description |
| - | - | - |
| `ES_CUSTOM_BACKEND` | `http://elasticsearch:9200` | *Deprecated*. Use [`OPENSEARCH_CUSTOM_BACKEND`](#opensearch) instead. URL to a custom elasticsearch backend cluster. If this is set to a valid URL, then localstack will not create elasticsearch cluster instances, but instead forward all domains to the given backend (see [Elasticsearch#custom-elasticsearch-backends]({{< ref "elasticsearch#custom-elasticsearch-backends" >}})). |
| `ES_MULTI_CLUSTER` | `0`\|`1` | *Deprecated*. Use [`OPENSEARCH_MULTI_CLUSTER`](#opensearch) instead. When activated, LocalStack will spawn one Elasticsearch cluster per domain. Otherwise all domains will share a single cluster instance. This is ignored if `ES_CUSTOM_BACKEND` is set. |
| `ES_ENDPOINT_STRATEGY` | `path`\|`domain`\|`port` (formerly `off`) | *Deprecated*. Use [`OPENSEARCH_ENDPOINT_STRATEGY`](#opensearch) instead. Governs how domain endpoints are created to access a cluster (see [Elasticsearch#endpoints]({{< ref "elasticsearch#endpoints" >}})) |

### Kinesis

| Variable | Example Values | Description |
| - | - | - |
| `KINESIS_ERROR_PROBABILITY` | Decimal value between `0.0`(default) and `1.0` | Randomly inject `ProvisionedThroughputExceededException` errors into Kinesis API responses. |
| `KINESIS_SHARD_LIMIT` | `100` (default), `Infinity` (to disable) | Integer value , causing the Kinesis API to start throwing exceptions to mimick the default shard limit. |
| `KINESIS_LATENCY` | `500` (default), `0` (to disable)| Integer value of milliseconds, causing the Kinesis API to delay returning a response in order to mimick latency from a live AWS call. |
| `KINESIS_INITIALIZE_STREAMS` | `"my-first-stream:1,my-other-stream:2:us-west-2,my-last-stream:1"` | A comma-delimited string of stream names, its corresponding shard count and an optional region to initialize during startup. If the region is not provided, the default region is used. Only works with the `kinesis-mock` `KINESIS_PROVIDER`. |

### Lambda

| Variable| Example Values | Description |
| - | - | - |
| `LAMBDA_EXECUTOR` |  | Method to use for executing Lambda functions. For `docker` and `docker-reuse`, if LocalStack itself is started inside Docker, then the `docker` command needs to be available inside the container (usually requires to run the container in privileged mode). More information in [Lambda Executor Modes]({{< ref "lambda-executors" >}}). |
| | `docker` (default) | Run each function invocation in a separate Docker container. |
| | `local` (fallback) | Run Lambda functions in a temporary directory on the local machine. |
| | `docker-reuse` | Create one Docker container per function and reuse it across invocations. |
| `LAMBDA_STAY_OPEN_MODE` | `1` (default) | Usage of the [stay-open mode]({{< ref "lambda-executors#stay-open-mode" >}}) of Lambda containers. Only applicable if `LAMBDA_EXECUTOR=docker-reuse`. Set to `0` if you want to use [Hot Swapping]({{< ref "hot-swapping" >}}).|
| `LAMBDA_REMOTE_DOCKER` | | determines whether Lambda code is copied or mounted into containers |
| | `true` (default) | your Lambda function definitions will be passed to the container by copying the zip file (potentially slower). It allows for remote execution, where the host and the client are not on the same machine.|
| | `false` | your Lambda function definitions will be passed to the container by mounting a volume (potentially faster). This requires to have the Docker client and the Docker host on the same machine. Also, `HOST_TMP_FOLDER` must be set properly, and a volume mount like `${HOST_TMP_FOLDER}:/tmp/localstack` needs to be configured if you're using docker-compose. |
| `LAMBDA_TRUNCATE_STDOUT` | `2000` | Allows increasing the default char value for truncation of lambda logs.|
| `BUCKET_MARKER_LOCAL` | | Optional bucket name for running lambdas locally.|
| `LAMBDA_CODE_EXTRACT_TIME` | `25` | Time in seconds to wait at max while extracting Lambda code. By default it is 25 seconds for limiting the execution time to avoid client/network timeout issues.| 
| `LAMBDA_DOCKER_NETWORK` | | Optional Docker network for the container running your lambda function. This configuration value also applies to ECS containers. Needs to be set to the network the LocalStack container is connected to if not default bridge network. |
| `LAMBDA_DOCKER_DNS` | | Optional DNS server for the container running your lambda function. |
| `LAMBDA_DOCKER_FLAGS` | `-e KEY=VALUE`, `-v host:container`, `-p host:container`, `--add-host domain:ip` | Additional flags passed to Lambda Docker `run`\|`create` commands (e.g., useful for specifying custom volume mounts). Does only support environment, volume, port and add-host flags |
| `LAMBDA_CONTAINER_REGISTRY` | `lambci/lambda` (default) | An alternative docker registry from where to pull lambda execution containers.|
| `LAMBDA_REMOVE_CONTAINERS` | `1` (default) | Whether to remove containers after Lambdas finished executing.|
| `LAMBDA_FALLBACK_URL` | | Fallback URL to use when a non-existing Lambda is invoked. Either records invocations in DynamoDB (value `dynamodb://<table_name>`) or forwards invocations as a POST request (value `http(s)://...`).|
| `LAMBDA_FORWARD_URL` | | URL used to forward all Lambda invocations (useful to run Lambdas via an external service).
| `LAMBDA_JAVA_OPTS` | `-Xmx512M` | Allow passing custom JVM options to Java Lambdas executed in Docker. Use `_debug_port_` placeholder to configure the debug port, e.g., `-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=_debug_port_`. |
| `HOSTNAME_FROM_LAMBDA` | `localstack` | Endpoint host under which APIs are accessible from Lambda containers (optional). This can be useful in docker-compose stacks to use the local container hostname if neither IP address nor container name of the main container are available (e.g., in CI). Often used in combination with `LAMBDA_DOCKER_NETWORK`. |
| `LAMBDA_XRAY_INIT` | `1` / `0` (default) | Whether to fully initialize XRay daemon for Lambda containers (may increase Lambda startup times) |

### OpenSearch

| Variable | Example Values | Description |
| - | - | - |
| `OPENSEARCH_CUSTOM_BACKEND` | `http://opensearch:9200` | URL to a custom OpenSearch backend cluster. If this is set to a valid URL, then LocalStack will not create OpenSearch cluster instances, but instead forward all domains to the given backend (see [OpenSearch#custom-opensearch-backends]({{< ref "opensearch#custom-opensearch-backends" >}})). |
| `OPENSEARCH_MULTI_CLUSTER` | `0`\|`1` | When activated, LocalStack will spawn one OpenSearch cluster per domain. Otherwise all domains will share a single cluster instance. This is ignored if `OPENSEARCH_CUSTOM_BACKEND` is set. |
| `OPENSEARCH_ENDPOINT_STRATEGY` | `path`\|`domain`\|`port` | Governs how domain endpoints are created to access a cluster (see [OpenSearch#endpoints]({{< ref "opensearch#endpoints" >}})). |

### StepFunctions

| Variable | Example Values | Description |
| - | - | - |
| `STEPFUNCTIONS_LAMBDA_ENDPOINT` | `default` | URL to use as the Lambda service endpoint in Step Functions. By default this is the LocalStack Lambda endpoint. Use default to select the original AWS Lambda endpoint. |


## Security 

Please be aware that the following configurations may have severe security implications!

| Variable| Example Values | Description |
| - | - | - |
| `DISABLE_CORS_HEADERS` | `0` (default) | Whether to disable the returning of default CORS headers in API responses (disables access from https://app.localstack.cloud) |
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
| `SMTP_HOST` | `localhost` | Hostname of the SMTP server. The port defaults to 25. |
| `SMTP_USER` |  | Login username for the SMTP server if required. |
| `SMTP_PASS` |  | Login password for the SMTP server if required. |
| `SMTP_EMAIL` | `sender@example.com` | Origin email address. Required for Cognito only. |


## Provider

Some of the services can be configured to switch to a particular provider:

| Variable| Valid options | 
| - | - | 
| `KINESIS_PROVIDER` |  `kinesis-mock` (default) and `kinesalite` |
| `KMS_PROVIDER` |  `moto` (default) and `local-kms` |
| `SQS_PROVIDER` |  `moto` (default) and `elasticmq` |


## Miscellaneous 

| Variable | Example Values | Description |
| - | - | - |
| `SKIP_INFRA_DOWNLOADS` | | Whether to skip downloading additional infrastructure components (e.g., specific Elasticsearch versions)
| `SKIP_SSL_CERT_DOWNLOAD` | | Whether to skip downloading the SSL certificate for localhost.localstack.cloud
| `IGNORE_ES_DOWNLOAD_ERRORS` | | Whether to ignore errors (e.g., network/SSL) when downloading Elasticsearch plugins
| `OVERRIDE_IN_DOCKER` | | Overrides the check whether LocalStack is executed within a docker container. If set to `true`, LocalStack assumes it runs in a docker container. Should not be set unless necessary.
| `EDGE_FORWARD_URL` | | Optional target URL to forward all edge requests to (e.g., for distributed deployments)
| `MOCK_UNIMPLEMENTED` | | Whether to return mocked success responses (instead of 501 errors) for currently unimplemented API methods
| `DISABLE_EVENTS` | `1` | Whether to disable publishing LocalStack events
| `OUTBOUND_HTTP_PROXY` | `http://10.10.1.3` | HTTP Proxy used for downloads of runtime dependencies and connections outside LocalStack itself
| `OUTBOUND_HTTPS_PROXY` | `https://10.10.1.3` | HTTPS Proxy used for downloads of runtime dependencies and connections outside LocalStack itself
| `REQUESTS_CA_BUNDLE` | `/tmp/localstack/ca_bundle.pem` | CA Bundle to be used to verify HTTPS requests made by LocalStack
| `DISABLE_TERM_HANDLER` | | Whether to disable signal passing to LocalStack when running in docker. Enabling this will prevent an orderly shutdown when running inside LS in docker.


## Debugging

| Variable | Example Values | Description |
| - | - | - |
| `DEVELOP` | | Starts a debugpy server before starting LocalStack services
| `DEVELOP_PORT` | | Port number for debugpy server
| `WAIT_FOR_DEBUGGER` | | Forces LocalStack to wait for a debugger to start the services

Additionally, the following *read-only* environment variables are available:

* `LOCALSTACK_HOSTNAME`: Name of the host where LocalStack services are available. Use this     hostname as endpoint (e.g., `http://${LOCALSTACK_HOSTNAME}:4566`) in order to **access the services from within your Lambda functions** (e.g., to store an item to DynamoDB or S3 from a Lambda).


## DNS

More information [here]({{< ref "dns-server" >}}).

| Variable | Example Values | Description |
| - | - | - |
| `DNS_ADDRESS` | 0.0.0.0 (default) | Address the LocalStack should bind the DNS server on (port 53 tcp/udp). Value `0` to disable.
| `DNS_SERVER` | 8.8.8.8 (default) | Fallback DNS server for non-modified queries.
| `DNS_LOCAL_NAME_PATTERNS` | | Names which should be resolved to the LocalStack IP, as python-compatible regex.

## LocalStack Pro

More information [here]({{< ref "pro" >}}).

| Variable | Example Values | Description |
| - | - | - |
| `LOCALSTACK_API_KEY` | | API key to activate LocalStack Pro.
| `LOG_LICENSE_ISSUES` | 1 (default) | Whether to log issues with the license activation to the console.
| `REQUIRE_PRO` | 0 (default) | Whether to require license activation to succeed to start LocalStack. If set to 0 (default) LocalStack will start as community version if the license cannot be activated.

## Read-only

| Variable | Usage Example | Description |
| - | - | - |
| `LOCALSTACK_HOSTNAME` | `http://${LOCALSTACK_HOSTNAME}:4566` | Name of the host where LocalStack services are available. Use this hostname as endpoint in order to access the services from within your Lambda functions (e.g., to store an item to DynamoDB or S3 from a Lambda). |

## Deprecated

| Variable | Example Values | Description |
| - | - | - |
| `USE_SSL` | `false` (default) | Whether to use https://... URLs with SSL encryption. *Deprecated as of version 0.11.3* - each service endpoint now supports multiplexing HTTP/HTTPS traffic over the same port.
| `DEFAULT_REGION` | | AWS region to use when talking to the API (needs to be activated via `USE_SINGLE_REGION=1`). *Deprecated and inactive as of version 0.12.17* - LocalStack now has full multi-region support.
| `USE_SINGLE_REGION` | | Whether to use the legacy single-region mode, defined via `DEFAULT_REGION`.
