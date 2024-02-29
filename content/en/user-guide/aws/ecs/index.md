---
title: "Elastic Container Service (ECS)"
linkTitle: "Elastic Container Service (ECS)"
categories: ["LocalStack Pro"]
description: >
  Get started with Elastic Container Service (ECS) on LocalStack
aliases:
  - /aws/elastic-container-service/
  - /user-guide/aws/elastic-container-service/
---

## Introduction

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service provided by Amazon Web Services (AWS).
It allows you to run, stop, and manage Docker containers on a cluster.
ECS eliminates the need for you to install, operate, and scale your own cluster management infrastructure.

## Getting Started

This guide is designed for users new to ECS and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an ECS serivce using the AWS CLI

### Create a cluster

{{< alert title="Note">}}
By default, the **ECS Fargate** launch type is assumed, i.e., the local Docker engine is used for deployment of applications, and there is no need to create and manage EC2 virtual machines to run the containers.
{{< /alert >}}

ECS tasks and services run on a Cluster.
Execute the following command to create an ECS cluster named `mycluster`:

{{< command >}}
$ awslocal ecs create-cluster --cluster-name mycluster
<disable-copy>
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:us-east-1:000000000000:cluster/mycluster",
        "clusterName": "mycluster",
        "status": "ACTIVE",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ]
    }
}
</disable-copy>
{{< / command >}}

### Create a task definition

Containers within tasks are defined by a task definition that is managed outside of the context of a cluster.
To create a task definition that runs an `ubuntu` container forever (by running `sleep infinity` on startup), create the following file as `task_definition.json`:

```json
{
  "containerDefinitions": [
    {
      "name": "server",
      "image": "ubuntu",
      "cpu": 10,
      "memory": 10,
      "command": [
        "sleep",
        "infinity"
      ],
      "essential": true
    }
  ],
  "family": "myfamily"
}
```

and then run the following command:

{{< command >}}
$ awslocal ecs register-task-definition --cli-input-json file://task_definition.json
<disable-copy>
{
    "taskDefinition": {
        "taskDefinitionArn": "arn:aws:ecs:us-east-1:000000000000:task-definition/myfamily:1",
        "containerDefinitions": [
            {
                "name": "server",
                "image": "ubuntu",
                "cpu": 10,
                "memory": 10,
                "portMappings": [],
                "essential": true,
                "command": [
                    "sleep",
                    "infinity"
                ],
                "environment": [],
                "mountPoints": [],
                "volumesFrom": []
            }
        ],
        "family": "myfamily",
        "networkMode": "bridge",
        "revision": 1,
        "volumes": [],
        "status": "ACTIVE",
        "placementConstraints": [],
        "compatibilities": [
            "EXTERNAL",
            "EC2"
        ],
        "registeredAt": 1709242097.870379
    }
}
</disable-copy>
{{< / command >}}

Task definitions are immutable, and are identified by their `family` field, and calling `register-task-definition` again with the same `family` value creates a new _version_ of a task definition.

### Launch a service

Finally we launch an ECS service using the task definition above.
This will create a number of containers in replica mode meaning they are distributed over the nodes of the cluster, or with the case of Fargate, over availability zones within the region of the cluster. To create a service, execute the following command:


{{< command >}}
$ awslocal ecs create-service --service-name myservice --cluster mycluster --task-definition myfamily --desired-count 1
<disable-copy>
{
    "service": {
        "serviceArn": "arn:aws:ecs:us-east-1:000000000000:service/mycluster/myservice",
        "serviceName": "myservice",
        "clusterArn": "arn:aws:ecs:us-east-1:000000000000:cluster/mycluster",
        "loadBalancers": [],
        "serviceRegistries": [],
        "status": "ACTIVE",
        "desiredCount": 1,
        "runningCount": 1,
        "pendingCount": 0,
        "launchType": "EC2",
        "taskDefinition": "arn:aws:ecs:us-east-1:000000000000:task-definition/myfamily:1",
        "deploymentConfiguration": {
            "deploymentCircuitBreaker": {
                "enable": false,
                "rollback": false
            },
            "maximumPercent": 200,
            "minimumHealthyPercent": 100
        },
        "deployments": [
            {
                "id": "ecs-svc/49976591540684372",
                "status": "PRIMARY",
                "taskDefinition": "arn:aws:ecs:us-east-1:000000000000:task-definition/myfamily:1",
                "desiredCount": 1,
                "pendingCount": 0,
                "runningCount": 1,
                "failedTasks": 0,
                "createdAt": 1709242525.05109,
                "updatedAt": 1709242525.051093,
                "launchType": "EC2",
                "rolloutState": "IN_PROGRESS",
                "rolloutStateReason": "ECS deployment ecs-svc/49976591540684372 in progress."
            }
        ],
        "events": [],
        "createdAt": 1709242525.051096,
        "placementStrategy": [],
        "schedulingStrategy": "REPLICA",
        "createdBy": "arn:aws:iam::000000000000:user/test"
    }
}
</disable-copy>
{{< / command >}}

