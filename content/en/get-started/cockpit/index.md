---
title: "LocalStack Cockpit"
weight: 10
categories: ["LocalStack Cockpit"]
description: >
  Get a desktop experience and work with your local LocalStack instance via the UI.
---

## Features
- Start and Stop your LocalStack instance with a click of a button
- See the current status of your LocalStack instance
- Easily accessible via a tray icon
- Initialization checks to see if your setup is correct
- Quick links to our website, documentation and the Web App
- See runtime and environment information on the info page
- See available services and their status on the service page
- See log information of the LocalStack instance
- Directly manage and use your profiles (run configurations)
- Quickly give feedback and report issues

## Prerequisites
- [`localstack-cli`]({{< ref "get-started#localstack-cli" >}}) is installed and to be on your path
    - CLI version ≥ 0.13.0
    - check in terminal: `localstack --version`

## Known issues

- MacOS ≤ v10 not supported yet.

## Report issues

If you experience a problem, have feedback or a feature request for us, please [submit an issue](https://github.com/localstack/cockpit/issues).
Ideally add your log files, so that we can investigate into your problem more easily.

Logs folder:

- Linux: `~/.config/localstack-cockpit/logs/`
- macOS: `~/Library/Logs/localstack-cockpit/`
- Windows: `%USERPROFILE%\AppData\Roaming\localstack-cockpit\logs\`
