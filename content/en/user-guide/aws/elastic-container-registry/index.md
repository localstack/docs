---
title: "Elastic Container Registry (ECR)"
linkTitle: "Elastic Container Registry (ECR)"
categories: ["LocalStack Pro"]
description: >
  Get started with Elastic Container Registry (ECR) on LocalStack
aliases:
  - /aws/elastic-container-registry/
---

A basic version of Elastic Container Registry (ECR) is available to store application images. ECR is often used in combination with other APIs that deploy containerized apps, like ECS or EKS.

{{< command >}}
$ awslocal ecr create-repository --repository-name repo1
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:000000000000:repository/repo1",
        "registryId": "abc898c8",
        "repositoryName": "repo1",
        "repositoryUri": "localhost:4510/repo1"
    }
}
{{< / command >}}

You can then build and tag a new Docker image, and push it to the repository URL (`localhost:4510/repo1` in the example above):
{{< command >}}
$ cat Dockerfile
FROM nginx
ENV foo=bar
{{< / command >}}

{{< command >}}
$ docker build -t localhost:4510/repo1 .
...
Successfully built e2cfb3cf012d
Successfully tagged localhost:4510/repo1:latest
{{< / command >}}

{{< command >}}
$ docker push localhost:4510/repo1
The push refers to repository [localhost:4510/repo1]
318be7aea8fc: Pushed
fe08d5d042ab: Pushed
f2cb0ecef392: Pushed
latest: digest: sha256:4dd893a43df24c8f779a5ab343b7ef172fb147c69ed5e1278d95b97fe0f584a5 size: 948
...
{{< / command >}}
