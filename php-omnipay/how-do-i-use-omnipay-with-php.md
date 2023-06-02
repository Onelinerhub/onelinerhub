# How do I use Omnipay with PHP?
// plain

Omnipay is a payment processing library for PHP. It provides a simple and consistent interface for processing payments with various payment gateways.

To use Omnipay with PHP, you first need to install it via Composer. Once installed, you can then create a gateway instance and use it to process payments.

For example, to create a gateway instance for Stripe:

```php
$gateway = Omnipay::create('Stripe');
$gateway->setApiKey('YOUR_STRIPE_API_KEY');
```

You can then use the gateway instance to process payments. For example, to charge a credit card:

```php
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => $cardData,
])->send();

if ($response->isSuccessful()) {
    echo "Payment was successful!\n";
} else {
    echo "Payment failed.\n";
}
```

## Code explanation

- `Omnipay::create('Stripe')` - to create a gateway instance for Stripe
- `$gateway->setApiKey('YOUR_STRIPE_API_KEY')` - to set the Stripe API key
- `$gateway->purchase()` - to initiate a purchase request
- `$response->isSuccessful()` - to check if the payment was successful

For more information on using Omnipay with PHP, please refer to the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use Omnipay with PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-with-php)