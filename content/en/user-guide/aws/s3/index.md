---
title: "S3"
linkTitle: "S3"
categories: ["LocalStack Community"]
description: >
  Get started with Amazon S3 on LocalStack
aliases:
  - /aws/s3/
---

AWS S3 is a managed scalable object storage service that can be used to store any amount of data for a wide range of use cases. 

S3 is shipped with the LocalStack Community version and is [extensively supported]({{< ref "feature-coverage" >}}). Trying to run the examples in the [official AWS developer](https://docs.aws.amazon.com/s3/index.html) guide against LocalStack is a great place to start.

## Getting started

Assuming you have [`awslocal`]({{< ref "aws-cli" >}}) installed you can also try the following commands. Make sure the file you put into the bucket exists:

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
}

$ awslocal s3api put-object --bucket sample-bucket --key index.html --body index.html

{
    "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\""
}
{{< / command >}}


{{< alert title="Note" >}}
Just like AWS, LocalStack differentiates between [Path-Style and Virtual Hosted-Style Requests](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html) depending on your `Host` header for a request.

Example:

```plaintext
<bucket-name>.s3.<region>.localhost.localstack.cloud # host-style request
```

As a special case in LocalStack, leaving out `<region>` also works for the `s3.localhost.localstack.cloud` domain:

`<bucket-name>.s3.localhost.localstack.cloud` is also a host-style request.

All other requests will be considered path-style requests. It is advised to use the `s3.localhost.localstack.cloud` endpoint URL for all requests targeting S3.
{{% /alert %}}

## S3 Providers

LocalStack's S3 support is currently available via two providers: `old` and `asf`. For users, switching between the two providers has a lot of impacts. Using the `PROVIDER_OVERRIDE_S3`, you can switch between the two providers. The `old` provider is the default provider, and the `asf` provider is ASF, our new and more stable provider. The `old` provider is loaded by default, and you need to set `PROVIDER_OVERRIDE_S3=asf` to use the ASF provider. Licensed users can use `asf_pro` to use the ASF provider with the [Pro features]({{< ref "references/coverage#s3" >}}).

With v2.0, the default will be changed to ASF, but the old provider will still be available (using the feature flag with the value `legacy`), though it will be removed in further releases.

## Storage Configuration

Localstack Pro can be configured to store S3 files in specific locations on the filesystem. This can be useful in many different ways, including moving multiple files into place in one or more S3 buckets without needing to use `awslocal` to upload them. Localstack will use the path(s) specified in the `S3_DIRS` environment variable to store files within the container. Paired with a docker mount, this can be used to store files in the path of choice on the filesystem.

Paths may be specified in two different configurations. Specifying only a path will store all S3 buckets in that path:

```bash
S3_DIR=/tmp/s3-buckets
```

New S3 buckets will be created as directories with the same name as the S3 Bucket. Uploaded files will be placed within these directories.

Specifying in the following format: `<path>:<name>` will create an S3 bucket named `<name>` and utilize `<path>` for that S3 bucket's files. Multiple S3 buckets may be created at one time by using a comma to separate each path and name mapping (i.e. `<path>:<name>,<path>:<name>`).

```bash
S3_DIRS=/tmp/s3-buckets/first-bucket:my-first-bucket,/tmp/s3-buckets/second-bucket:my-second-bucket
```

In both configurations of `S3_DIRS`, if Localstack is started and the path(s) specified in `S3_DIRS` are not empty, the S3 buckets will be pre-populated with files.

## Configuring Cross-Origin Resource Sharing on S3

You can configure Cross-Origin Resource Sharing (CORS) on a LocalStack S3 bucket using AWS Command Line Interface (CLI). It would allow your local application to communicate directly with an S3 bucket in LocalStack. By default, LocalStack will apply specific CORS rules to all requests to allow you to display and access your resources through [LocalStack Web Application](https://app.localstack.cloud). If no CORS rules are configured for your S3 bucket, LocalStack will apply default rules unless specified otherwise.

To configure CORS rules for your S3 bucket, you need to have the `awslocal` wrapper installed and configured. Optionally, you can run a local web application on [localhost:3000](http://localhost:3000). Run the following command on your terminal to create your S3 bucket:

{{< command >}}
$ awslocal s3api create-bucket --bucket cors-bucket
{
    "Location": "/cors-bucket"
}
{{< / command >}}

Next, create a JSON file with the CORS configuration. The file should have the following format:

```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "POST", "PUT"],
      "AllowedOrigins": ["http://localhost:3000"],
      "ExposeHeaders": ["ETag"]
    }
  ]
}
```

{{< alert title="Note" >}}
Note that this configuration is a sample, and you can tailor it so fit your needs better, for example restricting the **AllowedHeaders** to specific ones.
{{% /alert %}}

Save the file locally with a name of your choice, for example `cors-config.json`. Run the following command to apply the CORS configuration to your S3 bucket:

{{< command >}}
$ awslocal s3api put-bucket-cors --bucket cors-bucket --cors-configuration file://cors-config.json
{{< / command >}}

You can further verify that the CORS configuration was applied successfully by running the following command:

{{< command >}}
$ awslocal s3api get-bucket-cors --bucket cors-bucket
{{< / command >}}

On applying the configuration successfully, you should see the same JSON configuration file you created earlier. Your S3 bucket is configured to allow cross-origin resource sharing, and if you try to send requests from your local application running on [localhost:3000](http://localhost:3000), they should be successful.

However, if you try to access your bucket from [LocalStack Web Application](https://app.localstack.cloud), you’ll see errors, and your bucket won’t be accessible anymore. We can edit the JSON file `cors-config.json` you created earlier with the following configuration and save it:

```json
{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "POST", "PUT", "HEAD", "DELETE"],
      "AllowedOrigins": [
        "http://localhost:3000",
        "https://app.localstack.cloud",
        "http://app.localstack.cloud"
      ],
      "ExposeHeaders": ["ETag"]
    }
  ]
}
```

You can now run the same steps as before to update the CORS configuration and verifying if it is applied correctly:

{{< command >}}
$ awslocal s3api put-bucket-cors --bucket cors-bucket --cors-configuration file://cors-config.json
$ awslocal s3api get-bucket-cors --bucket cors-bucket
{{< / command >}}

You can try again to upload files in your bucket from the [LocalStack Web Application](https://app.localstack.cloud) and it should work.
