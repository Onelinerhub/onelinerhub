# How do I set up Amazon RDS with read replicas?
// plain

1. First, log into the [AWS Management Console](https://console.aws.amazon.com/console/home) and select the Amazon RDS service.

2. Create a new database instance, and select the desired engine (e.g. MySQL, PostgreSQL, etc).

3. Enter the desired settings for the instance, including the username/password, storage size, etc.

4. Once the instance is created, select the instance and choose the "Modify" option.

5. Under "Enable Enhanced Monitoring", select the "Enable Read Replicas" option.

6. Enter the desired settings for the read replica, including the number of replicas, the instance type, and the storage size.

7. Once the settings are entered, click "Apply Changes" to enable the read replicas.

## Example code


```
aws rds modify-db-instance \
  --db-instance-identifier <RDS instance identifier> \
  --enable-read-replica \
  --read-replica-count <number of read replicas> \
  --read-replica-instance-type <instance type> \
  --read-replica-storage-size <storage size>
```

Output (if any):

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "<RDS instance identifier>",
        "ReadReplicaCount": <number of read replicas>,
        "ReadReplicaSourceDBInstanceIdentifier": "<RDS instance identifier>",
        "ReadReplicaDBInstanceIdentifiers": [
            "<RDS instance identifier>-001",
            "<RDS instance identifier>-002",
            ...
        ],
        ...
    }
}
```

## Code explanation


* `aws rds modify-db-instance`: The command to modify an existing Amazon RDS instance.
* `--db-instance-identifier <RDS instance identifier>`: The identifier of the existing Amazon RDS instance to modify.
* `--enable-read-replica`: Enables read replicas on the existing Amazon RDS instance.
* `--read-replica-count <number of read replicas>`: The number of read replicas to enable on the existing Amazon RDS instance.
* `--read-replica-instance-type <instance type>`: The instance type to use for the read replicas.
* `--read-replica-storage-size <storage size>`: The storage size to use for the read replicas.

List of ## Helpful links

* [AWS Management Console](https://console.aws.amazon.com/console/home)
* [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
* [Modifying an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Modifying.html)

onelinerhub: [How do I set up Amazon RDS with read replicas?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-with-read-replicas)