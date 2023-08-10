---
title: AWS Batch
linkTitle: Batch
categories: [" LocalStack Pro"]
description: >
  Get started with AWS Batch on LocalStack
---

## Introduction

LocalStack supports AWS Batch via the Community/Pro/Team offering, allowing you to use the AWS Batch APIs in your local environment.
The supported APIs are available on our API Coverage Page, which provides information on the extent of AWS Batch integration with LocalStack.

## Getting started

This guide is designed for users new to AWS Batch and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

Start your LocalStack container using your preferred method.
We will create and run an AWS Batch job by following these steps:

1. Create a service role for the compute environment
2. Create the compute environment
3. Create a job queue using the compute environment
4. Create a job definition
5. Submit a job to the job queue

### Create a service role

For LocalStack the service role just has to exist, however when [enforcing IAM policies]({{< ref "user-guide/aws/iam#enforcing-iam-policies" >}}) the policy must be a valid one.

{{< command >}}
$ awslocal iam create-role --role-name myrole  --assume-role-policy-document "{}"
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
{{< / command >}}

###  Create the compute environment

Using the role ARN above (`arn:aws:iam::000000000000:role/myrole`), create the compute environment

{{< command >}}
$ awslocal batch create-compute-environment \
    --compute-environment-name myenv \
    --type UNMANAGED \
    --service-role <role-arn>
{
    "computeEnvironmentName": "myenv",
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:000000000000:compute-environment/myenv"
}
{{< / command >}}

Note: even though we have specified an unmanaged compute environment, no compute resources need to be provisioned for this to work.
Your tasks run individually in new docker containers alongside the LocalStack container.

###  Create a job queue using the compute environment

First fetch the ARN of the compute environment you created in the previous step

{{< command >}}
$ awslocal batch describe-compute-environments --compute-environments myenv
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
{{< / command >}}

Then use the ARN to create the job queue using this compute environment

{{< command >}}
$ awslocal batch create-job-queue \
    --job-queue-name myqueue \
    --priority 1 \
    --compute-environment-order order=0,computeEnvironment=arn:aws:batch:us-east-1:000000000000:compute-environment/myenv \
    --state ENABLED
{
    "jobQueueName": "myqueue",
    "jobQueueArn": "arn:aws:batch:us-east-1:000000000000:job-queue/myqueue"
}
{{< / command >}}

###  Create a job definition

Now we need to define what happens during a job run, or at least what happens by default.

In this example we will run the `busybox` container from DockerHub, and run the command: `sleep 30` inside it.
We will override this command when we submit the job.

{{< command >}}
$ awslocal batch register-job-definition \
    --job-definition-name myjobdefn \
    --type container \
    --container-properties '{"image":"busybox","vcpus":1,"memory":128,"command":["sleep","30"]}'
{
    "jobDefinitionName": "myjobdefn",
    "jobDefinitionArn": "arn:aws:batch:us-east-1:000000000000:job-definition/myjobdefn:1",
    "revision": 1
}
{{< / command >}}

###  Submit a job to the job queue

Finally after all this setup, we can run a compute job.

This command runs a job on the queue that we set up previously, overriding the container command to run: `sh -c "sleep 5; pwd"`.
This command simulates work being done in the container.

{{< command >}}
$ awslocal batch submit-job \
    --job-name myjob \
    --job-queue myqueue \
    --job-definition myjobdefn \
    --container-overrides '{"command":["sh", "-c", "sleep 5; pwd"]}'
{
    "jobName": "myjob",
    "jobId": "23027eb6-cce0-4365-a412-36917a2dfd03"
}
{{< / command >}}

## Limitations 

As stated in the example above, creating a compute environment does not create EC2 or Fargrate instances.
Instead, it runs Batch jobs on the local Docker daemon, alongside LocalStack.
