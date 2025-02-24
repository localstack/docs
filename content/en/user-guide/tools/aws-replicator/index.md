---
title: "AWS Replicator"
weight: 13
description: "AWS Replicator makes it easier to use LocalStack in shared AWS environments by copying resources into LocalStack using their ARNs."
tags: ["Pro image"]
---

## Introduction

LocalStack AWS Replicator copies AWS resources into a running LocalStack instance.
It helps when deploying applications that rely on existing resources like SSM parameters or VPCs, ensuring they are available before deploying the main stack.

This removes the need to change existing stacks or create custom infrastructure, making LocalStack setup easier.

## Getting started

To get started, set `LOCALSTACK_ENABLE_REPLICATOR=1` configuration variable when starting LocalStack.
A valid `LOCALSTACK_AUTH_TOKEN` must be configured to start the LocalStack Pro image.

### Retrieve credentials to access AWS

The AWS Replicator needs read access to your AWS account and can perform a limited set of read-only operations on supported resources.

Replication is triggered using the LocalStack CLI, which must run in a shell configured to access AWS.

The following environment variables must be set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN` (optional)
- `AWS_DEFAULT_REGION`

{{< callout "tip" >}}
Use `aws configure export-credentials --format env` to print the required environment variables in a format that can be evaluated.

{{< command >}}
$ eval $(AWS_PROFILE=<aws-profile> aws configure export-credentials \
 --format env)
{{< /command >}}
{{< /callout >}}

### Trigger a replication job

Replication jobs can be triggered using the LocalStack CLI or an HTTP API.
Both methods have two steps:

1. Submit a replication job.
2. Check the job status.

#### Using the LocalStack CLI

The Replicator CLI is part of the LocalStack CLI.
Follow the [installation instructions](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) to set it up.

{{< callout "note" >}}

The Replicator is in limited preview and must be enabled with `LOCALSTACK_ENABLE_REPLICATOR=1` when using the CLI.

It is available from LocalStack CLI version 4.2.0.
If you encounter issues, update your [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#updating).
{{< /callout >}}

To start a replication job, get the ARN of the resource to replicate.
Then, trigger the job using the command:

{{< command >}}
export LOCALSTACK_ENABLE_REPLICATOR=1
export LOCALSTACK_AUTH_TOKEN=<auth token>
export AWS_DEFAULT_REGION=...
<disable-copy>
# if required
# export AWS_ACCESS_KEY_ID=
# export AWS_SECRET_ACCESS_KEY=
</disable-copy>
localstack replicator start \
  --replication-type SINGLE_RESOURCE \
 --resource-arn <resource-arn> \
 [--target-account-id <account-id>] \
 [--target-region-name <region-name>]
{{< /command >}}

This triggers the replication job.
The output will look similar to:

```bash
{
  "job_id": "50005865-1589-4f6d-a720-c86f5a5dd021",
  "state": "TESTING_CONNECTION",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_arn": "arn:aws:ssm:<region>:<account-id>:parameter/myparam"
  }
}
```

{{< callout "note" >}}
- `--target-account-id` specifies the destination AWS account for replication.
  If not set, the resource is replicated into account `000000000000`.
- `--target-region-name` specifies the destination AWS region.
  If not set, the resource is replicated into the default region from the provided credentials.
{{< /callout >}}

#### Using the HTTP API

To trigger replication via the HTTP API, send a `POST` request to `http://localhost.localstack.cloud:4566/_localstack/replicator/jobs` with the following payload:

```json
{
  "replication_type": "SINGLE_RESOURCE",
  "replication_job_config": {
    "resource_arn": "<arn>"
  },
  "source_aws_config": {
    "aws_access_key_id": "...",
    "aws_secret_access_key": "...",
    "aws_session_token": "...", // optional
    "region_name": "...",
    "endpoint_url": "..." // optional
  },
  "target_aws_config": {} // optional, same shape as `source_aws_config`
}
```

### Check Replication Job Status

Replication jobs run asynchronously, so you need to poll their status to check when they finish.

#### Using the LocalStack CLI

When creating a replication job, the response includes a `job_id`.
Use this ID to check the job status:

{{< command >}}
$ export LOCALSTACK_ENABLE_REPLICATOR=1
$ export LOCALSTACK_AUTH_TOKEN=<auth token>

$ localstack replicator status <job-id>
{{< /command >}}

This command returns the job status in JSON format, for example:

