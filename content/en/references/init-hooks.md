---
title: "Initialization Hooks"
weight: 50
description: >
  Writing shell or Python scripts to customize or initialize your LocalStack instance
aliases:
  - /localstack/init-hooks/
---

## Lifecycle stages and hooks

LocalStack has four well-known lifecycle phases or stages:
* `BOOT`: the container is running but the LocalStack runtime has not been started
* `START`: the Python process is running and the LocalStack runtime is starting
* `READY`: LocalStack is ready to serve requests
* `SHUTDOWN`: LocalStack is shutting down

You can hook into each of these lifecycle phases using custom shell or Python scripts.
Each lifecycle phase has its own directory in `/etc/localstack/init`.
You can mount individual files, stage directories, or the entire init directory from your host into the container.

```plaintext
/etc
└── localstack
    └── init
        ├── boot.d           <-- executed in the container before localstack starts
        ├── ready.d          <-- executed when localstack becomes ready
        ├── shutdown.d       <-- executed when localstack shuts down
        └── start.d          <-- executed when localstack starts up
```

In these directories, you can put either executable shell scripts or Python programs, which will be executed from within a Python process.
All except `boot.d` will be run in the same Python interpreter as LocalStack, which gives additional ways of configuring/extending LocalStack.
You can also use subdirectories to organize your init scripts.

Currently, known script extensions are `.sh`, and `.py`.
Shell scripts have to be executable, and have to have a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) (usually `#!/bin/bash`).

A script can be in one of four states: `UNKNOWN`, `RUNNING`, `SUCCESSFUL`, `ERROR`.
Scripts are by default in the `UNKNOWN` state once they have been discovered.
The remaining states should be self-explanatory.

### Execution order and script failures

Scripts are sorted and executed in alphanumerical order.
If you use subdirectories, scripts in parent folders are executed first, and then the directories are traversed in alphabetical order, depth first.
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

You can also query a specific stage at `localhost:4566/_localstack/init/<stage>`:
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
If you have more complex state, [Cloud Pods]({{< ref "user-guide/state-management/cloud-pods" >}})  and  [how to auto-load them on startup]({{< ref "user-guide/state-management/cloud-pods#auto-loading-cloud-pods" >}})  may be a good option to look into!

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
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"
    environment:
      - DEBUG=1
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

Another use for init hooks can be seen when [adding custom TLS certificates to LocalStack]({{< ref "custom-tls-certificates#custom-tls-certificates-with-init-hooks" >}}).

## Troubleshooting
If you are having issues with your initialization hooks not being executed, please perform the following checks:
- Do the scripts have a known file extensions (`.sh` or `.py`)?
  - If not, rename the files to the matching file extension.
- Is the script marked as executable?
  - If not, set the executable flag on the file (`chmod +x ...`).
- If it's a shell script, does it have a shebang (e.g., `#!/bin/bash`) as the first line in the file?
  - If not, add the shebang header (usually `#!/bin/bash`) on top of your script file.
- Is the script being listed in the logs when running LocalStack with `DEBUG=1`?
  - The detected scripts are logged like this:
    ```
    ...
    Init scripts discovered: {BOOT: [], START: [], READY: [Script(path='/etc/localstack/init/ready.d/setup.sh', stage=READY, state=UNKNOWN)], SHUTDOWN: []}
    ...
    Running READY script /etc/localstack/init/ready.d/setup.sh
    ...
    ```
  - If your script does not show up in the list of discovered init scripts, please check your Docker volume mount.
    Most likely the scripts are not properly mounted into the Docker container.