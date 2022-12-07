---
title: "Creating reproducible machine learning applications using Cloud Pods for persistent state snapshots"
linkTitle: "Creating reproducible machine learning applications using Cloud Pods for persistent state snapshots"
weight: 5
description: >
  With LocalStack Cloud Pods, you can create persistent state snapshots to enable next-generation state management and team collaboration features for your local development environment. Learn how you can create reproducible machine learning applications & samples using Cloud Pods to take a snapshot of your LocalStack state at any point in time.
type: tutorials
---

LocalStack Cloud Pods enable you to create persistent state snapshots of your LocalStack instance, which can then be versioned, shared, and restored. It allows next-generation state management and team collaboration for your local cloud development environment, which you can utilize to create persistent shareable cloud sandboxes. Cloud Pods works similarly to the `git` version control system and uses the same concepts and commands to save, merge, and restore snapshots of your LocalStack state. You can always tear down your LocalStack instance and restore it from a snapshot at any point in time.

Cloud Pods is supported by both [LocalStack Pro](https://app.localstack.cloud/) and [LocalStack Community](https://github.com/localstack/localstack). Using Community Cloud Pods, you get a limited experience saving and loading your LocalStack state in a Cloud Pod, only with the AWS services emulated in the Community Edition. With LocalStack Pro, you can utilize an extended CLI that allows you to inspect your Cloud Pods, version them using tags similar to `git`, and push them to LocalStack Pod's platform.

In this tutorial, we will use [LocalStack Pro]({{< ref "getting-started/api-key" >}}) to train a simple machine-learning model that recognizes handwritten digits on an image. We will use Cloud Pods to create a reproducible sample by using an S3 bucket to host our training data, a Lambda function to train the model and a Lambda layer that contains the dependencies for our training code. We will then create a Cloud Pod to save the state of our LocalStack instance and restore it from the Cloud Pod to share it with our team.

{{< figure src="reproducible_ml_application.png" width="60%" alt="Reproducible machine-learning applications with LocalStack Cloud Pods">}}

## Prerequisites

For this tutorial, you will need the following:

- [LocalStack Pro](https://localstack.cloud/pricing/)
- [awslocal](https://docs.localstack.cloud/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [Optical recognition of handwritten digits dataset](https://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits)

If you don't have a subscription to LocalStack Pro, you can request a trial license upon sign-up. For this tutorial to work, you must have the LocalStack CLI installed, which must be version 1.3 or higher. The Cloud Pods CLI is shipped with the LocalStack CLI, so you don't need to install it separately.

## Training the machine learning model

We will use the Optical Recognition of Handwritten Digits Data Set to train a simple machine-learning model to recognise handwritten texts. It contains images of individual digits, represented as arrays of pixel values, along with their corresponding labels, indicating the correct digit that each image represents. You can download the dataset from UCI's Machine Learning Repository (linked above) or from our [samples repository](). To train our model, we will upload our dataset on a local S3 bucket and use a Lambda function to train the model.

Create a new file named `train.py` and import the required libraries:

```python
import os
import boto3
import numpy
from sklearn import datasets, svm, metrics
from sklearn.utils import Bunch
from sklearn.model_selection import train_test_split
```

We will now create a separate function named `load_digits` to load the dataset from the S3 bucket and return it as a `Bunch` object. The `Bunch` object is a container object that allows us to access the dataset's attributes as dictionary keys. It is similar to a Python dictionary but provides attribute-style access and can be used to store the dataset and its attributes.

```python
def load_digits(*, n_class=10, return_X_y=False, as_frame=False):
    # download files from S3
    s3_client = boto3.client("s3")
    s3_client.download_file(Bucket="pods-test", Key="digits.csv.gz", Filename="digits.csv.gz")

    data = numpy.loadtxt('digits.csv.gz', delimiter=',')
    target = data[:, -1].astype(numpy.int, copy=False)
    flat_data = data[:, :-1]
    images = flat_data.view()
    images.shape = (-1, 8, 8)

    if n_class < 10:
        idx = target < n_class
        flat_data, target = flat_data[idx], target[idx]
        images = images[idx]

    feature_names = ['pixel_{}_{}'.format(row_idx, col_idx)
                     for row_idx in range(8)
                     for col_idx in range(8)]

    frame = None
    target_columns = ['target', ]
    if as_frame:
        frame, flat_data, target = datasets._convert_data_dataframe(
            "load_digits", flat_data, target, feature_names, target_columns)

    if return_X_y:
        return flat_data, target

    return Bunch(data=flat_data,
                 target=target,
                 frame=frame,
                 feature_names=feature_names,
                 target_names=numpy.arange(10),
                 images=images)
```

The above code uses the `boto3` library to download the data file from an S3 bucket. The file is then loaded into a NumPy array using the `numpy.loadtxt` function, and the target values (i.e. the labels corresponding to each image) are extracted from the last column of the array. The images are then reshaped into 2-dimensional arrays, and the function has been configured to return only a subset of the available classes by filtering the target values. Finally, the function returns an object containing the data, target values, and metadata.

Let us now define a `handler` function that would be executed by the Lambda every time a trigger event occurs. In this case, we would like to use the above function to load the dataset and train a model using the Support Vector Machine (SVM) algorithm. After a train-test split, we will predict the value of the digit on the test subset:

```python
def handler(event, context):

    digits = load_digits()

    # flatten the images
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    # Create a classifier: a support vector classifier
    clf = svm.SVC(gamma=0.001)

    # Split data into 50% train and 50% test subsets
    X_train, X_test, y_train, y_test = train_test_split(
        data, digits.target, test_size=0.5, shuffle=False
    )

    # Learn the digits on the train subset
    clf.fit(X_train, y_train)

    # Predict the value of the digit on the test subset
    predicted = clf.predict(X_test)
    print("--> prediction result:", predicted)
```

After loading the images, they are flattened into 1-dimensional arrays and split into a training set and a test set using the `train_test_split` function from the `sklearn.model_selection` module. An SVM classifier is trained on the training set using the fit method. Finally, the trained model makes predictions on the test set using the prediction method, and the predicted values are printed to the console.

## Deploying the Lambda function

Before creating our Lambda function, let us start LocalStack to use emulated S3 and Lambda services to deploy and train our model. Let's start LocalStack:

{{< command >}}
$ DEBUG=1 LOCALSTACK_API_KEY=<your-api-key> localstack start -d
{{< / command >}}

We have specified `DEBUG=1` to get the printed LocalStack logs from our Lambda invocation in the console. We can now create an S3 bucket to upload our Lambda function and the dataset:

{{< command >}}
$ zip lambda.zip train.py
$ awslocal s3 mb s3://reproducible-ml
$ awslocal s3 cp lambda.zip s3://reproducible-ml/lambda.zip
$ awslocal s3 cp digits.csv.gz s3://reproducible-ml/digits.csv.gz
{{< / command >}}

We first zip our Lambda function into a `lambda.zip` file in the above commands. Next, we created an S3 bucket named `reproducible-ml` and uploaded the zip file and the dataset. We can now create a Lambda function using `awslocal` CLI by specifying the Lambda handler function and the S3 bucket where the `zip` file is located:

{{< command >}}
$ awslocal lambda create-function --function-name reproducible-ml-sample \
  --runtime python3.8 \
  --role r1 \
  --handler train.handler \
  --timeout 600 \
  --code '{"S3Bucket":"reproducible-ml","S3Key":"lambda.zip"}' \
  --layers arn:aws:lambda:us-east-1:446751924810:layer:python-3-8-scikit-learn-0-23-1:2
{{< / command >}}

We have specified the function name as `reproducible-ml-sample`, the runtime as `python3.8`, the handler function as `train.handler`, and the S3 bucket and key where the `zip` file is located. We have also specified the `python-3-8-scikit-learn-0-23-1` layer to be used by the Lambda function. This layer contains the `scikit-learn` library and its dependencies. We can now invoke the Lambda function using the `awslocal` CLI:

{{< command >}}
$ awslocal lambda invoke --function-name reproducible-ml-sample /tmp/test.tmp
{{< / command >}}

The logs of the Lambda invocation should be visible in the LocalStack container output (with `DEBUG=1` enabled):

```bash
null
>START RequestId: 65dc894d-25e0-168e-dea1-a3e8bfdb563b Version: $LATEST
> --> prediction result: [8 8 4 9 0 8 9 8 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 9 6 7 8 9
...
...
>  9 5 4 8 8 4 9 0 8 9 8]
> END RequestId: 6...
```

## Creating a Cloud Pod

After deploying the Lambda function, we can now create a Cloud Pod to share our local infrastructure & instance state with other LocalStack users in your organization. To save the state of our LocalStack instance, we will use the `save` command:

{{< command >}}
$ localstack pod save reproducible-ml

Cloud Pod reproducible-ml successfully created
{{< / command >}}

{{< alert title="Saving Cloud Pods locally" >}}
You can also export a Cloud Pod locally by specifying a file URI as an argument. To export on a local path, run the following command:

{{< command >}}
$ localstack pod save file://<path_on_disk>/<pod_name>
{{< / command >}}

The output of the above command will be a `<pod_name>.zip` file in the specified directory. We can restore it at any time with the `load` command.
{{< /alert >}}

To list all the Cloud Pods available locally or remote (LocalStack Pod's platform), you can use the `list` command:

{{< command >}}
$ localstack pod list

localstack pod list
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ local/remote ┃ Name            ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ local+remote │ reproducible-ml │
└──────────────┴─────────────────┘
{{< / command >}}

You can inspect the contents of a Cloud Pod using the `inspect` command:

{{< command >}}
$ localstack pod inspect reproducible-ml
{{< / command >}}

While you save a Cloud Pod, it is automatically published on the LocalStack Pod's platform and can be shared with other users in your organization. While saving an already existing Cloud Pod, we would create a new version, which is eventually uploaded to the LocalStack Pod's platform.

{{< alert title="Setting visibility of a Cloud Pod" >}}
You can optionally set the visibility of a Cloud Pod to `private` or `public` using the `--visibility` flag. By default, the visibility of a Cloud Pod is set to `private`. To set a Cloud Pod to `public`, you can use the following command:
{{< command >}}
$ localstack pod push --name <pod_name> --visibility public
{{< / command >}}
The above command does not create a new version and requires a version already registered with the platform.
{{< /alert >}}

You can also attach an optional message and a list of services to a Cloud Pod using the `--message` and `--services` flags. You can check all the Cloud Pods in your organization over the [LocalStack Web Application](https://app.localstack.cloud/cloudpods). Now that we have created a Cloud Pod, we can ask one of our team members to start LocalStack and load the Cloud Pod using the `load` command.

{{< command >}}
$ localstack pod load reproducible-ml
{{< / command >}}

The `load` command will retrieve the content of our Cloud Pod named `reproducible-ml` from the LocalStack Pod's platform and inject it into our running LocalStack instance. Upon successfully loading the Cloud Pod, the Lambda function can be invoked again, and the log output should be the same as before.

LocalStack Cloud Pods also feature different merge strategies to merge the state of a Cloud Pod with the current LocalStack instance. You can use the `--merge` flag to specify the merge strategy. The available merge strategies are:

- **Inject with overwrite**: This is the default merge strategy. It will inject the state of the Cloud Pod into the current LocalStack instance and overwrite the existing state.
- **Inject with basic merge**: This merge strategy will inject the state of the Cloud Pod into the current LocalStack instance and merge the existing state with the state of the Cloud Pod.
- **Inject with deep merge**: This merge strategy will inject the state of the Cloud Pod into the current LocalStack instance and merge the existing state with the state of the Cloud Pod. It will also merge the existing state with the state of the Cloud Pod recursively.

{{< figure src="cloud-pods-state-merge-mechanisms.png" width="80%" alt="State Merge mechanisms with LocalStack Cloud Pods">}}

## Conclusion

LocalStack Cloud Pods fosters team collaboration & debugging by enabling the sharing of local cloud infrastructure & instance state. Furthermore, it allows us to create reproducible environments for various use cases, not just limited to machine learning. Using Cloud Pods, you can collaborate with your team members to create a reproducible environment for your application and share it with other team members. You can also use Cloud Pods to pre-seed your continuous integration (CI) pipelines with the required instance state to bootstrap your testing environment or debug failures in your CI pipeline. 

Check out the [LocalStack Cloud Pods documentation]({{< ref "user-guide/tools/cloud-pods" >}}) to learn more about Cloud Pods. To use Cloud Pods with LocalStack Community, refer to our [Community Cloud Pods documentation]({{< ref "user-guide/tools/cloud-pods/community" >}}) to get started with saving and loading Cloud Pods locally. You can find the code for this tutorial (including a `Makefile` to execute it step-by-step) in our [LocalStack Pro samples over GitHub]().
