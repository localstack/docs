---
title: Elemental MediaStore
linkTitle: Elemental MediaStore
description: >
  Get started with Elemental MediaStore on LocalStack
---

## Introduction

LocalStack supports Elemental MediaStore via the Pro/Team offering, allowing you to use the Elemental MediaStore APIs in your local environment.
The supported APIs are available on our API Coverage Page, which provides information on the extent of Elemental MediaStore integration with LocalStack.

## Getting started

This guide is designed for users new to Elemental MediaStore and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.
We will walk through creating a container, uploading and downloading an asset.

### Create a container

A container can be created with the `create-container` command.
The response contains the `Endpoint` value which should be used in subsequent requests.

{{< command >}}
$ awslocal mediastore create-container --container-name mycontainer
{
    "Container": {
        "Endpoint": "http://mediastore-mycontainer.mediastore.localhost.localstack.cloud:4566",
        "CreationTime": "2023-08-11T09:43:19.982754+01:00",
        "ARN": "arn:aws:mediastore:us-east-1:000000000000:container/mycontainer",
        "Name": "mycontainer"
    }
}
{{< / command >}}

### Upload an asset

In order to upload a file (in this case, `myfile.txt`) to the container, use the `put-object` method.
This will upload the file to the path `/myfolder/myfile.txt` in the container.
Here we pass the `endpoint` from the previous step.

{{< command >}}
$ awslocal mediastore-data put-object \
    --endpoint http://mediastore-mycontainer.mediastore.localhost.localstack.cloud:4566 \
    --body myfile.txt \
    --path /myfolder/myfile.txt \
    --content-type binary/octet-stream
{
    "ContentSHA256": "",
    "ETag": "\"111d787cdcfcc358fd15684131f586d8\""
}
{{< / command >}}

### Download an asset

In order to fetch the file back from the container, use the `get-object` method.
We specify the endpoint, path to download, and the output file (`/tmp/out.txt`), and the file is available at the output path.

{{< command >}}
$ awslocal mediastore-data get-object \
    --endpoint http://mediastore-mycontainer.mediastore.localhost.localstack.cloud:4566 \
    --path /myfolder/myfile.txt \
    /tmp/out.txt
{
    "ContentLength": "716",
    "ContentType": "binary/octet-stream",
    "ETag": "\"111d787cdcfcc358fd15684131f586d8\"",
    "LastModified": "2023-08-11T08:43:20+00:00",
    "StatusCode": 200
}
{{< / command >}}

## Troubleshooting

The Elemental MediaStore service requires use of a custom HTTP/HTTPS endpoint.
If you encounter any problems, please refer to our [Networking documentation]({{< ref "references/network-troubleshooting" >}}).
