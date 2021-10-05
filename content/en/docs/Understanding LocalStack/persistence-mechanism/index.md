---
title: "Persistence Mechanism Configuration"
weight: 5
description: >
  How the LocalStack persistence mechanism works and how you can configure it.
---

The persistence mechanism is essentially a "pause and resume" feature for your LocalStack application state.
For instance, you may want to run consecutive integration tests where each test loads in a different context but depends on the state produced by a previous test.
Commonly, you may simply have a local development server that relies on a non-ephemeral application state.

While the persistence mechanism covers most services, not all of them are supported yet.
Please make sure to check the [feature coverage page]({{< ref "feature-coverage" >}} to see whether your desired services are covered.
Please note that the coverage is only guaranteed for the _Pro_ version, while the _Community_ version attempts to restore the state on a best-effort basis using a *record-and-replay* approach (more on that in the [Technical Details]({{< ref "#technical-details" >}} section).

To enable the persistence mechanism simply set the `DATA_DIR` environment variable.
For instance, `DATA_DIR=/tmp/localstack/data` will store all relevant files to the `/tmp/localstack/data` directory.
Please note that the path is created recursively, that is you do not have to make sure that the set path exists.

When working with Docker you may want to specify a different location for temporary folders using the `HOST_TMP_FOLDER` flag.
In this case, it is advisable to use a `$TMPDIR` variable, which you can re-use for both flags.
For instance, you'll set `$TMPDIR=/tmp/my-tmp` then your environment configuration in your `docker-compose` file could look as follows: 

```yaml
    ...
    environment:
      - LOCALSTACK_API_KEY=...
      - DATA_DIR=${TMPDIR}/localstack/data
      - HOST_TMP_FOLDER=${TMPDIR}
    volumes:
      - ${TMPDIR}:/tmp/localstack
```

Once the application has been set and configured properly, the `/health` endpoint of LocalStack will indicate whether the persistence mechanism has been initialized successfully.
```json
"features": {
    "persistence": "initialized"
}
```

Otherwise, the endpoint will inform you that the mechanism is disabled.

```json
"features": {
    "persistence": "disabled"
}
```

## Technical Details

Depending on whether you use the Pro or the Community version, the persistence mechanism uses different ways to restore the application state.

### Persistence Mechanism - Community Version

When starting the Community version of LocalStack the persistence mechanism is based on a simplistic *record-and-replay* approach.
That is, API calls are recorded while the application is running, which then are replayed once the application reboots.
Whether API calls have successfully been replayed can be seen in the logs.
For instance, starting the application and creating an SQS queue with the `awslocal sqs create-queue --queue-name sample-queue` CLI command, followed by a reboot will produce the following log:

```
2021-09-27T14:38:07:INFO:localstack.utils.persistence: Restored 1 API calls from persistent file: /tmp/localstack/data/recorded_api_calls.json
```

While this approach is generic enough to cover a sizable amount of services, there are three crucial limitations:

1. Every recorded API call is literally being replayed on startup, which will inevitability lead to prolonged startup times.
2. Replaying the exact same API calls is **not** guaranteed to converge to the same state.
   Rather, diverging states is the more likely outcome.
   This limitation is not the result of any implementation details related to LocalStack, but a result of how related AWS resources reference each other.
   For instance, sending messages to an SQS queue is done by providing the queue URL.
   However, there is no guarantee that our `sample-queue` will have the same URL after a reboot, which then would result in `NonExistingQueue` during the replay of `send-message` API calls.
   For this reason, LocalStack provides no guarantees of the correctness and completeness for any state restored using the *record-and-replay* approach.
3. The state recorded this way cannot be used to create [CloudPods]({{< ref "cloud-pods" >}}.

### Persistence Mechanism - Pro Version

The persistence mechanism of the Pro version is much more sophisticated and is based on *serialized state*.
Starting the Pro version of LocalStack will traverse the `DATA_DIR` root folder recursively and directly deserialize the file into the application state.
Typically, each service has one state file for each region.

Each serialization mechanism has its own root folder.
As of now, all supported services are serialized as pickle files, except for Kinesis (which is serialized as JSON) and DynamoDB (which is serialized as an SQLite database).
This is illustrated with the diagram below.

![Structure of the DATA_DIR](datadir_structure.png)

This approach does not suffer from the same limitations as *record-and-replay*.
Restoring the state -- even for large projects -- usually only takes a few milliseconds.
Moreover, since the files store accurate snapshots of application state it can restore a state that is identical to the one prior to the reboot.

However, the limitation of this approach is that it is not quite as generic.
The *record-and-replay* approach can treat the AWS services as "black-boxes", i.e. the persistence mechanism is entirely decoupled from the underlying services, while the *serialized state* approach is coupled to the serialization mechanism of each service.
The consequence of this limitation is that, as of now, not all services have a supported persistence mechanism yet.
