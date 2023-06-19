# How can I set up an Amazon RDS MySQL instance?
// plain

1. First, you need to log in to your Amazon Web Services (AWS) account.
2. After you are logged in, go to the Amazon RDS page.
3. Select the "MySQL" option from the list of database engines.
4. Select the instance type and the size of the instance you need.
5. Enter the username and password for the database.
6. Click on the "Create DB Instance" button to create the instance.
7. You can use the following example code to check if the instance is created successfully:

```
aws rds describe-db-instances
```

## Output example

```
{
    "DBInstances": [
        {
            "DBInstanceIdentifier": "my-db-instance",
            "DBInstanceClass": "db.t2.micro",
            "Engine": "mysql",
            "DBInstanceStatus": "available"
        }
    ]
}
```

## Code explanation

- `aws rds describe-db-instances`: This command is used to retrieve information about your Amazon RDS database instances.
- `DBInstanceIdentifier`: This is the name of the database instance.
- `DBInstanceClass`: This is the type of instance you have chosen.
- `Engine`: This is the type of database engine you have chosen.
- `DBInstanceStatus`: This is the status of the instance, which should be “available” if the instance was created successfully.

## Helpful links
- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [AWS CLI Reference Guide](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html)

onelinerhub: [How can I set up an Amazon RDS MySQL instance?](https://onelinerhub.com/amazon-redshift/how-can-i-set-up-an-amazon-rds-mysql-instance)