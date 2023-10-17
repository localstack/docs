---
title: "Cloud Pods"
weight: 10
description: >
  Cloud Pods provides a new way of collaborating in cloud application development workflows.
---

## Introduction

Cloud pods are persistent state snapshots of your LocalStack instance that can easily be stored, versioned, shared, and restored. Cloud Pods can be used for various purposes, such as:

- Sharing state snapshots amongst your team to foster collaborative debugging.
- Pre-seeding CI environments to bootstrap your testing pipelines automatically.
- Preparing reproducible application development & testing environments locally.

You can save and load the persistent state of Cloud Pods, you can use the [Cloud Pods command-line interface (CLI)]({{< ref "pods-cli" >}}). LocalStack provides a remote storage backend that can be used to store the state of your running application and share it with your team members. You can interact with the Cloud Pods over the storage backend via the LocalStack Web Application.

These Cloud Pods are securely stored within an AWS storage backend, where each user or organization is allocated a dedicated and isolated S3 bucket. The LocalStack Cloud Pods CLI utilizes secure S3 presigned URLs to directly interface with the S3 bucket, bypassing the need to transmit the state files through LocalStack Platform APIs.

<img src="pods-ui.png" alt="Cloud Pods Web UI" title="Cloud Pods Web UI" width="800" />

## Cloud Pods & Persistence

[Persistence]({{< ref "persistence-mechanism" >}}) ensures that the service state persists across container restarts. You can enable persistence via a LocalStack config flag `PERSISTENCE=1` to restore your local resources, in case you’re stopping and re-starting the LocalStack instance on the same machine.

In contrast, Cloud Pods provide more detailed control over your state. Rather than just restoring a state during LocalStack restarts, Cloud Pods enable you to capture snapshots of your local instance using the `save` command and inject these snapshots into a running instance using the `load` command, all without needing to perform a full restart.

<img src="cloud-pods-persistence.png" alt="Cloud Pods v/s Persistence" title="Cloud Pods v/s Persistence" width="800" />
