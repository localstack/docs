---
title: "Filesystem Layout"
weight: 5
description: >
  Overview of runtime directory structure
---

This page describes the filesystem directory layout used internally by LocalStack.

{{< alert title="Information" color="primary">}}
This filesystem hierarchy was introduced in LocalStack v1 and can be disabled by setting `LEGACY_DIRECTORIES` to `1`.
{{< /alert >}}

LocalStack uses following directories when running within a container.

- `/var/lib/localstack`: the root directory
- `/var/lib/localstack/lib`: variable packages (like lazy-loaded third-party dependencies)
- `/var/lib/localstack/logs`: logs for recent LocalStack runs
- `/var/lib/localstack/state`: persistence state of third-party services (or what is sometimes called 'data' or 'assets', e.g., Opensearch cluster data)
- `/var/lib/localstack/tmp`: temporary data that is not expected to survive LocalStack runs (may be cleared when LocalStack starts)
- `/var/lib/localstack/cache`: temporary data that is expected to survive LocalStack runs (is not cleared when LocalStack starts)
- `/usr/lib/localstack`: static third-party packages installed into the container images
<!-- For future use, not currently in use
- `/etc/localstack`: configuration directory
- `/etc/localstack/conf.d`: configuration overrides
- `/etc/localstack/init`: initialisation hooks
-->

In order to persist data across runs, these directories must be mounted from the host into the container.
For Docker Compose, this can be achieved using following:

```yaml
volumes:
  - "${TMPDIR}/localstack:/var/lib/localstack"
```

`${TMPDIR}` could be an arbitrary location on the host e.g. `/some/path/`.
In this case the effective layout would be something like:

```
$ tree -L 4 /some/path/localstack
.
└── localstack
    ├── cache
    │   ├── machine.json
    │   ├── server.test.pem
    │   ├── server.test.pem.crt
    │   └── server.test.pem.key
    ├── lib
    │   └── opensearch
    │       └── 1.1.0
    ├── logs
    │   ├── localstack_infra.err
    │   └── localstack_infra.log
    ├── state
    │   ├── recorded_api_calls.json
    │   └── startup_info.json
    └── tmp
        └── zipfile.4986fb95
```


{{< alert title="Warning" color="warning">}}
`DATA_DIR` and `HOST_TMP_DIR` are deprecated since LocalStack v1.

`DATA_DIR` implicitly points to `/var/lib/localstack/state`.
Use `PERSISTENCE=1` to enable persistence.
If `DATA_DIR` is set, its value is ignored, a warning is logged and `PERSISTENCE` is set to `1`.

`HOST_TMP_FOLDER` is determined by inspecting the volume mounts and using the source of the bind mount to `/var/lib/localstack`.
{{< /alert >}}


When LocalStack is running in host mode, the system `/usr/lib/localstack` or `/var/lib/localstack` are not used.
Instead, the root directory is changed to `FILESYSTEM_ROOT` which defaults to `./.filesystem`, i.e. the LocalStack project root.

<!-- For further details, see https://github.com/localstack/localstack/pull/6302, https://github.com/localstack/localstack/pull/5011 -->
