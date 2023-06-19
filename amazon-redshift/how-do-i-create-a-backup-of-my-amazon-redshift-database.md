# How do I create a backup of my Amazon Redshift database?
// plain

Creating a backup of an Amazon Redshift database requires a few steps.

1. Create a snapshot of the cluster:
```
aws redshift create-cluster-snapshot --cluster-identifier <cluster-name> --snapshot-identifier <snapshot-name>
```
This will create a snapshot of the cluster, which is saved to Amazon S3.

2. Create a manual snapshot copy:
```
aws redshift copy-cluster-snapshot --source-snapshot-identifier <source-snapshot-name> --target-snapshot-identifier <target-snapshot-name>
```
This will create a manual snapshot copy, which can be used to restore the cluster to a specific point in time.

3. Create a manual snapshot copy from a different region:
```
aws redshift copy-cluster-snapshot --source-snapshot-identifier <source-snapshot-name> --target-snapshot-identifier <target-snapshot-name> --source-region <source-region> --target-region <target-region>
```
This will create a manual snapshot copy from a different region, which can be used to restore the cluster in a different region.

4. Restore a cluster from a snapshot:
```
aws redshift restore-from-cluster-snapshot --cluster-identifier <cluster-name> --snapshot-identifier <snapshot-name>
```
This will restore a cluster from a snapshot, which can be used to create a new cluster with the same data as the original.

These steps will create a backup of an Amazon Redshift database.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-snapshots.html)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/redshift/index.html)

onelinerhub: [How do I create a backup of my Amazon Redshift database?](https://onelinerhub.com/amazon-redshift/how-do-i-create-a-backup-of-my-amazon-redshift-database)