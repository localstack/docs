---
title: "S3"
linkTitle: "S3"
categories: ["LocalStack Community"]
description: >
  S3
---

AWS S3 is a managed scalable object storage service that can be used to store any amount of data for a wide range of use cases. 

S3 is shipped with the LocalStack Community version and is [extensively supported]({{< ref "feature-coverage" >}}). Trying to run the examples in the [official AWS developer](https://docs.aws.amazon.com/s3/index.html) guide against LocalStack is a great place to start.

Assuming you have [`awslocal`]({{< ref "aws-cli" >}}) installed you can also try the following commands:

{{< command >}}
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
{{< / command >}}

 When working with the `SERVICES` environment variable, please make sure to include `s3` in the list of services.
For instance, to load the S3, SQS, and Kinesis service you'd pass the variable as `SERVICES=s3,sqs,kinesis`.

{{% alert title="Path-Style Requests versus Virtual Hosted-Style Requests " color="info" %}}
Just like AWS, LocalStack differentiates between [Path-Style and Virtual Hosted-Style Requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html) depending on your `Host` header for a request.

Example:

```
<bucket-name>.s3.<region>.localhost.localstack.cloud # host-style request
<bucket-name>.s3.<region>.amazonaws.com # host-style request
```

As a special case in LocalStack, leaving out `.s3.<region>` also works for the `localhost.localstack.cloud` domain:

`<bucket-name>.localhost.localstack.cloud` is also a host-style request.

All other requests will be considered path-style requests.
{{% /alert %}}
