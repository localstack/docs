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

LocalStack Pro version provides a basic support for creating and deploying containerized apps using [Amazon ECS](https://aws.amazon.com/ecs). LocalStack offers the basic APIs locally, including creation of ECS task definitions, services, and tasks.

By default, the **ECS Fargate** launch type is assumed, i.e., the local Docker engine is used for deployment of applications, and there is no need to create and manage EC2 virtual machines to run the containers.

{{< alert title="Note">}}
More complex features like integration of application load balancers (ALBs) are currently not available. Nonetheless, they are being developed and will be available in the near future.
{{< /alert >}}

## Executing ECS tasks in Docker

Task instances are started in a local Docker engine, which needs to be accessible to the LocalStack container. The name pattern for task containers is `localstack_<family>_<revision>`, where `<family>` refers to the task family and `<revision>` refers to a task revision (for example, `localstack_nginx_1`).

You can use the configuration option `LAMBDA_DOCKER_NETWORK` to specify the network the ECS containers are started in.
If your ECS containers depend on LocalStack services, this should be the network the LocalStack container is located in.
For more information regarding the configuration of LocalStack, please check the [LocalStack configuration]({{< ref "configuration" >}}) section.

If you are running LocalStack through a `docker run` command, do not forget to enable the communication from the container to the Docker Engine API. You can provide the access by adding the following option `-v /var/run/docker.sock:/var/run/docker.sock`.

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
