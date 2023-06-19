# tier

How can I use Amazon RDS Free Tier?
// plain

Amazon RDS Free Tier is a free service that provides access to a single Amazon Relational Database Service (RDS) instance for up to 750 hours per month. It allows customers to experiment with the features and capabilities of Amazon RDS without incurring any charge.

To use Amazon RDS Free Tier, customers can set up an Amazon RDS instance using the Amazon RDS Management Console. Once the instance is set up, customers can use the Amazon RDS API to access the instance and its associated features.

For example, the following code uses the Amazon RDS API to create a new Amazon RDS instance:

```
import boto3

# Create an RDS client
rds = boto3.client('rds')

# Create a new RDS instance
response = rds.create_db_instance(
    DBInstanceIdentifier='mydb',
    AllocatedStorage=5,
    DBInstanceClass='db.t2.micro',
    Engine='mysql',
    MasterUsername='admin',
    MasterUserPassword='adminpassword'
)

print(response)
```

## Output example

```
{
    'DBInstance': {
        'DBInstanceIdentifier': 'mydb',
        'DBInstanceClass': 'db.t2.micro',
        'Engine': 'mysql',
        'MasterUsername': 'admin',
        'AllocatedStorage': 5,
        'DBInstanceStatus': 'creating',
        ...
    }
}
```

## Code explanation


1. `boto3.client('rds')`: This creates an RDS client using the Boto3 library.

2. `response = rds.create_db_instance()`: This uses the RDS client to create a new RDS instance.

3. `print(response)`: This prints the response from the API call.

For more information on Amazon RDS Free Tier, please refer to the [Amazon RDS Free Tier documentation](https://aws.amazon.com/rds/free/).

onelinerhub: [tier

How can I use Amazon RDS Free Tier?](https://onelinerhub.com/amazon-redshift/tier--how-can-i-use-amazon-rds-free-tier)