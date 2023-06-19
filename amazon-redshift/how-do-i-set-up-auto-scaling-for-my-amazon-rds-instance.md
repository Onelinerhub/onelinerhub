# How do I set up auto scaling for my Amazon RDS instance?
// plain

Auto scaling for Amazon RDS instances can be set up by using the Amazon RDS API. The following steps can be taken to set up auto scaling for an RDS instance:

1. Create a scaling policy using the `CreateScalingPolicy` API call.
```
aws rds create-scaling-policy --resource-id <rds-instance-id> --auto-scaling-role-arn <role-arn> --policy-name <policy-name>
```

2. Create a scaling trigger using the `PutScalingTrigger` API call.
```
aws rds put-scaling-trigger --resource-id <rds-instance-id> --scaling-policy-name <policy-name> --trigger-name <trigger-name> --trigger-type <trigger-type> --trigger-target-value <target-value>
```

3. Create a CloudWatch alarm using the `PutMetricAlarm` API call.
```
aws cloudwatch put-metric-alarm --alarm-name <alarm-name> --metric-name <metric-name> --comparison-operator <comparison-operator> --threshold <threshold> --period <period> --evaluation-periods <evaluation-periods> --alarm-actions <action-arn>
```

4. Associate the scaling policy with the CloudWatch alarm using the `PutScalingPolicy` API call.
```
aws rds put-scaling-policy --resource-id <rds-instance-id> --scaling-policy-name <policy-name> --alarm-name <alarm-name>
```

Once these steps are completed, the RDS instance will be set up for auto scaling.

## Code explanation


1. `CreateScalingPolicy` API call: Used to create a scaling policy for the RDS instance.
2. `PutScalingTrigger` API call: Used to create a scaling trigger for the scaling policy.
3. `PutMetricAlarm` API call: Used to create a CloudWatch alarm for the scaling policy.
4. `PutScalingPolicy` API call: Used to associate the scaling policy with the CloudWatch alarm.

## Helpful links

1. [Amazon RDS API Reference](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/Welcome.html)
2. [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/Welcome.html)

onelinerhub: [How do I set up auto scaling for my Amazon RDS instance?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-auto-scaling-for-my-amazon-rds-instance)