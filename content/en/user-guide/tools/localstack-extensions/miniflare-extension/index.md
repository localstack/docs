---
title: "Miniflare"
linkTitle: "Miniflare"
weight: 3
description: A LocalStack extension that makes Miniflare available in LocalStack!
---

This extension makes [Miniflare](https://miniflare.dev/), a simulator for developing and testing [Cloudflare Workers](https://workers.cloudflare.com/), available directly in LocalStack.

{{<alert title="Note">}}
This Extension is experimental and still under active development. Report any issues or feature requests on our [GitHub repository](https://github.com/localstack/localstack-extensions).
{{</alert>}}

## Installation

To install the Extension, run the following command:

{{< command >}}
$ localstack extensions install "git+https://github.com/localstack/localstack-extensions/#egg=localstack-extension-miniflare&subdirectory=miniflare"
{{< / command >}}

You can also install the Extension using the [Extensions Installer](https://app.localstack.cloud/extensions/remote?url=git+https://github.com/localstack/localstack-extensions/#egg=localstack-extension-miniflare&subdirectory=miniflare) which is available in the LocalStack Web Application.

## Usage

To publish the sample application to Miniflare running in LocalStack, we can use the `wrangler` CLI with the following environment variables for local dev mode:

{{< command >}}
$ export CLOUDFLARE_API_TOKEN=test
$ export CLOUDFLARE_API_BASE_URL=http://localhost:4566/miniflare
$ wrangler publish
{{< / command >}}

{{<alert title="Note">}}
If you encounter issues with this configuration, such as receiving `Fetch failed` error messages during `wrangler publish`, consider using this alternative API endpoint:

{{< command >}}
$ export CLOUDFLARE_API_BASE_URL=https://localhost.localstack.cloud:4566/miniflare
{{< / command >}}
{{</alert>}}

Once deployed, the Cloudflare worker can be easily invoked via `curl`:

{{< command >}}
$ curl http://hello.miniflare.localhost.localstack.cloud:4566/test
<disable-copy>
Hello World!
</disable-copy>
{{< / command >}}
