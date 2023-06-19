# How do I set up Amazon RDS for SQL Server?
// plain

Setting up Amazon RDS for SQL Server is a simple process.

1. Log into the Amazon RDS Console and create a new instance.
2. Select the desired database engine, version, and instance class.
3. Create a master username and password.
4. Set up the database security group, which will control network access to the instance.
5. Select an existing VPC or create a new one.
6. Set up the database options, such as backup retention period, automated backups, and maintenance window.
7. Launch the instance.

## Example code


```
$ rds-create-db-instance --db-instance-identifier mydbinstance --allocated-storage 5 --db-instance-class db.m1.small --engine MySQL --master-username masteruser --master-user-password masteruserpassword
```

## Output example


```
DBINSTANCE  mydbinstance  creating
```

## Helpful links
- [Amazon RDS Documentation](https://aws.amazon.com/documentation/rds/)
- [Creating a DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.html)

onelinerhub: [How do I set up Amazon RDS for SQL Server?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-for-sql-server)