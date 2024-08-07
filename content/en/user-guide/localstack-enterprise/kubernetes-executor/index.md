---
title: "Kubernetes Executor"
weight: 4
description: >
  Configuring Kubernetes Executor for compute services in LocalStack Enterprise
tags: ["Enterprise plan"]
---

## Introduction

## ECS Kubernetes Executor

LocalStack Enterprise image allows you to run ECS tasks on Kubernetes.
The tasks are added to ELB load balancer target groups.
You can do so by setting the `ECS_TASK_EXECUTOR` environment variable to `kubernetes` in the LocalStack container.

In this guide, you will learn how to run ECS tasks on Kubernetes by using [`k3d](https://k3d.io/), a lightweight Kubernetes distribution.

### Create a new cluster

After installing `k3d`, you can run the following commands to create a Kubernetes cluster:

{{< command >}}
$ export NODE_PORT=31566
$ k3d cluster create ls-cluster -p "4566:$NODE_PORT" --wait --timeout 5m
{{< / command >}}

### Install LocalStack in the cluster

You can now install LocalStack in the Kubernetes cluster by using LocalStack's Helm chart.
The following command installs LocalStack with the `kubernetes` executor for ECS and sets the `LOCALSTACK_AUTH_TOKEN` environment variable:

{{< command >}}
$ helm upgrade --install localstack localstack/localstack \
               --set debug=true \
               --set image.repository=localstack/localstack-pro \
               --set image.tag=latest \
               --set readinessProbe.initialDelaySeconds=10 --set livenessProbe.initialDelaySeconds=10 \
               --set service.edgeService.nodePort=$NODE_PORT \
               --set "extraEnvVars[0].name=LOCALSTACK_AUTH_TOKEN" --set-string "extraEnvVars[0].value=${LOCALSTACK_AUTH_TOKEN}" \
               --set "extraEnvVars[1].name=ECS_TASK_EXECUTOR" --set-string "extraEnvVars[1].value=kubernetes" \
               --wait --timeout 5m
{{< / command >}}

After a successful installation, you can access the LocalStack running the following command:

{{< command >}}
$ curl http://localhost:4566/_localstack/health
{{< / command >}}

You can now create ECS tasks on Kubernetes by following the steps in the [ECS Getting Started]({{< ref "ecs#getting-started" >}}).
