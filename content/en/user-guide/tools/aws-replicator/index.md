---
title: "AWS Replicator"
weight: 13
description: "AWS Replicator makes it easier to use LocalStack in shared AWS environments by copying resources into LocalStack."
tags: ["Ultimate"]
---

## Introduction

Infrastructure deployed on AWS often requires access to shared resources defined externally.
For example a VPC defined by another team to contain the application infrastructure.
This makes it harder to deploy applications into LocalStack as these resource dependencies must be deployed first.
These dependencies may not live in IaC where deployment is easy, or accessing the IaC may not be easy.
Some resources may be referred to by ARN, for example Secrets Manager secrets, but these ARNs are partly random meaning that simply creating a new resource in LocalStack will generate a resource with a different ARN.

LocalStack AWS Replicator creates identical copies of AWS resources in a running LocalStack instance.
This means that external resources can easily be replicated before deploying the main application, and removes the need to change existing stacks or create custom infrastructure, making LocalStack setup easier.

{{< callout "note">}}
The AWS Replicator is in a preview state, supporting only [selected resources](#supported-resources).
It is only available as part of the **LocalStack Teams** plan and higher.
{{< /callout >}}

## Getting started

A valid `LOCALSTACK_AUTH_TOKEN` must be configured to start LocalStack.

{{< callout "note" >}}
The Replicator is in limited preview and is available from LocalStack CLI version 4.2.0.
If you encounter issues, update your [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#updating).
{{< /callout >}}

### Retrieve credentials to access AWS

The AWS Replicator needs read access to your AWS account and performs a limited set of read-only operations on supported resources.
These operations can be limited by creating a minimal IAM role with just the policy actions required for replication, and providing credentials to assume this role.

See the [supported resources section](#supported-resources) for details of what policy actions are required for each resource.

When the replication is triggered using the LocalStack CLI, which must run in a shell configured to access AWS.
Here are some options:

{{< tabpane text=true >}}
{{< tab header="AWS CLI v2" >}}
{{% markdown %}}

If you have the AWS CLI v2 installed, the CLI will read credentials from your configured `AWS_PROFILE`.

{{< command >}}
$ export AWS_PROFILE=my-aws-profile
$ localstack replicator ...
{{< /command >}}

{{% /markdown %}}
{{< /tab >}}
{{< tab header="AWS CLI v1" >}}
{{% markdown %}}
If you have the AWS CLI v1 installed or no installation of the AWS CLI, the following environment variables must be set:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN` (optional)
- `AWS_DEFAULT_REGION`
{{% /markdown %}}
{{< /tab >}}
{{< /tabpane >}}

### Trigger a replication job

Replication jobs can be triggered using the LocalStack CLI or an HTTP API.
Both methods have two steps:

1. Submit a replication job.
2. Check the job status.

#### Using the LocalStack CLI

The Replicator CLI is part of the LocalStack CLI.
Follow the [installation instructions](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) to set it up.

To start a replication job, get the ARN of the resource to replicate.
Then, trigger the job using the command:

{{< command >}}
export LOCALSTACK_AUTH_TOKEN=<auth token>
export AWS_DEFAULT_REGION=...
<disable-copy>
# if required
# export AWS_ACCESS_KEY_ID=
# export AWS_SECRET_ACCESS_KEY=
</disable-copy>
localstack replicator start \
 --resource-type <resource-type> \
 --resource-identifier <identifier> \
 [--target-account-id <account-id>] \
 [--target-region-name <region-name>]
{{< /command >}}

{{< callout "note" >}}
Resources that supports replicating with arn can be replicated by providing `--resource-arn` instead of `--resource-type` and `--resource-identifier`.

{{< command >}}
<disable-copy>$ </disable-copy>localstack replicator start --resource-arn <resource-arn>
{{< /command >}}
{{< /callout >}}

This triggers the replication job.
The output will look similar to:

```json
{
  "job_id": "50005865-1589-4f6d-a720-c86f5a5dd021",
  "state": "TESTING_CONNECTION",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_type": "AWS::SSM::PARAMETER",
    "identifier": "myParameter"
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
    "resource_type": "<resource-type>",
    "identifier": "<identifier>"
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
$ export LOCALSTACK_AUTH_TOKEN=<auth token>

$ localstack replicator status <job-id>
{{< /command >}}

This command returns the job status in JSON format, for example:

```json
{
  "job_id": "50005865-1589-4f6d-a720-c86f5a5dd021",
  "state": "SUCCEEDED",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_type": "AWS::SSM::PARAMETER",
    "identifier": "myParameter"
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
This example uses an SSO profile named `ls-sandbox` for AWS configuration, and replicates resources from the `eu-central-1` region.

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
  localstack replicator start  \
    --resource-type AWS::SSM::Parameter \
 --resource-identifier <identifier> \
<disable-copy>
Configured credentials from the AWS CLI
{
  "job_id": "9acdc850-f71b-4474-b138-1668eb8b8396",
  "state": "TESTING_CONNECTION",
  "error_message": null,
  "type": "SINGLE_RESOURCE",
  "replication_config": {
    "resource_type": "AWS::SSM::PARAMETER",
    "identifier": "myparam"
  }
}
</disable-copy>
{{< /command >}}

You can check the replication job status using the `job_id`:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<ls-auth-token> \
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
{{< /command >}}

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

The project is still in preview state and we welcome feedback and bug reports.
We have opened a [github issue where you can request and upvote](https://github.com/localstack/localstack/issues/12439) to help us prioritize our efforts and support the resources with the most impact.
For any other requests or reports, please open a [new github issue](https://github.com/localstack/localstack/issues/new/choose).

{{< callout "tip" >}}
To ensure support for all resources, use the latest LocalStack Docker image.
{{< /callout >}}

{{< localstack_replicator_table >}}
