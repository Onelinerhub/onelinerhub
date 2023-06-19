# How do I set up auto scaling on Amazon EC2?
// plain

Auto scaling on Amazon EC2 allows you to automatically increase or decrease the number of EC2 instances based on the demand of your application.

To set up auto scaling, you need to do the following:

1. Create an Auto Scaling group: You can use the Amazon EC2 console, AWS CLI, or AWS SDKs to create an Auto Scaling group. For example, the following command creates an Auto Scaling group with two EC2 instances:

```
aws autoscaling create-auto-scaling-group --auto-scaling-group-name my-asg --launch-configuration-name my-lc --min-size 2 --max-size 5 --desired-capacity 2
```

2. Create launch configuration: This defines the EC2 instance types, AMIs, and other parameters used when launching EC2 instances. For example, the following command creates a launch configuration named my-lc:

```
aws autoscaling create-launch-configuration --launch-configuration-name my-lc --image-id ami-12345678 --instance-type t2.micro
```

3. Create scaling policies: This defines the conditions for scaling the number of EC2 instances in the Auto Scaling group. For example, the following command creates a scaling policy that increases the number of EC2 instances by two when the CPU utilization reaches 70%:

```
aws autoscaling put-scaling-policy --policy-name my-scaleout-policy --auto-scaling-group-name my-asg --scaling-adjustment 2 --adjustment-type ChangeInCapacity --cooldown 300 --min-adjustment-magnitude 1 --metric-aggregation-type Average --threshold 70
```

4. Create CloudWatch alarms: This defines the conditions under which the scaling policies are triggered. For example, the following command creates an alarm that triggers the scaling policy when the CPU utilization reaches 70%:

```
aws cloudwatch put-metric-alarm --alarm-name my-cpu-alarm --metric-name CPUUtilization --namespace AWS/EC2 --statistic Average --period 300 --threshold 70 --comparison-operator GreaterThanOrEqualToThreshold --dimensions Name=AutoScalingGroupName,Value=my-asg --evaluation-periods 2 --alarm-actions arn:aws:autoscaling:us-east-1:123456789012:scalingPolicy:abcd1234-a123-456a-a12b-a123b4cd56ef:autoScalingGroupName/my-asg:policyName/my-scaleout-policy
```

Once you have completed the above steps, your Auto Scaling group will be ready to automatically scale the number of EC2 instances based on the conditions defined in your scaling policies and CloudWatch alarms.

## Helpful links

- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
- [Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)

onelinerhub: [How do I set up auto scaling on Amazon EC2?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-auto-scaling-on-amazon-ec-)