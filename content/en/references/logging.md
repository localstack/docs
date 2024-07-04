---
title: Logging
weight: 50
tags:
- logging
description: >
  Overview of LocalStack logging and error reporting
---

LocalStack supports logging output and error reporting through the `localstack` CLI or a Docker/Docker Compose based setup. LocalStack's logging setup allows you to:

- Discover errors in your code during development & testing.
- Get visibility into how and why your API calls are failing.
- Figure out unexpected errors such as Lambda timeouts and more!

With LocalStack logging, you can easily retrieve additional detail around errors using various configuration variables to specify the verbosity and the log level.

## Log Level

You can explicitly set a log level via two configuration variables: `DEBUG` and `LS_LOG`. You can configure them while starting the LocalStack container, either with the CLI or a Docker/Docker-Compose setup.

`DEBUG` can be either `0` or `1` (`0` is the default). With `DEBUG`, you can print more verbose logs, useful for troubleshooting issues. With `DEBUG=1`, errors inside LocalStack are reported to the client in full, and these stack traces can help you better triage your issues.

`LS_LOG` supports the following values:

- `trace`
- `trace-internal`
- `debug`
- `info`
- `warn`
- `error`
- `warning`

The `LS_LOG` affects the log handlers level directly. If `LS_LOG` is configured as `trace` or `trace-internal`, it will automatically set `DEBUG=1`. To retrieve the debug information, it is recommended to set `DEBUG=1`. While configuring `LS_LOG` as `trace` or `trace-internal`, the LocalStack container will report the same log format but append the request and response objects and the HTTP headers to the log line.

## Error reporting

AWS requests are logged uniformly in the `INFO` log level (set by default or when `DEBUG=0`). The shape is `AWS <service>.<operation> => <http-status> (<error type>)`. Requests to HTTP endpoints are logged in a similar way.

```sh
2022-07-12T10:12:03.250  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.PutObject => 404 (NoSuchBucket)
2022-07-12T10:12:11.295  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS s3.CreateBucket => 200
2022-07-12T10:12:13.159  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS s3.PutObject => 200
2022-07-12T10:12:28.761  INFO --- [   asgi_gw_0] localstack.request.http    : GET /_localstack/health => 200
```

## Log inspection

You can inspect the logs of the LocalStack container using the `localstack` CLI or your Docker/Docker Compose setup. With the `localstack` CLI, you can run the following command to inspect the logs of the LocalStack container:

{{< command >}}
$ localstack logs
{{< / command >}}

With Docker/Docker-Compose, you can run `docker ps` to get the container ID of the LocalStack container and then run `docker logs <container-id>` to inspect the logs.

To view the logs via a user interface, you can use the following options:

- [LocalStack Desktop App](https://docs.localstack.cloud/user-guide/tools/localstack-desktop/)
- [LocalStack Docker Extension](https://docs.localstack.cloud/user-guide/tools/localstack-docker-extension/)
