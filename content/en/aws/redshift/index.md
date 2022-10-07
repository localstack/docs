---
title: "Redshift"
linkTitle: "Redshift"
categories: ["LocalStack Pro"]
description: Get started with Amazon Redshift
---

Redshift is a cloud-based data warehouse solution which allows end users to aggregate huge volumes of data & parallel processing of data. Redshift is fully managed by AWS and serves as a petabyte-scale service which allows users to create visualization reports and critically analyze collected data. The query results can be saved to an S3 Data Lake while additional analytics can be provided by Athena or SageMaker.

A basic version of Redshift is available in LocalStack Pro - see the supported APIs are available over our [configuration page]({{< ref "configuration" >}}).

## Getting started

In this getting started guide, you'll learn how to make a basic usage of Redshift over LocalStack. This guide is intended for users who wish to get more acquainted with SNS, and assumes you have basic knowledge of the AWS CLI (and our `awslocal` wrapper script). To get started, start your LocalStack instance using your preferred method:

1. Create a cluster named `mysamplecluster` using the `awslocal` CLI:
   {{< command >}}
   $ awslocal redshift create-cluster --cluster-identifier mysamplecluster --master-username masteruser --master-user-password secret1 --node-type ds2.xlarge --cluster-type single-node
   {{< /command >}}

2. Check the Redshift cluster creation progress by running the following command:
   {{< command >}}
   $ awslocal redshift describe-clusters --cluster-identifier mysamplecluster
   {{< /command >}}
   {{< alert >}}
   **Note**: Redshift is essentially mocked in LocalStack along side the node type. Hence while developing and testing locally, you can use any node type.
   {{< /alert >}}

3. Get all the information about all cluster security groups in the account:
   {{< command >}}
   $ awslocal redshift describe-cluster-security-groups
   {{< /command >}}

4. Get all the general cluster properties: 
   {{< command >}}
   $ awslocal redshift describe-clusters
   {{< /command >}}

5. Associate a cluster with a cluster security group:
   {{< command >}}
   $ awslocal redshift modify-cluster --cluster-identifier mysamplecluster --cluster-security-groups mysamplesecuritygroup
   {{< /command >}}

6. Delete a cluster without specifying a final snapshot:
   {{< command >}}
   $ awslocal redshift delete-cluster --cluster-identifier mysamplecluster --skip-final-cluster-snapshot
   {{< /command >}}

To get started with a more extensive example, refer the [Glue Crawler RedShift Integration (JDBC)](https://github.com/localstack/localstack-pro-samples/tree/master/glue-redshift-crawler) sample project.