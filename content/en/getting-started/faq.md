---
title: "Frequently Asked Questions"
linkTitle: "FAQ"
weight: 40
description: >
  This page answers the frequently asked questions about LocalStack Pro, Enterprise, and Community Editions. 
cascade:
  type: docs
hide_readingtime: true
---

## LocalStack Core FAQs

### How to update my LocalStack CLI?

If the LocalStack CLI version is heavily outdated, it might lead to issues with container startup and debug commands. If you are using an older version of LocalStack, you can update it by running the following command:

{{< command >}}
pip install --upgrade localstack localstack-ext
{{< / command >}}

If you are running a newer version of LocalStack, you can check the version by running the following command:

{{< command >}}
localstack update localstack-cli
{{< / command >}}

### Is using `localhost.localstack.cloud:4566` to set as the endpoint for AWS services recommended?

`localhost.localstack.cloud` is the recommended endpoint - especially for S3, in order to enable host-based bucket endpoints.
* When using this domain within LocalStack compute environments like Lambda, ECS or EC2, this domain name resolves to the LocalStack container via our DNS server available in version 2.3.
* By configuring your environment, your applications can also use `localhost.localstack.cloud` to resolve to the LocalStack container via our DNS server.
* In addition, we also publish an SSL certificate that is automatically used inside LocalStack, in order to enable HTTPS endpoints with valid certificates.

Across our docs, we use `localhost:4566` instead of `localhost.localstack.cloud`, to provide a fallback option to users.
The primary reason being that some users are behind a corporate firewall or an internet service provider that does not allow resolving `localhost.localstack.cloud` properly.

### How should I use the latest LocalStack Docker images?

To use the latest LocalStack Docker images, you either run `docker pull localstack/localstack:latest` or use the `docker-compose pull` if the image is set to `localstack/localstack:latest`. You can also specify a particular digest to make sure you are using the correct image, like this: `localstack/localstack:latest@sha256:f803cc657843c6c7acf2631d15600783c3593e496fba418415afc87680d9d5bc`.

