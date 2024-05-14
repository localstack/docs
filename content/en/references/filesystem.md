---
title: "Filesystem Layout"
weight: 50
description: >
  Overview of runtime directory structure
aliases:
  - /localstack/filesystem/
---

This page describes the filesystem directory layout used internally by LocalStack.

{{< callout >}}
This filesystem layout was introduced in LocalStack v1 and can be disabled by setting `LEGACY_DIRECTORIES` to `1`.
{{< /callout >}}

LocalStack uses following directory layout when running within a container.

```plaintext
/
├── etc
│   └── localstack
│       └── init
├── usr
│   └── lib
│       └── localstack
└── var
    └── lib
        └── localstack  <- the LocalStack volume directory root
            ├── cache
            ├── lib
            ├── logs
            ├── state
            └── tmp

```

## Directory contents

### LocalStack volume directory

- `/var/lib/localstack`: the [LocalStack volume](#localstack-volume) directory root
- `/var/lib/localstack/lib`: variable packages (like extensions or lazy-loaded third-party dependencies)
- `/var/lib/localstack/logs`: logs for recent LocalStack runs
- `/var/lib/localstack/state`: contains the state of services if persistence is enabled (such as OpenSearch cluster data)
- `/var/lib/localstack/tmp`: temporary data that is not expected to survive LocalStack runs (may be cleared when LocalStack starts or stops)
- `/var/lib/localstack/cache`: temporary data that is expected to survive LocalStack runs (is not cleared when LocalStack starts or stops)


### Configuration
- `/etc/localstack`: configuration directory
- `/etc/localstack/init`: root directory for [initialization hooks]({{< ref `init-hooks` >}})
<!-- For future use, not currently in use
- `/etc/localstack/conf.d`: configuration overrides
-->

### Static libraries

- `/usr/lib/localstack`: static third-party packages installed into the container images


{{< callout >}}
Previously, directories were individually configurable, e.g., via `DATA_DIR` or `HOST_TMP_DIR`.
These have been deprecated since LocalStack v1, since we now follow a directory convention.

`DATA_DIR` implicitly points to `/var/lib/localstack/state` if persistence is enabled.
Use `PERSISTENCE=1` to enable persistence.
If `DATA_DIR` is set, its value is ignored, a warning is logged and `PERSISTENCE` is set to `1`.

`HOST_TMP_FOLDER` is determined by inspecting the volume mounts and using the source of the bind mount to `/var/lib/localstack`.
{{< /callout >}}

## LocalStack volume

For LocalStack to function correctly, the LocalStack volume must be mounted from the host into the container at `/var/lib/localstack`.

### Using docker-compose

When using Docker Compose, this can be achieved using following:

```yaml
volumes:
  - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
```

`${LOCALSTACK_VOLUME_DIR}` could be an arbitrary location on the host, e.g., `./volume`.
In this case, the effective layout would be something like:

```plaintext
$ tree -L 4 ./volume
.
└── localstack
    ├── cache
    │   ├── machine.json
    │   ├── server.test.pem
    │   ├── server.test.pem.crt
    │   └── server.test.pem.key
    ├── lib
    │   └── opensearch
    │       └── 1.1.0
    ├── logs
    │   ├── localstack_infra.err
    │   └── localstack_infra.log
    ├── state
    │   └── startup_info.json
    └── tmp
        └── zipfile.4986fb95
```

### Using the CLI

When using the CLI to start LocalStack, the volume directory can be configured via the `LOCALSTACK_VOLUME_DIR`.
It should point to a directory on the host which is then automatically mounted into `/var/lib/localstack`.
The defaults are:

* Mac: `~/Library/Caches/localstack/volume`
* Linux: `~/.cache/localstack/volume`
* Windows: `%LOCALAPPDATA%\cache\localstack\volume`

## Host mode

When LocalStack is running in host mode, the system directories `/usr/lib/localstack` or `/var/lib/localstack` are not used.
Instead, the root directory is changed to `FILESYSTEM_ROOT` which defaults to `./.filesystem`, i.e. the LocalStack project root.

<!-- For further details, see https://github.com/localstack/localstack/pull/6302, https://github.com/localstack/localstack/pull/5011 -->
