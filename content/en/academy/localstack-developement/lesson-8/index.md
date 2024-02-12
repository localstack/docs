---
title: "Cloud pods - Team Collaboration"
linkTitle: "Cloud pods - Team Collaboration"
weight: 8
description: >
  In this video we will discuss about Cloud pods, extending the discussion from module - 1. By default, LocalStack is an ephemeral environment, meaning that, once you terminate your LocalStack instance, all state will be discarded. Cloud Pods are a mechanism that allows you to take a snapshot of the current state of your LocalStack instance and easily share it with your team members. Furthermore we will pick a `QuickStart` guide to cloudpod and follow the on-screen tutorial to load a cloudpod in our environment using the web app. This cloudpod would 'load' the infrastructure and the deployed application onto our running localstack instance. The cloudpod contains the same application we deployed in this module.
length: 03:47
leadimage: cloud-pods.png
videoUrl: https://www.youtube.com/embed/ZJP2xfvwR_g?si=aG9TPQK7XtwlvFq5
type: lessons
url: "/academy/localstack-deployment/cloud-pods"
---

By default, LocalStack operates as an ephemeral environment, meaning that once you terminate your LocalStack instance, all state will be discarded. However, with Cloud Pods, you can save LocalStack instances. Cloud pods are persistent state snapshots of your LocalStack instance that can easily be stored, versioned, shared, and restored. Cloud Pods can be used for various purposes, such as:

- Save and manage snapshots of active LocalStack instances.
- Share state snapshots with your team to debug collectively.
- Automate your testing pipelines by pre-seeding CI environments.
- Create reproducible development and testing environments locally.

In this video we will be using quickstart guide, which you can access at [app.localstack.cloud/quickstart](https://app.localstack.cloud/quickstart). We will load cloudpods shared by our team member in our localstack instance. We will see how this helps us develop and deploy cloud applications locally.

Further reading:

- [State Management](https://docs.localstack.cloud/user-guide/state-management/)
- [LocalStack Cloud Pods Docs](https://docs.localstack.cloud/user-guide/state-management/cloud-pods/)
- [Persistence](https://docs.localstack.cloud/user-guide/state-management/persistence/)
- [LocalStack Cloud Pods CLI](https://docs.localstack.cloud/user-guide/state-management/pods-cli/)
- [Cloud Pods Launchpad ](https://docs.localstack.cloud/user-guide/state-management/launchpad/)