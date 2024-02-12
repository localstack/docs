---
title: "Security Testing with IAM Policy Stream"
linkTitle: "Security Testing with IAM Policy Stream"
weight: 6
description: >
  In this video let’s discuss IAM policy Stream. So when we build an application, we usually require access to aws resrouces such as dynamodb, rds, etc. to provide access to these we create iam roles and attach permission to it in form of policies. Figuring out these policies can be cumbersome. IAM policy stream eases out this job for you. These streams can help you find the appropriate permissions for your cloud applications
length: 02:56
leadimage: iam-policy-stream.png
videoUrl: https://www.youtube.com/embed/TOBLG2Z6xAM?si=Lk6P7j7VpMQoob0F
type: lessons
url: "/academy/localstack-deployment/iam-policy-stream/"
---

In this video we will be discussing about IAM Policy Stream which can help us give right sized IAM permissions to a resource. Thus ensuring proper and secure access to the resource.  
To provide access to a resource in AWS, we need to create iam roles and attach permissions to it in the form of policies. Figuring out these policies can be cumbersome. IAM policy stream eases out this job for us. These streams can help you find the appropriate permissions for your cloud applications.

- We will enable IAM Policy Stream from the Localstack Webapp and then try doing an AWS API request from the cli.
- This would generate the corresponding policy required for the request to go through.
- Further we send another request that generates the corresponding policy for the resource. You can also see a consolidated policy for both the requests in the 'Summary Policy' setion

Further reading:

- [IAM Policy Stream docs](https://docs.localstack.cloud/user-guide/security-testing/iam-policy-stream/)
- [Security Testing](https://docs.localstack.cloud/user-guide/security-testing/)
- [IAM Policy Enforcement](https://docs.localstack.cloud/user-guide/security-testing/iam-enforcement/)
- [LocalStack Continuous Integration](https://docs.localstack.cloud/user-guide/ci/)
- [IAM Policy Stream Video](https://www.youtube.com/watch?v=HQ2V44ImJ3E)