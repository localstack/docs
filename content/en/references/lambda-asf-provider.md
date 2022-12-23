---
title: "Lambda new Provider"
weight: 5
description: >
  Behavioral changes to become default with the new lambda provider
---

# Lambda Provider Behavioral Changes
The new lambda provider has some significant changes in its behavior.

## API
Increased parity across all Lambda API methods.
Another improvement is the better input validation, so expect more invalid input to fail.
This includes, but is not limited to Lambda roles, which, while not having to be existent, now have to be a correct IAM role arn. (Using arbitrary strings like "r1" is no longer supported).

## Execution
Lambda will now, by default, reuse containers for each lambda version.
This leads to significantly increased execution times (from ~800 - 1000ms from the old `docker` executor to around 10ms for a simple echo lambda).
This reuse leads to initialization / global state of your lambdas will stay the same between, as long as it is executed on the same environment.

Multiple concurrent executions will cause LocalStack to scale up to multiple environments, which leads to real parallel execution being available.

Timeouts are now properly supported, and will, as in AWS, not kill the environment itself (filesystem stays the same) but only restart the internal infrastructure (your code), as do function errors.


## Changes in Hot Swapping
The magic key for hot reloading (or swapping) buckets has changed from `__local__` to `hot-reload`.
While the former is still supported in the old provider, the new one will only support the latter.
The configuration variable `BUCKET_MARKER_LOCAL` is still respected.
Since the new Lambda provider does not restart the containers after each invocation, even for hot reloading, the filesystem will stay the same.

Also, the runtime inside the container will only be restarted after a change. 
So any initialization you do, will only be redone for invocations after a change in the specified code folders which leads to faster invocation times if nothing changed.
Please keep in mind that any changes to the filesystem (for example in /tmp) will not be deleted if the function code changed.

{{< alert title="Keep in mind" color="warning">}}
It can take up to 700ms for the lambda to represent the changes you did in the code folder. Until that time has passed, any invocations will still be executed on the former code.

If using Docker Desktop, you might need to allow file sharing for your target folders: [https://docs.docker.com/desktop/settings/mac/#file-sharing](https://docs.docker.com/desktop/settings/mac/#file-sharing)
{{< /alert >}}