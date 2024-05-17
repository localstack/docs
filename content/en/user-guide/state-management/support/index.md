---
title: Persistence Coverage for AWS Services
linkTitle: Persistence Coverage
description: Overview of the persistence coverage across the implemented AWS services
hide_readingtime: true
tags: ["Pro Image"]
---

## Persistence Coverage Overview

{{< localstack_persistence_table >}}

### Terminology

- **Persistence Test Suite**: tested by LocalStack's internal persistence test suite.
To test persistence, we use an approach similar to snapshot parity test:
we first record API responses from LocalStack, we then reset and restore the snapshotted state,
and finally verify that the same API responses matches with the initial ones.

