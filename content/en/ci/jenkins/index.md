---
title: "Jenkins"
tags: ["continuous-integration", "ci", "continuous-delivery", "testing"] 
weight: 14
description: >
  Use LocalStack with [Jenkins](https://www.jenkins.io/)
---


<img src="jenkins-logo.svg" width="100px" alt="Jenkins logo">


## Quick Start

In this quick start we'll start our Jenkins server as a Docker container. 
Localstack will be run in a Docker build agent.

To keep requirements low for this guide, we're going to assume you're running everything on a single debian-based local machine with docker and docker-compose installed.


```yaml
version: "3.7"
services:
  jenkins:
    privileged: true
    user: root
    image: jenkins/jenkins:2.322-jdk11
    ports:
      - 8080:8080
      - 50000:50000
    volumes:
      - .jenkins:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
      - /usr/bin/docker:/usr/bin/docker
```

We're starting a jenkins server as a Docker container. The Docker socket and client are mounted into the container.
Alternatively you can also point the docker client in Jenkins to the URL of a remote Docker host with an exposed API.

In your production environment you might also want to install Docker on the runner directly.

```bash
docker-compose up -d
docker-compose logs -f # check the log output for the initial admin user password
```

Head to http://localhost:8080 and initialize Jenkins.
After the initial setup, go to "Manage Jenkins"->"Manage Plugins"->"Available" and install the [Docker plugin](https://plugins.jenkins.io/docker-plugin/).
After the plugin is installed it needs to be configured.
Go to "Manage Jenkins"->"Manage Nodes and Clouds"->"Configure Clouds" and follow the documentation in https://plugins.jenkins.io/docker-plugin/ to set up your docker client and make sure you verify the setup with "Test Connection". 


