---
title: "CloudFront"
linkTitle: "CloudFront"
categories: ["LocalStack Pro"]
description: >
  CloudFront
---

LocalStack Pro supports creation of local CloudFront distributions, which allows you to transparently access your applications and file artifacts via CloudFront URLs like `https://abc123.cloudfront.net`.

For example, take the following simple example which creates an S3 bucket, puts a small text file `hello.txt` to the bucket, and then creates a CloudFront distribution which makes the file accessible via a `https://abc123.cloudfront.net/hello.txt` proxy URL (where `abc123` is a placeholder for the real distribution ID):

{{< command >}}
$ awslocal s3 mb s3://bucket1
$ echo 'Hello World' > /tmp/hello.txt
$ awslocal s3 cp /tmp/hello.txt s3://bucket1/hello.txt --acl public-read
$ domain=$(awslocal cloudfront create-distribution \
   --origin-domain-name bucket1.s3.amazonaws.com | jq -r '.Distribution.DomainName')
$ curl -k https://$domain/hello.txt
{{< / command >}}

{{< alert >}}
**Note:** In order for CloudFront to be fully functional, your local DNS setup needs to be properly configured. See the section on [configuring the local DNS server]({{< ref "#configuring-local-dns-server" >}}) for details.
{{< /alert >}}

{{< alert >}}
**Note:** In the code example above, the last command (`curl https://$domain/hello.txt`) may temporarily fail with a warning message `Could not resolve host`. This is due to the fact that operating systems use different DNS caching strategies, and it may take some time for the CloudFront distribution's DNS name (e.g., `abc123.cloudfront.net`) to become available in the system. Usually after a few retries the command should work, though. Note that a similar behavior can also be observed in the real AWS - CloudFront DNS names can also take up to 10-15 minutes to propagate across the network.
{{< /alert >}}
