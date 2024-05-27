---
title: Accessing LocalStack via the endpoint URL
weight: 1
tags:
- troubleshooting
- networking
---

This documentation provides step-by-step guidance on how to access LocalStack services via the endpoint URL and troubleshoot common issues.

## From the same computer

{{< figure src="../images/1.svg" width="400" >}}

Suppose you have LocalStack installed on your machine and want to access it using the AWS CLI. To connect, you must expose port 4566 from your LocalStack instance and connect to `localhost` or a domain name that points to `localhost`. While the LocalStack CLI does this automatically, when running the Docker container directly or with docker compose, you must configure it manually. Check out the [getting started documentation]({{< ref "getting-started/installation" >}}) for more information.

{{< callout "tip" >}}
If you bind a domain name to `localhost`, ensure that you are not subject to [DNS rebind protection]({{< ref "dns-server#dns-rebind-protection" >}}).
{{</callout>}}

You can also use the `GATEWAY_LISTEN` [configuration variable]({{< ref "references/configuration" >}}) to change the exposed port if necessary.

## From a container LocalStack created

{{< figure src="../images/4.svg" width="400" >}}

Suppose your code is running inside an ECS container that LocalStack has created. 

The LocalStack instance is available at the domain `localhost.localstack.cloud`.
All subdomains of `localhost.localstack.cloud` also resolve to the LocalStack instance, e.g. API Gateway default URLs.

<details>
<summary>For LocalStack versions before 2.3.0</summary>
To enable access to the LocalStack instance, it's advisable to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), and then set the `MAIN_DOCKER_NETWORK` environment variable to this network's name.
This allows the code running inside the container to access the LocalStack instance using its hostname.
For example:

{{<tabpane lang="bash">}}
{{<tab header="CLI" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
MAIN_DOCKER_NETWORK=my-network DOCKER_FLAGS="--network my-network" localstack start
# then your code can access localstack at its container name (by default: localstack-main)
aws --endpoint-url http://localstack-main:4566 s3api list-buckets
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
docker run --rm -it --network my-network -e MAIN_DOCKER_NETWORK=my-network <other flags> localstack/localstack[-pro]
# then your code can access localstack at its container name (by default: localstack-main)
aws --endpoint-url http://localstack-main:4566 s3api list-buckets
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
</details>


## From your container

{{< figure src="../images/7.svg" width="400" >}}

Suppose you're accessing AWS resources such as S3 in LocalStack by running your application code in a container.
Your application container should be configured to use LocalStack as its DNS server.
Once this is done, the domain name `localhost.localstack.cloud` will resolve to the LocalStack container.
All subdomains of `localhost.localstack.cloud` will also resolve to the LocalStack instance, e.g. API Gateway default URLs.

To configure your application container:

* add a user-managed docker network;
* either determine your LocalStack container IP, or configure your LocalStack container to have a fixed known IP address;
* set the DNS server of your application container to the IP address of the LocalStack container.

{{% tabpane lang="bash" %}}
{{< tab header="CLI" lang="bash" >}}
# start localstack
localstack start -d --network ls
localstack wait

# get the ip address of the LocalStack container
docker inspect localstack-main | \
	jq -r '.[0].NetworkSettings.Networks | to_entries | .[].value.IPAddress'
# prints 172.27.0.2

# run your application container
docker run --rm -it --dns 172.27.0.2 --network ls <arguments> <image name>
{{< / tab >}}
{{< tab header="Docker" lang="bash" >}}
# start localstack
docker network create ls
docker run --rm -it --network ls --name localstack-main <other flags> localstack/localstack[-pro]

# get the ip address of the LocalStack container
docker inspect localstack-main | \
	jq -r '.[0].NetworkSettings.Networks | to_entries | .[].value.IPAddress'
# prints 172.27.0.2

# run your application container
docker run --rm -it --dns 172.27.0.2 --network ls <arguments> <image name>
{{< / tab >}}
{{< tab header="docker-compose.yml" lang="yaml" >}}
version: "3.8"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      # Now only required if you need to access LocalStack from the host
      - "127.0.0.1:4566:4566"            
      # Now only required if you need to access LocalStack from the host
      - "127.0.0.1:4510-4559:4510-4559"
    environment:
      - DEBUG=${DEBUG:-0}
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
    networks:
      ls:
        # Set the container IP address in the 10.0.2.0/24 subnet
        ipv4_address: 10.0.2.20

  application:
    image: ghcr.io/localstack/localstack-docker-debug:main
    entrypoint: ""
    command: ["sleep", "infinity"]
    dns:
      # Set the DNS server to be the LocalStack container
      - 10.0.2.20
    networks:
      - ls

networks:
  ls:
    ipam:
      config:
        # Specify the subnet range for IP address allocation
        - subnet: 10.0.2.0/24
{{< / tab >}}
{{% / tabpane %}}


<details>
<summary>For LocalStack versions before 2.3.0</summary>
To facilitate access to LocalStack from within the container, it's recommended to start LocalStack in a <a href="https://docs.docker.com/network/bridge/">user-defined network</a> and set the <code>MAIN_DOCKER_NETWORK</code> environment variable to the network's name.
Doing so enables the containerized code to connect to the LocalStack instance using its hostname.
For instance:

{{<tabpane lang="bash">}}
{{<tab header="CLI" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
DOCKER_FLAGS="--network my-network" localstack start
# launch your container
docker run --rm it --network my-network <image name>
# then your code can access localstack at its container name (by default: localstack-main)
{{</tab>}}
{{<tab header="Docker" lang="bash">}}
# create the network
docker network create my-network
# launch localstack
docker run --rm -it --network my-network <other flags> localstack/localstack[-pro]
# launch your container
docker run --rm it --network my-network <image name>
# then your code can access localstack at its container name (by default: localstack-main)
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

### Wildcard DNS access

LocalStack newer than version 2.3.0 supports wildcard DNS access by default.
Please update your LocalStack container and see the [instructions]({{< ref "#from-your-container" >}}).

</details>

## From a separate host

{{< figure src="../images/10.svg" width="400" >}}

LocalStack must listen to the address of the host, or `0.0.0.0`.

{{<tabpane lang="bash">}}
{{<tab header="CLI" lang="bash">}}
GATEWAY_LISTEN="0.0.0.0" localstack start
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

Check out our [FAQ article on accessing LocalStack from another computer]({{<ref "getting-started/faq#how-can-i-access-localstack-from-an-alternative-computer">}}).
