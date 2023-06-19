# How can I use Amazon RDS with MySQL?
// plain

Amazon RDS with MySQL can be used to easily set up, operate, and scale a MySQL database in the cloud. It provides cost-efficient and resizable capacity while managing complex database administration tasks, freeing up developers to focus on their applications.

To use Amazon RDS with MySQL, first create a DB instance. This can be done using the AWS Management Console, AWS CLI, or AWS SDK.

Example code using the AWS CLI:
```
aws rds create-db-instance --db-instance-identifier mydbinstance --db-instance-class db.t2.micro --engine MySQL --allocated-storage 5 --master-username masteruser --master-user-password mymasterpassword
```

Once the DB instance is created, then create a DB security group. This can be done using the same methods as creating the DB instance.

Example code using the AWS CLI:
```
aws rds create-db-security-group --db-security-group-name mysecuritygroup --db-security-group-description "My security group"
```

After creating a DB security group, add rules to it. These rules specify which IP addresses or EC2 security groups are allowed to access the DB instance. This can also be done using the same methods as creating the DB instance and DB security group.

Example code using the AWS CLI:
```
aws rds authorize-db-security-group-ingress --db-security-group-name mysecuritygroup --cidrip 123.123.123.123/32
```

Finally, create a DB subnet group. This groups the DB subnets together for use with the DB instance. This can also be done using the same methods as creating the DB instance, DB security group, and DB security group rules.

Example code using the AWS CLI:
```
aws rds create-db-subnet-group --db-subnet-group-name mydbsubnetgroup --db-subnet-group-description "My DB subnet group" --subnet-ids subnet-12345678 subnet-87654321
```

Once the DB instance, DB security group, DB security group rules, and DB subnet group are created, then the DB instance can be launched. This can be done using the same methods as creating the DB instance, DB security group, DB security group rules, and DB subnet group.

Example code using the AWS CLI:
```
aws rds modify-db-instance --db-instance-identifier mydbinstance --db-security-groups mysecuritygroup --db-subnet-group-name mydbsubnetgroup
```

## Helpful links

- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Creating a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)
- [Creating a DB Security Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.SecurityGroups.html)
- [Creating a DB Subnet Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.Subnets.html)
- [Launching a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.LaunchInstance.html)

onelinerhub: [How can I use Amazon RDS with MySQL?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-rds-with-mysql)