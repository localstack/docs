---
title: "Extensions Library"
weight: 5
description: Get started with Extensions Library to extend LocalStack by adding new services and features via Extension mechanism.
---

## Introduction

LocalStack Extensions that allow developers to extend and customize LocalStack. A LocalStack Extension is a Python application that runs together with LocalStack within the LocalStack container.

LocalStack Extensions are available to the licensed users, and the list of available extensions is available in the [Extensions Library](https://app.localstack.cloud/extensions/library).

<img src="extensions-library-ui.png" alt="LocalStack Extensions Library" title="LocalStack Extensions Library" width="900" />

## Installing an Extension

To install an Extension using the LocalStack Extensions Library, you can navigate to the [**app.localstack.cloud/extensions/library**](https://app.localstack.cloud/extensions/library) and click on the **Go to Instance** button to open the list of available instances. If you are running your LocalStack instance locally, you can click on the **Default** option.

You will be redirected to the LocalStack Instance page, where you can directly click the **Install** button to install the Extension. The installation process will take a few seconds, and will restart your LocalStack instance. Click **Continue** to proceed.

## Managing Extensions

You can further manage the installed Extensions by navigating to the **Extensions** tab in the LocalStack Instance page. You can remove an Extension by clicking the **Remove** button.

<img src="extensions-library-management.png" alt="Installed LocalStack Extensions Library" title="Installed LocalStack Extensions Library" width="900" />

### Supported Extensions

The following Extensions are currently available in the Extensions Library:

-   [AWS Replicator](https://docs.localstack.cloud/user-guide/tools/localstack-extensions/aws-replicator-extension/)
-   [Stripe](https://docs.localstack.cloud/user-guide/tools/localstack-extensions/stripe-extension/)
-   [Miniflare](https://docs.localstack.cloud/user-guide/tools/localstack-extensions/miniflare-extension/)
-   [MailHog](https://docs.localstack.cloud/user-guide/tools/localstack-extensions/mailhog/)
-   [httpbin](https://docs.localstack.cloud/user-guide/tools/localstack-extensions/httpbin-extension/)
-   [Diagnostic Viewer](https://docs.localstack.cloud/user-guide/tools/localstack-extensions/diagnosis-viewer-extension/)
