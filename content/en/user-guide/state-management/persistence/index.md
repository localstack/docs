---
title: "Persistence"
weight: 2
description: >
  Internals of LocalStack persistence mechanism
aliases:
  - /localstack/persistence-mechanism/
  - /references/persistence-mechanism/
tags: ["Pro image"]
---

## Introduction

LocalStack's Persistence mechanism enables the saving and restoration of the entire LocalStack state, including all AWS resources and data, on your local machine. It functions as a "pause and resume" feature, allowing you to take a snapshot of your LocalStack instance and save this data to disk. This mechanism ensures a quick and efficient way to preserve and continue your work with AWS resources locally.

## Configuration

To start snapshot-based persistence, launch LocalStack with the configuration option `PERSISTENCE=1`. This setting instructs LocalStack to save all AWS resources and their respective application states into the LocalStack Volume Directory. Upon restarting LocalStack, you'll be able to resume your activities exactly where you left off.

{{< tabpane lang="bash" >}}
{{< tab header="LocalStack CLI" lang="bash" >}}
LOCALSTACK_AUTH_TOKEN=... PERSISTENCE=1 localstack start
{{< /tab >}}
{{< tab header="Docker Compose" lang="yaml" >}}
    ...
    image: localstack/localstack-pro
    environment:
      - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?}
      - PERSISTENCE=1
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
{{< /tab >}}
{{< tab header="Docker" lang="bash" >}}
docker run \
  -e LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?} \
  -e PERSISTENCE=1 \
  -v ./volume:/var/lib/localstack \
  -p 4566:4566 \
  localstack/localstack-pro
{{< /tab >}}
{{< /tabpane >}}

{{< callout >}}
Snapshots may not be compatible across different versions of LocalStack.
It is possible that snapshots from older versions can be restored, but there are no guarantees to whether LocalStack will start into a consistent state.
We are actively working on a solution for this problem.
{{< /callout >}}

### Save strategies

LocalStack takes point-in-time snapshot of its state and dumps them to disk.
There are four strategies that you can choose from that govern when these snapshots are taken.
You can select a particular save strategy by setting `SNAPSHOT_SAVE_STRATEGY=<strategy>`.

* **`ON_REQUEST`**: On every AWS API call that potentially modifies the state of a service, LocalStack will save the state of that service.
  This strategy minimizes the chance for data loss, but also has significant performance implications. The service has to be locked during snapshotting, meaning that any requests to the particular AWS service will be blocked until the snapshot is complete.  In many cases this is just a few milliseconds, but can become significant in some services.
* **`ON_SHUTDOWN`**: The state of all services are saved during the shutdown phase of LocalStack.
  This strategy has zero performance impact, but is not good when you want to minimize the chance for data loss. Should LocalStack for some reason not shut down properly or is terminated before it can finalize the snapshot, you may be left with an incomplete state on disk.
* **`SCHEDULED`** (**default**): Saves at regular intervals the state of all the services that have been modified since the last snapshot.
  By default, the flush interval is 15 seconds. It can be configured via the `SNAPSHOT_FLUSH_INTERVAL` configuration variable.
  This is a compromise between `ON_REQUEST` and `ON_SHUTDOWN` in terms of performance and reliability.
* **`MANUAL`**: Turns off automatic snapshotting and gives you control through the internal state endpoints.

### Load Strategies

Similarly, you can configure when LocalStack should restore the state snapshots, by using `SNAPSHOT_LOAD_STRATEGY=<strategy>`.

* **`ON_REQUEST`**: (**default**) The state is loaded lazily when the service is requested. This maintains LocalStack's lazy-loading behavior for AWS services.
* **`ON_STARTUP`**: The state of all services in the snapshot is restored when LocalStack starts up. This means that services that have stored state are also started on LocalStack start, which will increase the startup time, but also give you immediate feedback whether the state was restored correctly.
* **`MANUAL`**: Turns off automatic loading of snapshots and gives you control through the internal state endpoints.

### Endpoints

As mentioned, with the `MANUAL` save or load strategy you can trigger snapshotting manually when it best suits your application flow.

* `POST /_localstack/state/<service>/save` take a snapshot the given service
* `POST /_localstack/state/<service>/load` load the most recent snapshot of the given service

For example, a snapshot for a particular service (e.g., `s3`) can be triggered by running the following command. The service name refers to the AWS service code.

{{< command >}}
$ curl -X POST http://localhost:4566/_localstack/state/s3/save
{{< /command >}}

It is also possible to take and load a snapshot of all the services at once. We provide the following endpoints:

* `POST /_localstack/state/save`
* `POST /_localstack/state/load`

The response streams line by line the service that has been saved/loaded and the status of the operation.

{{< command >}}
$ curl -X POST localhost:4566/_localstack/state/save
<disable-copy>
{"service": "sqs", "status": "ok"}
{"service": "s3", "status": "ok"}
</disable-copy>
{{< /command >}}

## Service coverage

Although we are working to support both snapshot-based persistence and Cloud pods for all AWS services,
there are some common issues, known limitations, and also services that are not well tested for persistence support.
An overview is available [here]({{<ref "user-guide/state-management/support">}}).

Please help us improve persistence support by reporting bugs on our [GitHub issue tracker](https://github.com/localstack/localstack/issues/new/choose).

## Technical Details

State persistence in LocalStack works on a per-service basis and uses a custom state serialization protocol based on [Python's pickle mechanism](https://docs.python.org/3/library/pickle.html).
Some services also store application-specific data, which we call _assets_.
For example, when you start an RDS PostgreSQL database, LocalStack not only stores the RDS resource information, but also the PostgreSQL data.
Another example is Kinesis, which persists some data in form of JSON objects per account, or DynamoDB that serializes its stat into an SQLite database per account and region.

The current LocalStack snapshot is stored into `/var/lib/localstack/state`, and separated into `api_states` (LocalStack internal state), and assets (one directory per service).
Here is what this looks like:

```plaintext
/var/lib/localstack/state    # state directory
├── api_states               # serialized LocalStack stores
│   ├── dynamodb
│   │   └── store.state
│   ├── ec2
│   │   └── backend.state
│   ├── iot
│   │   └── store.state
│   └── lambda
│       └── store.state
├── dynamodb                # dynamodb assets
│   ├── 000000000000_eu-central-1.db
│   └── 886002141588_us-east-1.db
└── kinesis                 # kinesis assets
    ├── 000000000000.json
    └── 886002141588.json
```

To load a snapshot, LocalStack traverses the state directory and deserializes state files to loads them into the memory.
When we restore server backends (like an RDS server or DynamoDB server), we make sure that they are configured to use the state stored in the respective asset directory.

When LocalStack saves snapshots, it has to lock the particular service to avoid state pollution.
That means that, while a snapshot for a particular service is created, all requests to the service are blocked.
Depending on what you are building, you may find this behavior is slowing down your application.
In most cases, the `ON_SHUTDOWN` save strategy should solve this problem.
