---
title: "Kinesis Data Firehose"
linkTitle: "Kinesis Data Firehose"
categories: ["LocalStack Community"]
description: >
  Kinesis Data Firehose
---

Kinesis Data Firehose is a service to extract, transform and load (ETL service) data to multiple destinations.
LocalStack supports Firehose with Kinesis as source, and S3, Elasticsearch or HttpEndpoints as targets.

## Examples

We will provide some examples to illustrate the possibilities of Firehose in LocalStack.

### Using Firehose to load Kinesis data into Elasticsearch with S3 Backup

As example, we want to deliver data sent to a Kinesis stream into Elasticsearch via Firehose, while making a full backup into a S3 bucket.
We will assume LocalStack is already [started correctly]({{< ref "get-started" >}}) and we have `awslocal` [installed]({{< ref "aws-cli" >}}).

First we will create our Elasticsearch domain:

{{< command >}}
$ awslocal es create-elasticsearch-domain --domain-name es-local
{
  "DomainStatus": {
    "DomainId": "000000000000/es-local",
    "DomainName": "es-local",
    "ARN": "arn:aws:es:us-east-1:000000000000:domain/es-local",
    "Created": true,
    "Deleted": false,
    "Endpoint": "es-local.us-east-1.es.localhost.localstack.cloud:443",
    "Processing": true,
    "ElasticsearchVersion": "7.10.0",
    "ElasticsearchClusterConfig": {
      "InstanceType": "m3.medium.elasticsearch",
      "InstanceCount": 1,
      "DedicatedMasterEnabled": true,
      "ZoneAwarenessEnabled": false,
      "DedicatedMasterType": "m3.medium.elasticsearch",
      "DedicatedMasterCount": 1
    },
    "EBSOptions": {
      "EBSEnabled": true,
      "VolumeType": "gp2",
      "VolumeSize": 10,
      "Iops": 0
    },
    "CognitoOptions": {
      "Enabled": false
    }
  }
}
{{< / command >}}

We need the `Endpoint` returned here later for the confirmation of our setup.

Now let us create our target S3 bucket and our source Kinesis stream:

{{< command >}}
$ awslocal s3 mb s3://kinesis-activity-backup-local
make_bucket: kinesis-activity-backup-local
{{< / command >}}

{{< command >}}
$ awslocal kinesis create-stream --stream-name kinesis-es-local-stream --shard-count 2
{{< / command >}}


Next, we will create our Firehose delivery stream with Elasticsearch as destination, and S3 as target for our AllDocuments backup.
We set the ARN of our Kinesis stream in the `kinesis-stream-source-configuration` as well as the role we want to use for accessing the stream.
In the `elasticsearch-destination-configuration` we set (again) the access role, the `DomainARN` of the Elasticsearch domain we want to publish to, as well as `IndexName` and `TypeName` for Elasticsearch.
Since we want to backup all documents to S3, we also set `S3BackupMode` to `AllDocuments` and provide a `S3Configuration` pointing to our created bucket.

{{< alert >}}
**Note:** In LocalStack, per default, the IAM roles will not be verified, so you can provide any ARN here. In AWS, you need to check the access rights of the specified role for the task.
{{< /alert >}}

{{< command >}}
$ awslocal firehose create-delivery-stream --delivery-stream-name activity-to-elasticsearch-local --delivery-stream-type KinesisStreamAsSource --kinesis-stream-source-configuration "KinesisStreamARN=arn:aws:kinesis:us-east-1:000000000000:stream/kinesis-es-local-stream,RoleARN=arn:aws:iam::000000000000:role/Firehose-Reader-Role" --elasticsearch-destination-configuration "RoleARN=arn:aws:iam::000000000000:role/Firehose-Reader-Role,DomainARN=arn:aws:es:us-east-1:000000000000:domain/es-local,IndexName=activity,TypeName=activity,S3BackupMode=AllDocuments,S3Configuration={RoleARN=arn:aws:iam::000000000000:role/Firehose-Reader-Role,BucketARN=arn:aws:s3:::kinesis-activity-backup-local}"
{
    "DeliveryStreamARN": "arn:aws:firehose:us-east-1:000000000000:deliverystream/activity-to-elasticsearch-local"
}
{{< / command >}}

Before testing the integration, we should check whether the Elasticsearch cluster is already started up.
We can do this using the following command (for more information about this, check out the [docs page about Elasticsearch]({{< ref "elasticsearch" >}}).


{{< command >}}
$ awslocal es describe-elasticsearch-domain --domain-name es-local | jq ".DomainStatus.Processing"
false
{{< / command >}}

Once this command returns `false`, we are ready to proceed with ingesting our data.
We can input our data into our source Kinesis stream, our put it directly into the Firehose delivery stream.

To put it into Kinesis, run:

{{< command >}}
$ awslocal kinesis put-record --stream-name kinesis_es-local_stream --data '{ "target": "barry" }' --partition-key partition
{
    "ShardId": "shardId-000000000001",
    "SequenceNumber": "49625461294598302663271645332877318906244481566013128722",
    "EncryptionType": "NONE"
}
{{< / command >}}
{{< alert >}}
**Note:** If you are using aws cli v2, you can add `--cli-binary-format raw-in-base64-out` to the above command
{{< /alert >}}



Or directly into the Firehose delivery stream:

{{< command >}}
$ awslocal firehose put-record --delivery-stream-name activity-to-elasticsearch-local --record '{ "Data": "eyJ0YXJnZXQiOiAiSGVsbG8gd29ybGQifQ==" }' 
{
    "RecordId": "00333086-7581-48a2-bc7c-8ac1ed97ed3d"
}
{{< / command >}}

If we now check the entries we made in Elasticsearch (we will use curl for simplicity). Note to replace the url with the "Endpoint" field of our `create-elasticsearch-domain` operation at the beginning.

{{< command >}}
$ curl -s http://es-local.us-east-1.es.localhost.localstack.cloud:443/activity/_search | jq '.hits.hits'
[
  {
    "_index": "activity",
    "_type": "activity",
    "_id": "f38e2c49-d101-46aa-9ce2-0d2ea8fcd133",
    "_score": 1,
    "_source": {
      "target": "Hello world"
    }
  },
  {
    "_index": "activity",
    "_type": "activity",
    "_id": "d2f1c125-b3b0-4c7c-ba90-8acf4075a682",
    "_score": 1,
    "_source": {
      "target": "barry"
    }
  }
]
{{< / command >}}

If you get a similar output, you have correctly set up a Firehose delivery stream!
Also checkout the specified S3 bucket to check if your backup is working correctly.