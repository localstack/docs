---
title: "Lambda new Provider"
weight: 5
description: >
  Behavioral changes to become default with the new lambda provider
---

# Lambda Provider Behavioral Changes

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