You can also use the our diagnose endpoint (`http://localhost:4566/_localstack/diagnose`) to get the specific image hashes and compare them with the current (latest) images on [Docker Hub](https://hub.docker.com/r/localstack/).
The diagnose endpoint is only available if you run LocalStack with `DEBUG=1`.

### How can I access LocalStack from an alternative computer?

You can access LocalStack from an alternative computer, by exposing port `4566` to the public network interface (`0.0.0.0` instead of `127.0.0.1`) in your `docker-compose.yml` configuration. However, we do not recommend using this setup - for security reasons, as it exposes your local computer to potential attacks from the outside world.

### How to fix LocalStack CLI (Python) UTF-8 encoding issue under Windows?

If you are using LocalStack CLI under Windows, you might run into encoding issues. To fix this, set the following environment variables:  
Set the system locale (language for non-Unicode programs) to UTF-8 to avoid Unicode errors.

Follow these steps:
- Open the Control Panel.
- Go to "Clock and Region" or "Region and Language."
- Click on the "Administrative" tab.
- Click on the "Change system locale" button.
- Select "Beta: Use Unicode UTF-8 for worldwide language support" and click "OK."
- Restart your computer to apply the changes.

If you would like to keep the system locale as it is, you can mitigate the issue by using the command `localstack --no-banner`.

### How do I resolve connection issues with proxy blocking access to LocalStack's BigData image?

A company proxy can lead to connection issues. To allow access to the `localstack/bigdata` image, use the following Docker configuration in your `docker-compose.yml` file:

```yaml
...
environment: 
- HTTP_PROXY = 
- NO_PROXY = .s3.localhost.localstack.cloud,127.0.0.1,*.localhost
...
```

### How to troubleshoot the DNS issue for LocalStack's BigData image?

Occasionally, users have wrong configuration of their `docker-compose.yml` or `ENV` variables. ´Some Glue scripts depend on the local DNS setup. To resolve DNS issues, set TCP port `53` in LocalStack's `docker-compose.yml` file:

```yaml
ports:
       - "53:53"
       …
```

Furthermore, use either the default name `localstack_main` for the container, or alternatively configure the environment variable `MAIN_CONTAINER_NAME` to point to the correct name.

```yaml
container_name: localstack_main
```

Ensure that `127.0.0.1` is configured as the target DNS server for the `bigdata` container:

```yaml
docker inspect localstack_bigdata --format '{{ .HostConfig.Dns }}'

Output: [127.0.0.1]
```

You can test it by attempting to resolve an S3 hostname, which should then internally get routed to the LocalStack API endpoints.

```bash
docker exec -it localstack_bigdata curl -vk https://test.s3.amazonaws.com
```

### Why is it that LocalStack is unable to connect to internet?

You might be able to connect to the internet, but your Docker container can't connect. This can affect start of LocalStack.

More details can be found on [official docker documentation](https://docs.docker.com/network/bridge/#enable-forwarding-from-docker-containers-to-the-outside-world).

Solution for this is enabling the IP forwarding: 

```bash
sudo sysctl -w net.ipv4.ip_forward=1
```

### Why can't my other Docker containers reach LocalStack?

Using LocalStack inside a Docker network with multiple other containers can lead to connectivity issues from/to those containers. For example, a container which attempts to deploy a stack and interact with the services directly, from within the same Docker network.

To resolve this, set `HOSTNAME_EXTERNAL` for correct response values for endpoints. Use network aliases to ensure resolution of `localhost.localstack.cloud` to the correct container:

```yaml
...
    networks:
      default:
        aliases:
          - localhost.localstack.cloud
  sdkstack:
    image: ubuntu
    command: ["bash", "-c", "apt update && apt install -y curl && sleep 5 && curl -v http://localhost.localstack.cloud:4566/_localstack/health"]
...
```

Note the missing `network: bridge` here! The default bridge network does not support DNS name resolution.

### How to resolve the pull rate limit issue for LocalStack's Docker image?

If you receive `ERROR: toomanyrequests: Too Many Requests.` when pulling the LocalStack Docker image, you have reached your pull rate limit. You may increase the limit by [authenticating and upgrading](https://www.docker.com/increase-rate-limits). Set your DockerHub credentials:

```bash
(sudo) docker login --username=yourUsername
```

You can add in the volume `~/.docker/config.json:/config.json` where the `config.json` is saved and point the `DOCKER_CONFIG=/config.json` variable to the JSON file in the Docker image.

```yaml
...
    environment:
      - DOCKER_CONFIG=/config.json
    volumes:
      - ~/.docker/config.json:/config.json
...
```

### How to increase IO performance for LocalStack's Docker image under Windows?

{{< alert title="Note">}}
Some options that are not part of the standard configuration may have unintended consequences for AWS services that operate within LocalStack.
For example, these options may interfere with the functionality of AppSync function executor, RDS MySQL persistence and SageMaker.
We advise you to exercise caution.
{{< /alert >}}

You can change the LocalStack `volume` folder to use the WSL Linux file system instead of the Windows host folder.  
To do so, you need to change the [`docker-compose.yml`](https://github.com/localstack/localstack/blob/master/docker-compose-pro.yml) file and add the following lines:

{{< tabpane text=true >}}
{{< tab header="WSL Linux File System" >}}
{{% markdown %}}

```yaml
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
       - "\\\\wsl$\\<Ubuntu>\\home\\<USERNAME>\\volume:/var/lib/localstack" # mount volume in WSL2 Linux file system
```

---

As an alternative, you can set the volume as `- "~/volume:/var/lib/localstack"` then start Docker using command `wsl docker compose -f docker-compose.yml up`.

{{% /markdown %}}
{{< /tab >}}
{{< tab header="Docker Volumes" >}}
{{% markdown %}}

```yaml
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
       - "localstack_data:/var/lib/localstack" # mount Docker volume
volumes:
  localstack_data:
```

{{% /markdown %}}
{{< /tab >}}
{{< /tabpane >}}

For more details visit [Docker WSL documentation](https://docs.docker.com/desktop/wsl), [Docker WSL best practices](https://docs.docker.com/desktop/wsl/best-practices) and [Docker Volumes documentation](https://docs.docker.com/storage/volumes/).

## LocalStack Platform FAQs

### How do I check if my API key is valid and activated?

The easiest way to check if LocalStack Pro or Enterprise is activated is to check the health endpoint of LocalStack for a list of the running services:

{{< command >}}
$ curl localhost:4566/_localstack/health | jq
{{< / command >}}

If a Pro-only [service]({{< ref "aws" >}}) -- like [XRay]({{< ref "xray" >}}) -- is running, LocalStack Pro or Enterprise has started successfully. If your API key is invalid, you will see an error message like this in the logs of LocalStack:

```bash
Activation key "abc..."(10) is invalid or expired! Reason: ...
```

If this error occurs, something is wrong with your API key or license. Make sure your API key is set correctly (check for typos!) and your license is valid. If the API key still does not work, please [contact us](https://localstack.cloud/contact/).

### How are CI credits in LocalStack calculated?

A CI key allows you to use LocalStack in your CI environment. Every activation of a CI key consumes one build credit. This means that with every build triggered through the LocalStack container you will consume one credit. To understand the CI pricing across our product tiers, follow up with our [LocalStack in CI]({{<ref "user-guide/ci">}}) documentation.

### What should I do if I cannot connect to LocalStack API?

If your log output contains lines like:

```shell
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
ConnectionRefusedError: [Errno 111] Connection refused
```

LocalStack cannot contact our API to perform the license activation. Confirm with your network administrator that no policies block the connection to our backend.

### What should I do if I cannot resolve `api.localstack.cloud`?

Log output like the following indicates that your machine cannot resolve the domain of the LocalStack API.

```shell
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
socket.gaierror: [Errno -3] Temporary failure in name resolution
```

Confirm this by using a tool like `dig`:

{{< command >}}
$ dig api.localstack.cloud
{{< / command >}}

If the result has some other status than `status: NOERROR,` your machine cannot resolve this domain.

Some corporate DNS servers might filter requests to certain domains. Contact your network administrator to safelist` localstack.cloud` domains.

### How does LocalStack Pro handle security patches and bug fixes?

We take security seriously and respond to any emergency vulnerabilities as soon as possible. Our cloud provider (AWS) handles most of the infrastructure maintenance for us. We also use Infrastructure-as-Code scripts to ensure that our infrastructure configuration is consistent and recoverable in case of a disaster.

### How does LocalStack ensure the security of its containers and images? 

Our software assets are regularly checked for vulnerabilities, such as code issues and outdated dependencies. We use Dependabot to scan our GitHub repositories, and Trivy as well as Snyk (among other security tools) to scan our Docker images.

### Do you have any penetration test reports or SOC2 reports that demonstrate your security compliance?

We conduct regular penetration tests and audits to ensure our services are secure and compliant. If you want to access our security documentation and test reports, please contact us at info@localstack.cloud, and we will be happy to share them with you.

### Does LocalStack provide offline capabilities?

LocalStack Community and Pro/Team provide limited offline capabilities. To use a fully-fledged offline mode, you may use LocalStack Enterprise, which can be used in air-gapped environments. The regular LocalStack Docker images may need to download additional dependencies for specific services (e.g., Elasticsearch, Big Data services) at runtime, while the offline image bakes all dependencies into the image, along with any other configuration that you might need. For more details, please take a look at our [Enterprise offering](https://localstack.cloud/pricing).
