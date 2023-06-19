# How can I determine the price of Amazon Redshift?
// plain

The price of Amazon Redshift depends on the type of node you choose, the number of nodes, and the duration of the cluster. To determine the exact cost, you can use the Amazon Redshift pricing calculator.

For example, if you wanted to estimate the cost of a 3-node dc2.large cluster with a 1-year term, you could use the following code:

```
$ aws redshift get-cluster-price --cluster-type dc2.large --cluster-node-type 3 --term 1-year
```

The output of this code would be something like this:

```
{
    "ClusterPrice": {
        "RateCode": "R5D3XNETWXCYH3",
        "StartTime": 1577750400.0,
        "EndTime": 1609328000.0,
        "CurrencyCode": "USD",
        "Amount": 4.05
    }
}
```

This output indicates that the cost of the 3-node dc2.large cluster with a 1-year term would be $4.05 per hour.

The code consists of the following parts:

1. `aws redshift get-cluster-price`: This is the command used to get the price of a Redshift cluster.
2. `--cluster-type dc2.large`: This specifies the type of node for the cluster.
3. `--cluster-node-type 3`: This specifies the number of nodes for the cluster.
4. `--term 1-year`: This specifies the duration of the cluster.

For more information about Amazon Redshift pricing, please see the [Amazon Redshift Pricing page](https://aws.amazon.com/redshift/pricing/).

onelinerhub: [How can I determine the price of Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-can-i-determine-the-price-of-amazon-redshift)