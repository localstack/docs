---
title: "Stripe Extension"
linkTitle: "Stripe Extension"
weight: 2
description: >
  A LocalStack extension that provides a mocked version of Stripe as a service
---

The Stripe Extension provides a mocked version of Stripe as a service, via [`localstripe`](https://github.com/adrienverge/localstripe), a stateful Stripe server implementation in Python. The extension is purely for testing purposes, and is not intended for production use. The LocalStack Stripe Extension does not modify `localstripe` in any way.

{{<alert title="Note">}}
This Extension is experimental and still under active development. Please report any issues or feature requests on our [GitHub repository](https://github.com/localstack/localstack-extensions).
{{</alert>}}

## Installation

To install the Stripe Extension, run the following command:

{{< command >}}
$ localstack extensions install "git+https://github.com/localstack/localstack-extensions/#egg=localstack-extensions-stripe&subdirectory=stripe"
{{< / command >}}

## Usage

After installation, you can query Strip either through [`localhost:4566/stripe`](https://localhost:4566/stripe) or [`stripe.localhost.localstack.cloud:4566`](https://stripe.localhost.localstack.cloud:4566).

{{< command >}}
$ curl stripe.localhost.localstack.cloud:4566/v1/customers \
	-u sk_test_12345: \
	-d description="Customer data for Alice"
{{< / command >}}
