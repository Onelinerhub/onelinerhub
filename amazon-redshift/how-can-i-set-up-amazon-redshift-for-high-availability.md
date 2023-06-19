# How can I set up Amazon Redshift for high availability?
// plain

Setting up Amazon Redshift for high availability requires a few steps:

1. Create a cluster with two nodes in different Availability Zones. This can be done using the following code:

```
aws redshift create-cluster \
--node-type dc2.large \
--number-of-nodes 2 \
--availability-zone us-east-1a \
--availability-zone us-east-1b
```

2. Enable Enhanced VPC Routing. This can be done using the following code:

```
aws redshift modify-cluster \
--enhanced-vpc-routing \
--cluster-identifier mycluster
```

3. Enable Snapshot Copy. This can be done using the following code:

```
aws redshift enable-snapshot-copy \
--cluster-identifier mycluster \
--destination-region us-east-1
```

4. Create a Read Replica. This can be done using the following code:

```
aws redshift create-cluster-read-replica \
--cluster-identifier mycluster \
--source-cluster-identifier mycluster
```

These steps will ensure that your Amazon Redshift cluster is highly available.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html)
- [Creating a Cluster with Two Nodes in Different Availability Zones](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters-creating.html#create-two-node-cluster-az)
- [Enabling Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html)
- [Enabling Snapshot Copy](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters-snapshots.html#enable-snapshot-copy)
- [Creating a Read Replica](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters-replication.html#create-read-replica)

onelinerhub: [How can I set up Amazon Redshift for high availability?](https://onelinerhub.com/amazon-redshift/how-can-i-set-up-amazon-redshift-for-high-availability)