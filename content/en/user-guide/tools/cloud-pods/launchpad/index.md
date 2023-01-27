---
title: "Cloud Pods Launchpad"
weight: 10
categories: ["LocalStack Pro", "Tools"]
description: >
  Our Cloud Pods Launchpad offers the easiest way of sharing and injecting cloud pods directly from GitHub.
---

## Adding a badge to your repository

If you want to add a badge to your README that links to the Cloud Pod Launchpad, you can use the following markdown snippet:

```markdown
[![LocalStack Pods Launchpad](https://localstack.cloud/gh/pod_badge.svg)](https://app.localstack.cloud/launchpad?url=url_of_your_pod)
```

Please note that you have to add your `url_of_your_pod` as the `url` query parameter to the URL.
For example if you are hosting the pod in the same repository, just use the URL pointing to the raw pod zip.

Check out a proper example <a href="https://github.com/localstack/cloud-pod-badge" target="_blank">on this GitHub repository</a>.

## Security concerns regarding the launchpad

Please consider that the launchpad takes an arbitrary URL as input and passes it onto your LocalStack instance to inject the pod. 
This may lead to unintended side effects, as the URL that is passed to the launchpad is not validated in any way. 

We also display the URL on the UI, so we recommend to only use the launchpad with trusted URLs.

