# How can I calculate the serverless pricing for Amazon Redshift?
// plain

The pricing for Amazon Redshift is based on the number of nodes in the cluster, the type of node, and the duration of use. To calculate the cost of a serverless Amazon Redshift cluster, you will need to factor in the following:

1. Number of nodes: The number of nodes determines the number of cores and the amount of memory available for the cluster.
2. Node type: You can select from a variety of node types, including dense compute, dense storage, and RA3 instances.
3. Duration of use: You can choose from hourly or annual pricing models.

For example, to calculate the cost of an Amazon Redshift cluster with two dense compute nodes and hourly pricing, you can use the following code:

```
import boto3

client = boto3.client('redshift')

response = client.describe_reserved_node_offering(
    ReservedNodeOfferingId='<offering-id>',
    NodeType='dc2.large',
    Duration='Hourly'
)

pricing = response['RecurringCharges'][0]['RecurringChargeAmount']

total_price = pricing * 2

print("The total cost of the cluster is: $" + str(total_price))
```

## Output example

```
The total cost of the cluster is: $0.9
```

## Helpful links
- [Amazon Redshift Pricing](https://aws.amazon.com/redshift/pricing/)
- [boto3 Describe Reserved Node Offering](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/redshift.html#Redshift.Client.describe_reserved_node_offering)

onelinerhub: [How can I calculate the serverless pricing for Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-can-i-calculate-the-serverless-pricing-for-amazon-redshift)