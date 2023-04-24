---
title: "Cloud Pods Browser"
tags: ["LocalStack Team", "LocalStack Enterprise"]
weight: 5
description: >
    The Cloud Pods Browser allows you to view, manage, and explore your Cloud Pods through the LocalStack Web Application.
---

[The Cloud Pods Browser](https://app.localstack.cloud/pods) lets you access and manage all your Cloud Pods. The Cloud Pods Browser is a feature of our LocalStack Web Application that is exclusive to **LocalStack Team & Enterprise users**.

With Cloud Pods, you can have individual or shared ownership of a snapshot of your LocalStack instance. 
The LocalStack CLI allows you to create new Cloud Pods and configure their [visibility settings](https://docs.localstack.cloud/user-guide/tools/cloud-pods/pods-cli/#save).

<img src="cloud-pods-browser.png" alt="LocalStack Web Application's Cloud Pods Browser outlining various saved Clod Pods" title="Cloud Pods Browser" width="900" />

## Usage

You can use [Cloud Pods](https://docs.localstack.cloud/user-guide/tools/cloud-pods/) to manage your local AWS infrastructure and collaborate with others:

- Cloud Pods are accessible to all LocalStack Team users in your organization namespace. Public Cloud Pods are accessible to all LocalStack users.
- Cloud Pods version history is available, which allows you to view the version history of a Cloud Pod and access previous versions of specific Cloud Pods.
- Cloud Pods can be made public, injected into a running LocalStack container, or deleted - all from the LocalStack Web Application.

{{< alert title="Warning" color="warning">}}
LocalStack Pro users cannot access the Cloud Pods Browser. Community & Pro users can use the [Community Cloud Pods](https://docs.localstack.cloud/user-guide/tools/cloud-pods/community/) and save their Cloud Pods locally or share them via a GitHub/GitLab repository. The [Cloud Pods launchpad](https://docs.localstack.cloud/user-guide/tools/cloud-pods/launchpad/) can be used to inject a Cloud Pod into a running LocalStack container through a simple click.
{{< /alert >}}

## Access the version history

To view the version history of a Cloud Pod, click on the Cloud Pod's name in the Cloud Pods Browser. You will be able to see a list of all versions, and view details of a specific version, in JSON format, by clicking on it.

<img src="cloud-pods-version-history.png" alt="LocalStack Web Application's Cloud Pods Browser outlining the versions of the Clod Pod" title="Cloud Pods Browser displaying the version history of the Cloud Pod" width="900" />

To create a new version of a Cloud Pod, refer to the [Cloud Pods CLI](https://docs.localstack.cloud/user-guide/tools/cloud-pods/pods-cli/#save) documentation.

## Save a Cloud Pod

Users do not need to upload their Cloud Pod to the LocalStack Web Application since the Cloud Pods CLI automatically uploads pods via the `save` operation. Similarly, the Cloud Pods CLI automatically injects the Cloud Pod into a running LocalStack container via the `load` operation after specifying the Cloud Pod's name. You can alternatively select a Cloud Pod on the Cloud Pods Browser and inject it into a running LocalStack container.

<img src="cloud-pod-inject.png" alt="Inject a Cloud Pod through the Cloud Pods Browser" title="Inject a Cloud Pod through the Cloud Pods Browser" width="900" />

We use a secure storage mechanism to store Cloud Pods on the LocalStack Web Application. When you push a Cloud Pod, it is stored securely in our storage backend in AWS, with each user/organization receiving a dedicated, isolated S3 bucket. Pushing and pulling a Cloud Pod from our Web Application is facilitated by using secure S3 pre-signed URLs for the Cloud Pods CLI to interact directly with the S3 bucket, rather than piping the state files through our LocalStack Platform APIs.
