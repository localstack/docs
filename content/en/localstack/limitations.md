---
title: "LocalStack Limitations"
weight: 50
description: >
  Known limitations of LocalStack and its services
---

This page describes known limitations of LocalStack and its services, either due to missing implementations or due to third-party integrations.

## Implementation Limitations

Limitations that exist due to missing features in LocalStack.

### DynamoDB

At the moment only a locally launched LocalStack instance can properly run the DynamoDB service.

### Lambda Functions

Only the local executor with locally launched LocalStack can be used together with JVM Lambda Functions.

## Integration Limitations

Limitations that may occur because of third party integrations behavior.

### CDK

#### Stacks with validated certificates

By default, stacks with validated certificates may not be deployed using the `local` lambda executor.
This originates from the way how CDK ensures the certificate is ready - it creates a single-file lambda function with a single dependency on `aws-sdk` which is usually preinstalled and available globally in lambda runtime.
When this lambda is executed locally from the `/tmp` folder, the package can not be discovered by Node due to the way how Node package resolution works.
