# How do I set up Amazon RDS with Multi-AZ for high availability?
// plain

1. Create an Amazon RDS instance in the AWS Management Console.
2. Select the Multi-AZ option for high availability.
3. Select the database engine and version that you need.
4. Specify the instance type and storage capacity.
5. Provide a database name, username and password.
6. Create a new VPC security group and add the required inbound and outbound rules.
7. Click Create Database button to launch the instance.

## Example code

```
aws rds create-db-instance \
    --db-instance-identifier mydbinstance \
    --db-name mydbname \
    --allocated-storage 5 \
    --db-instance-class db.t2.micro \
    --engine mysql \
    --master-username admin \
    --master-user-password mypassword \
    --multi-az

```
## Output example

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "mydbinstance",
        "DBInstanceClass": "db.t2.micro",
        "Engine": "mysql",
        "DBName": "mydbname",
        "MultiAZ": true,
        "AllocatedStorage": 5,
        "MasterUsername": "admin"
    }
}
```

## Code explanation


`aws rds create-db-instance`: Creates a new DB instance.

`--db-instance-identifier mydbinstance`: Specifies the identifier for the DB instance.

`--db-name mydbname`: Specifies the name of the database to be created when the DB instance is created.

`--allocated-storage 5`: Specifies the allocated storage size specified in gigabytes.

`--db-instance-class db.t2.micro`: Specifies the compute and memory capacity of the DB instance.

`--engine mysql`: Specifies the database engine to be used for this DB instance.

`--master-username admin`: Specifies the master user name for the DB instance.

`--master-user-password mypassword`: Specifies the password for the master user.

`--multi-az`: Specifies that the DB instance is a Multi-AZ deployment.

## Helpful links

- [Amazon RDS Documentation](https://aws.amazon.com/documentation/rds/)
- [CreateDBInstance API](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html)

onelinerhub: [How do I set up Amazon RDS with Multi-AZ for high availability?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-with-multi-az-for-high-availability)