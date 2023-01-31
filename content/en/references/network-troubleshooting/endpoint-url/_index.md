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

For example, you have run `localstack start`, or you are accessing LocalStack started in Docker (or docker-compose).

The hostname `localhost.localstack.cloud` maps to 127.0.0.1, i.e. your computer, and if you expose port 4566 from LocalStack then you should be able to connect.
If not, you can use `localhost` or any domain name that refers to `localhost`.

* TODO

# Accessing LocalStack from a container LocalStack created

{{< figure src="../images/4.png" width="400" >}}

* TODO

# Accessing LocalStack from your container

{{< figure src="../images/7.png" width="400" >}}

* TODO

# Accessing LocalStack from a separate host

{{< figure src="../images/10.png" width="400" >}}

* TODO
