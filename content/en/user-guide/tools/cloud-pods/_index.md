---
title: "Cloud Pods"
weight: 10
description: >
  Cloud Pods provides a new way of collaborating in cloud application development workflows.
---

## Introduction

Cloud Pods are a mechanism that allows you to take a snapshot of the state in your current LocalStack instance, persist it to a storage backend, and easily share it with your team members.

![Persistence versus Cloud Pods](pods-persistence.png)

## Cloud Pods & Persistence

The [Persistence]({{< ref "persistence-mechanism" >}}) feature ensures that the service state persists across container restarts. In contrast, Cloud Pods provide more detailed control over your state.

Rather than just restoring a state during LocalStack restarts, Cloud Pods enable you to capture snapshots of your local instance using the `save` command and inject these snapshots into a running instance using the `load` command, all without needing to perform a full restart.

In addition, LocalStack provides a remote storage backend that can be used to store the state of your running application and share it with your team members.

## Getting started

You can interact with Cloud Pods via the LocalStack Web Application. To save and load the persistent state of Cloud Pods, you can use the [Cloud Pods command-line interface (CLI)]({{< ref "pods-cli" >}}).

![Cloud Pods Web UI](pods-ui.png)
