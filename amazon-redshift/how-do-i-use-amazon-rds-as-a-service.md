# How do I use Amazon RDS as a service?
// plain

Amazon RDS (Relational Database Service) is a cloud-based service that makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while managing complex database administration tasks, freeing up developers to focus on their applications.

Example code for creating a MySQL RDS instance using the AWS SDK for Java:
```
AmazonRDSClient rdsClient = new AmazonRDSClient();

CreateDBInstanceRequest request = new CreateDBInstanceRequest()
    .withDBName("myDB")
    .withDBInstanceIdentifier("myDBInstance")
    .withAllocatedStorage(5)
    .withEngine("MySQL")
    .withMasterUsername("admin")
    .withMasterUserPassword("password");

CreateDBInstanceResult result = rdsClient.createDBInstance(request);
```

This code will create a MySQL RDS instance with 5GB of storage, a master username of "admin", and a master password of "password".

## Code explanation

1. `AmazonRDSClient rdsClient = new AmazonRDSClient();` - creates a new AmazonRDSClient object to interact with the AWS SDK for Java.
2. `CreateDBInstanceRequest request = new CreateDBInstanceRequest()` - creates a new CreateDBInstanceRequest object to specify the parameters for the new RDS instance.
3. `.withDBName("myDB")` - specifies the name of the RDS instance.
4. `.withDBInstanceIdentifier("myDBInstance")` - specifies the identifier of the RDS instance.
5. `.withAllocatedStorage(5)` - specifies the amount of storage in GB for the RDS instance.
6. `.withEngine("MySQL")` - specifies the type of engine for the RDS instance.
7. `.withMasterUsername("admin")` - specifies the master username for the RDS instance.
8. `.withMasterUserPassword("password")` - specifies the master password for the RDS instance.
9. `CreateDBInstanceResult result = rdsClient.createDBInstance(request);` - creates the RDS instance with the specified parameters.

## Helpful links
1. [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
2. [AWS SDK for Java Documentation](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/welcome.html)

onelinerhub: [How do I use Amazon RDS as a service?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-rds-as-a-service)