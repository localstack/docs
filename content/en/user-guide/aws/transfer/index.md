---
title: "Transfer"
linkTitle: "Transfer"
categories: ["LocalStack Pro"]
description: >
  Get started with Amazon Transfer on LocalStack
aliases:
  - /aws/transfer/
---

## Introduction

The AWS Transfer API is a powerful tool that empowers users to establish FTP(S) servers with ease.
These servers serve as gateways, allowing direct access to files residing in Amazon S3 buckets.
This functionality streamlines file management processes, making it simpler and more efficient to handle data stored in S3 by providing a familiar FTP interface for users to interact with their files securely.
Whether you're looking to facilitate file transfers or enhance your data access capabilities, the AWS Transfer API simplifies the process and extends the versatility of your cloud storage infrastructure.

## Getting started
This Python code demonstrates a basic workflow for transferring a file between a local machine and AWS S3 using the AWS Transfer Family service and FTP (File Transfer Protocol).

```python
import io
import time
import uuid
import boto3
from ftplib import FTP, FTP_TLS

EDGE_URL = 'http://localhost:4566'
USERNAME = 'user_123'
BUCKET = 'transfer-files'
S3_FILENAME = 'test-file-aws-transfer.txt'
FTP_USER_DEFAULT_PASSWD = '12345'
FILE_CONTENT = b'title "Test" \nfile content!!'

# create bucket
s3_client = boto3.client('s3', endpoint_url=EDGE_URL)
s3_client.create_bucket(Bucket=BUCKET)
transfer_client = boto3.client('transfer', endpoint_url=EDGE_URL)

# create transfer server
rs = transfer_client.create_server(
        EndpointType='PUBLIC',
        IdentityProviderType='SERVICE_MANAGED',
        Protocols=['FTP']
    )
time.sleep(1)

server_id = rs['ServerId']
port = int(server_id[-4:])

transfer_client.create_user(
    ServerId=server_id,
    HomeDirectory=BUCKET,
    HomeDirectoryType='PATH',
    Role='arn:aws:iam::testrole',
    UserName=USERNAME
)

# upload file through AWS Transfer
ftp = FTP()
ftp.connect('localhost', port=port)
result = ftp.login(USERNAME, FTP_USER_DEFAULT_PASSWD)
assert 'Login successful.' in result
ftp.storbinary(cmd='STOR %s' % S3_FILENAME, fp=io.BytesIO(FILE_CONTENT))
ftp.quit()

# download file through AWS S3
rs = s3_client.get_object(Bucket=BUCKET, Key=S3_FILENAME)
assert rs['Body'].read() == FILE_CONTENT
```

Please note that this code is a simplified example for demonstration purposes.
In a production environment, you should use more secure practices, including setting proper IAM roles and handling sensitive credentials securely.
Additionally, error handling and cleanup code may be needed to ensure the script behaves robustly in all scenarios.

## Current Limitations 
The Transfer API does not provide a way to return the endpoint URL of created FTP servers.
Hence, in order to determine the server endpoint, the local port is encoded as a suffix within the `ServerId` attribute, constituting the only numeric digits within the ID string.
For example, assume the following is the response from the `CreateServer` API call, then the FTP server is accessible on port `4511` (i.e., `ftp://localhost:4511`):
```json
{
    "ServerId": "s-afcedbffaecca4511"
}
```
