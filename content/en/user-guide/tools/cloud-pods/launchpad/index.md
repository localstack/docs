---
title: "Cloud Pods Launchpad"
weight: 10
categories: ["LocalStack Pro", "Tools"]
description: >
  The LocalStack Cloud Pods Launchpad offers the easiest way of sharing and injecting cloud pods directly from your repositories or via a simple URL.
---

The LocalStack Cloud Pods Launchpad allows you to quickly share and inject cloud pods into a LocalStack instance.


## Creating your sharable link

Navigate to <https://app.localstack.cloud/launchpad> where you can create a sharable link for your pods.

![Cloud Pods Launchpad Link Generator](link-generator.png)

Enter a public URl to your pod in the first input field, and click on 'Generate Link'.
The resulting link can be copied and shared with others.

You can also copy the markdown snippet to quickly add a badge to your repository.

{{< alert title="Warning" color="warning" >}}
Please consider that the launchpad takes an arbitrary URL as input and passes it onto your LocalStack instance to inject the pod. 
This may lead to unintended side effects, as the URL that is passed to the launchpad is not validated in any way. 

We also display the URL on the UI, so please make sure that your trust the URL when using the launchpad.
{{< /alert >}}


## Adding a badge to your repository

If you want to add a badge to your README that links to the Cloud Pod Launchpad, you can use the following markdown snippet:

```markdown
[![Launch LocalStack Cloudpod](https://localstack.cloud/gh/launch-pod-badge.svg)](https://app.localstack.cloud/launchpad?url=url_of_your_pod)
```

![Cloud Pods Badge Demonstration](badge-demo.png)

Please note that you have to add the `url_of_your_pod` as the `url` query parameter to the URL.
For example if you are hosting the pod in the same repository, just use the URL pointing to the raw pod file.
Additionally, you can use the [Link Generator]({{< ref "#creating-your-sharable-link" >}}) to create the sharable link for your pod and copy the markdown for your repo.

Check out a proper example <a href="https://github.com/localstack/cloud-pod-badge" target="_blank">on this GitHub repository</a>.


## Troubleshooting common problems

In this section we present an overview of common problems and how to solve them.

### LocalStack is not running

In case your LocalStack instance is not running, you will see the following error message:

![Cloud Pods Launchpad Error LocalStack not running](ls-not-running.png)

Please start up your LocalStack instance and try again.
Find out more about how to start LocalStack in the [Getting Started]({{< ref "getting-started" >}}) section.

### Failed to load metadata

In case the launchpad fails to load the metadata of your pod, you will see the following error message:

![Cloud Pods Launchpad Error failed to load metadata](metadata-load-failed.png)

This can happen if the pod is not available anymore or if the URL is not valid.
Please check the URL and try again.

### Failed to inject pod

In case the launchpad fails to inject the pod into your LocalStack instance, you will see 'Pod injection failed' in the log message.
This may be due to a couple of reasons, like version mismatch.
Please check out your LocalStack logs for more information.
