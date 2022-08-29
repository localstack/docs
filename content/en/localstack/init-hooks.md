---
title: "Initialization hooks"
weight: 5
description: >
  Write shell or Python scripts to customize or initialize your LocalStack instance.
---

## Lifecycle stages and hooks

LocalStack has four well-known lifecycle phases or stages:
* `BOOT`: the container is running but the LocalStack runtime has not been started
* `START`: the Python process is running and the LocalStack runtime is starting
* `READY`: LocalStack is ready to serve requests
* `SHUTDOWN`: LocalStack is shutting down

You can hook into each of these lifecycle phases using custom shell or python scripts.
Each lifecycle phase has it's own directory in `/etc/localstack/init`.
You can mount individual files, stage directories, or the entire init directory from your host into the container.

```
/etc
└── localstack
    └── init
        ├── boot.d           <-- executed in the container before localstack starts
        ├── ready.d          <-- executed when localstack becomes ready (currently equivalent to `/docker-entrypoint-initaws.d`)
        ├── shutdown.d       <-- executed when localstack shuts down
        └── start.d          <-- executed when localstack starts up
```

In these directories, you can put either executable shell scripts or python programs, which will be executed from within a Python process.
All except `boot.d` will be run in the same Python interpreter as LocalStack, which gives additional ways of configuring/extending LocalStack.

Currently, known script extensions are `.sh`, and `.py`.
Shell scripts have to be executable.

A script can be in one of four states: `UNKNOWN`, `RUNNING`, `SUCCESSFUL`, `ERROR`.
Scripts are by default in the `UNKNOWN` state once they have been discovered.
The remaining states should be self-explanatory.

### Execution order and script failures

Scripts are sorted and executed in alphanumerical order.
If an init script fails, the remaining scripts will still be executed in order.
A script is considered in `ERROR` state if it is a shell script and returns with a non-zero exit code, or if a Python script raises an exception during its execution.


## Status endpoint

There is an additional endpoint at `localhost:4566/_localstack/init` which returns the state of the initialization procedure.
Boot scripts (scripts placed in `boot.d`) are currently always in the `UNKNOWN` state, since they are executed outside the LocalStack process and we don't know whether they have been successfully executed or not.

```bash
curl -s localhost:4566/_localstack/init | jq .
```
```json
{
  "completed": {
    "BOOT": false,
    "START": true,
    "READY": true,
    "SHUTDOWN": false
  },
  "scripts": [
    {
      "stage": "BOOT",
      "name": "booting.sh",
      "state": "UNKNOWN"
    },
    {
      "stage": "READY",
      "name": "pre_seed.py",
      "state": "SUCCESSFUL"
    }
  ]
}
```

### Query individual stages

You can also query a specific stage:
```bash
curl -s localhost:4566/_localstack/init/ready | jq .
```
```json
{
  "completed": true,
  "scripts": [
    {
      "stage": "READY",
      "name": "pre_seed.py",
      "state": "OK"
    }
  ]
}
```

To check whether a given stage has been completed you can now run, for example:

```bash
curl -s localhost:4566/_localstack/init/ready | jq .completed
```
which returns either `true` or `false`.


## Usage example

A common use case for init hooks is pre-seeding LocalStack with custom state.
If you have more complex state, [Cloud Pods]({{< ref `cloud-pods` >}}) may be a good option to look into!
But for simple state, for example if you want to have a certain S3 bucket or DynamoDB table created when starting LocalStack, init hooks can be very useful.

To execute aws cli commands when LocalStack becomes ready,
simply create a script `init-aws.sh` and mount it into `/etc/localstack/init/ready.d/`.
Make sure the script is executable: run `chmod +x init-aws.sh` on the file first.
You can use anything available inside the container, including `awslocal`:

```bash
#!/bin/bash
awslocal s3 mb s3://my-bucket
awslocal sqs create-queue --queue-name my-queue
```

Start Localstack:

{{< tabpane >}}
{{< tab header="docker-compose.yml" lang="yml" >}}
version: "3.8"

services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME-localstack_main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"
    environment:
      - DEBUG=1
      - DOCKER_HOST=unix:///var/run/docker.sock
    volumes:
      - "/path/to/init-aws.sh:/etc/localstack/init/ready.d/init-aws.sh"  # ready hook
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
{{< /tab >}}
{{< tab header="CLI" lang="bash" >}}
# DOCKER_FLAGS are additional parameters to the `docker run` command of localstack start
DOCKER_FLAGS='-v /path/to/init-aws.sh:/etc/localstack/init/ready.d/init-aws.sh' localstack start
{{< /tab >}}
{{< /tabpane >}}
