---
title: "Lambda Provider Behavioral Changes"
weight: 5
description: >
  Behavioral changes of the new lambda provider
aliases:
  /references/lambda-asf-provider/
---

## Overview
The new lambda provider `v2` (formerly known as `asf`) offers a completely re-written implementation with improved performance, [feature coverage]({{< ref "references/coverage/coverage_lambda" >}}), and [parity compared to AWS](https://localstack.cloud/blog/2022-08-04-parity-explained/).
It comes with significant behavioral changes related to the
Lambda API,
Docker Execution Environment,
Configuration,
and Hot Reloading.

{{< alert title="Note">}}
The new lambda provider is active by default starting with Localstack&nbsp;v2.0.<br>
The old lambda provider is temporarily available in Localstack&nbsp;v2 using `PROVIDER_OVERRIDE_LAMBDA=legacy` but we highly recommend migrating to the new lambda provider.
{{< /alert >}}

## Lambda API

**Improved parity compared to AWS:**
Lambda API methods in LocalStack behave like in [AWS](https://docs.aws.amazon.com/lambda/latest/dg/API_Reference.html).
This was not always the case in the old provider without systematic testing.
If you discover a difference between LocalStack and AWS in the new provider, please report a [bug on GitHub](https://github.com/localstack/localstack/issues/new/choose).

**Stricter input validation:**
Expect more exceptions in the new provider due to invalid input.
For example, the old provider accepted arbitrary strings such as `r1` as a [lambda role](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Role) when creating a function.
The new provider validates the role arn in the format `arn:aws:iam::000000000000:role/lambda-role` using an appropriate regex but currently does not check whether it actually exists.

**Asynchronous function creation:**
Creating and updating lambda functions now happens asynchronously following the [AWS Lambda state model](https://aws.amazon.com/blogs/compute/tracking-the-state-of-lambda-functions/).
The old provider created functions synchronously by blocking until the function state was active.
In the new provider, functions are always created in the `Pending` state and move to `Active` once they ready for handling invocations.
Migration instructions are provided in the troubleshooting example [Function in Pending state](#function-in-pending-state) below.

## Docker Execution Environment

**Docker socket mounting required:**
Mounting the Docker socket into the LocalStack container is now required to run Lambdas.
Please add the Docker volume mount `"/var/run/docker.sock:/var/run/docker.sock"` to your LocalStack startup as exemplified in our official [docker-compose.yml](https://github.com/localstack/localstack/blob/master/docker-compose.yml).
If mounting the Docker socket is impossible and no external `DOCKER_HOST` is available, self-managed worker containers will be available (coming soon).

**Local executor mode is discontinued:**
The [Lambda Executor Modes]({{< ref "references/lambda-executors" >}}) such as `LAMBDA_EXECUTOR=local` are discontinued in the new provider.
In the old provider, lambda functions were executed within the LocalStack container in the local executor mode.
This was mostly used as a fallback if the Docker socket was not available in the LocalStack container.
Hence, many users unintentionally used the local executor mode despite configuring `LAMBDA_EXECUTOR=docker`.
The new provider requires no such configuration and now behaves equivalent to the old `docker-reuse` executor.

**No container restart after each invocation:**
Lambda containers are reused between invocations.
Therefore, filesystem changes (for example in `/tmp`) persist between subsequent invocations if dispatched to the same container.
This is called a "warm start" (see [Operating Lambda](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)).
If you want to force "cold starts", you could set `LAMBDA_KEEPALIVE_MS` to 0 milliseconds.

**Official AWS-provided Lambda images:**
The new provider uses the official AWS [base images for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html) pulled from `public.ecr.aws/lambda/` instead of *lambci* images.
Hence, the filesystem in Lambda functions now match the AWS Lambda production environment.

**ARM64 lambda functions:**
Lambda now supports ARM containers for compatible runtimes based on Amazon Linux 2.
ARM-compatible hosts can create functions with the `arm64` architecture.
More details are provided under [ARM64 support]({{< ref "references/arm64-support" >}}).

**Transparent endpoint injection in LocalStack Pro:**
Lambda functions resolve AWS domains such as `s3.amazonaws.com` to the LocalStack container.
This domain resolution is now completely DNS-based and can be disabled by setting `DNS_ADDRESS=0`.
For more details, please refer to [Transparent Endpoint Injection]({{< ref "user-guide/tools/transparent-endpoint-injection" >}}).
The old provider provided patched AWS SDKs to transparently redirect AWS API calls to LocalStack.

## Configuration

The new provider offers new configuration options documented under [Configuration]({{< ref "references/configuration" >}}).
Please open a [feature request on GitHub](https://github.com/localstack/localstack/issues/new/choose) and motivate your scenario if you miss something.

The following configuration options from the old provider are discontinued in the new provider:
* `LAMBDA_EXECUTOR` and in particular `LAMBDA_EXECUTOR=local` should be removed (see "Local executor mode is discontinued" above).
* `LAMBDA_STAY_OPEN_MODE` is now the default behavior and can be removed. Instead, `LAMBDA_KEEPALIVE_MS` can be used to configure how long containers should be kept running in-between invocations.  
* `LAMBDA_REMOTE_DOCKER` is not used anymore because the new provider always copies zip files and automatically configures hot reloading.
* `LAMBDA_CODE_EXTRACT_TIME` is not used anymore because function creation now happens asynchronously.
* `LAMBDA_DOCKER_DNS` is currently not supported.
* `LAMBDA_CONTAINER_REGISTRY` is not used anymore. Use the more flexible `LAMBDA_RUNTIME_IMAGE_MAPPING` to customize individual runtimes.
* `LAMBDA_FALLBACK_URL` is not supported anymore.
* `LAMBDA_FORWARD_URL` is not supported anymore.
* `HOSTNAME_FROM_LAMBDA` is not supported anymore.
* `LAMBDA_XRAY_INIT` is not needed anymore because the X-Ray daemon is always initialized.
* `SYNCHRONOUS_KINESIS_EVENTS` and `SYNCHRONOUS_SNS_EVENTS` are not supported anymore.

The following configuration options are still supported in the new provider:
* `BUCKET_MARKER_LOCAL` has a new default value `hot-reload` (new) because the former default `__local__` (old) is an invalid bucket name.
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
Hot reloading triggers after 500ms without changes, and it can take up to 200ms until the change is notified.
In the old provider, changes were reflected instantly using code mounting but container restarting added extra delay.

**Runtime restart after each code change:**
The runtime inside the container is restarted after every code change.
Therefore, any initialization code *outside* the handler function re-executes after every code change.
However, the container itself does not restart.
Therefore, filesystem changes persist between code changes for invocations dispatched to the same container.

**File sharing permissions with Docker Desktop on macOS:**
If using Docker Desktop on macOS, you might need to allow [file sharing](https://docs.docker.com/desktop/settings/mac/#file-sharing) for your target folders.
MacOS may prompt you to grant Docker access to your target folders.

**Startup configuration automated:**
Hot reloading now works without additional LocalStack startup configuration.
In the old provider, it was required to start LocalStack with `LAMBDA_REMOTE_DOCKER=0`.
This configuration is not used anymore because the new provider always copies zip files and automatically configures hot reloading.

## Troubleshooting

### Docker not available

If all lambda functions fail to deploy or invoke with a similar error than below,
mount the Docker socket `"/var/run/docker.sock:/var/run/docker.sock"` as a volume when starting LocalStack as exemplified in our official [docker-compose.yml](https://github.com/localstack/localstack/blob/master/docker-compose.yml).

* LocalStack logs:

  ```log
  Lambda 'arn:aws:lambda:us-east-1:000000000000:function:my-function:$LATEST' changed to failed. Reason: Docker not available
  ...
  raise ContainerException("Docker not available")
  ```

  ```log
  Error applying changes for CloudFormation stack "sam-app": Waiter FunctionActiveV2 failed: Waiter encountered a terminal failure state: For expression "Configuration.State" we matched expected path: "Failed" Traceback (most recent call last):
  ...
  botocore.exceptions.WaiterError: Waiter FunctionActiveV2 failed: Waiter encountered a terminal failure state: For expression "Configuration.State" we matched expected path: "Failed"
  ```

* awslocal CLI:

  {{< command >}}
  $ awslocal lambda get-function --function-name my-function
  An error occurred (ResourceConflictException) when calling the Invoke operation (reached max retries: 0): The operation cannot be performed at this time. The function is currently in the following state: Failed
  {{< / command >}}

* samlocal / cloudformation:

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

Wait until the function becomes active using a [waiter](https://docs.aws.amazon.com/cli/latest/reference/lambda/wait/function-active-v2.html)
or check the function state with a [GetFunction](https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunction.html) call:

{{< command >}}
$ awslocal lambda wait function-active-v2 --function-name my-lambda
{{< / command >}}

Alternatively, `LAMBDA_SYNCHRONOUS_CREATE=1` forces synchronous (not recommended).
