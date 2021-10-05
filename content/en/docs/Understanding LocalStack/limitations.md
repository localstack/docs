---
title: "LocalStack Limitations"
weight: 50
description: >
  Known limitations of LocalStack and its services
---

## Covered Topics

* [Implementation Limitations](#implementation-limitations)
* [Runtime Environment Limitations](#runtime-environment-limitations)
* [Integration Limitations](#integration-limitations)

## Implementation Limitations

Limitations that exist due to missing features in LocalStack

## Runtime Environment Limitations

OS-specific and other runtime environment limitations

* [ARM64 (Including Apple M1 chip)](#arm64-including-apple-m1-chip)

### ARM64 (Including Apple M1 chip)

{{% alert title="Aarch64 Support" color="info" %}}
The LocalStack team and community are working hard to bring M1 support to LocalStack images.
There are still several limitations with LocalStack dependencies on ARM architectures.
{{% /alert %}}

Currently, LocalStack images do not fully support `aarch64`, including
Apple M1 silicon.

However, this does not mean you cannot run LocalStack on M1 machines. Folow the
next workaround tip to get LocalStack up and running on your M1.

{{% alert title="Note on JVM Lambda" color="warning" %}}
You need to use the `local` lambda executor for JVM Lambda functions
{{% /alert %}}

To be on a safer side, you can enable "Rosetta" on your preferred Terminal. This
way you'll be installing packages for `x86_64` platform.

![Rosetta](../m1-trouble-1.png)

What we will be doing now is installing Java and Python executables using
Homebrew, it should automatically resolve packages to proper architecture versions.

```shell
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install java11 and follow instructions
brew install java11

# Install jenv and follow instructions
brew install jenv

# Add Java11 to jenv and use it globally
jenv add /Library/Java/JavaVirtualMachines/openjdk-11.jdk/Contents/Home/
jenv global 11

# Install pyenv and follow instructions
brew install pyenv

# Install python 3.8.10 and enable it globally
pyenv install 3.8.10
pyenv global 3.8.10
```

Then clone LocalStack to your machine, run `make install` and then `make start`.

#### DynamoDB

At the moment only a locally launched LocalStack instance can properly run the DynamoDB service.

#### Lambda Functions

Only the local executor with locally launched LocalStack can be used together with JVM Lambda Functions.

## Integration Limitations

Limitations that may occur because of third party integrations behavior

* [CDK](#cdk)

### CDK

#### Stacks with validated certificates

By default, stacks with validated certificates may not be deployed using the `local` lambda executor.
This originates from the way how CDK ensures the certificate is ready - it creates a single-file lambda function with a single dependency on `aws-sdk` which is usually preinstalled and available globally in lambda runtime.
When this lambda is executed locally from the `/tmp` folder, the package can not be discovered by Node due to the way how Node package resolution works.
