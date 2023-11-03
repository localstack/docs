---
title: "Live Policy Stream"
linkTitle: "Live Policy Stream"
weight: 3
description: Generate a live stream of policies as requests are coming into LocalStack
---

## Introduction

Live Policy Stream produces a continuous flow of policies and the associated principals or resources. With each request, it starts by displaying the principal or resource that the policy should be linked to. This will either be a service resource in the case of resource-based policies, or an IAM principal in other scenarios. Following that, it presents the recommended policy.