```bash
{
  "job_id": "50005865-1589-4f6d-a720-c86f5a5dd021",
  "state": "SUCCEEDED",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_arn": "arn:aws:ssm:<region>:<account-id>:parameter/myparam"
  }
}
```

For long-running jobs, the CLI can poll the status until the job reaches a terminal state.
To wait for the job to finish, use the `--follow` flag.

#### Using the HTTP API

To check the status of a replication job via the HTTP API, send a `GET` request to `http://localhost.localstack.cloud:4566/_localstack/replicator/jobs/<job-id>`.

{{< callout "tip" >}}
If the replication state is `SUCCEEDED` but the resource is missing, check in account `000000000000`.
{{< /callout >}}

## Quickstart

This quickstart example creates an SSM parameter in AWS and replicates it to LocalStack.

To start, create the parameter in AWS.
This example uses an SSO profile named `ls-sandbox` for AWS configuration.

{{< command >}}
$ AWS_PROFILE=ls-sandbox aws ssm put-parameter\
  --name myparam \
  --type String \
  --value abc123
<disable-copy>
{
    "Version": 1,
    "Tier": "Standard"
}
</disable-copy>
$ AWS_PROFILE=ls-sandbox aws ssm get-parameters --names myparam
<disable-copy>
{
    "Parameters": [
        {
            "Name": "myparam",
            "Type": "String",
            "Value": "abc123",
            "Version": 1,
            "LastModifiedDate": "2025-02-07T13:36:56.240000+00:00",
            "ARN": "arn:aws:ssm:eu-central-1:<account-id>:parameter/myparam",
            "DataType": "text"
        }
    ],
    "InvalidParameters": []
}
</disable-copy>
{{< /command >}}

The SSM parameter has the ARN: `arn:aws:ssm:eu-central-1:<account-id>:parameter/myparam`.

Next, we can check that the parameter is not present in LocalStack using `awslocal`:

{{< command >}}
$ awslocal ssm get-parameters --name myparam
<disable-copy>
{
    "Parameters": [],
    "InvalidParameters": [
        "myparam"
    ]
}
</disable-copy>
{{< /command >}}

Next, trigger replication from AWS to LocalStack.
This example uses an SSO profile named `ls-sandbox` for AWS configuration.

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<ls-auth-token> \
  AWS_PROFILE=ls-sandbox \
  LOCALSTACK_ENABLE_REPLICATOR=1 \
  localstack replicator start  \
    --replication-type SINGLE_RESOURCE \
 --resource-arn arn:aws:ssm:eu-central-1:<account-id>:parameter/myparam
<disable-copy>
Configured credentials from the AWS CLI
{
  "job_id": "9acdc850-f71b-4474-b138-1668eb8b8396",
  "state": "TESTING_CONNECTION",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_arn": "arn:aws:ssm:eu-central-1:<account-id>:parameter/myparam"
  }
}
</disable-copy>
{{< /command >}}

You can check the replication job status using the `job_id`:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<ls-auth-token> \
  LOCALSTACK_ENABLE_REPLICATOR=1 \
  localstack replicator status 9acdc850-f71b-4474-b138-1668eb8b8396
<disable-copy>
{
  "job_id": "9acdc850-f71b-4474-b138-1668eb8b8396",
  "state": "SUCCEEDED",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_arn": "arn:aws:ssm:eu-central-1:<account-id>:parameter/myparam"
  }
}
</disable-copy>
{{< command >}}

The state is `SUCCEEDED`, indicating the replication job completed successfully.
The SSM parameter is now accessible.

{{< command >}}
$ awslocal ssm get-parameters --name myparam --region eu-central-1
<disable-copy>
{
    "Parameters": [
        {
            "Name": "myparam",
            "Type": "String",
            "Value": "abc123",
            "Version": 1,
            "LastModifiedDate": 1738935663.08,
            "ARN": "arn:aws:ssm:eu-central-1:000000000000:parameter/myparam",
            "DataType": "text"
        }
    ],
    "InvalidParameters": []
}
</disable-copy>
{{< /command >}}

The resource is replicated into the same AWS region by default.
Use the `--target-region-name` flag to change it.
By default, replication occurs in LocalStack account `000000000000`.
Use the `--target-account-id` flag to specify a different account.

## Supported Resources

{{< callout "tip" >}}
To ensure support for all resources, use the latest LocalStack Docker image.
{{< /callout >}}

// WIP
