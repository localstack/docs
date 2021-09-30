---
title: "Lambda Executor Modes"
weight: 5
description: >
  Overview of the different Lambda execution modes
---
LocalStack currently supports 3 different modes for lambda execution. They mostly differ in term of feature set and execution speed.

The active lambda executor can be set using the `LAMBDA_EXECUTOR` environment variable, which has the 3 possible options `local`, `docker` and `docker-reuse`.

The default option is `docker`, unless LocalStack has no access to a docker daemon itself when it will be set to `local`.

* `local` executor:
In this execution mode, the lambda code is executed directly in the context of LocalStack itself.
Therefore, if LocalStack is executed within docker, all the Lambda executions take place within that same container, and if it is executed in host mode, it will be executed directly on your machine. 
If lambda container images are used, and the `local` executor is set, the execution of these images will automatically take place using the `docker` executor (regular lambdas will continue to use the `local` executor).
Local executor mode currently supports python, javascript, java and go lambdas.
Other lambdas, like .Net lambdas, currently need to be executed in one of the docker modes.

* `docker` executor:
The `docker` execution mode will execute lambdas in an docker container.
For this, every lambda invocation creates and runs a new docker container and returns its result when its finished.
The advantage of this mode is the fresh lambda environment from each start, so possible leftovers during previous invocations will be purged.
Due to the nature of this mode, mainly recreating the container for each invocation, this mode is rather slow.
A typical invocation of a dummy python lambda can take around 3 seconds from start to finish.
All supported lambda types can be used with this executor.

* `docker-reuse` executor:
This execution mode provides a balance between the speed of a local execution and the feature set and isolation of the `docker` executor.
While the initial call, which creates the container, will take roughly the same time of `docker` executor, the subsequent invocations will only take around 1 second (start to finish, invoked using the awscli), which roughly the time an actual aws invocation using this method takes.
The container is kept running 10 minutes after the last invocation for this lambda, then it will be destroyed (and recreated if necessary for the next invocation).