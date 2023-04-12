---
title: "Lambda Provider Behavioral Changes"
weight: 5
description: >
  Behavioral changes of the new lambda provider
aliases:
  /references/lambda-asf-provider/
  /references/lambda-v2-provider/
---

{{< alert title="Note">}}
**New implementation active since LocalStack&nbsp;2.0 (Docker `latest` since 2023-03-23)**<br>
The old lambda provider is temporarily available in LocalStack&nbsp;v2 using `PROVIDER_OVERRIDE_LAMBDA=legacy` but we highly recommend migrating to the new lambda provider.
{{< /alert >}}

## Overview
The new lambda provider `v2` (formerly known as `asf`) offers a completely re-written implementation of our [local Lambda service]({{< ref "lambda" >}}) with improved performance, [feature coverage]({{< ref "references/coverage/coverage_lambda" >}}), and [AWS parity](https://localstack.cloud/blog/2022-08-04-parity-explained/).
It comes with significant behavioral changes related to the
Lambda API,
Docker Execution Environment,
Configuration,
and Hot Reloading.

## Highlights

- **[Feature coverage]({{< ref "coverage_lambda" >}}):** LocalStack&nbsp;2.0 supports 95% of all Lambda API operations.
- **[AWS Parity](https://localstack.cloud/blog/2022-08-04-parity-explained/):** The local Lambda API behaves like in AWS with 90% parity test coverage.
- **[Official AWS images](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html):** Lambda functions use the official Docker base images pulled from `public.ecr.aws/lambda/`.
- **[Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html):** All supported managed runtimes from AWS are available and tested in LocalStack. The new provider added `nodejs18.x`.
- **[ARM support]({{< ref "arm64-support#lambda-multi-architecture-support" >}}):** Run arm64 and x86_64 Lambda functions on hosts with multi-architecture support.
- **[Extensions API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-extensions-api.html):** Use third-party extensions to customize the Lambda execution environment. This deep integration enables monitoring, observability, or advanced developer tooling.
- **[Lambda concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html):** Prevent cold-starts with provisioned concurrency and limit the number of concurrent function instances with reserved concurrency.
- **Performance:** 10ms warm-start and 600ms cold-start for an Echo Python Lambda
- **[Hot reloading]({{< ref "hot-reloading" >}}):** Continuously apply code changes to Lambda functions and layers (Pro) for all managed runtimes.
- **[Persistence]({{< ref "persistence-mechanism" >}}) and [Cloud Pods]({{< ref "cloud-pods" >}}):** Save your Lambda state across restarts and share a snapshot of your Lambda infrastructure.

Check out our [Lambda release announcement](https://discuss.localstack.cloud/t/new-lambda-implementation-in-localstack-2-0/258) for more details about further improvements.

## Lambda API

**Improved parity compared to AWS:**
Lambda API methods in LocalStack behave like in [AWS](https://docs.aws.amazon.com/lambda/latest/dg/API_Reference.html).
This was not always the case in the old provider without systematic testing.
If you discover a difference between LocalStack and AWS in the new provider, please report a [bug on GitHub](https://github.com/localstack/localstack/issues/new/choose).

**Stricter input validation:**
Expect more exceptions in the new provider due to invalid input.
For example, the old provider accepted arbitrary strings such as `r1` as a [lambda role](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Role) when creating a function.
The new provider validates the role ARN in the format `arn:aws:iam::000000000000:role/lambda-role` using an appropriate regex but currently does not check whether it exists.

**Asynchronous function creation:**
Creating and updating lambda functions now happens asynchronously following the [AWS Lambda state model](https://aws.amazon.com/blogs/compute/tracking-the-state-of-lambda-functions/).
The old provider created functions synchronously by blocking until the function state was active.
In the new provider, functions are always created in the `Pending` state and move to `Active` once they are ready to accept invocations.
Migration instructions are provided in the troubleshooting example [Function in Pending state](#function-in-pending-state) below.

## Docker Execution Environment

**Docker socket mounting required:**
Mounting the Docker socket into the LocalStack container is now required to run lambda functions.
Please add the Docker volume mount `"/var/run/docker.sock:/var/run/docker.sock"` to your LocalStack startup as exemplified in our official [docker-compose.yml](https://github.com/localstack/localstack/blob/master/docker-compose.yml).
If mounting the Docker socket is impossible and no external `DOCKER_HOST` is available, self-managed worker containers will be available (coming soon).

**Local executor mode is discontinued:**
The [Lambda Executor Modes]({{< ref "references/lambda-executors" >}}) such as `LAMBDA_EXECUTOR=local` are discontinued in the new provider.
In the old provider, lambda functions were executed within the LocalStack container in the local executor mode.
It was primarily used as a fallback if the Docker socket was unavailable in the LocalStack container.
Hence, many users unintentionally used the local executor mode despite configuring `LAMBDA_EXECUTOR=docker`.
The new provider requires no such configuration and now behaves similar to the old `docker-reuse` executor.

**No container restart after each invocation:**
Lambda containers are reused between invocations.
Therefore, filesystem changes (for example, in `/tmp`) persist between subsequent invocations if dispatched to the same container.
It is called a "warm start" (see [Operating Lambda](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)).
If you want to force "cold starts", you could set `LAMBDA_KEEPALIVE_MS` to 0 milliseconds.

**Official AWS-provided Lambda images:**
The new provider uses the official AWS [base images for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html) pulled from `public.ecr.aws/lambda/` instead of `lambci` images.
Hence, Lambda functions' filesystem now matches the AWS Lambda production environment.

**ARM64 lambda functions:**
Lambda now supports ARM containers for compatible runtimes based on Amazon Linux 2.
ARM-compatible hosts can create functions with the `arm64` architecture.
More details are provided under [ARM64 support]({{< ref "references/arm64-support" >}}).

**Transparent endpoint injection in LocalStack Pro:**
Lambda functions resolve AWS domains such as `s3.amazonaws.com` to the LocalStack container.
This domain resolution is now completely DNS-based and can be disabled by setting `DNS_ADDRESS=0`.
For more details, please refer to [Transparent Endpoint Injection]({{< ref "user-guide/tools/transparent-endpoint-injection" >}}).
The old provider provided patched AWS SDKs to redirect AWS API transparently calls to LocalStack.

## Configuration

The new provider offers new configuration options documented under [Configuration]({{< ref "references/configuration#lambda" >}}).
Please open a [feature request on GitHub](https://github.com/localstack/localstack/issues/new/choose) and motivate your scenario if you miss something.

The following configuration options from the old provider are discontinued in the new provider:
* `LAMBDA_EXECUTOR` and, in particular, `LAMBDA_EXECUTOR=local` should be removed (see "Local executor mode is discontinued" above).
* `LAMBDA_STAY_OPEN_MODE` is now the default behavior and can be removed. Instead, `LAMBDA_KEEPALIVE_MS` can be used to configure how long containers should be kept running in-between invocations.  
* `LAMBDA_REMOTE_DOCKER` is not used anymore because the new provider always copies zip files and automatically configures hot reloading.
* `LAMBDA_CODE_EXTRACT_TIME` is no longer used because function creation now happens asynchronously.
* `LAMBDA_DOCKER_DNS` is currently not supported.
* `LAMBDA_CONTAINER_REGISTRY` is not used anymore. Use the more flexible `LAMBDA_RUNTIME_IMAGE_MAPPING` to customize individual runtimes.
* `LAMBDA_FALLBACK_URL` is not supported anymore.
* `LAMBDA_FORWARD_URL` is not supported anymore.
* `HOSTNAME_FROM_LAMBDA` is not supported anymore.
* `LAMBDA_XRAY_INIT` is no longer needed because the X-Ray daemon is always initialized.
* `SYNCHRONOUS_KINESIS_EVENTS` and `SYNCHRONOUS_SNS_EVENTS` are not supported anymore.

The new provider still supports the following configuration options:
* `BUCKET_MARKER_LOCAL` has a new default value, `hot-reload` (new), because the former default `__local__` (old) is an invalid bucket name.
* `LAMBDA_TRUNCATE_STDOUT`
* `LAMBDA_DOCKER_NETWORK`
* `LAMBDA_DOCKER_FLAGS`
* `LAMBDA_REMOVE_CONTAINERS`

## Hot Reloading

[Hot Reloading]({{< ref "user-guide/tools/lambda-tools/hot-reloading" >}}) (formerly known as hot swapping) continuously applies code changes to Lambda functions without manual redeployment.

**Default S3 bucket name changed:**
The default magic S3 bucket name changed from `__local__` to `hot-reload`.
Please change your deployment configuration accordingly, or use the `BUCKET_MARKER_LOCAL` configuration to customize the value.

**Delay in code change detection:**
It can take up to 700ms to detect code changes.
In the meantime, invocations still execute the former code.
Hot reloading triggers after 500ms without changes can take up to 200ms until the change is notified.
In the old provider, changes were reflected instantly using code mounting but container restarting added extra delay.

**Runtime restart after each code change:**
The runtime inside the container is restarted after every code change.
During the runtime restart, the handler function re-executes any initialization code *outside* your handler function.
The container itself is not restarted.
Therefore, filesystem changes persist between code changes for invocations dispatched to the same container.

**File sharing permissions with Docker Desktop on macOS:**
If using Docker Desktop on macOS, you might need to allow [file sharing](https://docs.docker.com/desktop/settings/mac/#file-sharing) for your target folders.
MacOS may prompt you to grant Docker access to your target folders.

**Startup configuration automated:**
Hot reloading now works without additional LocalStack startup configuration.
In the old provider, starting LocalStack with `LAMBDA_REMOTE_DOCKER=0` was required.
This configuration is not used anymore because the new provider always copies zip files and automatically configures hot reloading.

## Troubleshooting

### Docker not available

If deploying or invoking any lambda function fails with a similar error than below,
add the Docker volume mount `"/var/run/docker.sock:/var/run/docker.sock"` to your LocalStack startup
as exemplified in our official [docker-compose.yml](https://github.com/localstack/localstack/blob/master/docker-compose.yml).

* LocalStack logs:

  ```log
  Lambda 'arn:aws:lambda:us-east-1:000000000000:function:my-function:$LATEST' changed to failed. Reason: Docker not available
  ...
  raise DockerNotAvailable("Docker not available")
  ```

  ```log
  Error applying changes for CloudFormation stack "sam-app": Waiter FunctionActiveV2 failed: Waiter encountered a terminal failure state: For expression "Configuration.State" we matched expected path: "Failed" Traceback (most recent call last):
  ...
  botocore.exceptions.WaiterError: Waiter FunctionActiveV2 failed: Waiter encountered a terminal failure state: For expression "Configuration.State" we matched expected path: "Failed"
  ```

* `awslocal` CLI:

  {{< command >}}
  $ awslocal lambda get-function --function-name my-function
  An error occurred (ResourceConflictException) when calling the Invoke operation (reached max retries: 0): The operation cannot be performed at this time. The function is currently in the following state: Failed
  {{< / command >}}

* `samlocal` / CloudFormation:

  {{< command >}}
  $ samlocal sync --stack-name sam-app
  Error: Failed to create/update the stack: sam-app, Waiter StackCreateComplete failed: Waiter encountered a terminal failure state: For expression "Stacks[].StackStatus" we matched expected path: "CREATE_FAILED" at least once
  {{< / command >}}

### Function in Pending state

If you experience the following `ResourceConflictException` exception when trying to invoke a function:

{{< command >}}
$ awslocal lambda get-function --function-name my-function
An error occurred (ResourceConflictException) when calling the Invoke operation (reached max retries: 0):
The operation cannot be performed at this time.
The function is currently in the following state: Pending
{{< / command >}}

Wait until the function becomes active using a [waiter](https://docs.aws.amazon.com/cli/latest/reference/lambda/wait/function-active-v2.html):

{{< command >}}
$ awslocal lambda wait function-active-v2 --function-name my-function
{{< / command >}}

Alternatively, check the function state using a [get-function](https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/lambda/get-function.html) call:

{{< command >}}
$ awslocal lambda get-function --function-name my-function
{
  "Configuration": {
    ...
    "RevisionId": "c61d6139-1441-4ad5-983a-5a1cec7a1847",
    "State": "Pending",
    "StateReason": "The function is being created.",
    "StateReasonCode": "Creating",
    ...
  }
}

$ awslocal lambda get-function --function-name my-function
{
  "Configuration": {
    ...
    "RevisionId": "c6633a28-b8d2-40f7-b8e1-02f6f32e8473",
    "State": "Active",
    "LastUpdateStatus": "Successful",
    ...
  }
}
{{< / command >}}

The [configuration]({{< ref "configuration#lambda" >}}) `LAMBDA_SYNCHRONOUS_CREATE=1` forces synchronous function creation but is not recommended.

### Not implemented error

If creating any lambda function fails with a `NotImplementedError` in the LocalStack logs and an `InternalFailure` (501) in the client:

{{< command >}}
$ awslocal lambda create-function <parameters>
An error occurred (InternalFailure) when calling the CreateFunction operation (reached max retries: 0): API action 'CreateFunction' for service 'lambda' not yet implemented or pro feature - check https://docs.localstack.cloud/user-guide/aws/feature-coverage for further information
{{< / command >}}

Please check your [configuration]({{< ref "configuration#lambda" >}}) for `PROVIDER_OVERRIDE_LAMBDA`.
If you are not using LocalStack&nbsp;2.0 yet, remove `PROVIDER_OVERRIDE_LAMBDA=legacy`.
