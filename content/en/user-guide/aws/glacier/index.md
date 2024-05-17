---
title: "Glacier"
linkTitle: "Glacier"
description: Get started with S3 Glacier on LocalStack
tags: ["Pro image"]
persistence: supported

---

## Introduction

Glacier is a data storage service provided by Amazon Web Services to suit the long-term storage of archives and backup of infrequently accessed data.
It offers various retrieval options, different levels of retrieval speed, and more.
Glacier uses a Vault container to store your data, similar to how S3 stores data in Buckets.
A Vault further holds the data in an Archive, which can contain text, images, video, and audio files.
Glacier uses Jobs to retrieve the data in an Archive or list the inventory of a Vault.

LocalStack allows you to use the Glacier APIs in your local environment to manage Vaults and Archives.
You can use the Glacier API to configure and set up vaults where you can store archives and manage them.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_glacier/), which provides information on the extent of Glacier's integration with LocalStack.

## Getting started

This guide is designed for users new to Glacier and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a vault, upload an archive, initiate a job to get an inventory details or download an archive, and delete the archive and vault with the AWS CLI.

### Create a vault

You can create a vault using the [`CreateVault`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html) API.
Run the follow command to create a Glacier Vault named `sample-vault`.

{{< command >}}
$ awslocal glacier create-vault --vault-name sample-vault --account-id -
{{< /command >}}

You can get the details from your vault using the [`DescribeVault`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html) API.
Run the following command to describe your vault.

{{< command >}}
$ awslocal glacier describe-vault --vault-name sample-vault --account-id -
{{< /command >}}

On successful creation of the Glacier vault, you will see the following output:

```bash
{
    "VaultARN": "arn:aws:glacier:us-east-1:000000000000:vaults/sample-vault",
    "VaultName": "sample-vault",
    "CreationDate": "2023-09-11T15:07:28.000Z",
    "LastInventoryDate": "2023-09-11T15:07:28.000Z",
    "NumberOfArchives": 0,
    "SizeInBytes": 0
}
```

### Upload an archive to a vault

You can upload an archive or an individual file to a vault using the [`UploadArchive`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html) API.
Download a random image from the internet and save it as `image.jpg`.
Run the following command to upload the file to your Glacier vault:

{{< command >}}
$ awslocal glacier upload-archive --vault-name sample-vault --account-id - --body image.jpg
{{< /command >}}

On successful upload of the Glacier archive, you will see the following output:

```bash
{
    "location": "/000000000000/vaults/sample-vault/archives/d41d8cd98f00b204e9800998ecf8427e",
    "checksum": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "archiveId": "d41d8cd98f00b204e9800998ecf8427e"
}
```

### Initiate the retrieval of an archive from a vault

You can initiate the retrieval of an archive from a vault using the [`InitiateJob`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html) API.

To download an archive, you will need to initiate an `archive-retrieval` job first to make the Archive available for download.
{{< command >}}
$ awslocal glacier initiate-job --vault-name sample-vault  --account-id - --job-parameters '{"Type":"archive-retrieval","ArchiveId":"d41d8cd98f00b204e9800998ecf8427e"}'
{{< /command >}}

On successful execution of the job, you will see the following output:

```bash
{
    "location": "//vaults/sample-vault/jobs/25CEOTJ7ZUR5Q7YY0B1O55AE4C3L1502EOHWMNY10IIYEBWEQB73D23S8BVYO9RTRTPLRK2LJLUCCRM52GDV87C9A4JW",
    "jobId": "25CEOTJ7ZUR5Q7YY0B1O55AE4C3L1502EOHWMNY10IIYEBWEQB73D23S8BVYO9RTRTPLRK2LJLUCCRM52GDV87C9A4JW"
}
```

### List the jobs

You can list the current and previous processes, called Jobs, to monitor the requests sent to the Glacier API using the [`ListJobs`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html) API.

{{< command >}}
$ awslocal glacier list-jobs --vault-name sample-vault --account-id -
{{< /command >}}

On successful execution of the command, you will see the following output:

