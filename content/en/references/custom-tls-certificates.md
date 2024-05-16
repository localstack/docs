---
title: Custom TLS certificates
weight: 50
tags:
- ssl
description: >
  Using custom TLS certificates with LocalStack
---

## Background

LocalStack sometimes performs on-demand fetching of resources from the public internet.
This requires that LocalStack is able to access public URLs.
If there is a proxy server in your network that uses a non-standard TLS certificate, LocalStack will not be able to download any files on demand.
You may see errors in the logs relating to TLS such as "unable to get local issuer certificate".

There are three options when running LocalStack:

1. [creating a custom Docker image]({{< ref "#creating-a-custom-docker-image" >}}),
2. [using init hooks]({{< ref "#custom-ssl-certificates-with-init-hooks" >}}) or
3. [when running in host mode]({{< ref "#custom-ssl-certificates-with-host-mode" >}}).

They all can be summarised as:

1. get your proxy's custom certificate into the system certificate store, and
2. configure [`requests`](https://pypi.python.org/pypi/requests) to use the custom certificate,
3. configure [`curl`](https://curl.se/) to use the custom certificate, and 
4. configure [`node.js`](https://nodejs.org/) to use the custom certificate.

## Creating a custom docker image

If you run LocalStack in a docker container (which includes using [the CLI]({{< ref "/getting-started#localstack-cli" >}}), [docker]({{< ref "/getting-started/#docker" >}}), [docker-compose]({{< ref "/getting-started/#docker-compose" >}}), [cockpit]({{< ref "/getting-started/#localstack-cockpit" >}}) or [helm]({{< ref "/getting-started/#helm" >}})), to include a custom TLS root certificate a new docker image should be created.

Create a `Dockerfile` containing the following commands:

```docker
FROM localstack/localstack:latest
# or if using the pro image:
FROM localstack/localstack-pro:latest

COPY <your custom certificate.crt> /usr/local/share/ca-certificates/cert-bundle.crt
RUN update-ca-certificates
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt
```

and build the image:

{{< command >}}
$ docker build -t <image name> .
{{< / command >}}

{{< callout "tip" >}}
Certificate files must end in `.crt` to be included in the system certificate store.
If your certificate file ends with `.pem`, you can rename it to end in `.crt`. 
{{< /callout >}}

### Starting LocalStack with the custom image

LocalStack now needs to be configured to use this custom image. The workflow is different depending on how you start localstack.

{{< tabpane lang="bash">}}
{{< tab header="CLI" lang="bash" >}}
IMAGE_NAME=<image name> localstack start
{{< /tab >}}
{{< tab header="Docker" lang="bash" >}}
docker run <docker arguments> <image name>
{{< /tab >}}
{{< tab header="docker-compose.yml" lang="yml" >}}
services:
  localstack:
    image: <image name>
    # the rest of your configuration
{{< /tab >}}
{{< / tabpane >}}

## Custom TLS certificates with init hooks

It is recommended to create a `boot` init hook. Create a directory on your local system that includes

* the certificate you wish to copy, and
* the following shell script:

```bash
#!/bin/bash

set -euo pipefail

cp /etc/localstack/init/boot.d/<your certificate file>.crt /usr/local/share/ca-certificates
update-ca-certificates
```

Then run LocalStack with the environment variables

* `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`, and
* `CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`, and
* `NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt`

and follow the instructions fn the [init hooks documentation]({{< ref "init-hooks" >}}) for configuring LocalStack to use the hook directory as a `boot` hook.

## Custom TLS certificates with host mode

### Linux

On linux the custom certificate should be added to your `ca-certificates` bundle. For example on Debian based systems (as root):

{{< command >}}
# cp <your custom certificate.crt> /usr/local/share/ca-certificates
# update-ca-certificates
{{< / command >}}

Then run LocalStack with the environment variables `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`, and `NODE_EXTRA_CA_CERTS``:

{{< command >}}
$ NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt \
  CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
  REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
  localstack start --host
{{< / command >}}

### macOS

On macOS the custom certificate should be added to your keychain. See [this Apple support article](https://support.apple.com/en-gb/guide/keychain-access/kyca2431/mac) for more information.

Then run LocalStack with the environment variables `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE`, and `NODE_EXTRA_CA_CERTS``:

{{< command >}}
$ NODE_EXTRA_CA_CERTS=/etc/ssl/certs/ca-certificates.crt \
  CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
  REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
  localstack start --host
{{< / command >}}

### Windows

Currently host mode does not work with Windows. If you are using WSL2 you should follow the [Linux]({{< ref "#linux" >}}) steps above.
