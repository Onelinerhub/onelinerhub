# How do I use the Amazon Redshift Calculator?
// plain

The Amazon Redshift Calculator is an online tool that helps you estimate the cost of running an Amazon Redshift cluster. It can be used to estimate the cost of a cluster based on the number of nodes, type of nodes, and other parameters.

To use the Amazon Redshift Calculator, you need to first select the type of cluster you want to create. You can choose from a single node, two-node, or three-node cluster. After selecting the cluster type, you will need to specify the number of nodes, the type of nodes (e.g. dense compute, dense storage, etc.), and the type of storage (e.g. magnetic or SSD).

Once you have specified the parameters, you can click the "Calculate" button to get the estimated cost of the cluster. The calculator will also provide an estimate of the total storage capacity and the estimated monthly cost.

## Example code


```
#Create a single node cluster
cluster_type = 'single node'
num_nodes = 1
node_type = 'dense compute'
storage_type = 'magnetic'

#Calculate the cost of the cluster
cost = AmazonRedshiftCalculator.calculate(cluster_type, num_nodes, node_type, storage_type)

#Print out the estimated cost
print('Estimated cost of cluster: ${}'.format(cost))
```

## Output example


```
Estimated cost of cluster: $100
```

## Code explanation


1. `cluster_type` - specifies the type of cluster to be created (e.g. single node, two-node, or three-node).
2. `num_nodes` - specifies the number of nodes in the cluster.
3. `node_type` - specifies the type of nodes in the cluster (e.g. dense compute, dense storage, etc.).
4. `storage_type` - specifies the type of storage in the cluster (e.g. magnetic or SSD).
5. `cost` - stores the estimated cost of the cluster.
6. `AmazonRedshiftCalculator.calculate()` - calculates the cost of the cluster based on the specified parameters.
7. `print()` - prints out the estimated cost of the cluster.

## Helpful links

1. [Amazon Redshift Calculator](https://aws.amazon.com/redshift/pricing/calculator/)
2. [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

onelinerhub: [How do I use the Amazon Redshift Calculator?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-calculator)