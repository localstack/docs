---
title: "Analytics Dashboard"
linkTitle: "Analytics Dashboard"
weight: 5
categories: ["LocalStack Pro"]
description: >
  An Introduction to the LocalStack Pro Analytics Dashboard
---

LocalStack allows for transparent collection of execution events, in order to provide usage analytics and insights into the testing process overall.

Simply configure your system with the `LOCALSTACK_API_KEY` environment variable, and the system will start making your events accessible on the LocalStack dashboard at https://app.localstack.cloud/dashboard.

{{< alert title="Data Privacy" >}}
Please note that data privacy is one of our key concerns; data is only collected in an anonymized way, and never exposes any sensitive information about your application.
{{< /alert >}}

The following screenshot shows an the Analytics Dashboard in action:

![Analytics Dashboard](analytics-dashboard.png)