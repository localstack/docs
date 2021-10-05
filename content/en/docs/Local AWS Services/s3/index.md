---
title: "S3"
linkTitle: "S3"
categories: ["LocalStack Community"]
description: >
  S3
---

AWS S3 is a managed scalable object storage service that can be used to store any amount of data for a wide range of use cases. 

S3 is shipped with the LocalStack Community version and is [extensively supported](../feature-coverage/). Trying to run the examples in the [official AWS developer](https://docs.aws.amazon.com/s3/index.html) guide against LocalStack is a great place to start.

Assuming you have [`awslocal`](../../integrations/aws-cli/) installed you can also try the following commands:

```bash
$ awslocal s3api create-bucket --bucket sample-bucket

{
    "Location": "/sample-bucket"
}

$ awslocal s3api list-buckets

{
    "Buckets": [
        {
            "Name": "sample-bucket",
            "CreationDate": "2021-10-05T10:48:38+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "webfile",
        "ID": "bcaf1ffd86f41161ca5fb16fd081034f"
}

$ awslocal s3api put-object --bucket sample-bucket --key index.html --body index.html

{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\""
}
```

 When working with the `SERVICES` environment variable, please make sure to include `s3` in the list of services.
For instance, to load the S3, SQS, and Kinesis service you'd pass the variable as `SERVICES=s3,sqs,kinesis`.

{{% alert title="Path-Style Requests versus Virtual Hosted-Style Requests " color="info" %}}
Just like AWS does, LocalStack differentiates the same way between [Path-Style Requests and Virtual Hosted-Style Request](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html). The only difference being that, `localhost.localstack.cloud` is treated as a special case for a Path-Style request. 
{{% /alert %}}
