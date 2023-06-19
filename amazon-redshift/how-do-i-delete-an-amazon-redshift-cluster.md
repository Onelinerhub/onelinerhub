# How do I delete an Amazon Redshift cluster?
// plain

To delete an Amazon Redshift cluster, you must first delete any existing snapshots and then delete the cluster itself.

1. Delete any existing snapshots:

```
aws redshift delete-cluster-snapshot --snapshot-identifier <snapshot-identifier>
```

The output will be a JSON response confirming the deletion of the snapshot.

2. Delete the cluster itself:

```
aws redshift delete-cluster --cluster-identifier <cluster-identifier>
```

The output will be a JSON response confirming the deletion of the cluster.

Once both of these steps have been completed, the Amazon Redshift cluster will be deleted.

## Helpful links

- [AWS Documentation on Deleting a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#rs-console-delete-cluster)
- [AWS Documentation on Deleting a Snapshot](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-snapshots.html#rs-managing-snapshots-delete)

onelinerhub: [How do I delete an Amazon Redshift cluster?](https://onelinerhub.com/amazon-redshift/how-do-i-delete-an-amazon-redshift-cluster)