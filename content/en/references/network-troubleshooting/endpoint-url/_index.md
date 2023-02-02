---
title: Accessing LocalStack via the Endpoint URL
weight: 1
tags:
- troubleshooting
- networking
---

Use this page to find the scenario that best matches your use case

# From the same computer

{{< figure src="../images/1.svg" width="400" >}}

**Example**: you have run `localstack start`, or you are accessing LocalStack started in Docker (or docker-compose).

The hostname `localhost.localstack.cloud` maps to 127.0.0.1, i.e. your computer, and if you expose port 4566 from LocalStack then you should be able to connect.
If not, you can use `localhost` or any domain name that refers to `localhost`.

# From a container LocalStack created

{{< figure src="../images/4.svg" width="400" >}}

**Example**: your code is running in an ECS container that LocalStack has created.

It may be useful to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), and set the `LAMBDA_DOCKER_NETWORK` environment variable to this value.
Then code running in ECS can access the LocalStack instance by its hostname. For example:

{{<tabpane>}}
{{<tab header="CLI" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
LAMBDA_DOCKER_NETWORK=my-network DOCKER_FLAGS="--network my-network" localstack start
# then your code can access localstack at its container name (default localstack_main)
aws --endpoint-url http://localstack_main:4566 s3api list-buckets
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
docker run --rm -it --network my-network -e LAMBDA_DOCKER_NETWORK=my-network <other flags> localstack/localstack[-pro]
# then your code can access localstack at its container name (default localstack_main)
aws --endpoint-url http://localstack_main:4566 s3api list-buckets
{{</tab>}}
{{<tab header="docker-compose.yml" lang="yml">}}
services:
  localstack:
    # ... configuration here
    environment:
      LAMBDA_DOCKER_NETWORK=ls
    networks:
    - ls
networks:
  ls:
    name: ls
{{</tab>}}
{{</tabpane>}}

# From your container

{{< figure src="../images/7.svg" width="400" >}}

**Example**: you are running your application code in a container and accessing AWS resources such as S3 through LocalStack.

Similar to the example above, consider configuring docker networking when launching your container.

{{<tabpane>}}
{{<tab header="CLI" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
DOCKER_FLAGS="--network my-network" localstack start
# launch your container
docker run --rm it --network my-network <image name>
# then your code can access localstack at its container name (default localstack_main)
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
docker run --rm -it --network my-network <other flags> localstack/localstack[-pro]
# launch your container
docker run --rm it --network my-network <image name>
# then your code can access localstack at its container name (default localstack_main)
{{</tab>}}
{{<tab header="docker-compose.yml" lang="yml">}}
services:
  localstack:
    # ... configuration here
    networks:
    - ls
  your_container:
    # ... configuration here
    networks:
    - ls
networks:
  ls:
    name: ls
{{</tab>}}
{{</tabpane>}}

# From a separate host

{{< figure src="../images/10.svg" width="400" >}}

**Example**:

TODO
