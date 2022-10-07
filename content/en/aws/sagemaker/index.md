---
title: "SageMaker"
linkTitle: "SageMaker"
categories: ["LocalStack Pro"]
description: >
  SageMaker
---

LocalStack Pro provides a local version of the SageMaker API, which allows running jobs to create machine learning models (e.g., using PyTorch) and to deploy them.

## Model Training

A basic training example using the `sagemaker.tensorflow.TensorFlow` class is provided in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/sagemaker-ml-jobs). Essentially, the code boils down to these core lines:
```
inputs = ...  # load training data files
mnist_estimator = TensorFlow(entry_point='mnist.py', role='arn:aws:...',
    framework_version='1.12.0', sagemaker_session=sagemaker_session,
    train_instance_count=1, training_steps=10, evaluation_steps=10)
mnist_estimator.fit(inputs, logs=False)
```

The code snippet above uploads the model training code to local S3, submits a new training job to the local SageMaker API, and finally puts the trained model back to an output S3 bucket. Please refer to the sample repo for more details.

## Model Deployment and Inference

SageMaker supports the deployment and real-time inference of singular local ML models. An example for that is provided in our [PRO samples repository](https://github.com/localstack/localstack-pro-samples/tree/master/sagemaker-ml-jobs). As explained in the ReadMe of the sample, you will need to retrieve the image with your AWS account by connecting with [the provided ECR repository](https://github.com/aws/deep-learning-containers/blob/master/available_images.md):

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com
```

The example also shows the two currently supported options of inference - on the container itself or through the `sagemaker-runtime` invocation endpoint:

```python
def inference_model_container(run_id: str = "0"):
    ep = sagemaker.describe_endpoint(EndpointName=f"{ENDPOINT_NAME}-{run_id}")
    arn = ep["EndpointArn"]
    tag_list = sagemaker.list_tags(ResourceArn=arn)
    port = "4510"
    for tag in tag_list["Tags"]:
        if tag["Key"] == "_LS_ENDPOINT_PORT_":
            port = tag["Value"]
    inputs = _get_input_dict()
    response = httpx.post(f"http://localhost.localstack.cloud:{port}/invocations", json=inputs,
                          headers={"Content-Type": "application/json", "Accept": "application/json"})
    _show_predictions(json.loads(response.text))


def inference_model_boto3(run_id: str = "0"):
    inputs = _get_input_dict()
    response = sagemaker_runtime.invoke_endpoint(EndpointName=f"{ENDPOINT_NAME}-{run_id}", Body=json.dumps(inputs),
                                                 Accept="application/json",
                                                 ContentType="application/json")
    _show_predictions(json.loads(response["Body"].read()))
```

{{< alert >}}
**Note:** SageMaker is a fairly comprehensive API - for now, only a subset of the functionality is provided locally, but new features are being added on a regular basis.
{{< /alert >}}
