---
title: "Organizations"
linkTitle: "Organizations"
tags: ["Ultimate"]
description: Get started with AWS Organizations on LocalStack
---

Amazon Web Services Organizations is an account management service that allows you to consolidate multiple different AWS accounts into an organization.
It allows you to manage different accounts in a single organization and consolidate billing.
With Organizations, you can also attach different policies to your organizational units (OUs) or individual accounts in your organization.

Organizations is available over LocalStack Pro and the supported APIs are available over our [configuration page]({{< ref "configuration" >}}).

## Getting started

In this getting started guide, you'll learn how to create your local AWS Organization and configure it with member accounts.
This guide is intended for users who wish to get more acquainted with Organizations, and assumes you have basic knowledge of the AWS CLI (and our `awslocal` wrapper script).
To get started, start your LocalStack instance using your preferred method:

1. Create a new local AWS Organization with the feature set flag set to `ALL`:
   {{< command >}}
   $ awslocal organizations create-organization --feature-set ALL
   {{< /command >}}

2. You can now run the `describe-organization` command to see the details of your organization:
   {{< command >}}
   $ awslocal organizations describe-organization
   {{< /command >}}

3. You can now create an AWS account that would be a member of your organization:
   {{< command >}}
   $ awslocal organizations create-account \
      --email example@example.com \
      --account-name "Test Account"
   {{< /command >}}
   Since LocalStack essentially mocks AWS, the account creation is instantaneous.
  You can now run the `list-accounts` command to see the details of your organization:
   {{< command >}}
   $ awslocal organizations list-accounts
   {{< /command >}}

4. You can also remove a member account from your organization:
   {{< command >}}
   $ awslocal organizations remove-account-from-organization --account-id <ACCOUNT_ID>
   {{< /command >}}

5. To close an account in your organization, you can run the `close-account` command:
   {{< command >}}
   $ awslocal organizations close-account --account-id 000000000000
   {{< /command >}}

6. You can use organizational units (OUs) to group accounts together to administer as a single unit.
  To create an OU, you can run:
   {{< command >}}
   $ awslocal organizations list-roots
   $ awslocal organizations list-children \
        --parent-id <PARENT-ID> \
        --child-type ORGANIZATIONAL_UNIT
   $ awslocal organizations create-organizational-unit \
        --parent-id <PARENT-ID> \
        --name New-Child-OU
   {{< /command >}}

7. Before you can create and attach a policy to your organization, you must enable a policy type.
  To enable a policy type, you can run:
   {{< command >}}
   $ awslocal organizations enable-policy-type \
        --root-id <ROOT-ID> \
        --policy-type BACKUP_POLICY
   {{< /command >}}
   To disable a policy type, you can run:
   {{< command >}}
   $ awslocal organizations disable-policy-type \
        --root-id <ROOT-ID> \
        --policy-type BACKUP_POLICY
   {{< /command >}}

8. To view the policies that are attached to your organization, you can run:
   {{< command >}}
   $ awslocal organizations list-policies --filter SERVICE_CONTROL_POLICY
   {{< /command >}}

9. To delete an organization, you can run:
   {{< command >}}
   $ awslocal organizations delete-organization
   {{< /command >}}
