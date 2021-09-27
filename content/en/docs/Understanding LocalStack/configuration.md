---
title: "Configuration"
date: 2021-09-27
weight: 5
description: >
  Environment variables which affect LocalStack.
---

LocalStack allows for many different configuration options.
You can pass these via environment variables.

## Core Configuration

| Variable                  | Example Values                                                   | Description                                                                                                                                                                           |
| ------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SERVICES`                | `kinesis,lambda,sqs`,`serverless`                                | Comma-separated list of [AWS CLI service names](http://docs.aws.amazon.com/cli/latest/reference/#available-services) or shorthands to start up.                                       |
| `EDGE_BIND_HOST`          | `127.0.0.1`(default), `0.0.0.0`(docker)                          | Address the edge service binds to.                                                                                                                                                    |
| `EDGE_PORT`               | `4566`(default)                                                  | Port number for the edge service, the main entry point for all API invocations.                                                                                                       |
| `HOSTNAME`                | `localhost`(default)                                             | Name of the host to expose the services internally. For framework-internal communication, e.g., services are started in different containers using docker-compose.                    |
| `HOSTNAME_EXTERNAL`       | `localhost`(default)                                             | Name of the host to expose the services externally. This host is used, e.g., when returning queue URLs from the SQS service to the client.                                            |
| `DEBUG`                   | `0`/`1`                                                          | Flag to increase log level and print more verbose logs (useful for troubleshooting issues)                                                                                            |
| `<SERVICE>_PORT_EXTERNAL` | `4567`                                                           | Port number to expose a specific service externally . `SQS_PORT_EXTERNAL`, e.g. , is used when returning queue URLs from the SQS service to the client.                               |
| `IMAGE_NAME`              | `localstack/localstack`(default), `localstack/localstack:0.11.0` | Specific name and tag of LocalStack Docker image to use.                                                                                                                              |
| `USE_LIGHT_IMAGE`         | `1`(default)                                                     | Whether to use the light-weight Docker image. Overwritten by `IMAGE_NAME`.                                                                                                            |
| `TMPDIR`                  | `/tmp`(default)                                                  | Temporary folder on the host running the CLI and inside the LocalStack container .                                                                                                    |
| `HOST_TMP_FOLDER`         | `/some/path`                                                     | Temporary folder on the host that gets mounted as `$TMPDIR/localstack` into the LocalStack container. Required only for Lambda volume mounts when using `LAMBDA_REMOTE_DOCKER=false.` |
| `DATA_DIR`                | blank (disabled/default), `/tmp/localstack/data`                 | Local directory for saving persistent data (see: TODO)                                                                                                                                |
| `PERSISTENCE_SINGLE_FILE` | `true`(default)                                                  | Specify if persistence files should be combined..                                                                                                                                     |


## Lambda Configuration

## Other Service-Specific Configuration

## Security Configuration

## Provider Configuration

## Miscellaneous 

## Debugging