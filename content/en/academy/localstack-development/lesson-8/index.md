---
title: "Cloud pods - Team Collaboration"
linkTitle: "Cloud pods - Team Collaboration"
weight: 8
description: >
  In this video, we'll delve into Cloud pods, which allow you to snapshot the present state of your LocalStack instance and share it with your team. We'll load a Cloud Pod in our environment through the Web Application. This Cloud Pod will load the infrastructure and application onto our currently active LocalStack instance without manually deploying any resources.
length: 03:47
leadimage: cloud-pods.png
videoUrl: https://www.youtube.com/embed/ZJP2xfvwR_g?si=aG9TPQK7XtwlvFq5
type: lessons
url: "/academy/localstack-deployment/cloud-pods"
---

LocalStack is an ephemeral environment by nature.
It means that when you stop your LocalStack instance, all data is removed.
However, by using [Cloud Pods](https://docs.localstack.cloud/user-guide/state-management/cloud-pods/), you can preserve the LocalStack state.
Cloud Pods are snapshots of your LocalStack instance's state that can be saved, versioned, shared, and restored.

In this video, we'll follow the [quickstart](https://app.localstack.cloud/quickstart) to import Cloud Pods shared by our team member into our LocalStack instance and observe how this process supports local development and deployment of cloud applications.

Further reading:

- [State Management in LocalStack](https://docs.localstack.cloud/user-guide/state-management/)
- [LocalStack Cloud Pods](https://hashnode.localstack.cloud/localstack-cloud-pods)
- [LocalStack 101: Cloud Pods and Collaborative Work](https://youtu.be/InqTdSvxuag)
