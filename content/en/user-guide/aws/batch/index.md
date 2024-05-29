---
title: Batch
linkTitle: Batch
description: Get started with Batch on LocalStack
tags: ["Pro image"]
---

## Introduction

Batch is a cloud-based service provided by Amazon Web Services (AWS) that simplifies the process of running batch computing workloads on the AWS cloud infrastructure. Batch allows you to efficiently process large volumes of data and run batch jobs without the need to manage and provision underlying compute resources.

LocalStack allows you to use the Batch APIs to automate and scale computational tasks in your local environment while handling batch workloads. The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_batch/), which provides information on the extent of Batch integration with LocalStack.

## Getting started

This guide is designed for users new to AWS Batch and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how you create and run a Batch job by following these steps:

1. Creating a service role for the compute environment.
2. Creating the compute environment.
3. Creating a job queue using the compute environment.
4. Creating a job definition.
5. Submitting a job to the job queue.

### Create a service role

You can create a role using the [`CreateRole`](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) API. For LocalStack, the service role simply needs to exist. However, when [enforcing IAM policies]({{< ref "user-guide/aws/iam#enforcing-iam-policies" >}}), it is necessary that the policy is valid.

Run the following command to create a role with an empty policy document:

{{< command >}}
$ awslocal iam create-role \
    --role-name myrole  \
    --assume-role-policy-document "{}"
{{< / command >}}

You should see the following output:

```bash
{
    "Role": {
        "Path": "/",
        "RoleName": "myrole",
        "RoleId": "AROAQAAAAAAAMKIDGTHVC",
        "Arn": "arn:aws:iam::000000000000:role/myrole",
        "CreateDate": "2023-08-10T20:52:06.196000Z",
        "AssumeRolePolicyDocument": {}
    }
}
```

### Create the compute environment

You can use the [`CreateComputeEnvironment`](https://docs.aws.amazon.com/cli/latest/reference/batch/create-compute-environment.html) API to create a compute environment. Run the following command using the role ARN above (`arn:aws:iam::000000000000:role/myrole`), to create the compute environment:

{{< command >}}
$ awslocal batch create-compute-environment \
    --compute-environment-name myenv \
    --type UNMANAGED \
    --service-role <role-arn>
{{< / command >}}

You should see the following output:

```bash
{
    "computeEnvironmentName": "myenv",
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:000000000000:compute-environment/myenv"
}
```

{{< callout >}}
While an unmanaged compute environment has been specified, there is no need to provision any compute resources for this setup to function. Your tasks will run independently in new Docker containers, alongside the LocalStack container.
{{< /callout >}}

### Create a job queue

You can fetch the ARN using the [`DescribeComputeEnvironments`](https://docs.aws.amazon.com/cli/latest/reference/batch/describe-compute-environments.html) API. Run the following command to fetch the ARN of the compute environment:

{{< command >}}
$ awslocal batch describe-compute-environments --compute-environments myenv
{{< / command >}}

You should see the following output:

```bash
{
    "computeEnvironments": [
        {
            "computeEnvironmentName": "myenv",
            "computeEnvironmentArn": "arn:aws:batch:us-east-1:000000000000:compute-environment/myenv",
            "ecsClusterArn": "arn:aws:ecs:us-east-1:000000000000:cluster/OnDemand_Batch_f2faa82c-8c31-466d-ab22-579925d810ac",
            "type": "UNMANAGED",
            "status": "VALID",
            "statusReason": "Compute environment is available",
            "serviceRole": "arn:aws:iam::000000000000:role/myrole"
        }
    ]
}
```

You can use the ARN to create the job queue using [`CreateJobQueue`](https://docs.aws.amazon.com/cli/latest/reference/batch/create-job-queue.html) API. Run the following command to create the job queue:

{{< command >}}
$ awslocal batch create-job-queue \
    --job-queue-name myqueue \
    --priority 1 \
    --compute-environment-order order=0,computeEnvironment=arn:aws:batch:us-east-1:000000000000:compute-environment/myenv \
    --state ENABLED
{{< / command >}}

You should see the following output:

```bash
{
    "jobQueueName": "myqueue",
    "jobQueueArn": "arn:aws:batch:us-east-1:000000000000:job-queue/myqueue"
}
```

### Create a job definition

Now, you can define what occurs during a job run, or at least what transpires by default. In this example, you can execute the `busybox` container from DockerHub and initiate the command: `sleep 30` within it. It's important to note that you can override this command when submitting the job.

Run the following command to create the job definition using the [`RegisterJobDefinition`](https://docs.aws.amazon.com/cli/latest/reference/batch/register-job-definition.html) API:

{{< command >}}
$ awslocal batch register-job-definition \
    --job-definition-name myjobdefn \
    --type container \
    --container-properties '{"image":"busybox","vcpus":1,"memory":128,"command":["sleep","30"]}'
{{< / command >}}

You should see the following output:

```bash
{
    "jobDefinitionName": "myjobdefn",
    "jobDefinitionArn": "arn:aws:batch:us-east-1:000000000000:job-definition/myjobdefn:1",
    "revision": 1
}
```

### Submit a job to the job queue

You can now run a compute job. This command runs a job on the queue that you have set up previously, overriding the container command to run: `sh -c "sleep 5; pwd"`. This command simulates work being done in the container. 

Run the following command to submit a job to the job queue using the [`SubmitJob`](https://docs.aws.amazon.com/cli/latest/reference/batch/submit-job.html) API:

{{< command >}}
$ awslocal batch submit-job \
    --job-name myjob \
    --job-queue myqueue \
    --job-definition myjobdefn \
    --container-overrides '{"command":["sh", "-c", "sleep 5; pwd"]}'
{{< / command >}}

You should see the following output:

```bash
{
    "jobName": "myjob",
    "jobId": "23027eb6-cce0-4365-a412-36917a2dfd03"
}
```

## Current Limitations 

As mentioned in the example above, the creation of a compute environment does not entail the provisioning of EC2 or Fargate instances. Rather, it executes Batch jobs on the local Docker daemon, operating alongside LocalStack.
