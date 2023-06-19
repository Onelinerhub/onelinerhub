# How can I use Amazon RDS to create a serverless environment?
// plain

Amazon RDS can be used to create a serverless environment by leveraging the managed database services that it provides. For example, a MySQL database can be created and configured using the AWS Management Console, AWS CLI, or an SDK. The following example code creates a MySQL database instance using the AWS CLI:

```
aws rds create-db-instance --db-instance-identifier my-mysql-instance --db-instance-class db.t2.micro --engine mysql --allocated-storage 10
```

The output of the above command will be the Amazon Resource Name (ARN) of the newly created MySQL database instance.

## Code explanation


* `aws rds` - this is the AWS CLI command to interact with the Amazon RDS service.
* `create-db-instance` - this is the command to create a new database instance.
* `--db-instance-identifier` - this is the name of the newly created database instance.
* `--db-instance-class` - this is the type of database instance to create.
* `--engine` - this is the type of database engine to use.
* `--allocated-storage` - this is the amount of storage allocated to the database instance.

By leveraging the managed database services provided by Amazon RDS, it is possible to create a serverless environment without having to manage any of the underlying infrastructure.

## Helpful links
* [AWS Documentation - Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
* [AWS CLI Command Reference - Amazon RDS](https://docs.aws.amazon.com/cli/latest/reference/rds/index.html)

onelinerhub: [How can I use Amazon RDS to create a serverless environment?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-rds-to-create-a-serverless-environment)