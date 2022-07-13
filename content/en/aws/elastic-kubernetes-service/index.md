---
title: "Elastic Kubernetes Service (EKS)"
linkTitle: "Elastic Kubernetes Service (EKS)"
categories: ["LocalStack Pro"]
description: >
  Elastic Kubernetes Service (EKS)
---
LocalStack Pro allows you to use the [EKS](https://docs.aws.amazon.com/eks/) API to create Kubernetes clusters and easily deploy containerized apps locally.

There are two modes for creating EKS clusters on LocalStack:
* spinning up an embedded kube cluster in your local Docker engine (preferred, simpler), or
* using an existing Kubernetes installation you can access from your local machine (defined in `$HOME/.kube/config`)

## Auto-installing an embedded Kubernetes cluster

The default method for creating Kubernetes clusters via the local EKS API is to spin up an embedded [k3d](https://k3d.io) kube cluster within Docker. LocalStack handles the download and installation transparently - on most systems the installation is performed automatically, and no customizations should be required.

A new cluster can be created using the following command:
{{< command >}}
$ awslocal eks create-cluster --name cluster1 --role-arn r1 --resources-vpc-config '{}'
{{</ command >}}

You should then see some Docker containers getting started, e.g.:
{{< command >}}
$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS          PORTS                                           NAMES
b335f7f089e4   rancher/k3d-proxy:5.0.1-rc.1   "/bin/sh -c nginx-pr…"   1 minute ago   Up 1 minute   0.0.0.0:8081->80/tcp, 0.0.0.0:44959->6443/tcp   k3d-cluster1-serverlb
f05770ec8523   rancher/k3s:v1.21.5-k3s2       "/bin/k3s server --t…"   1 minute ago   Up 1 minute
{{</ command >}}

Once the cluster has been created and initialized, we can determine the server `endpoint`:
{{< command >}}
$ awslocal eks describe-cluster --name cluster1
{
    "cluster": {
        "name": "cluster1",
        "status": "ACTIVE",
        "endpoint": "https://localhost.localstack.cloud:4513",
        ...
    }
}
{{</ command >}}

We can then configure the `kubectl` command line to interact with the new cluster endpoint:
{{< command >}}
$ awslocal eks update-kubeconfig --name cluster1
Updated context arn:aws:eks:us-east-1:000000000000:cluster/cluster1 in ~/.kube/config
$ kubectl config use-context arn:aws:eks:us-east-1:000000000000:cluster/cluster1
Switched to context "arn:aws:eks:us-east-1:000000000000:cluster/cluster1".
$ kubectl get services
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.43.0.1    <none>        443/TCP   70s
{{</ command >}}

### Use images pushed to ECR in EKS

In this section we will, by the use of an example, explore the usage of ECR images inside EKS.

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

Assuming we have created an `nginx` Kubernetes service for our sample above, we can now use the following ingress configuration to expose the nginx service on path `/test123`:

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

## Using an existing Kubernetes installation

You can also use the EKS API using an existing local Kubernetes installation. This works by mounting the `$HOME/.kube/config` file into the LocalStack container - e.g., when using docker-compose.yml:
```yaml
volumes:
  - "${HOME}/.kube/config:/root/.kube/config"
```

In recent versions of Docker, you can simply enable Kubernetes as an embedded service running inside Docker. See below for a screenshot of the Docker settings for Kubernetes in MacOS (similar configurations apply for Linux/Windows). By default, it is asssumed that Kubernetes API runs on the local TCP port `6443`.

<img src="kubernetes.png" alt="Kubernetes in Docker" title="Kubernetes in Docker" width="450" />

The example below illustrates how to create an EKS cluster configuration (assuming you have [`awslocal`](https://github.com/localstack/awscli-local) installed):
{{< command >}}
$ awslocal eks create-cluster --name cluster1 --role-arn r1 --resources-vpc-config '{}'
{
    "cluster": {
        "name": "cluster1",
        "arn": "arn:aws:eks:eu-central-1:000000000000:cluster/cluster1",
        "createdAt": "Sat, 05 Oct 2019 12:29:26 GMT",
        "endpoint": "https://172.17.0.1:6443",
        "status": "ACTIVE",
        ...
    }
}
$ awslocal eks list-clusters
{
    "clusters": [
        "cluster1"
    ]
}
{{< / command >}}

Simply configure your Kubernetes client (e.g., `kubectl` or other SDK) to point to the `endpoint` specified in the `create-cluster` output above. Depending on whether you're calling the Kubernetes API from the local machine or from within a Lambda, you may have to use different endpoint URLs (`https://localhost:6443` vs `https://172.17.0.1:6443`).

## Mounting directories from host to pod

If you have specific directories which you want to mount from your local dev machine into one of your pods you can do this with two simple steps:

First, make sure to create your cluster with the special tag `__k3d_volume_mount__`, specifying how you want to mount a volume from your dev machine to the cluster nodes:

{{< command >}}
$ awslocal eks create-cluster --name cluster1 --role-arn r1 --resources-vpc-config '{}' --tags '{"__k3d_volume_mount__":"/path/on/host:/path/on/node"}'
{
    "cluster": {
        "name": "cluster1",
        "arn": "arn:aws:eks:eu-central-1:000000000000:cluster/cluster1",
        "createdAt": "Sat, 05 Oct 2019 12:29:26 GMT",
        "endpoint": "https://172.17.0.1:6443",
        "status": "ACTIVE",
        "tags": {
            "__k3d_volume_mount__" : "/path/on/host:/path/on/node"
        }
        ...
    }
}
{{< / command >}}

Then, you can create your path with volume mounts as usual, with a configuration similar to this:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: test
spec:
  volumes:
    - name: example-volume
      hostPath:
         path: /path/on/node
  containers:
  - image: alpine:3.12
    command: ["/bin/sh","-c"]
    args:
      - echo "Starting the update command";
        apk update;
        echo "Adding the openssh command";
        apk add openssh;
        echo "openssh completed";
        sleep 240m;
    imagePullPolicy: IfNotPresent
    name: alpine
    volumeMounts:
      - mountPath: "/path/on/pod"
        name: example-volume
  restartPolicy: Always
```
