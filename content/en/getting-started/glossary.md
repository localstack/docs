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

## LocalStack terms

| Term | Definition |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud Pods                        | Advanced persistence mechanism that allows to take a snapshot of the state of your LocalStack instance, as well as easily share the application state to enable collaborative debugging.                                                                                                        |
| Diagnostics Endpoint              | The endpoint on the running LocalStack Container that prints diagnostic data about LocalStack to assist with debugging and troubleshooting.                                                                                                                                                     |
| Edge Port                         | The HTTP port LocalStack listens on for any type of request (e.g. from AWS SDKs). The default port is 4566.                                                                                                                                                                                     |
| External Service Ports            | The ports reserved for infrastructure that is started as part of a managed service like database server, Redis cluster, and are exposed through the LocalStack Container.                                                                                                                       |
| Lambda Code Mounting/Hot Swapping | The ability to make changes in Lambda handler files, and have them immediately reflected on each invocation of a Lambda function, without the need to redeploy the Lambda function.                                                                                                             |
| LocalStack API Key                | An API key that can be configured via the LOCALSTACK_API_KEY environment variable, to enable advanced features in your LocalStack instance. We distinguish between individual developer keys, as well as CI keys for continuous integration environments (e.g., Github Actions, CircleCI, etc). |
| LocalStack Container              | The Docker/Podman container or Kubernetes pod running LocalStack.                                                                                                                                                                                                                               |
| LocalStack Extensions             | Extend and customize LocalStack using pluggable Python distributions to run applications alongside the main process in the LocalStack Docker container.                                                                                                                                         |
| LocalStack Platform               | The LocalStack Web Application for licensed users to use advanced features, such as Stack Insights, CI Analytics, Resource Browser, and Team Collaboration.                                                                                                                                     |
| Stack Insights                    | Web Application feature to allow LocalStack users to report AWS API usage telemetry of LocalStack runs to their LocalStack account via the central dashboard.                                                                                                                                   |

## Developer terms

| Term | Definition |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LocalStack Package Manager | A module in LocalStack CLI that provides an interface to trigger installations for downloading packages that define a specific kind of software.            |
| LocalStack Hooks           | Hooks are functions exposed as plugins that are collected and executed at specific points during the LocalStack lifecycle.                                  |
| AWS Server Framework (ASF) | AWS Server Framework (ASF) is a server-side implementation of AWS that generates server-side stubs for services and all their supported operations.         |
| LocalStack Plugins         | LocalStack Plugins, provided by Plux, is a dynamic code loading framework to load service providers, hooks, and extensions.                                 |
| LocalStack Configuration   | LocalStack configuration is a set of well-known environment variables which is passed to the running LocalStack Container.                                  |
| LocalStack Runtime         | LocalStack Runtime is a collective term for all the components necessary to run LocalStack server application, like Gateway, scheduled worker threads, etc. |
