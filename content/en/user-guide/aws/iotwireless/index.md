---
title: "IoT Wireless"
linkTitle: "IoT Wireless"
description: Get started with IoT Wireless on LocalStack
tags: ["Pro image"]
---

## Introduction

AWS IoT Wireless is a managed service that enables customers to connect and manage wireless devices. The service provides a set of APIs to manage wireless devices, gateways, and destinations. IoT Wireless supports LoRaWAN and Cellular connectivity options.

LocalStack allows you to use the IoT Wireless APIs in your local environment from creating wireless devices and gateways. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_iotwireless/), which provides information on the extent of IoT Wireless's integration with LocalStack.

## Getting started

This guide is designed for users new to IoT Wireless and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to use IoT Wireless to create wireless devices and gateways with the AWS CLI.

### Create a Wireless Device

You can create a wireless device using the [`CreateWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/2020-11-22/API_CreateWirelessDevice.html) API. Run the following command to create a wireless device:

{{< command >}}
$ awslocal iotwireless create-device-profile
{{< / command >}}

The following output would be retrieved:

```bash
{
    "Id": "b8a8e3a8"
}
```

You can list the device profiles using the [`ListDeviceProfiles`](https://docs.aws.amazon.com/iot-wireless/2020-11-22/API_ListDeviceProfiles.html) API. Run the following command to list the device profiles:

{{< command >}}
$ awslocal iotwireless list-device-profiles
{{< / command >}}

The following output would be retrieved:

```json
{
    "DeviceProfileList": [
        {
            "Id": "b8a8e3a8"
        }
    ]
}
```

### Create a Wireless device

You can create a wireless device using the [`CreateWirelessDevice`](https://docs.aws.amazon.com/iot-wireless/2020-11-22/API_CreateWirelessDevice.html) API. Run the following command to create a wireless device:

{{< command >}}
$ awslocal iotwireless create-wireless-device \
    --cli-input-json file://input.json
{{< / command >}}

The `input.json` file contains the following content:

```json
{
    "Description": "My LoRaWAN wireless device",
    "DestinationName": "IoTWirelessDestination",
    "LoRaWAN": {
        "DeviceProfileId": "ab0c23d3-b001-45ef-6a01-2bc3de4f5333",
        "ServiceProfileId": "fe98dc76-cd12-001e-2d34-5550432da100",
        "OtaaV1_1": {
            "AppKey": "3f4ca100e2fc675ea123f4eb12c4a012",
            "JoinEui": "b4c231a359bc2e3d",
            "NwkKey": "01c3f004a2d6efffe32c4eda14bcd2b4"
        },
        "DevEui": "ac12efc654d23fc2"
    },
    "Name": "SampleIoTWirelessThing",
    "Type": "LoRaWAN"
}
```

You can list the wireless devices using the [`ListWirelessDevices`](https://docs.aws.amazon.com/iot-wireless/2020-11-22/API_ListWirelessDevices.html) API. Run the following command to list the wireless devices:

{{< command >}}
$ awslocal iotwireless list-wireless-devices
{{< / command >}}

The following output would be retrieved:

```json
{
    "WirelessDeviceList": [
        {
            "Id": "0bca2fe2",
            "Type": "LoRaWAN",
            "Name": "SampleIoTWirelessThing",
            "DestinationName": "IoTWirelessDestination",
            "LoRaWAN": {
                "DevEui": "ac12efc654d23fc2"
            }
        }
    ]
}
```

### Create a Wireless Gateway

You can create a wireless gateway using the [`CreateWirelessGateway`](https://docs.aws.amazon.com/iot-wireless/2020-11-22/API_CreateWirelessGateway.html) API. Run the following command to create a wireless gateway:

{{< command >}}
$ awslocal iotwireless create-wireless-gateway \
    --lorawan GatewayEui="a1b2c3d4567890ab",RfRegion="US915" \
    --name "myFirstLoRaWANGateway" \
    --description "Using my first LoRaWAN gateway"
{{< / command >}}

The following output would be retrieved:

```bash
{
    "Id": "e519dc4e"
}
```

You can list the wireless gateways using the [`ListWirelessGateways`](https://docs.aws.amazon.com/iot-wireless/2020-11-22/API_ListWirelessGateways.html) API. Run the following command to list the wireless gateways:

{{< command >}}
$ awslocal iotwireless list-wireless-gateways
{{< / command >}}

The following output would be retrieved:

```bash
{
    "WirelessGatewayList": [
        {
            "Id": "e519dc4e",
            "Name": "myFirstLoRaWANGateway",
            "Description": "Using my first LoRaWAN gateway",
            "LoRaWAN": {
                "GatewayEui": "a1b2c3d4567890ab",
                "RfRegion": "US915"
            }
        }
    ]
}
```
