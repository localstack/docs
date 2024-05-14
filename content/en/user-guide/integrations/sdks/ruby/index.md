---
title: "Ruby"
categories: []
description: >
  How to use the AWS SDK for Ruby with LocalStack.
---

## Overview

The [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/), like other AWS SDKs, lets you set the endpoint when creating resource clients, which is the preferred way of integrating the Ruby SDK with LocalStack.

## Example

Here is an example of how to create a S3 bucket with the AWS configuration endpoint set to LocalStack:

```ruby
require "aws-sdk-s3"

# Wraps Amazon S3 bucket actions.
class BucketCreateWrapper
  attr_reader :bucket

  # @param bucket [Aws::S3::Bucket] An Amazon S3 bucket initialized with a name.
  def initialize(bucket)
    @bucket = bucket
  end

  # Creates an Amazon S3 bucket in the specified AWS Region.
  #
  # @param region [String] The Region where the bucket is created.
  # @return [Boolean] True when the bucket is created; otherwise, false.
  def create?(region)
    @bucket.create(create_bucket_configuration: { location_constraint: region })
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't create bucket. Here's why: #{e.message}"
    false
  end

  # Gets the Region where the bucket is located.
  #
  # @return [String] The location of the bucket.
  def location
    if @bucket.nil?
      "None. You must create a bucket before you can get its location!"
    else
      @bucket.client.get_bucket_location(bucket: @bucket.name).location_constraint
    end
  rescue Aws::Errors::ServiceError => e
    "Couldn't get the location of #{@bucket.name}. Here's why: #{e.message}"
  end
end

def run_demo
  region = "us-east-2"
  Aws.config.update(
    endpoint:  'http://s3.localhost.localstack.cloud:4566', # update with localstack endpoint
    access_key_id: 'test', # update with localstack credentials
    secret_access_key: 'test', # update with localstack credentials
    region: region,
    force_path_style: true, # Enable 'force_path_style' => true, if bucket name is non DNS compliant
  )
  bucket_name = "doc-example-bucket-#{SecureRandom.uuid}"
  wrapper = BucketCreateWrapper.new(Aws::S3::Bucket.new(bucket_name))
  return unless wrapper.create?(region)

  puts "Created bucket #{wrapper.bucket.name}."
  puts "Your bucket's region is: #{wrapper.location}"
end

run_demo if $PROGRAM_NAME == __FILE__
```

You can run the example by saving it to a file, for example `localstack.rb`, and then running it with:

{{< command >}}
$ ruby ./localstack.rb                                                                                                        
Created bucket doc-example-bucket-b911f85f-4dd3-4668-a32e-3f69aa4e37dc.
Your bucket's region is: us-east-2
{{< /command >}}

{{< callout >}}
The endpoint we configure for the S3 and virtual host bucket is `http://s3.localhost.localstack.cloud`. In case of issues resolving the DNS record, we can fall back to `http://localhost:4566` in combination with the provider setting `force_path_style: true`. The S3 service endpoint differs slightly from the other service endpoints because AWS deprecates path-style-based access for hosting buckets.
{{< /callout >}}

For alternative AWS services, you can use the following configuration:

```ruby
region = "us-east-2"
Aws.config.update(
    endpoint:  'http://localhost:4566', # update with localstack endpoint
    access_key_id: 'test', # update with localstack credentials
    secret_access_key: 'test', # update with localstack credentials
    region: region,
)
```

## Resources

* [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/)
* [Official repository of the AWS SDK for Ruby](https://github.com/aws/aws-sdk-ruby)
