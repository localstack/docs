---
title: "Glossary"
linkTitle: "Glossary"
weight: 7
description: >
  This page defines terms that you will encounter throughout the LocalStack documentation.
cascade:
  type: docs
hide_readingtime: true
---

This page defines LocalStack terminologies that you will encounter throughout the documentation.

## LocalStack terms

| Cloud Pods                        | Advanced persistence mechanism that allows to take a snapshot of the state of your LocalStack instance, as well as easily share the application state to enable collaborative debugging.                                                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Edge Port                         | The HTTP port LocalStack listens on for any type of request (e.g. from AWS SDKs). The default port is 4566.                                                                                                                                                                                       |
| External service ports            | The ports reserved for infrastructure that is started as part of a managed service like database server, Redis cluster, and are exposed through the LocalStack container.                                                                                                                         |
| Lambda Code Mounting/Hot Swapping | The ability to make changes in Lambda handler files, and have them immediately reflected on each invocation of a Lambda function, without the need to redeploy the Lambda function.                                                                                                               |
| LocalStack API Key                | An API key that can be configured via the `LOCALSTACK_API_KEY` environment variable, to enable advanced features in your LocalStack instance. We distinguish between individual developer keys, as well as CI keys for continuous integration environments (e.g., Github Actions, CircleCI, etc). |
| LocalStack container              | The Docker/Podman container or Kubernetes pod running LocalStack.                                                                                                                                                                                                                                 |