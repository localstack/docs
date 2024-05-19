---
title: "Support"
linkTitle: "Support"
description: Get started with Support on LocalStack
persistence: supported

---

## Introduction

AWS Support is a service provided by Amazon Web Services (AWS) that offers technical assistance and resources to help you optimize your AWS environment, troubleshoot issues, and maintain operational efficiency. Support APIs provide programmatic access to AWS Support services, including the ability to create and manage support cases programmatically. You can further automate your support workflow using various AWS services, such as Lambda, CloudWatch, and EventBridge.

LocalStack allows you to use the Support APIs in your local environment to create and manage new cases, while testing your configurations locally. LocalStack provides a mock implementation via a mock Support Center provided by [Moto](https://docs.getmoto.org/en/latest/docs/services/support.html), and does not create real cases in the AWS. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_support/), which provides information on the extent of Support API's integration with LocalStack.

{{< callout >}}
For technical support with LocalStack, you can reach out through our [support channels](https://docs.localstack.cloud/getting-started/help-and-support/). It's important to note that LocalStack doesn't offer a programmatic interface to create support cases, and this documentation is only intended to demonstrate how you can use and mock the AWS Support APIs in your local environment.
{{< /callout >}}

## Getting started

This guide is designed for users new to Support and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a case in the mock Support Center using the AWS CLI.

### Create a support case

To create a support case, you can use the [`CreateCase`](https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/CreateCase) API. The following example creates a case with the subject "Test case" and the description "This is a test case" in the category "General guidance".

{{< command >}}
$ awslocal support create-case \
    --subject "Test case" \
    --service-code "general-guidance" \
    --category-code "general-guidance" \
    --communication-body "This is a test case"
{{< / command >}}

The following output would be retrieved:

```bash
{
    "caseId": "case-12345678910-2020-kEa16f90bJE766J4"
}
```

### List support cases

To list all support cases, you can use the [`DescribeCases`](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCases.html) API. The following example lists all cases in the category "General guidance".

{{< command >}}
$ awslocal support describe-cases
{{< / command >}}

The following output would be retrieved:

```bash
{
    "cases": [
        {
            "caseId": "case-12345678910-2020-kEa16f90bJE766J4",
            ...
            "submittedBy": "moto@moto.com",
            "timeCreated": "2023-08-24T18:03:08.895247",
            "recentCommunications": {
                "communications": [
                    {
                        "caseId": "case-12345678910-2020-kEa16f90bJE766J4",
                        "body": "This is a test case",
                        "submittedBy": "moto@moto.com",
                        ...
                    }
                ],
                "nextToken": "foo_next_token"
            }
        }
    ]
}
```

### Resolve a support case

To resolve a support case, you can use the [`ResolveCase`](https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/ResolveCase) API. The following example resolves the case created in the previous step.

{{< command >}}
$ awslocal support resolve-case \
    --case-id "case-12345678910-2020-kEa16f90bJE766J4"
{{< / command >}}

Replace the case ID with the ID of the case you want to resolve. The following output would be retrieved:

```bash
{
    "initialCaseStatus": "resolved",
    "finalCaseStatus": "resolved"
}
```

You can also use the [`DescribeCases`](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCases.html) API to verify that the case has been resolved.
