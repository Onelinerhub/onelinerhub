# How do I use Amazon RDS?
// plain

Amazon RDS is a cloud service that makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming database administration tasks.

To use Amazon RDS, you need to create a database instance. This can be done using the AWS Management Console, AWS Command Line Interface (CLI), or Amazon RDS APIs.

Once you have created the database instance, you can connect to it using a variety of database tools, such as MySQL Workbench, Microsoft SQL Server Management Studio, or the AWS Command Line Interface (CLI).

Example code to create a database instance using the AWS CLI:

```
aws rds create-db-instance \
--db-instance-identifier mydbinstance \
--db-instance-class db.t2.micro \
--engine mysql \
--master-username mymasteruser \
--master-user-password mymasterpassword
```

## Output example


```
{
    "DBInstance": {
        "DBInstanceIdentifier": "mydbinstance",
        "DBInstanceClass": "db.t2.micro",
        "Engine": "mysql",
        "MasterUsername": "mymasteruser",
        "DBInstanceStatus": "creating",
        ...
    }
}
```

## Code explanation

- `aws rds create-db-instance`: This command creates a new database instance.
- `--db-instance-identifier mydbinstance`: This is the name of the database instance.
- `--db-instance-class db.t2.micro`: This is the type of instance to be created.
- `--engine mysql`: This is the database engine to be used.
- `--master-username mymasteruser`: This is the username of the master user for the database instance.
- `--master-user-password mymasterpassword`: This is the password of the master user for the database instance.

Once the database instance has been created, you can connect to it using the database tools mentioned above.

## Helpful links
- [Getting Started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)
- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

onelinerhub: [How do I use Amazon RDS?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-rds)