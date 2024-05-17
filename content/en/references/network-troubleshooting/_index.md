---
title: Network troubleshooting
weight: 1
tags:
- troubleshooting
- networking
description: >
  How to troubleshoot common network problems
---

If you have difficulties connecting your application code to LocalStack, please choose the scenario below that best describes your networking layout.

{{< callout "tip" >}}
LocalStack only binds to IPv4 addresses (e.g. `127.0.0.1`). Check you are not trying to access LocalStack over IPv6.
{{</callout>}}

---

<div class="container">
<div class="row pt-6">

## [Using the endpoint URL]({{< ref "endpoint-url" >}})

</div>

<div class="row mt-2">

For example, setting the `endpoint_url` parameter with a [language SDK]({{< ref "user-guide/integrations/sdks" >}}).

</div>

<div class="row mt-4">
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

<div class="row mt-2">

See the [lambda documentation]({{< ref "user-guide/tools/transparent-endpoint-injection" >}}) for more information about the capability.

</div>

<div class="row mt-4">
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

<div class="row mt-2">

For example, you have created an OpenSearch cluster and are trying to access that resource by its URL.

</div>

<div class="row mt-4">

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-your-host" >}}" class="justify-content-between d-flex flex-column text-center">

**From your host**

{{< figure src="./images/3.svg" width="300" >}}

</a>
</div>


<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-a-container-localstack-created" >}}" class="justify-content-between d-flex flex-column text-center">

**From a container LocalStack created**

{{< figure src="./images/6.svg" width="300" >}}

</a>
</div>
<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-your-container" >}}" class="justify-content-between d-flex flex-column text-center">

**From your container**

{{< figure src="./images/9.svg" width="300" >}}

</a>
</div>

<div class="col-lg-12 col-xl-6 d-flex justify-content-center">
<a href="{{< ref "created-resources#from-a-separate-host" >}}" class="justify-content-between d-flex flex-column text-center">

**From a separate host**

{{< figure src="./images/12.svg" width="300" >}}

</a>
</div>
</div> <!-- row -->
</div> <!-- container -->
