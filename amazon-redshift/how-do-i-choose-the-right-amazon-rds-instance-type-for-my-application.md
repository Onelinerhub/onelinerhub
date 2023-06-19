# How do I choose the right Amazon RDS instance type for my application?
// plain

When choosing the right Amazon RDS instance type for your application, there are several factors to consider.

1. **Compute Capacity**: Choose an instance type that can handle the workload of your application. Consider the amount of memory, CPU, and I/O performance needed.

2. **Database Engine**: Make sure the instance type supports the database engine you are using.

3. **Storage**: Consider the type of storage needed - Magnetic, General Purpose SSD, or Provisioned IOPS.

4. **Availability**: Choose an instance type that can provide the level of availability you require.

5. **Cost**: Select an instance type that fits your budget.

Below is an example of how to select an instance type using the AWS CLI:

```
aws rds describe-orderable-db-instance-options --engine mysql --query 'OrderableDBInstanceOptions[*].[DBInstanceClass,MaxIOPS]'
```

Example Output:

```
[
    [
        "db.t2.micro",
        1000
    ],
    [
        "db.t2.small",
        1000
    ],
    [
        "db.t2.medium",
        1000
    ],
    [
        "db.t2.large",
        1000
    ],
    [
        "db.m4.large",
        10000
    ],
    [
        "db.m4.xlarge",
        20000
    ],
    [
        "db.m4.2xlarge",
        40000
    ]
]
```

The output above shows the available instance types for MySQL with the maximum IOPS each instance type can provide.

For more information, see the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

onelinerhub: [How do I choose the right Amazon RDS instance type for my application?](https://onelinerhub.com/amazon-redshift/how-do-i-choose-the-right-amazon-rds-instance-type-for-my-application)