---
title: "Lake Formation"
linkTitle: "Lake Formation"
description: Get started with Lake Formation on LocalStack
---

## Introduction

Lake Formation is a service provided by Amazon Web Services (AWS) that facilitates the creation, management, and governance of data lakes. Lake Formation assists in setting up data lakes by automating the complex tasks associated with data provisioning and management. It supports various data sources, including S3, RDS, and Redshift, and allows you to define and enforce data access policies, ensuring data security and compliance.

LocalStack supports Lake Formation via the Pro/Team offering, allowing you to use the Lake Formation APIs in your local environment to manage resources, permissions, and data lake settings. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_lakeformation/), which provides information on the extent of Lake Formation's integration with LocalStack.

## Getting started

This guide is designed for users new to Lake Formation and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a data lake, define permissions, and manage access to your data using Lake Formation with the AWS CLI.

### Create a data lake

Create a new S3 bucket that will be used as your data lake. You can use the [`CreateBucket`](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) API to create a new bucket. Run the following command to create a new bucket named `mydatalake-bucket`:

{{ < command >}}
$ awslocal s3api create-bucket \
    --bucket mydatalake-bucket
{{ < /command >}}

### Define permissions and grant access

You can now create a database in the Glue Data Catalog to organize your data using the [`CreateDatabase`](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-database.html#aws-glue-api-catalog-database-CreateDatabase) API. Run the following command to create a new database named `mydatalake_db`:

{{ < command >}}
$ awslocal glue create-database \
    --database-input Name=mydatalake_db
{{ < /command >}}

You can now define a table within your database in the Glue Data Catalog using the [`CreateTable`](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-table.html#aws-glue-api-catalog-table-CreateTable) API. Run the following command to create a new table named `mydatalake_table`:

{{ < command >}}
$ glue create-table \
    --database-name mydatalake_db \
    --table-input '{
        "Name": "mydatalake_table",
        "StorageDescriptor": {
            "Columns": [{"Name": "column1", "Type": "string"}, {"Name": "column2", "Type": "int"}],
            "Location": "s3://mydatalake-bucket/",
            "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
            "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
            "SerdeInfo": {
                "SerializationLibrary": "org.apache.hadoop.hive.serde2.OpenCSVSerde",
                "Parameters": {"separatorChar": ","}
            }
        }
    }'
{{ < /command >}}

### Use Lake Formation to grant permissions

LocalStack does not enforce IAM permissions, and you can enable IAM policy enforcement using the `ENFORCE_IAM=1` environment variable while starting LocalStack. You can grant permissions to a mock IAM user or role using Lake Formation using the [`GrantPermissions`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_GrantPermissions.html) API to grant permissions to the IAM user or role. 

Run the following command to grant permissions to the IAM user or role:

{{ < command >}}
$ awslocal lakeformation grant-permissions \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::000000000000:user/myuser \
    --permissions "ALL" \
    --permissions-with-grant-option "SELECT" \
    --resource '{ "Table": { "DatabaseName": "mydatalake_db", "Name": "mydatalake_table" } }'
{{ < /command >}}

You can now register the table with Lake Formation, so access can be managed, using [`RegisterResource`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_RegisterResource.html) API. Run the following command to register the table with Lake Formation:

{{ < command >}}
$ awslocal lakeformation register-resource \
    --resource-arn arn:aws:glue:us-east-1:000000000000:table/mydatalake_db/mydatalake_table
{{ < /command >}}

Finally you can grant permissions to the registered table using the following command:

{{ < command >}}
$ awslocal lakeformation grant-permissions \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::000000000000:user/myuser \
    --permissions "SELECT" \
    --resource '{ "Table": { "DatabaseName": "mydatalake_db", "Name": "mydatalake_table" } }'
{{ < /command >}}

### List resources and permissions

You can list resources registered with Lake Formation using the [`ListResources`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_ListResources.html) API. Run the following command to list resources registered with Lake Formation:

{{ < command >}}
$ awslocal lakeformation list-resources
{{ < /command >}}

The following output would be retrieved:

```bash
{
    "ResourceInfoList": [
        {
            "ResourceArn": "arn:aws:glue:us-east-1:000000000000:table/mydatalake_db/mydatalake_table",
            "LastModified": 1692870642.351956
        }
    ]
}
```

In a similar fashion, you can list permissions granted to a principal using the [`ListPermissions`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_ListPermissions.html) API. Run the following command to list permissions granted to the IAM user or role:

{{ < command >}}
$ awslocal lakeformation list-permissions \
    --principal DataLakePrincipalIdentifier=arn:aws:iam::000000000000:user/myuser
{{ < /command >}}

The following output would be retrieved:

```bash
{
    "PrincipalResourcePermissions": [
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::000000000000:user/myuser"
            },
            "Resource": {
                "Table": {
                    "DatabaseName": "mydatalake_db",
                    "Name": "mydatalake_table"
                }
            },
            "Permissions": [
                "SELECT"
            ]
        }
    ]
}
```

### Add Data Lake settings

You can add Data Lake settings to set the list of data lake administrators who have admin privileges on all resources managed by Lake Formation using the [`PutDataLakeSettings`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_PutDataLakeSettings.html) API. Run the following command to add Data Lake settings:

{{ < command >}}
$ awslocal lakeformation put-data-lake-settings \
    --data-lake-settings '{
        "DataLakeAdmins": [
            {
                "DataLakePrincipalIdentifier": "arn:aws:iam::000000000000:user/myuser"
            }
        ],
        "CreateDatabaseDefaultPermissions": [
            {
                "Principal": {
                    "DataLakePrincipalIdentifier": "arn:aws:iam::000000000000:user/myuser"
                },
                "Permissions": [
                    "ALL"
                ]
            }
        ],
        "CreateTableDefaultPermissions": [
            {
                "Principal": {
                    "DataLakePrincipalIdentifier": "arn:aws:iam::000000000000:user/myuser"
                },
                "Permissions": [
                    "ALL"
                ]
            }
        ]
    }'
{{ < /command >}}

You can retrieve the Data Lake settings using the [`GetDataLakeSettings`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_GetDataLakeSettings.html) API. Run the following command to retrieve the Data Lake settings:

{{ < command >}}
$ awslocal lakeformation get-data-lake-settings
{{ < /command >}}
