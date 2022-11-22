---
title: "Glacier"
linkTitle: "Glacier"
categories: ["LocalStack Pro"]
description: >
  Getting started with Amazon S3 Glacier
---

Glacier is a data storage service provided by Amazon Web Services to suit the long-term storage of archives and backup of infrequently accessed data. It offers various retrieval options, different levels of retrieval speed, and more. Glacier uses a Vault container to store your data, similar to how S3 stores data in Buckets. A Vault further holds the data in an Archive, which can contain text, images, video, and audio files. Glacier uses Jobs to retrieve, update, or delete the data in an Archive.

LocalStack provides Glacier support via our Pro offering. You can use the Glacier API to configure and set up data archive backup, restore and delete operations. The supported APIs are available over our [feature coverage page]({{< ref "feature-coverage" >}}).

## Getting started

In this getting started guide, you'll learn how to make a basic usage of Glacier over LocalStack. This guide is intended for users who wish to get more acquainted with Glacier, and assumes you have basic knowledge of the AWS CLI (and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script). First, start your LocalStack instance using your preferred method, then run the following commands:

1. Create a vault with the `create-vault` command using the `awslocal` CLI:
   {{< command >}}
   $ awslocal glacier create-vault --account-id - --vault-name <VAULT-NAME>
   {{< /command >}}

2. Get the details of the vault using the `describe-vault` command:
   {{< command >}}
   $ awslocal glacier describe-vault --account-id - --vault-name <VAULT-NAME>
   {{< /command >}}

3. List out the current and previous processes, called Jobs, to monitor the requests sent to the Glacier API:
   {{< command >}}
   $ awslocal glacier list-jobs --account-id - --vault-name <VAULT-NAME>
   {{< /command >}}

4. Initiate a job of the specified type to get the details of the individual inventory items inside a Vault using the `initiate-job` command:
   {{< command >}}
   $ awslocal glacier initiate-job --account-id - --vault-name <VAULT-NAME> --vault-name <VAULT-NAME> --job-parameters <JSON-CONFIGURATION-FILE>
   {{< /command >}}
   {{< alert >}}
   **Note**: JSON Configuration Options can be found [on the official AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/glacier/initiate-job.html). The following setting can be used in case of Inventory retrieval: `{ "Type": "inventory-retrieval", "ArchiveId": <ARCHIVE-ID> }`. Archive ID can be got as an output of the Data Upload/List Jobs request.
   {{< /alert >}}

5. Use the `upload-archive` command to upload an archive to a vault:
   {{< command >}}
   $ awslocal glacier upload-archive --account-id - --vault-name <VAULT_NAME> --body <FILE-TO-UPLOAD>
   {{< /command >}}
   Data upload to Glacier can accept only Individual files or Archives.

6. Download the required archive based on the Archive ID using the `initiate-job` command:
   {{< command >}}
   $ awslocal glacier initiate-job --account-id - --vault-name <VAULT-NAME> --job-parameters <JSON-CONFIGURATION-FILE>
   {{< /command >}}
   {{< alert >}}
   **Note**: JSON Configuration Options can be found [on the official AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/glacier/initiate-job.html). The following setting can be used in case of Inventory retrieval: `{ "Type": "archive-retrieval", "ArchiveId": <ARCHIVE-ID> }`. Archive ID can be got as an output of the Data Upload/List Jobs request.
   {{< /alert >}}

7. The data download process can be verified through the List Jobs command to check progress. Once the Job is complete the data can be downloaded to the current location using the following command:
   {{< command >}}
   $ awslocal glacier get-job-output --account-id - --vault-name <VAULT-NAME> --job-id <JOB-ID> <OUTPUT-FILE-NAME.OUTPUT-FILE-TYPE>
   {{< /command >}}

8. Delete the archive using the `delete-archive` command:
   {{< command >}}
   $ awslocal glacier delete-archive --account-id - --vault-name <VAULT-NAME> --archive-id <ARCHIVE-ID>
   {{< /command >}}
