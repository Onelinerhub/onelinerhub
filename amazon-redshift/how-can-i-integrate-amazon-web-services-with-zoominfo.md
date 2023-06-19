# How can I integrate Amazon Web Services with ZoomInfo?
// plain

Integrating Amazon Web Services (AWS) with ZoomInfo is possible by using the AWS Marketplace. The AWS Marketplace provides customers with a single point of access to thousands of software products from independent software vendors.

Using the AWS Marketplace, customers can easily deploy ZoomInfo's products and services in the AWS cloud. For example, customers can deploy ZoomInfo's Contact Search API with the following code:

```
aws marketplace subscribe \
    --product-id <product-id> \
    --region <region> \
    --name <name>
```

This code will create a subscription to the product specified by the `product-id` parameter in the specified `region`. The `name` parameter is used to specify the name of the subscription.

Once the subscription is created, customers can use the AWS CLI to access ZoomInfo's products and services. For example, the following code can be used to access the Contact Search API:

```
aws marketplace get-subscription-details \
    --subscription-id <subscription-id>
```

This code will return an access token which can be used to authenticate with the Contact Search API.

## Code explanation


- `aws marketplace subscribe`: This command is used to create a subscription to a product in the AWS Marketplace.
- `aws marketplace get-subscription-details`: This command is used to retrieve subscription details, including an access token for authenticating with the product.

For more information about integrating AWS with ZoomInfo, please refer to the following links:

- [AWS Marketplace Documentation](https://docs.aws.amazon.com/marketplace/latest/userguide/what-is-aws-marketplace.html)
- [ZoomInfo Documentation](https://developer.zoominfo.com/docs/getting-started)

onelinerhub: [How can I integrate Amazon Web Services with ZoomInfo?](https://onelinerhub.com/amazon-redshift/how-can-i-integrate-amazon-web-services-with-zoominfo)