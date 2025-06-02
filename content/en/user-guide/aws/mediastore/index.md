---
title: Elemental MediaStore
linkTitle: Elemental MediaStore
description: Get started with Elemental MediaStore on LocalStack
tags: ["Ultimate"]
---

## Introduction

MediaStore is a scalable and highly available object storage service designed specifically for media content.
It provides a reliable way to store, manage, and serve media assets, such as audio, video, and images, with low latency and high performance.
MediaStore seamlessly integrates with other AWS services like Elemental MediaConvert, Elemental MediaLive, Elemental MediaPackage, and CloudFront.

LocalStack allows you to use the Elemental MediaStore APIs as a high-performance storage solution for media content in your local environment.
The supported APIs are available on our [API Coverage Page]({{< ref "coverage_mediastore" >}}), which provides information on the extent of Elemental MediaStore integration with LocalStack.

## Getting started

This guide is designed for users new to Elemental MediaStore and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how you can create a MediaStore container, upload an asset, and download the asset.

### Create a container

You can create a container using the [`CreateContainer`](https://docs.aws.amazon.com/mediastore/latest/apireference/API_CreateContainer.html) API.
Run the following command to create a container and retrieve the the `Endpoint` value which should be used in subsequent requests:

{{< command >}}
$ awslocal mediastore create-container --container-name mycontainer
{{< / command >}}

You should see the following output:

```bash
{
    "Container": {
        "Endpoint": "http://mediastore-mycontainer.mediastore.localhost.localstack.cloud:4566",
        "CreationTime": "2023-08-11T09:43:19.982754+01:00",
        "ARN": "arn:aws:mediastore:us-east-1:000000000000:container/mycontainer",
        "Name": "mycontainer"
    }
}
```

### Upload an asset

To upload a file named `myfile.txt` to the container, utilize the [`PutObject`](https://docs.aws.amazon.com/mediastore/latest/apireference/API_PutObject.html) API.
This action will transfer the file to the specified path, `/myfolder/myfile.txt`, within the container.
Provide the `endpoint` obtained in the previous step for the operation to be successful.
Run the following command to upload the file:

{{< command >}}
$ awslocal mediastore-data put-object \
    --endpoint http://mediastore-mycontainer.mediastore.localhost.localstack.cloud:4566 \
    --body myfile.txt \
    --path /myfolder/myfile.txt \
    --content-type binary/octet-stream
{{< / command >}}

You should see the following output:

```bash
{
    "ContentSHA256": "",
    "ETag": "\"111d787cdcfcc358fd15684131f586d8\""
}
```

### Download an asset

To retrieve the file from the container, utilize the [`GetObject`](https://docs.aws.amazon.com/mediastore/latest/apireference/API_GetObject.html) API.
In this process, you need to specify the endpoint, the path for downloading the file, and the location where the output file, such as `/tmp/out.txt`, will be stored.
The downloaded file will then be accessible at the specified output path.
Run the following command to download the file:

{{< command >}}
$ awslocal mediastore-data get-object \
    --endpoint http://mediastore-mycontainer.mediastore.localhost.localstack.cloud:4566 \
    --path /myfolder/myfile.txt \
    /tmp/out.txt
{{< / command >}}

You should see the following output:

```bash
{
    "ContentLength": "716",
    "ContentType": "binary/octet-stream",
    "ETag": "\"111d787cdcfcc358fd15684131f586d8\"",
    "LastModified": "2023-08-11T08:43:20+00:00",
    "StatusCode": 200
}
```

## Troubleshooting

The Elemental MediaStore service requires the use of a custom HTTP/HTTPS endpoint.
In case you encounter any issues, please consult our [Networking documentation]({{< ref "references/network-troubleshooting" >}}) for assistance.
