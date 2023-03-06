---
title: "CloudFront"
linkTitle: "CloudFront"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS CloudFront on LocalStack
aliases:
  - /aws/cloudfront/
---

LocalStack Pro supports creation of local CloudFront distributions, which allows you to transparently access your applications and file artifacts via CloudFront URLs like `https://abc123.cloudfront.net`.

For example, take the following simple example which creates an S3 bucket, puts a small text file `hello.txt` to the bucket, and then creates a CloudFront distribution which makes the file accessible via a `https://abc123.cloudfront.net/hello.txt` proxy URL (where `abc123` is a placeholder for the real distribution ID):

{{< command >}}
$ awslocal s3 mb s3://abc123
$ echo 'Hello World' > /tmp/hello.txt
$ awslocal s3 cp /tmp/hello.txt s3://abc123/hello.txt --acl public-read
$ domain=$(awslocal cloudfront create-distribution \
   --origin-domain-name abc123.s3.amazonaws.com | jq -r '.Distribution.DomainName')
$ curl -k https://$domain/hello.txt
{{< / command >}}

{{< alert title="Note" >}}
In order for CloudFront to be fully functional, your local DNS setup needs to be properly configured. See the section on [configuring the local DNS server]({{< ref "user-guide/tools/transparent-endpoint-injection/dns-server" >}}) for details.
{{< /alert >}}

{{< alert title="Note">}}
In the code example above, the last command (`curl https://$domain/hello.txt`) may temporarily fail with a warning message `Could not resolve host`. This is due to the fact that operating systems use different DNS caching strategies, and it may take some time for the CloudFront distribution's DNS name (e.g., `abc123.cloudfront.net`) to become available in the system. Usually after a few retries the command should work, though. Note that a similar behavior can also be observed in the real AWS - CloudFront DNS names can also take up to 10-15 minutes to propagate across the network.
{{< /alert >}}

## Using custom URLs

LocalStack Pro supports the use of an alternate domain name, also known as a CNAME or as a custom domain name, to access your applications and file artifacts instead of using the domain name that CloudFront generates for your distribution.

To do so, the custom domain name must be set up in your local DNS server first. You can further add the desired domain name as an alias for the target distribution. To achieve this, you will need to provide the `Aliases` field in the `--distribution-config` option while creating or updating a distribution. The format of this structure is similar to what is used in [AWS CloudFront options](https://docs.aws.amazon.com/cli/latest/reference/cloudfront/create-distribution.html#options).

The following example shows two domains being specified as `Aliases` for a distribution.
Please consider that a full configuration would require other values relevant to the
distribution beside these shown in this example. They were omited here for brevity.

{{< command >}}
--distribution-config {...'Aliases':'{'Quantity':2, 'Items': ['custom.domain.one', 'customDomain.two']}'...}
{{< / command >}}

{{< alert title="Note">}}
In order for CloudFront to be fully functional, your local DNS setup needs to be properly configured. See the section on [configuring the local DNS server]({{< ref "user-guide/tools/transparent-endpoint-injection/dns-server" >}}) for details.
{{< /alert >}}
