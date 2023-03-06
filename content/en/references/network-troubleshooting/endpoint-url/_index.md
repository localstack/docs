---
title: Accessing LocalStack via the Endpoint URL
weight: 1
tags:
- troubleshooting
- networking
---

Use this page to find the scenario that best matches your use case

## From the same computer

{{< figure src="../images/1.svg" width="400" >}}

**Example**: you have run `localstack start`, or you are accessing LocalStack started in Docker (or docker-compose).

If you expose port 4566 from your LocalStack container then you should be able to connect by connecting to `localhost`.
If not, you can use `localhost` or any domain name that refers to `localhost`.

{{<alert title="Note">}}
If you bind a domain name to `localhost`, check that you are not subject to [DNS rebind protection]({{< ref "user-guide/tools/transparent-endpoint-injection/dns-server#dns-rebind-protection" >}}).
{{</alert>}}

## From a container LocalStack created

{{< figure src="../images/4.svg" width="400" >}}

**Example**: your code is running in an ECS container that LocalStack has created.

It may be useful to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), and set the `MAIN_DOCKER_NETWORK` environment variable to this value.
Then code running in ECS can access the LocalStack instance by its hostname. For example:

{{<tabpane>}}
{{<tab header="CLI" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
MAIN_DOCKER_NETWORK=my-network DOCKER_FLAGS="--network my-network" localstack start
# then your code can access localstack at its container name (by default: localstack_main)
aws --endpoint-url http://localstack_main:4566 s3api list-buckets
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
docker run --rm -it --network my-network -e MAIN_DOCKER_NETWORK=my-network <other flags> localstack/localstack[-pro]
# then your code can access localstack at its container name (by default: localstack_main)
aws --endpoint-url http://localstack_main:4566 s3api list-buckets
{{</tab>}}
{{<tab header="docker-compose.yml" lang="yml">}}
services:
  localstack:
    # ... other configuration here
    environment:
      MAIN_DOCKER_NETWORK=ls
    networks:
    - ls
networks:
  ls:
    name: ls

# Your application code can then use
# http://localstack:4566 for the
# endpoint url
{{</tab>}}
{{</tabpane>}}

## From your container

{{< figure src="../images/7.svg" width="400" >}}

**Example**: you are running your application code in a container and accessing AWS resources such as S3 in LocalStack.

It may be useful to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), and set the `MAIN_DOCKER_NETWORK` environment variable to this value.
Then your application code can access the LocalStack instance by its hostname. For example:

{{<tabpane>}}
{{<tab header="CLI" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
DOCKER_FLAGS="--network my-network" localstack start
# launch your container
docker run --rm it --network my-network <image name>
# then your code can access localstack at its container name (by default: localstack_main)
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
docker run --rm -it --network my-network <other flags> localstack/localstack[-pro]
# launch your container
docker run --rm it --network my-network <image name>
# then your code can access localstack at its container name (by default: localstack_main)
{{</tab>}}
{{<tab header="docker-compose.yml" lang="yml">}}
services:
  localstack:
    # ... other configuration here
    networks:
    - ls
  your_container:
    # ... other configuration here
    networks:
    - ls
networks:
  ls:
    name: ls

# Your application code can then use
# http://localstack:4566 for the
# endpoint url
{{</tab>}}
{{</tabpane>}}

## From a separate host

{{< figure src="../images/10.svg" width="400" >}}

LocalStack must listen to the address of the host, or `0.0.0.0`.

{{<tabpane>}}
{{<tab header="CLI" lang="bash">}}
EDGE_BIND_HOST="0.0.0.0" localstack start
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# this command exposes ports on all interfaces by default
docker run --rm -it -p 4566:4566 <additional arguments> localstack
{{</tab>}}
{{<tab header="docker-compose" lang="yaml">}}
services:
  localstack:
    # ... other configuration here
    ports:
      - "4566:4566"
      # ... other ports
{{</tab>}}
{{</tabpane>}}

See our [FAQ article on accessing LocalStack from another computer]({{<ref "getting-started/faq#how-can-i-access-localstack-from-an-alternative-computer">}}).
