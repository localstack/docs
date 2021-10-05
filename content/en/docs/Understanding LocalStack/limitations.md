---
title: "LocalStack Limitations"
weight: 50
description: >
  Known limitations of LocalStack and its services
---

## Covered Topics

* [Implementation Limitations](#implementation-limitations)
* [Runtime Environment Limitations](#runtime-environment-limitations)
* [Integration Limitations](#integration-limitations)

## Implementation Limitations

Limitations that exist due to missing features in LocalStack

## Runtime Environment Limitations

OS-specific and other runtime environment limitations

* [ARM64 (Including Apple M1 chip)](#arm64-including-apple-m1-chip)

### ARM64 (Including Apple M1 chip)

#### DynamoDB

At the moment only locally launched LocalStack can properly run DynamoDB service.

#### Lambda Functions

Only local executor with locally launched LocalStack can be used together with JVM Lambda Functions.

## Integration Limitations

Limitations that may occur because of third party integrations behavior

* [CDK](#cdk)

### CDK

#### Stacks with validated certificates

By default, stacks with validated certificates may not be deployed using the `local` lambda executor. This originates from the way how CDK ensures the certificate is ready - it creates a single-file lambda function with a single dependency on `aws-sdk` which is usually preinstalled and available globally in lambda runtime. When this lambda is executed locally from the `/tmp` folder, the package can not be discovered by Node due to the way how Node package resolution works.
