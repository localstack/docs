---
title: Network troubleshooting
weight: 2
tags:
- troubleshooting
- networking
description: >
  How to troubleshoot common network problems
---

Below are several scenarios in which you may be trying to use LocalStack.
If you are having difficulties connecting your application code to LocalStack, please visit the links below each section which go into further details.

{{<alert title="Note">}}
LocalStack only binds to IPv4 addresses (e.g. `127.0.0.1`). Check you are not trying to access LocalStack over IPv6.
{{</alert>}}

---

<div class="container">
<div class="row pt-6">

## [Using the endpoint URL]({{< ref "endpoint-url" >}})


</div>
<div class="row">
<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "endpoint-url#from-the-same-computer" >}}" class="justify-content-between d-flex flex-column text-center">

  **From the same computer**

{{< figure src="./images/1.svg" width="400" >}}


</a>
</div>

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "endpoint-url#from-a-container-localstack-created" >}}" class="justify-content-between d-flex flex-column text-center">

**From a container LocalStack created**

{{< figure src="./images/4.svg" width="400" >}}

</a>
</div>

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "endpoint-url#from-your-container" >}}" class="justify-content-between d-flex flex-column text-center">

**From your container**

{{< figure src="./images/7.svg" width="400" >}}

</a>
</div>

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "endpoint-url#from-a-separate-host" >}}" class="justify-content-between d-flex flex-column text-center">


**From a separate host**

{{< figure src="./images/10.svg" width="400" >}}

</a>
</div>


</div> <!-- row -->

<div class="row pt-6">

## [Using transparent endpoint injection]({{< ref "transparent-endpoint-injection">}})

</div>

<div class="row">
<div class="col-xl-6 col-md-12 d-flex justify-content-center">
<a href="{{< ref "transparent-endpoint-injection#from-your-host" >}}" class="justify-content-between d-flex flex-column text-center">

**From your host**

{{< figure src="./images/2.svg" width="400" >}}

</a>
</div>
<div class="col-xl-6 col-md-12 d-flex justify-content-center">
<a href="{{< ref "transparent-endpoint-injection#from-a-lambda-function" >}}" class="justify-content-between d-flex flex-column text-center">

**From a lambda function**

{{< figure src="./images/5.svg" width="400" >}}

</a>
</div>

</div> <!-- row -->

<div class="row pt-6">

## [Accessing a resource created by LocalStack]({{< ref "created-resources">}})

</div>

<div class="row">

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-your-host" >}}" class="justify-content-between d-flex flex-column text-center">

**From your host**

{{< figure src="./images/3.svg" width="400" >}}

</a>
</div>


<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-a-container-localstack-created" >}}" class="justify-content-between d-flex flex-column text-center">

**From a container LocalStack created**

{{< figure src="./images/6.svg" width="400" >}}

</a>
</div>
<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-your-container" >}}" class="justify-content-between d-flex flex-column text-center">

**From your container**

{{< figure src="./images/9.svg" width="400" >}}

</a>
</div>

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-a-separate-host" >}}" class="justify-content-between d-flex flex-column text-center">

**From a separate host**

{{< figure src="./images/12.svg" width="400" >}}

</a>
</div>
</div> <!-- row -->
</div> <!-- container -->
