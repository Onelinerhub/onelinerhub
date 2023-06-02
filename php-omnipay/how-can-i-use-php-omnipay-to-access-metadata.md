# How can I use PHP Omnipay to access metadata?
// plain

PHP Omnipay is a library for processing payments through payment gateways. It provides an interface for accessing metadata related to payments.

Metadata consists of payment-related information such as amount, currency, payment method, and so on.

To access metadata with PHP Omnipay, you can use the `getMetadata()` method. This method takes a single parameter, which is the name of the payment gateway. Here's an example:

```php
$gateway = Omnipay::create('PayPal_Express');
$metadata = $gateway->getMetadata('PayPal_Express');
print_r($metadata);
```

The output of this code would be an array of metadata associated with the payment gateway.

The `getMetadata()` method is useful for getting information about the payment gateway, such as the supported currencies and payment methods. It can also be used to get information about the payment itself, such as the amount and currency.

## Code explanation


- `Omnipay::create('PayPal_Express')`: creates an instance of the PayPal Express gateway.
- `$gateway->getMetadata('PayPal_Express')`: gets the metadata associated with the PayPal Express gateway.
- `print_r($metadata)`: prints the metadata in an array.

Here are some ## Helpful links

- [PHP Omnipay Documentation](https://omnipay.thephpleague.com/docs/index.html)
- [PayPal Express Documentation](https://developer.paypal.com/docs/checkout/express-checkout/)

onelinerhub: [How can I use PHP Omnipay to access metadata?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-access-metadata)