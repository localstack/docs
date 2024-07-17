---
title: Usage Tracking
weight: 50
description: >
  Understand what data LocalStack collects and how you can opt out of usage tracking
aliases:
  - /localstack/usage-tracking/
---

## Overview

For license activations, we track the timestamp and the licensing credentials.
We need to do this to make CI credits work.
It is tracked regardless of whether the user disables event tracking since we collect this in the backend, not the client.

## LocalStack usage statistics

For Pro users, most of the information is collected to populate the [Stack Insights](https://docs.localstack.cloud/user-guide/web-application/stack-insights) dashboard.
Collecting basic anonymized usage of AWS services helps us better direct engineering efforts to services that are used the most or cause the most issues.

### Session information

The current usage event collection on the client side includes:

- A randomly generated ID pertaining to the session
- The auth token or legacyAPI key (if any)
- A randomly generated machine ID is kept throughout the session but deleted once the LocalStack cache directory is removed
- The operating system (mostly Linux since LocalStack typically runs in our Debian container)
- The LocalStack version being used
- Whether LocalStack is running in a CI environment
- Whether LocalStack is running in Docker
- Whether this is an internal test run (LocalStack development flag)

Here is an example of a usage event:

```json
{
  "session_id": "f41119fd-af20-4d48-af92-2b8d69f8cf7e",
  "machine_id": "1b6a2f12",
  "api_key": "0123456789",
  "system": "Linux",
  "version": "1.0.5.dev",
  "is_ci": false,
  "is_docker": true,
  "is_testing": false
}
```

### AWS API call metadata

The AWS API call metadata includes:

- The service being called (like `s3` or `lambda`)
- The operation being called (like `PutObject`, `CreateQueue`, `DeleteQueue`)
- The HTTP status code of the response
- If it is a 400 error, we collect the error type and message.
  If it is a 500 error (internal LocalStack error), and `DEBUG=1` is enabled, we may also collect the stack trace to help us identify LocalStack bugs
- Whether the call originated from inside LocalStack
- The region user made the call to
- The dummy account ID user made the request
- The user agent the request was made with (`aws-cli`, `terraform`)

Here is an example of AWS API call metadata:

```json
{
  "name": "aws_request",
  "metadata": {
    "session_id": "64517be1-7dd0-479b-a8ec-88d3e544afd9",
    "client_time": "2022-08-30 12:27:25.556001"
  },
  "payload": {
    "service": "sqs",
    "operation": "DeleteQueue",
    "status_code": 400,
    "err_type": "AWS.SimpleQueueService.NonExistentQueue",
    "err_msg": "The specified queue does not exist for this wsdl version.",
    "is_internal": false,
    "region": "us-east-1",
    "account_id": "000000000000",
    "user_agent": "aws-cli/1.25.52 Python/3.10.4 Linux/5.13.0-28-generic awscrt/0.14.0 botocore/1.27.52"
  }
}
```

For the community image, we only track service, operation, status code, and how often the combination of those occurred.

### CLI invocations

We collect an anonymized event if a CLI command was invoked, but do not collect any of the parameter values.
This event is not connected to the session or the auth token.

Here is an example of a CLI invocation event:

```json
{
  "name": "cli_cmd",
  "metadata": {
    "client_time": "2022-08-30 14:46:54.116457"
  },
  "payload": {
    "cmd": "localstack config validate",
    "params": [
      "file"
    ]
  }
}
```

### Feature usage

We collect the usage of particular features in an anonymized and aggregated way.

- If you use init scripts, we collect the stage, how many scripts are being executed, and how long they took
- Nothing else at the moment, but we may track additional features

## What we are not collecting?

- Specific LocalStack configuration values
- Content or file names of files being uploaded to S3
- More generally, we don't collect any parameters of AWS API Calls.
  We do not track S3 bucket names, Lambda function names, EC2 configurations, or anything similar
- Any sensitive information about the request (like credentials and URL parameters)

## Configuration

You can disable event reporting in your LocalStack instance by setting the environment variable `DISABLE_EVENTS=1`.
