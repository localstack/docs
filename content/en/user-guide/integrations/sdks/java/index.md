---
title: "Java"
categories: []
description: >
    How to use the AWS Java SDK with LocalStack.
aliases:
- /integrations/sdks/java/
---

## Overview

The AWS SDK for Java provides a Java API for AWS services. Using the SDK, your Java application can interact
with LocalStack services the same way it does with Amazon services. Support for new services is regularly added to
the SDK. For a list of the supported services and their API versions that are 
included with each release of the SDK, view the [release notes](https://github.com/aws/aws-sdk-java#release-notes) 
for the version that you’re working with.

The Java SDK currently supports two major versions:

* [AWS SDK for Java v1](https://github.com/aws/aws-sdk-java)
* [AWS SDK for Java v2](https://github.com/aws/aws-sdk-java-v2)

## Examples

Full examples for both SDK versions can be found in the 
[example repository](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/java). This includes proper
exception handling and all the necessary Maven dependencies.
The scripts to create the AWS services on LocalStack can be found under the `src/main/resources` folder
of each module in the repository. 

### S3 Service

Below you'll find an example of how to create an S3 client with the endpoint configured for LocalStack.
The client can be used to upload a file to an existing bucket and then retrieve it. 


#### Configuring the S3 Client

{{< tabpane lang="java" >}}
{{< tab header="v1" lang="java" >}}

    // Credentials that can be replaced with real AWS values. (To be handled properly and not hardcoded.)
    // These can be skipped altogether for LocalStack, but we generally want to avoid discrepancies with production code.
final String ACCESS_KEY = "test";
final String SECRET_KEY = "test";


    // S3 Client with configured credentials, endpoint directing to LocalStack and desired region.
AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
    .withCredentials(new AWSStaticCredentialsProvider(credentials))
    .withEndpointConfiguration(new EndpointConfiguration("s3.localhost.localstack.cloud:4566",
    Regions.US_EAST_1.getName()))
    .build();

{{< /tab >}}

{{< tab header="v2" lang="java" >}}

    // Credentials that can be replaced with real AWS values. (To be handled properly and not hardcoded.)
    // These can be skipped altogether for LocalStack, but we generally want to avoid discrepancies with production code.
final String ACCESS_KEY = "test";
final String SECRET_KEY = "test";

    // Desired region.
Region region = Region.US_EAST_1;

    // S3 Client with configured credentials, endpoint directing to LocalStack and desired region.
S3Client s3Client = S3Client.builder()
    .endpointOverride(URI.create("https://s3.localhost.localstack.cloud:4566"))
    .credentialsProvider(StaticCredentialsProvider.create(
    AwsBasicCredentials.create(ACCESS_KEY, SECRET_KEY)))
    .region(region)
    .build();

{{< /tab >}}
{{< /tabpane >}}

#### Interacting with S3

{{< tabpane lang="java" >}}
{{< tab header="v1" lang="java" >}}

    // Existing bucket name.
final String BUCKET_NAME = "records";

    // The key of the object in the bucket, usually the name of the file.
final String key = "hello-v1.txt";

    // Creating a File object and FileInputStream.
File file = new File(filePathOnDisk);
InputStream fileInputStream = new FileInputStream(file);

    // Creating an ObjectMetadata to specify the content type and content length.
ObjectMetadata metadata = new ObjectMetadata();
metadata.setContentType("text/plain");
metadata.setContentLength(file.length());

    // Put the file into the S3 bucket
s3Client.putObject(new PutObjectRequest(BUCKET_NAME, key, fileInputStream, metadata));

    // Retrieving the object from the bucket. 
S3Object s3Object = s3Client.getObject(BUCKET_NAME, key);

      // Read the text content of the file using a BufferedReader.
S3ObjectInputStream objectInputStream = s3Object.getObjectContent();
BufferedReader reader = new BufferedReader(new InputStreamReader(objectInputStream));

{{< /tab >}}

{{< tab header="v2" lang="java" >}}

    // Existing bucket name.
final String BUCKET_NAME = "records";

    // The key of the object in the bucket, usually the name of the file.
final String objectKey = "hello-v2x.txt";

    // Creating the PUT request with all the relevant information.
PutObjectRequest putObjectRequest = PutObjectRequest.builder()
    .bucket(BUCKET_NAME)
    .key(objectKey)
    .build();

    // Put the file into the S3 bucket
PutObjectResponse response = s3Client.putObject(putObjectRequest, Paths.get(filePath));

    // Creating the GET request with all the relevant information.
GetObjectRequest getObjectRequest = GetObjectRequest.builder()
    .bucket(BUCKET_NAME)
    .key(objectKey)
    .build();

    // Retrieving the object from the bucket.
ResponseInputStream<GetObjectResponse> response = s3Client.getObject(getObjectRequest);

{{< /tab >}}
{{< /tabpane >}}

### DynamoDB Service

Another interesting case is interacting with the DynamoDB service. Here we can see code snippets of
a DynamoDB client inserting an entity of type `Person` into a table with the same name. Once the object is in
the database, we would like to retrieve it as well.
Just like the example before, the scripts to create the AWS services on LocalStack can be found under 
the `src/main/resources` folder of each module in the repository.

Pay particular attention to the handling of the data model in the v2 example. As part of improvements, some
boilerplate code can be abstracted with the help of specific annotations, which help label the Java bean, the 
partition key and even specify converters for certain data types. 
Unfortunately, the enhanced mapping in v2 does not support Date type, but a handwritten converter is enough to
cater to the application's needs. The full list of supported converters can be found 
[here](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/internal/converter/attribute/package-summary.html).

#### Configuring the DynamoDB Client

{{< tabpane lang="java" >}}
{{< tab header="v1" lang="java">}}

    // Credentials that can be replaced with real AWS values. (To be handled properly and not hardcoded.)
    // These can be skipped altogether for LocalStack, but we generally want to avoid discrepancies with production code.
final String ACCESS_KEY = "test";
final String SECRET_KEY = "test";

    // Building a basic credentials object.
BasicAWSCredentials credentials = new BasicAWSCredentials(ACCESS_KEY, SECRET_KEY);

    // Creating the DynamoDB client using the credentials, specific region and an endpoint configured for LocalStack.
private static AmazonDynamoDB dynamoDBClient = AmazonDynamoDBClientBuilder.standard()
    .withCredentials(new AWSStaticCredentialsProvider(credentials))
    .withEndpointConfiguration(
    new EndpointConfiguration("localhost.localstack.cloud:4566", Regions.US_EAST_1.getName()))
    .build();

{{< /tab >}}

{{< tab header="v2" lang="java">}}

    // Credentials that can be replaced with real AWS values. (To be handled properly and not hardcoded.)
    // These can be skipped altogether for LocalStack, but we generally want to avoid discrepancies with production code.
final String ACCESS_KEY = "test";
final String SECRET_KEY = "test";


    // Creating the AWS Credentials provider, using the above access and secret keys.
AwsCredentialsProvider credentials = StaticCredentialsProvider.create(
AwsBasicCredentials.create(ACCESS_KEY, SECRET_KEY));

    // Selected region.
Region region = Region.US_EAST_1;

    // Creating the dynamoDB client using the credentials, the specific region and a LocalStack endpoint.
DynamoDbClient dynamoDbClient = DynamoDbClient.builder()
    .region(region)
    .credentialsProvider(
    credentials)
    .endpointOverride(URI.create("https://localhost.localstack.cloud:4566"))
    .build();

    // Creating an enhanced client, which provides additional actions to the plain client.
DynamoDbEnhancedClient enhancedClient = DynamoDbEnhancedClient.builder()
    .dynamoDbClient(dynamoDbClient)
    .build();

{{< /tab >}}
{{< /tabpane >}}


#### Interacting with DynamoDB

{{< tabpane lang="java" >}}

{{< tab header="v1" lang="java">}}

    // Existing table name
String TABLE_NAME = "person";

    // Creating a DynamoDB instance
DynamoDB dynamoDB = new DynamoDB(dynamoDBClient);

    // Creating a Table object that will be an interface in interacting with the DB table.
Table table = dynamoDB.getTable(TABLE_NAME);

    //Creating a Person object.
Person person = new Person();
person.setId(personID);
person.setName("John Doe");
person.setBirthdateFromString("1984-10-12");

    // Creating an Item to represent the Person object.
Item item = new Item()
    .withPrimaryKey("id", person.getId())
    .withString("name", person.getName())
    .withString("birthdate", person.getBirthdateAsString());

    // Adding the item to the DynamoDB table.
table.putItem(item);

    // The "id" field was defined as partition key.
String partitionKey = "id";

    // Getting the item from the DynamoDB table using the primary key.
Item item = table.getItem(partitionKey, personId);

    // Mapping the DynamoDB item to a Person object.
Person person = new Person();
person.setId(item.getString("id"));
person.setName(item.getString("name"));
person.setBirthdateFromString(item.getString("birthdate"));

{{< /tab >}}

{{< tab header="v2" lang="java">}}

    // Existing table name.
String TABLE_NAME = "person";

      // Creating the Person object.
Person person = new Person();
person.setId(personID);
person.setName("John Doe");
person.setBirthdateFromString("1979-01-01");

      // Using the enhanced client to interact with the table.
DynamoDbTable<Person> table = enhancedClient.table(TABLE_NAME,
          TableSchema.fromBean(Person.class));

    // Adding new entry to the table.
table.putItem(person);

    // Person's id.
String personId = "000012356";

    // Retrieving the entity based on id.
Person person = table.getItem(Key.builder().partitionValue(personId).build());

{{< /tab >}}
{{< /tabpane >}}

## Resources

* [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/)
* [Official repository of the AWS SDK for Java (v1)](https://github.com/aws/aws-sdk-java)
* [Official repository of the AWS SDK for Java (v2)](https://github.com/aws/aws-sdk-java-v2)
* [localstack-aws-sdk-examples for Java](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/java)

