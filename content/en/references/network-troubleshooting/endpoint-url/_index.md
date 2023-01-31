---
title: Accessing LocalStack via the Endpoint URL
weight: 1
tags:
- troubleshooting
- networking
---

Use this page to find the scenario that best matches your use case

# Accessing LocalStack from the same computer

{{< figure src="../images/1.png" width="400" >}}

**Example**: you have run `localstack start`, or you are accessing LocalStack started in Docker (or docker-compose).

The hostname `localhost.localstack.cloud` maps to 127.0.0.1, i.e. your computer, and if you expose port 4566 from LocalStack then you should be able to connect.
If not, you can use `localhost` or any domain name that refers to `localhost`.

# Accessing LocalStack from a container LocalStack created

{{< figure src="../images/4.png" width="400" >}}

**Example**: your code is running in an ECS container that LocalStack has created.

It may be useful to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), and set the `LAMBDA_DOCKER_NETWORK` environment variable to this value.
Then code running in ECS can access the LocalStack instance by its hostname. For example:

{{< command >}}
docker network create my-network
docker run --rm -it -e LAMBDA_DOCKER_NETWORK=my-network --network my-network --name localstack localstack/localstack-pro

# Then inside ECS container

aws --endpoint-url http://localstack:4566 s3api list-buckets
{{< / command >}}

# Accessing LocalStack from your container

{{< figure src="../images/7.png" width="400" >}}

* TODO

# Accessing LocalStack from a separate host

{{< figure src="../images/10.png" width="400" >}}

* TODO
