# How many pricing components are included in Amazon Redshift?
// plain

Amazon Redshift has three pricing components:

1. Compute Node Hours: This is the cost of running the compute nodes that process queries. It is charged on an hourly basis and is calculated by multiplying the number of nodes used by the number of hours the nodes are running. For example, if you have two nodes running for two hours, the cost would be 4 compute node hours.

2. Data Storage: This is the cost of storing data in Amazon Redshift. It is charged on a per-gigabyte basis and is calculated by multiplying the data stored by the per-gigabyte rate. For example, if you store 10GB of data, the cost would be 10GB * the per-gigabyte rate.

3. Data Transfer: This is the cost of transferring data in and out of Amazon Redshift. It is charged on a per-gigabyte basis and is calculated by multiplying the data transferred by the per-gigabyte rate. For example, if you transfer 10GB of data, the cost would be 10GB * the per-gigabyte rate.

```
Example Code

SELECT * FROM mytable WHERE cost > 10;
```

## Output example


```
id  cost
1   11
2   12
3   13
```

For more information on Amazon Redshift pricing, please visit the [Amazon Redshift Pricing Page](https://aws.amazon.com/redshift/pricing/).

onelinerhub: [How many pricing components are included in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-many-pricing-components-are-included-in-amazon-redshift)