You should see a new docker container has been created, using the `ubuntu:latest` image, and running the command `sleep infinity`.

```
$ docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED              STATUS                    PORTS                                                                                                                                        NAMES
a0dfa7a2cdd5   ubuntu                      "sleep infinity"         About a minute ago   Up About a minute                                                                                                                                                      ls-ecs-mycluster-a2fda12e-6a02-4eaa-a977-ded467a0227d-0-8ba33dc8
66fcc01adb99   localstack/localstack-pro   "docker-entrypoint.sh"   18 minutes ago       Up 18 minutes (healthy)   127.0.0.1:53->53/tcp, 127.0.0.1:443->443/tcp, 127.0.0.1:4510-4560->4510-4560/tcp, 127.0.0.1:4566->4566/tcp, 127.0.0.1:53->53/udp, 5678/tcp   localstack-main
```

## LocalStack ECS behavior

You can use the configuration option `MAIN_DOCKER_NETWORK` to specify the network the ECS containers are started in.
Otherwise, your ECS containers will be created in the same Docker network that LocalStack is in.
If your ECS containers depend on LocalStack services, your ECS task network should be the same as the LocalStack container network.

If you are running LocalStack through a `docker run` command, do not forget to enable the communication from the container to the Docker Engine API.
You can provide the access by adding the following option `-v /var/run/docker.sock:/var/run/docker.sock`.

For more information regarding the configuration of LocalStack, please check the [LocalStack configuration]({{< ref "configuration" >}}) section.

## Remote debugging

To enable a remote debugging port for your ECS tasks, set the environment variable `ECS_DOCKER_FLAGS="-p 0:<debugger port>"` to expose your debugger on a random port on your host.
You can then use this port to remote attach your debugger.
Or if you are working with a single container, you can set `ECS_DOCKER_FLAGS="-p <debugger port>:<debugger port>"` to expose the debugger port to your host system.

<!--

## Executing ECS tasks in Docker

Task instances are started in a local Docker engine, which needs to be accessible to the LocalStack container. The name pattern for task containers is `localstack_<family>_<revision>`, where `<family>` refers to the task family and `<revision>` refers to a task revision (for example, `localstack_nginx_1`).

You can use the configuration option `LAMBDA_DOCKER_NETWORK` to specify the network the ECS containers are started in.
If your ECS containers depend on LocalStack services, this should be the network the LocalStack container is located in.
For more information regarding the configuration of LocalStack, please check the [LocalStack configuration]({{< ref "configuration" >}}) section.
If you are running LocalStack through a `docker run` command, do not forget to enable the communication from the container to the Docker Engine API. You can provide the access by adding the following option `-v /var/run/docker.sock:/var/run/docker.sock`.
-->

## Mounting local directories for ECS tasks

In some cases, it can be useful to mount code from the host filesystem into the ECS container. For example, to enable a quick debugging loop where you can test changes without having to build and redeploy the task's Docker image each time - similar to the [Lambda Hot Reloading]({{< ref "hot-reloading" >}}) feature in LocalStack.

In order to leverage code mounting, we can use the ECS bind mounts feature, which is covered in the [AWS Bind mounts documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bind-mounts.html).

For example, the Python sample code below registers a task definition, mounting a host path `/host/path` into the container under `/container/path`:

```bash
ecs_client = boto3.client("ecs", endpoint_url="http://localhost:4566")
...
ecs_client.register_task_definition(
    family="...",
    containerDefinitions=[
        {
            "name": "...",
            "image": "alpine",
            "command": ["..."],
            "mountPoints": [
                {"containerPath": "/container/path", "sourceVolume": "test-volume"}
            ],
        }
    ],
    volumes=[{"host": {"sourcePath": "/host/path"}, "name": "test-volume"}],
)
```
