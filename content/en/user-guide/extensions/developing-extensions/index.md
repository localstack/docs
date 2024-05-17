---
title: "Developing extensions"
weight: 3
description: >
  How to develop your own extensions
tags: ["Pro image"]
---

## Introduction

This section provides a brief overview of how to develop your own extensions.

## Extensions API

LocalStack exposes a Python API for building extensions that can be found in the core codebase in [`localstack.extensions.api`](https://github.com/localstack/localstack/tree/master/localstack/extensions/api).

The basic interface to implement is as follows:

```python
class Extension(BaseExtension):
    """
    An extension that is loaded into LocalStack dynamically. The method
    execution order of an extension is as follows:

    - on_extension_load
    - on_platform_start
    - update_gateway_routes
    - update_request_handlers
    - update_response_handlers
    - on_platform_ready
    - on_platform_shutdown
    """

    namespace: str = "localstack.extensions"
    """The namespace of all basic localstack extensions."""

    name: str
    """The unique name of the extension set by the implementing class."""

    def on_extension_load(self):
        """
        Called when LocalStack loads the extension.
        """
        pass

    def on_platform_start(self):
        """
        Called when LocalStack starts the main runtime.
        """
        pass

    def update_gateway_routes(self, router: Router[RouteHandler]):
        """
        Called with the Router attached to the LocalStack gateway. Overwrite this to add or update routes.
        :param router: the Router attached in the gateway
        """
        pass

    def update_request_handlers(self, handlers: CompositeHandler):
        """
        Called with the custom request handlers of the LocalStack gateway. Overwrite this to add or update handlers.
        :param handlers: custom request handlers of the gateway
        """
        pass

    def update_response_handlers(self, handlers: CompositeResponseHandler):
        """
        Called with the custom response handlers of the LocalStack gateway. Overwrite this to add or update handlers.
        :param handlers: custom response handlers of the gateway
        """
        pass

    def on_platform_ready(self):
        """
        Called when LocalStack is ready and the Ready marker has been printed.
        """
        pass

    def on_platform_shutdown(self):
        """
        Called when LocalStack is shutting down. Can be used to close any resources (threads, processes, sockets, etc.).

        Added in v1.4
        """
        pass
```

A minimal example would look like this:

```python
import logging
from localstack.extensions.api import Extension

LOG = logging.getLogger(__name__)

class ReadyAnnouncerExtension(Extension):
    name = "my_ready_announcer"

    def on_platform_ready(self):
        LOG.setLevel(logging.INFO)
    	LOG.info("my plugin is loaded and localstack is ready to roll!")
```


{{< callout >}}
A note on importing LocalStack modules: since extensions run in the same Python process as the LocalStack runtime,
you can also import other LocalStack modules outside the `localstack.extensions.api` module, and work with them.
However, be aware that these modules are not part of our public API, and can change even with patch versions any time.
Your extension may break in unexpected ways, and we cannot provide support for internal APIs.
{{</callout>}}

## Packaging extensions

Your extensions needs to be packaged as a Python distribution with a
`setup.cfg` or `setup.py` config. LocalStack uses the
[Plux](https://github.com/localstack/plux) code loading framework to load your
code from a Python [entry point](https://packaging.python.org/en/latest/specifications/entry-points/).
You can either use Plux to discover the entrypoints from your code when
building and publishing your distribution, or manually define them as in the
example below.

A minimal `setup.cfg` for the extension above could look like this:

```ini
[metadata]
name = localstack-extension-ready-announcer
description = LocalStack extension that logs when LocalStack is ready to receive requests
author = Your Name
author_email = your@email.com
url = https://link-to-your-project

[options]
zip_safe = False
packages = find:
install_requires =
    localstack>=1.0.0

[options.entry_points]
localstack.extensions =
    my_ready_announcer = localstack_announcer.extension:ReadyAnnouncerExtension
```

The entry point group is the Plux namespace `locastack.extensions`, and the
entry point name is the plugin name `my_ready_announcer`. The object
reference points to the plugin class.


## Using the extensions developer CLI

The extensions CLI has a set of developer commands that allow you to create new extensions, and toggle local dev mode for extensions.
Extensions that are toggled for developer mode will be mounted into the localstack container so you don't need to re-install them every time you change something.

```console
Usage: localstack extensions dev [OPTIONS] COMMAND [ARGS]...

  Developer tools for developing Localstack extensions

Options:
  --help  Show this message and exit.

Commands:
  disable  Disables an extension on the host for developer mode.
  enable   Enables an extension on the host for developer mode.
  list     List LocalStack extensions for which dev mode is enabled.
  new      Create a new LocalStack extension from the official extension...
```

## Creating your first extension

### Creating an extension from a template

First, create a new extension from a template.
To use `localstack extensions dev new`, you will also need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter) via `pip install cookiecutter`.

{{< command >}}
$ localstack extensions dev new
project_name [My LocalStack Extension]:
project_short_description [All the boilerplate you need to create a LocalStack extension.]:
project_slug [my-localstack-extension]:
module_name [my_localstack_extension]:
full_name [Jane Doe]:
email [jane@example.com]:
github_username [janedoe]:
version [0.1.0]:
{{< / command >}}


This will create a new Python project with the following layout:

```
my-localstack-extension
├── Makefile
├── my_localstack_extension
│  ├── extension.py
│  └── __init__.py
├── README.md
├── setup.cfg
└── setup.py
```

Then run `make install` in the newly created project to make a distribution package.

### Start LocalStack with the extension

To start LocalStack with the extension in dev mode, first enable it by running:

{{< command >}}
$ localstack extensions dev enable ./my-localstack-extension
{{< / command >}}


Then, start LocalStack with `EXTENSION_DEV_MODE=1`

{{< command >}}
$ EXTENSION_DEV_MODE=1 LOCALSTACK_AUTH_TOKEN=... localstack start
{{< / command >}}

In the LocalStack logs you should then see something like:
```
==================================================
👷 LocalStack extension developer mode enabled 🏗
- mounting extension /opt/code/extensions/my-localstack-extension
Resuming normal execution, ...
==================================================
```

Now, when you make changes to your extensions, you just need to restart LocalStack and the changes will be picked up by LocalStack automatically.

## Advertise your extension

Once your extension is ready to be used, release it on a public GitHub repository.
To make your extension easily installable for everyone generate an extension badge for your extension on this page.
The resulting badge should look like this <img src="https://localstack.cloud/gh/extension-badge.svg">.
You can create a one-click installer for your extension using our [Extension Installer](https://app.localstack.cloud/extensions/remote).

{{< figure src="extension-installer.png" >}}

<!-- TODO: add screenshot of installer with a specific extension, currently doesn't work -->
