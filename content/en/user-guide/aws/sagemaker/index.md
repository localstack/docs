---
title: "SageMaker"
linkTitle: "SageMaker"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS SageMaker on LocalStack
aliases:
  - /aws/sagemaker/
---

## Introduction 

Amazon SageMaker is a fully managed service provided by Amazon Web Services (AWS) that provides the tools to build, train, and deploy machine-learning models in the cloud for predictive analytics applications. It streamlines the machine learning development process, reduces the time and effort required to build and deploy models, and offers the scalability and flexibility needed for large-scale machine learning projects in the AWS cloud.

LocalStack Pro provides a local version of the SageMaker API, which allows running jobs to create machine learning models (e.g., using PyTorch) and to deploy them. The supported APIs are available on our [Sagemaker coverage page](https://docs.localstack.cloud/references/coverage/coverage_sagemaker/), which provides information on the extent of Sagemaker integration with LocalStack.


## Getting started

This guide is designed for users new to Sagemaker and assumes basic knowledge of the AWS CLI and our awslocal wrapper script.


### Model Training

A basic training example using the `sagemaker.tensorflow.TensorFlow` class is provided in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/sample-archive/sagemaker-ml-jobs). Essentially, the code boils down to these core lines:
```python3
inputs = ...  # load training data files
mnist_estimator = TensorFlow(entry_point='mnist.py', role='arn:aws:...',
    framework_version='1.12.0', sagemaker_session=sagemaker_session,
    train_instance_count=1, training_steps=10, evaluation_steps=10)
mnist_estimator.fit(inputs, logs=False)
```

The code snippet above uploads the model training code to local S3, submits a new training job to the local SageMaker API, and finally puts the trained model back to an output S3 bucket. Please refer to the sample repo for more details.

### Model Deployment and Inference

SageMaker supports the deployment and real-time inference of singular local ML models. An example for that is provided in our [PRO samples repository](https://github.com/localstack/localstack-pro-samples/tree/master/sagemaker-inference). As explained in the ReadMe of the sample, you will need to retrieve the image with your AWS account by connecting with [the provided ECR repository](https://github.com/aws/deep-learning-containers/blob/master/available_images.md):

{{< command >}}
$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-east-1.amazonaws.com
{{< /command >}}

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

{{< alert title="Note" >}}
SageMaker is a fairly comprehensive API - for now, only a subset of the functionality is provided locally, but new features are being added on a regular basis.
{{< /alert >}}


## Resource Browser

The LocalStack Web Application provides a [Resource Browser](https://docs.localstack.cloud/user-guide/web-application/resource-browser/) for managing Lambda resources. You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **Sagemaker** under the **Compute** section.

The Resource Browser displays Models, Endpoint Configurations and Endpoint. You can click on individual resources to view their details.

<img src="sagemaker-resource-browser.png" alt="Sagemaker Resource Browser" title="Lambda Resource Browser" width="900" />

The Resource Browser allows you to perform the following actions:

- **Create and Remove Models**: You can remove existing model and create a new model with the required configuration


  <img src="sagemaker-create-model.png" alt="Sagemaker Resource Browser" title="Lambda Resource Browser" width="900" />


- **Endpoint Configurations & Endpoints**: You can create endpoints from the resource browser that hosts your deployed machine learning model. You can also create endpoint configuration that specifies the type and number of instances that will be used to serve your model on an endpoint.

## Examples 

The following code snippets and sample applications provide practical examples of how to use Sagemaker in LocalStack for various use cases:

- [MNIST handwritten digit recognition model running on a local SageMaker endpoint](https://github.com/localstack-samples/sample-mnist-digit-recognition-sagemaker) demonstrates how to use SageMaker on LocalStack. A simple web frontend allows users to draw a digit and submit it to a locally running SageMaker endpoint. The endpoint returns a prediction of the digit, which is then displayed in the web frontend. Request handling is performed by a Lambda function, accessible via a function URL, that uses the SageMaker SDK to invoke the endpoint.
