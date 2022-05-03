---
title: "CloudWatch"
linkTitle: "CloudWatch"
---

The [CloudWatch API](https://docs.aws.amazon.com/cloudwatch/) allows monitoring of AWS resources. 

## Metric Alarms
Alarms can be used to observe thresholds for data-of-interest, and trigger actions automatically. Please also consult the [AWS docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation) on how alarms are evaluated in general.
LocalStack currently supports metric-alarm evaluation with `statistic` and `comparison-operator`.

### Metric Alarm Examples
Metric alarms evaluate the state, by taking into account the data points of  E.g. you can create this alarm:
{{< command >}}
$ awslocal cloudwatch put-metric-alarm \
  --alarm-name my-alarm \
  --metric-name Orders \
  --namespace test \
  --threshold 1 \
  --comparison-operator LessThanThreshold \
  --evaluation-periods 1 \
  --period 30 \
  --statistic Minimum \
  --treat-missing notBreaching
{{< / command >}}

You can now in seperate terminal, watch the status of the alarm:
{{< command >}}
$ watch "awslocal cloudwatch describe-alarms --alarm-names my-alarm | jq '.MetricAlarms[0].StateValue'"
{{< / command >}}

And then add some data will cause a breach, and set the metric-alarm to state ALARM:
{{< command >}}
$ awslocal cloudwatch put-metric-data --namespace test --metric-data '[{"MetricName": "Orders", "Value": -1}]'
{{< / command >}}

The alarm state should change to ALARM after a few seconds, and eventually go back to OK - as we configured to treat missing data points as "not breaching".


#### Metric Alarm with Action
Actions are triggered when the state of the alarm changes. 
For this you can configure `alarm-actions`, `ok-actions` and `insufficient-data-actions`. 
Currently, we only support SNS Topics. The topic must be created beforehand.

Here is an example with an alarm that will send a message to the defined topic once the alarm is in state ALARM.
Note that the `alarm-actions` requires a valid ARN of an existing SNS topic.
{{< command >}}
$ awslocal cloudwatch put-metric-alarm \
  --alarm-name my-alarm \
  --metric-name Orders \
  --namespace test \
  --threshold 50 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 1 \
  --period 300 \
  --statistic Maximum \
  --treat-missing notBreaching \
  --alarm-actions <topic-arn> 
{{< / command >}}


{{< alert >}}
**Known Limitations:** 
* Anamoly detection, and extended-statics are not supported
* `unit` values are ignored
* composite-alarms are not evaluated
* metric-streams are not supported
{{< /alert >}}
