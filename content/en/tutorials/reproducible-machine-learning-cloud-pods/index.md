---
title: "Creating reproducible machine learning applications using Cloud Pods for persistent state snapshots"
linkTitle: "Creating reproducible machine learning applications using Cloud Pods for persistent state snapshots"
weight: 5
description: >
  With LocalStack Cloud Pods, you can create persistent state snapshots to enable next-generation state management and team collaboration features for your local development environment. Learn how you can create reproducible machine learning applications & samples using Cloud Pods to take a snapshot of your LocalStack state at any point in time.
type: tutorials
---

LocalStack Cloud Pods enable you to create persistent state snapshots of your LocalStack instance, which can then be versioned, shared, and restored. It allows next-generation state management and team collaboration for your local cloud development environment, which you can utilize to create persistent shareable cloud sandboxes. Cloud Pods works similarly to the `git` version control system and uses the same concepts and commands to save, merge, and restore snapshots of your LocalStack state. You can always tear down your LocalStack instance and restore it from a snapshot at any point in time.

Cloud Pods is supported by both [LocalStack Pro](https://app.localstack.cloud/) and [LocalStack Community](). Using Community Cloud Pods, you get a limited experience saving and loading your LocalStack state in a Cloud Pod, only with the AWS services emulated in the Community Edition. With LocalStack Pro, you can utilize an extended CLI that allows you to inspect your Cloud Pods, version them using tags similar to `git`, and push them to LocalStack Pod's platform.

In this tutorial, we will use [LocalStack Pro]() to train a simple machine-learning model that recognizes handwritten digits on an image. We will use Cloud Pods to create a reproducible sample by using an S3 bucket to host our training data, a Lambda function to train the model and a Lambda layer that contains the dependencies for our training code. We will then create a Cloud Pod to save the state of our LocalStack instance and restore it from the Cloud Pod to share it with our team.