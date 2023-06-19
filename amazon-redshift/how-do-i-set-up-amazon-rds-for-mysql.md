# How do I set up Amazon RDS for MySQL?
// plain

1. Sign up for an AWS account and log in to the Amazon RDS console.
2. Select the “Create Database” button and select the “MySQL” engine option.
3. Configure the database settings, such as DB instance class, storage type, and allocated storage size.
4. Set up the database authentication, such as the master username and password.
5. Configure the network settings, such as the VPC and subnet group.
6. Set up the database name, port, and parameter group.
7. Create the database by clicking the “Create Database” button.

## Example code


```
$ aws rds create-db-instance \
    --db-instance-identifier mydbinstance \
    --db-name mydbname \
    --db-instance-class db.t2.micro \
    --engine mysql \
    --master-username mymasteruser \
    --master-user-password mymasteruserpassword
```

## Output example

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "mydbinstance",
        "DBName": "mydbname",
        "DBInstanceClass": "db.t2.micro",
        "Engine": "mysql",
        "MasterUsername": "mymasteruser",
        "MasterUserPassword": "mymasteruserpassword"
    }
}
```

## Code explanation

- `aws rds create-db-instance`: This command creates an Amazon RDS database instance.
- `--db-instance-identifier mydbinstance`: This option sets the identifier for the database instance.
- `--db-name mydbname`: This option sets the name of the database.
- `--db-instance-class db.t2.micro`: This option sets the type of instance, such as a t2.micro instance.
- `--engine mysql`: This option sets the database engine to MySQL.
- `--master-username mymasteruser`: This option sets the master username for the database.
- `--master-user-password mymasteruserpassword`: This option sets the master user password for the database.

## Helpful links
- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Creating an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html)

onelinerhub: [How do I set up Amazon RDS for MySQL?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-for-mysql)