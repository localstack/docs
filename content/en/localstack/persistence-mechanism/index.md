---
title: "Persistence Mechanism"
weight: 5
description: >
  How the LocalStack persistence mechanism works and how you can configure it.
---

The persistence mechanism is essentially a "pause and resume" feature for your LocalStack application state.
For instance, you may want to run consecutive integration tests where each test loads in a different context but depends on the state produced by a previous test.
Commonly, you may simply have a local development server that relies on a non-ephemeral application state.

While the persistence mechanism covers most services, not all of them are supported yet.
Please make sure to check the [feature coverage page]({{< ref "feature-coverage" >}}) to see whether your desired services are covered.
While in the past we supported a version of persistence -- available in the _Community_ version -- based on a *record-and-replay* approach (basically, storing API calls and re-running them on restart), we discontinued this feature since [0.13.1](https://github.com/localstack/localstack/releases/tag/v0.13.1).
Therefore, please note that persistence in LocalStack, as currently intended, is a _Pro_ only feature (more on that in the [Technical Details]({{< ref "#technical-details" >}}) section).

To enable the persistence mechanism simply set the `PERSISTENCE` environment variable to `1`.
 
```yaml
    ...
    environment:
      - LOCALSTACK_API_KEY=...
      - PERSISTENCE=1
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
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

The persistence mechanism in LocalStack Pro is a sophisticated approach based on *serialized state*.
Starting the Pro version of LocalStack will traverse the state directory root folder recursively and directly deserialize the file into the application state.

Typically, each service has one state file for each region.

Each serialization mechanism has its root folder.
As of now, all supported services are serialized as pickle files. 
Particular services, in addition to their pickled files, can serialize additional artifacts.
For instance, Kinesis persists some data in form of JSON while DynamoDB serializes a SQLite database.
This is illustrated in the diagram below.

![Structure of the state directory](datadir_structure.png)

Restoring the state -- even for large projects -- usually only takes a few milliseconds.
Moreover, since the files store accurate snapshots of the application state, they can restore a state that is identical to the one before restarting the instance.