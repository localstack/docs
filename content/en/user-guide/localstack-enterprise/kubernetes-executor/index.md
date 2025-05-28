---
title: "Kubernetes Executor"
weight: 5
description: >
  Configuring Kubernetes Executor for compute services in LocalStack Enterprise
tags: ["Ultimate"]
---

## Introduction

LocalStack Enterprise provides a Kubernetes executor for various emulated services.
It allows you to run these services as Kubernetes pods in your Kubernetes clusters.
By default, LocalStack uses the `docker` backend for these services.
You can use either service-specific configuration variables or the generic  `CONTAINER_RUNTIME`  variable set to  `kubernetes`  to enable the Kubernetes executor.

## EC2 Kubernetes Executor

The LocalStack Enterprise image allows you to run EC2 instances on Kubernetes.
You can do so by setting the `EC2_VM_MANAGER` environment variable to `kubernetes` in the LocalStack container.
Each EC2 instance in the Kubernetes VM manager is backed by a Pod.

The following operations are supported:

| Operation            | Notes                                  |
| :------------------- | :------------------------------------- |
| `DescribeInstances`  | Returns all EC2 instances              |
| `RunInstances`       | Defines and starts an EC2 instance     |
| `StartInstances`     | Starts an already defined EC2 instance |
| `StopInstances`      | Stops a running EC2 instance           |
| `TerminateInstances` | Stops and undefines a EC2 instance     |

The current implementation is in preview and does not support volumes, custom AMIs, or networking features available in other VM managers.

## ECS Kubernetes Executor

The LocalStack Enterprise image allows you to run ECS tasks on Kubernetes.
The tasks are added to ELB load balancer target groups.
You can do so by setting the `ECS_TASK_EXECUTOR` environment variable to `kubernetes` in the LocalStack container.

## Lambda Kubernetes Executor

The LocalStack Enterprise image allows you to execute Lambda functions as Kubernetes pods.
You can do so by setting `LAMBDA_RUNTIME_EXECUTOR` ( or `lambda.executor` when using the Helm configuration) to `kubernetes`.
For more information, see the [Helm Chart configuration](https://github.com/localstack/helm-charts/blob/ce47b1590605901650ab788556bc871efbd78b8d/charts/localstack/values.yaml#L178-L208).

- Kubernetes Lambda Executor in LocalStack scales Lambda execution by spawning new environments (running in pods) during concurrent invocations.
  Inactive environments shut down after 10 minutes (configurable via `LAMBDA_KEEPALIVE_MS`).
- Executor schedules multiple Lambda functions according to Kubernetes cluster defaults without specifying node affinity.
  Users can assign labels to lambda pods using the `LAMBDA_K8S_LABELS` variable (e.g., `LAMBDA_K8S_LABELS=key=value,key2=value2`).
- Timeout configurations similar to AWS are enforced using the `Timeout` function parameter.
  No intrinsic limits on the number of Lambdas; default limit on concurrent executions is 1000 (`LAMBDA_LIMITS_CONCURRENT_EXECUTIONS`).
- Custom DNS configuration for Lambda on Kubernetes can be set through the `LAMBDA_DOCKER_DNS` configuration variable.
- Users can customize Lambda runtime behavior by building custom images, pushing them to their registry, and specifying these images using the `LAMBDA_RUNTIME_IMAGE_MAPPING` configuration variable.
- Lambda on Kubernetes supports Warm Start and Persistence.
  Persistence must be configured for the LocalStack pod.
  The `/var/lib/localstack` directory should be persisted over LocalStack runs, typically in a volume.

Lambda hot reloading & remote debugging are not supported in the Kubernetes executor as the bind mounting into pods cannot be done at runtime.

## Other services

You can run the following services on Kubernetes clusters using the LocalStack Enterprise image:

- [DocumentDB](https://docs.localstack.cloud/user-guide/aws/docdb/)
- [MWAA](https://docs.localstack.cloud/user-guide/aws/docdb/)
- [RDS](https://docs.localstack.cloud/user-guide/aws/rds/)  ([MySQL](https://docs.localstack.cloud/user-guide/aws/rds/#mysql-engine)  &  [MSSQL](https://docs.localstack.cloud/user-guide/aws/rds/#microsoft-sql-server-engine))

To use Kubernetes as the runtime backend, set the `CONTAINER_RUNTIME` configuration variable to `kubernetes`.
Note that there are no service-specific configuration variables for these services.
