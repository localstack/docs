---
title: "Web Application Firewall (WAF)"
linkTitle: "Web Application Firewall (WAF)"
description: Get started with Web Application Firewall (WAF) on LocalStack
tags: ["Ultimate"]
---

## Introduction

Web Application Firewall (WAF) is a service provided by Amazon Web Services (AWS) that helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources.
WAFv2 is the latest version of WAF, and it allows you to specify a single set of rules to protect your web applications, APIs, and mobile applications from common attack patterns, such as SQL injection and cross-site scripting.

LocalStack allows you to use the WAFv2 APIs for offline web application firewall jobs in your local environment.
The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_wafv2/), which provides information on the extent of WAFv2 integration with LocalStack.

## Getting started

This guide is for users who are familiar with the AWS CLI and [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will walk you through creating, listing, tagging, and viewing tags for Web Access Control Lists (WebACLs) using the Web Application Firewall (WAF) service in a LocalStack environment using the AWS CLI.

### Create a WebACL

Start by creating a Web Access Control List (WebACL) using the [`CreateWebACL`](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateWebACL.html) API.
Run the following command to create a WebACL named `TestWebAcl`:

{{< command >}}
$ awslocal wafv2 create-web-acl \
    --name TestWebAcl \
    --scope REGIONAL \
    --default-action Allow={} \
    --visibility-config SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=TestWebAclMetrics
<disable-copy>
{
    "Summary": {
        "Name": "TestWebAcl",
        "Id": "f94fd5bc-e4d4-4280-9f53-51e9441ad51d",
        "Description": "",
        "ARN": "arn:aws:wafv2:us-east-1:000000000000:regional/webacl/TestWebAcl/f94fd5bc-e4d4-4280-9f53-51e9441ad51d"
    }
}
</disable-copy>
{{< /command >}}

Note the `Id` and `ARN` from the output, as they will be needed for subsequent commands.

### List WebACLs

To view all the WebACLs you have created, use the [`ListWebACLs`](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListWebACLs.html) API.
Run the following command to list the WebACLs:

{{< command >}}
$ awslocal wafv2 list-web-acls --scope REGIONAL
<disable-copy>
{
    "NextMarker": "Not Implemented",
    "WebACLs": [
        {
            "Name": "TestWebAcl",
            "Id": "f94fd5bc-e4d4-4280-9f53-51e9441ad51d",
            "Description": "",
            "ARN": "arn:aws:wafv2:us-east-1:000000000000:regional/webacl/TestWebAcl/f94fd5bc-e4d4-4280-9f53-51e9441ad51d"
        }
    ]
}
</disable-copy>
{{< /command >}}

### Tag a WebACL

Tagging resources in AWS WAF helps you manage and identify them.
Use the [`TagResource`](https://docs.aws.amazon.com/waf/latest/APIReference/API_TagResource.html) API to add tags to a WebACL.
Run the following command to add a tag to the WebACL created in the previous step:

{{< command >}}
$ awslocal wafv2 tag-resource \
    --resource-arn arn:aws:wafv2:us-east-1:000000000000:regional/webacl/TestWebAcl/f94fd5bc-e4d4-4280-9f53-51e9441ad51d \
    --tags Key=Name,Value=AWSWAF
{{< /command >}}

After tagging your resources, you may want to view these tags.
Use the [`ListTagsForResource`](https://docs.aws.amazon.com/waf/latest/APIReference/API_ListTagsForResource.html) API to list the tags for a WebACL.
Run the following command to list the tags for the WebACL created in the previous step:

{{< command >}}
$ awslocal wafv2 list-tags-for-resource \
    --resource-arn arn:aws:wafv2:us-east-1:000000000000:regional/webacl/TestWebAcl/f94fd5bc-e4d4-4280-9f53-51e9441ad51d
<disable-copy>
{
    "TagInfoForResource": {
        "ResourceARN": "arn:aws:wafv2:us-east-1:000000000000:regional/webacl/TestWebAcl/f94fd5bc-e4d4-4280-9f53-51e9441ad51d",
        "TagList": [
            {
                "Key": "Name",
                "Value": "AWSWAF"
            }
        ]
    }
}
</disable-copy>
{{< /command >}}
