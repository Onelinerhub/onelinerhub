# How do I enable Amazon Redshift enhanced VPC routing?
// plain

Enabling Amazon Redshift enhanced VPC routing requires creating a cluster subnet group and a parameter group, and then modifying the cluster.

1. Create a cluster subnet group:

```
aws redshift create-cluster-subnet-group --cluster-subnet-group-name mysubnetgroup --description “My subnet group” --subnet-ids subnet-12345678
```

2. Create a parameter group:

```
aws redshift create-cluster-parameter-group --parameter-group-name myparametergroup --description “My parameter group” --family redshift-1.0
```

3. Modify the cluster:

```
aws redshift modify-cluster --cluster-identifier mycluster --vpc-security-group-ids sg-12345678 --cluster-subnet-group-name mysubnetgroup --cluster-parameter-group-name myparametergroup
```

This will enable enhanced VPC routing for the cluster, allowing it to take advantage of Amazon's routing optimizations.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/redshift/index.html)

onelinerhub: [How do I enable Amazon Redshift enhanced VPC routing?](https://onelinerhub.com/amazon-redshift/how-do-i-enable-amazon-redshift-enhanced-vpc-routing)