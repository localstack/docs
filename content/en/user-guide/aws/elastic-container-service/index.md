---
title: "Elastic Container Service (ECS)"
linkTitle: "Elastic Container Service (ECS)"
categories: ["LocalStack Pro"]
description: >
  Elastic Container Service (ECS)
---

LocalStack Pro version provides a basic support for creating and deploying containerized apps using [Amazon ECS](https://aws.amazon.com/ecs). LocalStack offers the basic APIs locally, including creation of ECS task definitions, services, and tasks.

By default, the **ECS Fargate** launch type is assumed, i.e., the local Docker engine is used for deployment of applications, and there is no need to create and manage EC2 virtual machines to run the containers.

{{< alert >}}**Note**:
More complex features like integration of application load balancers (ALBs) are currently not available. Nonetheless, they are being developed and will be available in the near future.
{{< /alert >}}

Task instances are started in a local Docker engine, which needs to be accessible to the LocalStack container. The name pattern for task containers is `localstack_<family>_<revision>`, where `<family>` refers to the task family and `<revision>` refers to a task revision (for example, `localstack_nginx_1`).

You can use the configuration option `LAMBDA_DOCKER_NETWORK` to specify the network the ECS containers are started in.
If your ECS containers depend on LocalStack services, this should be the network the LocalStack container is located in.
For more information regarding the configuration of LocalStack, please check the [LocalStack configuration]({{< ref "configuration" >}}) section.

If you are running LocalStack through a `docker run` command, do not forget to enable the communication from the container to the Docker Engine API. You can provide the access by adding the following option `-v /var/run/docker.sock:/var/run/docker.sock`.
