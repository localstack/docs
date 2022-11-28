---
title: "Deploying an ECS Image to EKS with LocalStack"
linkTitle: "Deploying an ECS Image to EKS with LocalStack"
weight: 7
description: >
  This tutorial showcases how to deploy an ECS image to EKS locally with LocalStack.
type: tutorials
---

In this tutorial we will, by the use of an example, explore the usage of ECR images inside EKS.

#### Initial configuration

You can use the [configuration]({{< ref "configuration" >}}) variable `HOSTNAME_EXTERNAL` to modify the return value of the resource URIs for most services, including ECR.
By default, ECR will return a `repositoryUri` starting with `localhost`, like: `localhost:<port>/<repository-name>`.
If we set the `HOSTNAME_EXTERNAL` to `localhost.localstack.cloud`, ECR will return a `repositoryUri` like `localhost.localstack.cloud:<port>/<repository_name>`.

{{< alert title="Notes" >}}
In this section, we will assume `localhost.localstack.cloud` resolves in your environment and LocalStack is connected to a non-default bridge network. Check the article about [DNS rebind protection]({{< ref "limitations#dns-rebind-protection" >}}) to learn more.
If this domain does not resolve on your host it is also possible not to set `HOSTNAME_EXTERNAL`, please nevertheless use `localhost.localstack.cloud` as registry in your pod configuration.
LocalStack will take care of the DNS resolution of `localhost.localstack.cloud` within ECR itself, and you can use the `localhost:<port>/<repository_name>` Uri for tagging and pushing the image on your host.
{{< / alert >}}

If this configuration is correct, you can use your ECR image in EKS like expected.

#### Deploying a sample application from an ECR image

In order to demonstrate this behavior, take a look at the following small tutorial which leads to the point where the image is correctly pulled.
For the sake of this tutorial, we will retag the `nginx` image to be pushed to ECR using another name, and use it for a pod configuration.
First, we create a new repository with a chosen name:
{{< command >}}
$ awslocal ecr create-repository --repository-name "fancier-nginx"
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:000000000000:repository/fancier-nginx",
        "registryId": "c75fd0e2",
        "repositoryName": "fancier-nginx",
        "repositoryUri": "localhost.localstack.cloud:4510/fancier-nginx",
        "createdAt": "2022-04-13T14:22:47+02:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
{{< / command >}}

{{< alert >}}**Note**:
When creating an ECR, a port from the [the external service port range]({{< ref "external-ports" >}}) is dynamically selected. \
Therefore, the port can differ from `4510` used in the samples below.
Make sure to use the correct URL / port by using the `repositoryUrl` of the `create-repository` request.
{{< /alert >}}

Now let us pull the nginx image:
{{< command >}}
$ docker pull nginx
{{< / command >}}
... tag it to our repository name:
{{< command >}}
$ docker tag nginx localhost.localstack.cloud:4510/fancier-nginx
{{< / command >}}
... and push it to ECR:
{{< command >}}
$ docker push localhost.localstack.cloud:4510/fancier-nginx
{{< / command >}}

Now, let us set up the EKS cluster using the image pushed to local ECR.
{{< command >}}
$ awslocal eks create-cluster --name fancier-cluster --role-arn "r1" --resources-vpc-config "{}"
{
    "cluster": {
        "name": "fancier-cluster",
        "arn": "arn:aws:eks:us-east-1:000000000000:cluster/fancier-cluster",
        "createdAt": "2022-04-13T16:38:24.850000+02:00",
        "roleArn": "r1",
        "resourcesVpcConfig": {},
        "identity": {
            "oidc": {
                "issuer": "https://localhost.localstack.cloud/eks-oidc"
            }
        },
        "status": "CREATING",
        "clientRequestToken": "cbdf2bb6-fd3b-42b1-afe0-3c70980b5959"
    }
}
{{< / command >}}

Once the cluster status is "ACTIVE":
{{< command >}}
awslocal eks describe-cluster --name "fancier-cluster"
{
    "cluster": {
        "name": "fancier-cluster",
        "arn": "arn:aws:eks:us-east-1:000000000000:cluster/fancier-cluster",
        "createdAt": "2022-04-13T17:12:39.738000+02:00",
        "endpoint": "https://localhost.localstack.cloud:4511",
        "roleArn": "r1",
        "resourcesVpcConfig": {},
        "identity": {
            "oidc": {
                "issuer": "https://localhost.localstack.cloud/eks-oidc"
            }
        },
        "status": "ACTIVE",
        "certificateAuthority": {
            "data": "..."
        },
        "clientRequestToken": "d188f578-b353-416b-b309-5d8c76ecc4e2"
    }
}
{{< / command >}}

... we will configure `kubectl`:
{{< command >}}
$ awslocal eks update-kubeconfig --name fancier-cluster && kubectl config use-context arn:aws:eks:us-east-1:000000000000:cluster/fancier-cluster
Added new context arn:aws:eks:us-east-1:000000000000:cluster/fancier-cluster to /home/localstack/.kube/config
Switched to context "arn:aws:eks:us-east-1:000000000000:cluster/fancier-cluster".
{{< / command >}}

... and add a deployment configuration:
{{< command >}}
$ cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fancier-nginx
  labels:
    app: fancier-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fancier-nginx
  template:
    metadata:
      labels:
        app: fancier-nginx
    spec:
      containers:
      - name: fancier-nginx
        image: localhost.localstack.cloud:4510/fancier-nginx:latest
        ports:
        - containerPort: 80
EOF
{{< / command >}}

Now, if we describe the pod:
{{< command >}}
kubectl describe pod fancier-nginx
{{< / command >}}
... we can see, in the events, that the pull from ECR was successful:
```
  Normal  Pulled     10s   kubelet            Successfully pulled image "localhost.localstack.cloud:4510/fancier-nginx:latest" in 2.412775896s
```

### Configuring an Ingress for your services

In order to make an EKS service externally accessible, we need to create an `Ingress` configuration that exposes the service on a certain path to the load balancer.

We can create an `nginx` Kubernetes service for our sample deployment above by applying the following configuration:
{{< command >}}
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  selector:
    app: fancier-nginx
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 80
EOF
{{< /command >}}

Now use the following ingress configuration to expose the nginx service on path `/test123`:

{{< command >}}
$ cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx
  annotations:
    ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - http:
      paths:
      - path: /test123
        pathType: Prefix
        backend:
          service:
            name: nginx
            port:
              number: 80
EOF
{{< /command >}}

We should then be able to send a request to `nginx` via the load balancer port `8081` from the host:
{{< command >}}
$ curl http://localhost:8081/test123
<html>
...
<hr><center>nginx/1.21.6</center>
...
{{< / command >}}

{{< alert title="Note" >}}
You can customize the load balancer port by configuring `EKS_LOADBALANCER_PORT` in your environment.
{{< /alert >}}
