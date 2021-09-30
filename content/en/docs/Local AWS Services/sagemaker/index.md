---
title: "SageMaker"
linkTitle: "SageMaker"
categories: ["LocalStack Pro"]
description: >
  SageMaker
---

LocalStack Pro provides a local version of the SageMaker API, which allows running jobs to create machine learning models (e.g., using TensorFlow).

A basic example using the `sagemaker.tensorflow.TensorFlow` class is provided in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/sagemaker-ml-jobs). Essentially, the code boils down to these core lines:
```
inputs = ...  # load training data files
mnist_estimator = TensorFlow(entry_point='mnist.py', role='arn:aws:...',
    framework_version='1.12.0', sagemaker_session=sagemaker_session,
    train_instance_count=1, training_steps=10, evaluation_steps=10)
mnist_estimator.fit(inputs, logs=False)
```

The code snippet above uploads the model training code to local S3, submits a new training job to the local SageMaker API, and finally puts the trained model back to an output S3 bucket. Please refer to the sample repo for more details.

{{< alert >}}
**Note:** SageMaker is a fairly comprehensive API - for now, only a subset of the functionality is provided locally, but new features are being added on a regular basis.
{{< /alert >}}
