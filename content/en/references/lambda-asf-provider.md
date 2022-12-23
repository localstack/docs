---
title: "Lambda Provider Behavioral Changes"
weight: 5
description: >
  Behavioral changes to become default with the new lambda provider
---

## Overview
The new lambda provider has some significant changes in its behavior.
This includes both its API parity, the execution and the container environments themselves.

## API
Parity with AWS has been increased across all Lambda API methods.
Another improvement is the stricter input validation, so expect more invalid input to fail.
One example of this, are Lambda roles. While don't have to actually exist, now have to be at least in a valid ARN format. Using arbitrary strings like `r1` is no longer supported.

## Execution
Lambda will now use the official AWS provided lambda images, instead of lambci images.
This leads to an increased parity with the AWS Lambda environments.
Another effect is that lambda now supports ARM containers, which will be executed depending on your host machine architecture (only available for runtimes based on amazon linux 2).

Lambda will now, by default, reuse containers for each lambda version.
This leads to significantly decreased execution times (from ~800 - 1000ms from the old `docker` executor to around 10ms for a simple echo lambda).
Initialization / global state of your lambdas will stay the same between invocations, as long as it is executed in the same environment.

Multiple concurrent executions will cause LocalStack to scale up and start additional environments for your function, to allow parallel executions.

Timeouts are now properly supported, and will, as in AWS, not kill the environment itself (filesystem stays the same) but only restart the internal infrastructure (your code), as do function errors.


## Changes in Hot Swapping
The magic key for hot reloading (or swapping) buckets has changed from `__local__` to `hot-reload`.
While the former is still supported in the old provider, the new one (`asf`) will only support the latter.
The configuration variable `BUCKET_MARKER_LOCAL` is still respected. Use this if you want to customize its name.
Since the new Lambda provider does not restart the containers after each invocation, even for hot reloading, the filesystem will stay the same.

Since the runtime inside the container will only be restarted after a change, any initialization you do, will only be reset for invocations after a change in the specified code folders.
This leads to faster invocation times if no changes have occurred.

Please keep in mind that any changes to the filesystem (for example in /tmp) will not be deleted if the function code changed.

{{< alert title="Keep in mind" color="warning">}}
It can take up to 700ms for the lambda to detect the changes you did in the code folder. Until that time has passed, any invocations will still be executed on the former code.

If using Docker Desktop, you might need to allow file sharing for your target folders: [https://docs.docker.com/desktop/settings/mac/#file-sharing](https://docs.docker.com/desktop/settings/mac/#file-sharing)
{{< /alert >}}