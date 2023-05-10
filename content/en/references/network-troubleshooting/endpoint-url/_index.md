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

{{<alert title="Note">}}
Additionally, if you bind a domain name to `localhost`, ensure that you are not subject to [DNS rebind protection]({{< ref "user-guide/tools/transparent-endpoint-injection/dns-server#dns-rebind-protection" >}}).
{{</alert>}}

You can also use the `EDGE_PORT` [configuration variable]({{< ref "references/configuration" >}}) to change the exposed port if necessary.

## From a container LocalStack created

{{< figure src="../images/4.svg" width="400" >}}

Suppose your code is running inside an ECS container that LocalStack has created. To enable access to the LocalStack instance, it's advisable to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), and then set the `MAIN_DOCKER_NETWORK` environment variable to this network's name. This allows the code running inside the container to access the LocalStack instance using its hostname. For example:

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

Suppose you're accessing AWS resources such as S3 in LocalStack by running your application code in a container. To facilitate access to LocalStack from within the container, it's recommended to start LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/) and set the MAIN_DOCKER_NETWORK environment variable to the network's name. Doing so enables the containerized code to connect to the LocalStack instance using its hostname. For instance:

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

### Wildcard DNS access

Resources created by LocalStack may be accessible via virtual host addressing, for example an S3 bucket can be accessed at `<bucket>.s3.<region>.localhost.localstack.cloud`, however this hostname resolves to the ip address `127.0.0.1`.
This may not be accessible from containers running in your docker network.
Also, docker does not support wildcard DNS configuration with `--add-host` (`docker` CLI) or `extra_hosts:` (`docker-compose`) so generated resource URLs cannot be easily mapped to the LocalStack container within the docker netwwork.

In order to map more complex domain names to the LocalStack container within the docker network, the LocalStack container can be used as a DNS server, but this requires more configuration.
Specifically the LocalStack container must have a static IP address within the network.
This can be achieved with the following `docker-compose.yml` example:

```yaml
services:
  localstack:
    # ... other configuration here
    environment:
      - DNS_RESOLVE_IP=<private ip address>
    networks:
      ls:
        ipv4_address: <private ip address>

  application:
    # ... other configuration here
    dns:
      - <localstack container ip address>
    networks:
      ls:

networks:
  ls:
    name: ls
    ipam:
      config:
        - subnet: <ip address range CIDR>
```

For example, with the following values:

* private ip address: 10.0.2.20
* ip address range CIDR: 10.0.2.0/24

{{<alert>}}
We suggest using a private IP address range for your containers, such as 10.0.0.0/8 since this does not conflict with IP addresses assigned by docker.
Also avoid using `X.X.X.1` as this often represents the host within that subnet.
{{</alert>}}

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

Check out our [FAQ article on accessing LocalStack from another computer]({{<ref "getting-started/faq#how-can-i-access-localstack-from-an-alternative-computer">}}).
