# How do I set up and use the Omnipay PHP package?
// plain

The Omnipay PHP package is a payment processing library for PHP. It provides an abstracted interface for various payment gateways, allowing developers to quickly and easily integrate payment processing into their applications.

To set up and use the Omnipay PHP package, first install it via Composer:
```
composer require league/omnipay
```

Once installed, you can create an Omnipay gateway instance:
```php
$gateway = Omnipay::create('Stripe');
```

You can then configure the gateway with your API credentials:
```php
$gateway->setApiKey('abc123');
```

You can then use the gateway to process payments:
```php
$response = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => $cardDetails
))->send();

if ($response->isSuccessful()) {
    echo "Payment was successful!\n";
} else {
    echo "Payment failed: " . $response->getMessage() . "\n";
}
```

For more details, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I set up and use the Omnipay PHP package?](https://onelinerhub.com/php-omnipay/how-do-i-set-up-and-use-the-omnipay-php-package)