# How do I use the free tier of Amazon RDS?
// plain

The free tier of Amazon RDS allows users to have access to a limited amount of resources for free. To use the free tier, you will need to have an AWS account. Once you have an account, you can use the Amazon RDS console to create a database instance.

The following example code will create an Amazon RDS instance using the free tier.

```
aws rds create-db-instance \
    --db-instance-identifier mydbinstance \
    --db-instance-class db.t2.micro \
    --engine MySQL \
    --allocated-storage 5 \
    --master-username adminuser \
    --master-user-password mypassword
```

The output of the above command should look something like this:

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "mydbinstance",
        "DBInstanceClass": "db.t2.micro",
        "Engine": "MySQL",
        "AllocatedStorage": 5,
        "MasterUsername": "adminuser",
        "MasterUserPassword": "mypassword"
    }
}
```

The code above will create a MySQL database instance with a DB instance identifier of `mydbinstance`, a DB instance class of `db.t2.micro`, and an allocated storage of `5GB`. It will also create a master username and password for the instance.

Once the instance is created, you can access it using the Amazon RDS console. You can also use the AWS CLI or SDKs to interact with the instance.

For more information on using the free tier of Amazon RDS, see the [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html).

onelinerhub: [How do I use the free tier of Amazon RDS?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-free-tier-of-amazon-rds)