# How do I calculate the pricing for Amazon Redshift?
// plain

The pricing for Amazon Redshift is based on the number of nodes and the type of nodes used.

The types of nodes are:

- DC1.large: 2 vCPUs, 15 GiB RAM, 160 GB SSD
- DC2.8xlarge: 32 vCPUs, 244 GiB RAM, 2.56 TB SSD
- DS2.xlarge: 4 vCPUs, 30.5 GiB RAM, 2 x 900 GB HDD

To calculate the pricing for Amazon Redshift, you can use the [AWS Simple Monthly Calculator](https://calculator.s3.amazonaws.com/index.html).

For example, if you want to use a DC1.large node with 2 vCPUs and 15 GiB RAM, you can enter the following information in the calculator:

```
Region: US East (N. Virginia)
Instance Type: dc1.large
Usage: 2
```

The output of the calculator will show the estimated cost for the node:

```
Estimated Monthly Cost: $37.67
```

You can also use the [AWS Pricing API](https://aws.amazon.com/blogs/aws/new-aws-price-list-api/) to programmatically calculate the pricing for Amazon Redshift.

## Helpful links

- [AWS Simple Monthly Calculator](https://calculator.s3.amazonaws.com/index.html)
- [AWS Pricing API](https://aws.amazon.com/blogs/aws/new-aws-price-list-api/)

onelinerhub: [How do I calculate the pricing for Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-calculate-the-pricing-for-amazon-redshift)