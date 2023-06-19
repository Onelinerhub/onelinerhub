# How do I set up an Amazon RDS instance?
// plain

1. First, log in to the AWS Management Console and select the Amazon RDS service.
2. Select the desired database engine and fill in the required information, such as the DB instance identifier, master username, and master password.
3. Select the desired instance type and the number of instances to be created.
4. Select the storage type and the size of the allocated storage.
5. Specify the backup and security options, such as the backup retention period and the security groups.
6. Configure the database parameters, such as the database name, port, and character set.
7. Finally, review the settings and launch the instance.

## Example code

```
aws rds create-db-instance \
  --db-instance-identifier mydbinstance \
  --db-name mydbname \
  --db-instance-class db.t2.micro \
  --engine mysql \
  --allocated-storage 10 \
  --master-username masteruser \
  --master-user-password masterpassword
```
## Output example

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "mydbinstance",
        "DBInstanceClass": "db.t2.micro",
        "Engine": "mysql",
        "AllocatedStorage": 10,
        "MasterUsername": "masteruser",
        "DBName": "mydbname",
        ...
    }
}
```

## Code explanation

- `aws rds create-db-instance`: creates a new Amazon RDS instance.
- `--db-instance-identifier`: specifies the name of the instance.
- `--db-name`: specifies the name of the database.
- `--db-instance-class`: specifies the instance type.
- `--engine`: specifies the database engine.
- `--allocated-storage`: specifies the size of the allocated storage.
- `--master-username`: specifies the master username.
- `--master-user-password`: specifies the master user password.

## Helpful links
- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [AWS CLI Reference for Amazon RDS](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html)

onelinerhub: [How do I set up an Amazon RDS instance?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-an-amazon-rds-instance)