# How do I restore a snapshot to an existing Amazon RDS instance?
// plain

To restore a snapshot to an existing Amazon RDS instance, you can use the AWS CLI.

First, you will need to create a new DB instance from the snapshot. To do this, use the `aws rds restore-db-instance-from-db-snapshot` command, which will create a new instance from the snapshot. For example:

```
aws rds restore-db-instance-from-db-snapshot \
    --db-instance-identifier my-restored-instance \
    --db-snapshot-identifier my-snapshot
```

This command will create a new DB instance named `my-restored-instance` from the snapshot `my-snapshot`.

Next, you will need to modify the existing instance to use the restored instance as a source. To do this, use the `aws rds modify-db-instance` command, which will modify the existing instance to use the restored instance as a source. For example:

```
aws rds modify-db-instance \
    --db-instance-identifier my-old-instance \
    --source-db-instance-identifier my-restored-instance
```

This command will modify the existing instance `my-old-instance` to use the restored instance `my-restored-instance` as a source.

Finally, you will need to delete the restored instance. To do this, use the `aws rds delete-db-instance` command, which will delete the restored instance. For example:

```
aws rds delete-db-instance \
    --db-instance-identifier my-restored-instance
```

This command will delete the restored instance `my-restored-instance`.

Once all of these steps have been completed, the existing instance will be restored from the snapshot.

## Helpful links
- [AWS CLI Reference - `aws rds restore-db-instance-from-db-snapshot`](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html)
- [AWS CLI Reference - `aws rds modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html)
- [AWS CLI Reference - `aws rds delete-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/delete-db-instance.html)

onelinerhub: [How do I restore a snapshot to an existing Amazon RDS instance?](https://onelinerhub.com/amazon-redshift/how-do-i-restore-a-snapshot-to-an-existing-amazon-rds-instance)