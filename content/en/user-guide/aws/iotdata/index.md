---
title: "IoT Data"
linkTitle: "IoT Data"
categories: ["LocalStack Pro"]
description: Get started with IoT Data on LocalStack
---

## Introduction

IoT Data provides secure, bi-directional communication between Internet-connected things, such as sensors, actuators, embedded devices, or smart appliances, and the AWS Cloud.
It allows you to connect your devices to the cloud and interact with them using the AWS Management Console, AWS CLI, or AWS SDKs.

LocalStack allows you to use the IoT Data APIs to update, get, and delete the shadow of a thing in your local environment.
The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_iot-data/), which provides information on the extent of IoT Data integration with LocalStack.

## Getting started

This guide is designed for users new to IoT Data and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a thing, update its shadow, get its shadow, and delete its shadow using IoT Data.

### Update the shadow

You can update the shadow of a thing using the [`UpdateThingShadow`](https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateThingShadow.html) API.
Run the following command to update the shadow of a thing named `MyRPi`:

{{< command >}}
$ awslocal iot-data update-thing-shadow \
    --thing-name "MyRPi" \
    --payload "{\"state\":{\"reported\":{\"moisture\":\"okay\"}}}" \
    output.txt --cli-binary-format raw-in-base64-out
{{< /command >}}

The `output.txt` file contains the following output:

```json
{
    "state": {
        "reported": {
            "moisture": "okay"
        }
    },
    "metadata": {
        "reported": {
            "moisture": {
                "timestamp": 1724226109
            }
        }
    },
    "version": 1,
    "timestamp": 1724226109
}
```

### Get the shadow

You can get the shadow of a thing using the [`GetThingShadow`](https://docs.aws.amazon.com/iot/latest/apireference/API_GetThingShadow.html) API.
Run the following command to get the shadow:

{{< command >}}
$ awslocal iot-data get-thing-shadow \
    --thing-name "MyRPi" \
    output.txt
{{< /command >}}

The `output.txt` will contain the same output as the previous command.

### Delete the shadow

You can delete the shadow of a thing using the [`DeleteThingShadow`](https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteThingShadow.html) API.
Run the following command to delete the shadow:

{{< command >}}
$ awslocal iot-data delete-thing-shadow \
    --thing-name "MyRPi" \
    output.txt
{{< /command >}}

The `output.txt` will contain the following output:

```json
{
    "version": 1,
    "timestamp": 1724226371
}
```
