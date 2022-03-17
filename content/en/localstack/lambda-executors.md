---
title: "Lambda Executor Modes"
weight: 5
description: >
  Overview of the different Lambda execution modes
---

## Overview

LocalStack currently supports three different modes for lambda execution.
They differ in when and where your lambda code is executed, and in term of feature set and execution speed.

## Execution modes

The active lambda executor can be set using the `LAMBDA_EXECUTOR` environment variable, which has the 3 possible options `local`, `docker` and `docker-reuse`.

The default option is `docker`, unless LocalStack has no access to a docker daemon itself when it will be set to `local`.

Running docker containers inside the Localstack docker images requires to bind mount the `/var/run/docker.sock`. See the example below:
{{< command >}}
$ docker run --rm -it -v "/var/run/docker.sock:/var/run/docker.sock" -e DEBUG=1 -e LAMBDA_EXECUTOR=<mode> -p 4566:4566  localstack/localstack
{{</command >}}


### Local execution

Configuration: `LAMBDA_EXECUTOR=local`

In this execution mode, the lambda code is executed directly in the context of LocalStack itself.
Therefore, if LocalStack is executed within docker, all the Lambda executions take place within that same container, and if it is executed in host mode, it will be executed directly on your machine.
If lambda container images are used, and the `local` executor is set, the execution of these images will automatically take place using the `docker` executor (regular lambdas will continue to use the `local` executor).

Local executor mode currently supports the following Lambda Platforms:
* Python
* Nodejs
* Java
* Go

Lambdas on other platforms like .Net currently need to be executed in one of the docker modes.

### Docker

Configuration: `LAMBDA_EXECUTOR=docker`


The `docker` execution mode will execute lambdas in a docker container.
For this, every lambda invocation creates and runs a new docker container and returns its result when it's finished.
The advantage of this mode is the fresh lambda environment from each start, so possible leftovers during previous invocations will be purged.
Due to the nature of this mode, mainly recreating the container for each invocation, this mode is rather slow.
A typical invocation of a dummy python lambda can take around 3 seconds from start to finish (awscli invoke - start to finish).
All supported lambda types can be used with this executor.

### Docker reuse

Configuration: `LAMBDA_EXECUTOR=docker-reuse`

#### Stay-open mode
LocalStack allows to use the stay-open mode of its lambda containers.
The containers stay open and wait for further invocations, without executing the initialization code of the lambda multiple times.
This results in way faster execution times, especially if the lambda has long-running initialization code.

The stay-open mode is the new default method when using `docker-reuse` as lambda executor, however, it has some restrictions:

* Only works if LocalStack runs in a Docker container
* Large Payloads (multiple MBs) do not work
* Problems with error handling in some runtimes

A list of failing tests with this mode can be found [in this GitHub issue](https://github.com/localstack/localstack/pull/5088).

#### Docker-exec execution mode
This mode is the default if LocalStack is started in host mode.
If you experience failures using the stay-open mode (either due to the mentioned restrictions or networking problems), you can force this mode by setting `LAMBDA_STAY_OPEN_MODE=0`.
Also if you want to use [Hot Swapping]({{< ref "hot-swapping" >}}) you should set `LAMBDA_STAY_OPEN_MODE=0`.

This execution mode provides a balance between the speed of a local execution and the feature set and isolation of the `docker` executor.
While the initial call, which creates the container, will take roughly the same time of `docker` executor, the subsequent invocations will only take around 1 second (start to finish, invoked using the awscli), which is roughly the time an actual aws invocation using this method takes.
The container is kept running 10 minutes after the last invocation for this lambda, then it will be destroyed (and recreated if necessary for the next invocation).
The complete lambda process is called using `docker-exec` each time of the invocation. While the invocation is still faster than `docker` execution mode, it is not as fast as with the stay-open mode (since the lambda has to be loaded and initialized every time).
