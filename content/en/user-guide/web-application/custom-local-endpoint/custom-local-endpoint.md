---
title: "Custom local endpoint"
linkTitle: "Custom local endpoint"
weight: 105
description: >
  Connect the web app to instances running on custom local endpoints
aliases:
  - /localstack/custom-local-endpoint/
---

To connect the LocalStack web app to a LocalStack instance running on a custom local endpoint, configure the endpoint in the instance bookmarks on the [LocalStack Instances](https://app.localstack.cloud/instances) page.

## Connecting to a LocalStack instance on a different machine

To ensure that the Web user interface can connect with your running LocalStack instance, you would need to configure the endpoint URL so that the server's SSL certificate matches the hostname/IP address of the endpoint URL. This situation arises when users configure the endpoint URL to be something like `https://myhost:4566` or use an IP address like `https://1.2.3.4:4566`. Websites with an `https://...` URL can only request other endpoints using HTTPS (i.e., not on `http://`). Additionally, while requesting an HTTPS page, the SSL certificate must match the hostname (i.e., `localhost.localstack.cloud` in our case).

To navigate this, we recommend you create a local TCP proxy server. The proxy server could listen on `127.0.0.1:4566` and forward all requests to your target endpoint where the LocalStack instance is running. You could leave the configuration in the Web user interface to use the default value, `https://localhost.localstack.cloud:4566`. We recommend [simpleproxy](https://manpages.ubuntu.com/manpages/trusty/man1/simpleproxy.1.html) or [proxy.py](https://github.com/abhinavsingh/proxy.py) as a way to implement this.

An alternate workaround would be to re-point `localhost.localstack.cloud` to the IP address of your target machine by adding an entry to `/etc/hosts`. This is especially useful if you're accessing the LocalStack Web UI on a macOS/Linux-based machine.
