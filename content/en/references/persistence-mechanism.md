---
title: "Persistence Mechanism"
weight: 5
description: >
  Configuration and internals of LocalStack persistence mechanism
aliases:
  - /localstack/persistence-mechanism/
---

## Overview

The persistence mechanism is essentially a "pause and resume" feature for your LocalStack application state.
For instance, you may want to run consecutive integration tests where each test loads in a different context but depends on the state produced by a previous test.
Commonly, you may simply have a local development server that relies on a non-ephemeral application state.

While the persistence mechanism covers most services, not all of them are supported yet.
Please make sure to check the [feature coverage page]({{< ref "feature-coverage" >}}) to see whether your desired services are covered.

To enable the persistence mechanism simply set the `PERSISTENCE` environment variable to `1`.
Note that persistence is a Pro feature, therefore the `LOCALSTACK_API_KEY` must also be set.
 
```yaml
    ...
    environment:
      - LOCALSTACK_API_KEY=...
      - PERSISTENCE=1
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
```

Once the application has been set and configured properly, the `/_localstack/health` endpoint of LocalStack will indicate whether the persistence mechanism has been initialized successfully.
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

The persistence mechanism in LocalStack Pro is based on [Pickle][pickle] object serialization.

On service invocation, LocalStack traverses the state directory and deserializes state files and loads it into the memory.
Each service has a single state file for all regions and accounts.
LocalStack stores and Moto backend objects are serialized separately.

Certain services may keep additional data files apart from serialized states.
For instance, Kinesis persists some data in form of JSON while DynamoDB serializes a SQLite database.

```
/var/lib/localstack/state    # state directory
├── api_states
│   ├── dynamodb
│   │   └── store.state      # serialised LocalStack stores
│   ├── ec2
│   │   └── backend.state    # serialised Moto backends
│   ├── iot
│   │   └── store.state
│   └── lambda
│       └── store.state
├── dynamodb
│   ├── 000000000000_eu-central-1.db
│   └── 886002141588_us-east-1.db
└── kinesis
    ├── 000000000000.json
    └── 886002141588.json
```

Restoring the persisted state usually only takes a few milliseconds, even for large projects.
Moreover, since the files store accurate snapshots of the application state, they can restore a state that is identical to the one before restarting the instance.

[pickle]: https://docs.python.org/3/library/pickle.html
