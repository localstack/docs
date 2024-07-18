---
title: "Security Testing with IAM Policy Stream"
linkTitle: "Security Testing with IAM Policy Stream"
weight: 6
description: >
  In this video, we'll talk about the IAM policy Stream. When developing an application, we often need access to AWS resources like DynamoDB, RDS, etc. To grant this access, we create IAM roles and assign permissions through policies. Determining these policies can be challenging — the IAM policy stream simplifies this task by identifying the necessary permissions for your cloud applications.
length: 02:56
leadimage: iam-policy-stream.png
videoUrl: https://www.youtube.com/embed/TOBLG2Z6xAM?si=Lk6P7j7VpMQoob0F
type: lessons
url: "/academy/localstack-deployment/iam-policy-stream/"
---

In this video, we'll explore the [IAM Policy Stream](https://docs.localstack.cloud/user-guide/security-testing/iam-policy-stream/) that assists in assigning precise IAM permissions to a resource.
This ensures accurate and secure access to the resource.

Here's a breakdown of the steps we'll take:

1. Enable IAM Policy Stream on the [LocalStack Web Application](https://app.localstack.cloud/policy-stream).
2. Trigger an AWS API request from the CLI, triggering the generation of the necessary policy for the request.
3. Submit another request to generate the corresponding policy for the resource.
4. Explore the **Summary Policy** section to view the consolidated policy for both requests.

Further reading:

- [Security Testing](https://docs.localstack.cloud/user-guide/security-testing/)
- [IAM Policy Stream](https://youtube.com/watch?v=HQ2V44ImJ3E)
- [Generate IAM policies locally with LocalStack](https://hashnode.localstack.cloud/generate-iam-policies-locally-using-localstack)
