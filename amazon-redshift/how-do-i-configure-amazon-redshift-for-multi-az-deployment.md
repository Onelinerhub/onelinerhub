# How do I configure Amazon Redshift for multi-AZ deployment?
// plain

To configure Amazon Redshift for multi-AZ deployment, you need to use the `CREATE CLUSTER` command. This command allows you to specify the availability zone (AZ) for each node in the cluster. For example, the following command creates a four-node cluster with two nodes in AZ1 and two nodes in AZ2:

```
CREATE CLUSTER mycluster
  (db_version='1.0',
   node_type='dc2.large',
   num_nodes=4,
   availability_zones=('us-west-2a','us-west-2b','us-west-2a','us-west-2b'))
```

The command parts are:

* `CREATE CLUSTER` - the command to create a new cluster
* `mycluster` - the name of the cluster
* `db_version` - the version of the database
* `node_type` - the type of node
* `num_nodes` - the number of nodes
* `availability_zones` - the availability zones for each node

For more information about configuring Amazon Redshift for multi-AZ deployment, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#create-cluster-availability-zones).

onelinerhub: [How do I configure Amazon Redshift for multi-AZ deployment?](https://onelinerhub.com/amazon-redshift/how-do-i-configure-amazon-redshift-for-multi-az-deployment)