---
title: "Textract"
linkTitle: "Textract"
description: Get started with Textract on LocalStack
tags: ["Pro image"]
persistence: supported

---

Textract is a machine learning service that automatically extracts text, forms, and tables from scanned documents. It simplifies the process of extracting valuable information from a variety of document types, enabling applications to quickly analyze and understand document content.

LocalStack allows you to mock Textract APIs in your local environment. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_textract/), providing details on the extent of Textract's integration with LocalStack.

## Getting started

This guide is tailored for users new to Textract and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to perform basic Textract operations, such as mocking text detection in a document.

### Detect document text

You can use the [`DetectDocumentText`](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html) API to identify and extract text from a document. Execute the following command:

{{< command >}}
$ awslocal textract detect-document-text \
    --document '{"S3Object":{"Bucket":"your-bucket","Name":"your-document"}}'
{{< /command >}}

The following output would be retrieved:

```bash
{
    "DocumentMetadata": {
        "Pages": {
            "Pages": 389
        }
    },
    "Blocks": [],
    "DetectDocumentTextModelVersion": "1.0"
}
```

### Start document text detection job

You can use the [`StartDocumentTextDetection`](https://docs.aws.amazon.com/textract/latest/dg/API_StartDocumentTextDetection.html) API to asynchronously detect text in a document. Execute the following command:

{{< command >}}
$ awslocal textract start-document-text-detection \
        --document-location '{"S3Object":{"Bucket":"bucket","Name":"document"}}'
{{< /command >}}

The following output would be retrieved:

```bash
{
    "JobId": "501d7251-1249-41e0-a0b3-898064bfc506"
}
```

Save the `JobId` value to use in the next command.

### Get document text detection job

You can use the [`GetDocumentTextDetection`](https://docs.aws.amazon.com/textract/latest/dg/API_GetDocumentTextDetection.html) API to retrieve the results of a document text detection job. Execute the following command:

{{< command >}}
$ awslocal textract get-document-text-detection \
    --job-id "501d7251-1249-41e0-a0b3-898064bfc506"
{{< /command >}}

Replace `501d7251-1249-41e0-a0b3-898064bfc506` with the `JobId` value retrieved from the previous command. The following output would be retrieved:

```bash
{
    "DocumentMetadata": {
        "Pages": {
            "Pages": 389
        }
    },
    "JobStatus": "SUCCEEDED",
    "Blocks": [],
    "DetectDocumentTextModelVersion": "1.0"
}
```