```bash
{
    "JobList": [
        {
            "JobId": "25CEOTJ7ZUR5Q7YY0B1O55AE4C3L1502EOHWMNY10IIYEBWEQB73D23S8BVYO9RTRTPLRK2LJLUCCRM52GDV87C9A4JW",
            "Action": "ArchiveRetrieval",
            "ArchiveId": "d41d8cd98f00b204e9800998ecf8427e",
            "VaultARN": "arn:aws:glacier:us-east-1:000000000000:vaults/sample-vault",
            "CreationDate": "2023-09-11T15:25:54.000Z",
            "Completed": true,
            "StatusCode": "Succeeded",
            "ArchiveSizeInBytes": 0,
            "InventorySizeInBytes": 10000,
            "CompletionDate": "2023-09-11T15:25:59.000Z",
            "Tier": "Standard"
        }
    ]
}
```

### Download the result of an archive retrieval

You can download the output of an `ArchiveRetrieval` job with the [`GetJobOutput`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html) API.

The data download process can be verified through the previous `ListJobs` call to check progress.
Once the `ArchiveRetrieval` Job is complete, the data can be downloaded.
You can use the `JobId` of the Job to download your archive with the following command:

{{< command >}}
$ awslocal glacier get-job-output --vault-name sample-vault --account-id - --job-id 25CEOTJ7ZUR5Q7YY0B1O55AE4C3L1502EOHWMNY10IIYEBWEQB73D23S8BVYO9RTRTPLRK2LJLUCCRM52GDV87C9A4JW my-archive.jpg
{{< /command >}}

{{< callout >}}
Please not that currently, this operation is only mocked, and will create an empty file named `my-archive.jpg`, not containing the contents of your archive. 
{{< /callout >}}

### Retrieve the inventory information

You can also initiate the retrieval of the inventory of a vault using the same [`InitiateJob`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html) API.

Initiate a job of the specified type to get the details of the individual inventory items inside a Vault using the `initiate-job` command:
{{< command >}}
$ awslocal glacier initiate-job --vault-name sample-vault  --account-id - --job-parameters '{"Type":"inventory-retrieval","ArchiveId":"d41d8cd98f00b204e9800998ecf8427e"}'
{{< /command >}}

On successful execution of the command, you will see the following output:

```bash
{
    "location": "//vaults/sample-vault/jobs/P5972CSWFR803BHX48OD1A7JWNBFJUMYVWCMZWY55ZJPIJMG1XWFV9ISZPZH1X3LBF0UV3UG6ORETM0EHE5R86Z47B1F",
    "jobId": "P5972CSWFR803BHX48OD1A7JWNBFJUMYVWCMZWY55ZJPIJMG1XWFV9ISZPZH1X3LBF0UV3UG6ORETM0EHE5R86Z47B1F"
}
```

In the same fashion as the archive retrieval, you can now download the result of the inventory retrieval job using `GetJobOutput` using the `JobId` from the result of the previous command:
{{< command >}}
$ awslocal glacier get-job-output \
   --vault-name sample-vault --account-id - --job-id P5972CSWFR803BHX48OD1A7JWNBFJUMYVWCMZWY55ZJPIJMG1XWFV9ISZPZH1X3LBF0UV3UG6ORETM0EHE5R86Z47B1F inventory.json
{{< /command >}}

Inspecting the content of the `inventory.json` file, we can find an inventory of the vault:
```json
{
  "VaultARN": "arn:aws:glacier:us-east-1:000000000000:vaults/sample-vault",
  "InventoryDate": "2023-09-11T17:20:48.000Z",
  "ArchiveList": [
    {
      "ArchiveId": "d41d8cd98f00b204e9800998ecf8427e",
      "ArchiveDescription": "",
      "CreationDate": "2023-09-11T15:13:41.000Z",
      "Size": 0,
      "SHA256TreeHash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

### Delete an archive

You can delete a Glacier archive using the [`DeleteArchive`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html) API.

Run the following command to delete the previously created archive:

{{< command >}}
$ awslocal glacier delete-archive \
      --vault-name sample-vault --account-id - --archive-id d41d8cd98f00b204e9800998ecf8427e
{{< /command >}}

### Delete a vault

You can delete a Glacier vault with the [`DeleteVault`](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html) API.

Run the following command to delete the vault:
{{< command >}}
$ awslocal glacier delete-vault --vault-name sample-vault --account-id -
{{< /command >}}
