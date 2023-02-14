---
title: Network troubleshooting
weight: 2
tags:
- troubleshooting
- networking
description: >
  How to troubleshoot common network problems
---

## Overview

Below are several scenarios in which you may be trying to use LocalStack.
If you are having difficulties connecting your application code to LocalStack, please visit the links below each section which go into further details.

{{<alert title="Note">}}
LocalStack only binds to IPv4 addresses (e.g. `127.0.0.1`). Check you are not trying to access LocalStack over IPv6.
{{</alert>}}

---

<div class="container">
<div class="row">

<h2><a href="{{< ref "endpoint-url" >}}">Using the endpoint URL</a></h2>

</div>
<div class="row py-4">
<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "endpoint-url#from-the-same-computer" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From the same computer</h4>

{{< figure src="./images/1.svg" width="400" >}}

<!-- **Example**: you have run `localstack start`, or you are accessing LocalStack started in Docker (or docker-compose). -->

</a>
</div>

<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "endpoint-url#from-a-container-localstack-created" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From a container LocalStack created</h4>

{{< figure src="./images/4.svg" width="400" >}}

<!-- **Example**: your code is running in an ECS container that LocalStack has created. -->

</a>
</div>

<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "endpoint-url#from-your-container" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From your container</h4>

{{< figure src="./images/7.svg" width="400" >}}

<!-- **Example**: you are running your application code in a container and accessing AWS resources such as S3 in LocalStack. -->

</a>
</div>

<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "endpoint-url#from-a-separate-host" >}}" class="justify-content-between d-flex flex-column flex-grow-1">


<h4>From a separate host</h4>

{{< figure src="./images/10.svg" width="400" >}}

</a>
</div>


</div> <!-- row -->

<div class="row">

<h2><a href="{{< ref "transparent-endpoint-injection">}}">Using transparent endpoint injection</a></h2>

</div>

<div class="row py-4">
<div class="col-xl-6  p-4 shadow d-flex flex-column">
<a href="{{< ref "transparent-endpoint-injection#from-your-host" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From your host</h4>

{{< figure src="./images/2.svg" width="400" >}}

<!-- If you are using LocalStack with an [API key]({{<ref "getting-started/api-key">}}), then you can use the [DNS server]({{<ref "user-guide/tools/local-endpoint-injection/dns-server">}}) to perform requests to LocalStack as if it were AWS. -->

</a>
</div>
<div class="col-xl-6  p-4 shadow d-flex flex-column">
<a href="{{< ref "transparent-endpoint-injection#from-a-lambda-function" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From a lambda function</h4>

{{< figure src="./images/5.svg" width="400" >}}

</a>
</div>

</div> <!-- row -->

<div class="row">

<h2><a href="{{< ref "created-resources">}}">Accessing a resource created by LocalStack</a></h2>

</div>

<div class="row py-4">

<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "created-resources#from-your-host" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From your host</h4>

{{< figure src="./images/3.svg" width="400" >}}

<!-- **Example**: you have created an OpenSearch cluster and wish to access it from the computer that is running LocalStack. -->

</a>
</div>


<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "created-resources#from-a-container-localstack-created" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From a container LocalStack created</h4>

{{< figure src="./images/6.svg" width="400" >}}

</a>
</div>
<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "created-resources#from-your-container" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From your container</h4>

{{< figure src="./images/9.svg" width="400" >}}

</a>
</div>

<div class="col-xl-3  p-4 shadow d-flex flex-column">
<a href="{{< ref "created-resources#from-a-separate-host" >}}" class="justify-content-between d-flex flex-column flex-grow-1">

<h4>From a separate host</h4>

{{< figure src="./images/12.svg" width="400" >}}

</a>
</div>
</div> <!-- row -->
</div> <!-- container -->
