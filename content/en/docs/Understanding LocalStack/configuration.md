---
title: "Configuration"
weight: 5
description: >
  Environment variables which affect LocalStack.
---

LocalStack allows for many different configuration options.
You can pass these via environment variables, e.g., like the following:

```bash
SERVICES=kinesis,lambda,sqs,dynamodb DEBUG=1 localstack start
```

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
| `PERSISTENCE_SINGLE_FILE` | `true` (default)| Specify if persistence files should be combined. |
| `<SERVICE>_BACKEND` | | Custom endpoint URL to use for a specific service, where <SERVICE> is the uppercase service name. See (TODO) for supported services and (TODO) for examples for third-party integration |
| `MAIN_CONTAINER_NAME` | `localstack_main` (default) | Specify the main docker container name |
| `INIT_SCRIPTS_PATH` | `/some/path` | Specify the path to the initializing files with extensions `.sh` that are found default in `/docker-entrypoint-initaws.d.` |
| `LS_LOG` | `trace`, `trace-internal`, `debug`, `info`, `warn`, `error`, `warning`| Specify the log level. Currently overrides the `DEBUG` configuration. `trace` for detailed request/response, `trace-internal` for internal calls, too. |

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

This section covers configuration values that are specific to AWS services.

* [DynamoDB](#dynamodb)
* [Kinesis](#kinesis)
* [Lambda](#lambda)
* [Stepfunctions](#stepfunctions)


### DynamoDB

| Variable | Example Values | Description |
| - | - | - |
| `DYNAMODB_ERROR_PROBABILITY` | Decimal value between `0.0`(default) and `1.0` | Randomly inject `ProvisionedThroughputExceededException` errors into DynamoDB API responses. |
| `DYNAMODB_HEAP_SIZE` | `256m` (default), `1G` | Sets the JAVA EE maximum memory size for DynamoDB; full table scans require more memory |


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
| `LAMBDA_EXECUTOR` |  | Method to use for executing Lambda functions. For `docker` and `docker-reuse`, if LocalStack itself is started inside Docker, then the `docker` command needs to be available inside the container (usually requires to run the container in privileged mode). More information in [Lambda Executor Modes](../lambda-executors). |
| | `docker` (default) | Run each function invocation in a separate Docker container. |
| | `local` (fallback) | Run Lambda functions in a temporary directory on the local machine. |
| | `docker-reuse` | Create one Docker container per function and reuse it across invocations. |
| `LAMBDA_REMOTE_DOCKER` | | determines whether Lambda code is copied or mounted into containers |
| | `true` (default) | your Lambda function definitions will be passed to the container by copying the zip file (potentially slower). It allows for remote execution, where the host and the client are not on the same machine.|
| | `false` | your Lambda function definitions will be passed to the container by mounting a volume (potentially faster). This requires to have the Docker client and the Docker host on the same machine. Also, `HOST_TMP_FOLDER` must be set properly, and a volume mount like `${HOST_TMP_FOLDER}:/tmp/localstack` needs to be configured if you're using docker-compose. |
| `BUCKET_MARKER_LOCAL` | | Optional bucket name for running lambdas locally.|
| `LAMBDA_CODE_EXTRACT_TIME` | `25` | Time in seconds to wait at max while extracting Lambda code. By default it is 25 seconds for limiting the execution time to avoid client/network timeout issues.| 
| `LAMBDA_DOCKER_NETWORK` | | Optional Docker network for the container running your lambda function. |
| `LAMBDA_DOCKER_DNS` | | Optional DNS server for the container running your lambda function. |
| `LAMBDA_DOCKER_FLAGS` | `-e KEY=VALUE`, `-v host:container`, `-p host:container`, `--add-host domain:ip` | Additional flags passed to Lambda Docker `run`\|`create` commands (e.g., useful for specifying custom volume mounts). Does only support environment, volume, port and add-host flags |
| `LAMBDA_CONTAINER_REGISTRY` | `lambci/lambda` (default) | An alternative docker registry from where to pull lambda execution containers.|
| `LAMBDA_REMOVE_CONTAINERS` | `true` (default) | Whether to remove containers after Lambdas finished executing.|
| `LAMBDA_FALLBACK_URL` | | Fallback URL to use when a non-existing Lambda is invoked. Either records invocations in DynamoDB (value `dynamodb://<table_name>`) or forwards invocations as a POST request (value `http(s)://...`).|
| `LAMBDA_FORWARD_URL` | | URL used to forward all Lambda invocations (useful to run Lambdas via an external service).
| `LAMBDA_JAVA_OPTS` | `-Xmx512M` | Allow passing custom JVM options to Java Lambdas executed in Docker. Use `_debug_port_` placeholder to configure the debug port, e.g., `-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=_debug_port_`. |
| `HOSTNAME_FROM_LAMBDA` | `localstack` | Endpoint host under which APIs are accessible from Lambda containers (optional). This can be useful in docker-compose stacks to use the local container hostname if neither IP address nor container name of the main container are available (e.g., in CI). Often used in combination with `LAMBDA_DOCKER_NETWORK`. |

### Stepfunction

| Variable | Example Values | Description |
| - | - | - |
| `STEPFUNCTIONS_LAMBDA_ENDPOINT` | `default` | URL to use as the Lambda service endpoint in Step Functions. By default this is the LocalStack Lambda endpoint. Use default to select the original AWS Lambda endpoint. |


## Security 

Please be aware that the following configurations may have severe security implications!

| Variable| Example Values | Description |
| - | - | - |
| `DISABLE_CORS_CHECKS` | `0` (default) | Whether to disable all CSRF mitigations. |
| `DISABLE_CUSTOM_CORS_S3` | `0` (default) | Whether to disable CORS override by S3. |
| `DISABLE_CUSTOM_CORS_APIGATEWAY` | `0` (default)| Whether to disable CORS override by apigateway. |
| `EXTRA_CORS_ALLOWED_ORIGINS` | | Comma-separated list of origins that are allowed to communicate with localstack. |
| `EXTRA_CORS_ALLOWED_HEADERS` | | Comma-separated list of header names to be be added to Access-Control-Allow-Headers CORS header. |
| `EXTRA_CORS_EXPOSE_HEADERS` | | Comma-separated list of header names to be be added to Access-Control-Expose-Headers CORS header. |



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
| `SKIP_INFRA_DOWNLOADS` | | Whether to skip downloading additional infrastructure components (e.g., specific Elasticsearch versions).
| `IGNORE_ES_DOWNLOAD_ERRORS` | | Whether to ignore errors (e.g., network/SSL) when downloading Elasticsearch plugins.
| `OVERRIDE_IN_DOCKER` | | Overrides the check whether LocalStack is executed within a docker container. If set to `true`, LocalStack assumes it runs in a docker container. Should not be set unless necessary.
| `EDGE_FORWARD_URL` | | Optional target URL to forward all edge requests to (e.g., for distributed deployments).
| `DISABLE_EVENTS` | `1` | Whether to disable publishing LocalStack events |


## Debugging

| Variable | Example Values | Description |
| - | - | - |
| `DEVELOP` | | Starts a debugpy server before starting LocalStack services
| `DEVELOP_PORT` | | Port number for debugpy server
| `WAIT_FOR_DEBUGGER` | | Forces LocalStack to wait for a debugger to start the services

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
