# How do I set up an Amazon RDS read replica?
// plain

1. Create a new Amazon RDS instance. This can be done through the Amazon RDS console, the AWS CLI, or the Amazon RDS API.

2. Configure the primary instance with the parameters needed for the read replica.

3. Create a new read replica instance using the parameters from the primary instance.

4. Configure the read replica instance with the parameters needed to connect to the primary instance.

5. Create a read replica of the primary instance using the following command:

```
aws rds create-db-instance-read-replica \
    --db-instance-identifier myreadreplica \
    --source-db-instance-identifier myprimaryinstance
```

6. Monitor the status of the read replica instance with the following command:

```
aws rds describe-db-instances \
    --db-instance-identifier myreadreplica
```

7. Once the read replica is in the available state, it can be used for read operations.

## Helpful links
- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateReadReplica.html)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance-read-replica.html)

onelinerhub: [How do I set up an Amazon RDS read replica?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-an-amazon-rds-read-replica)