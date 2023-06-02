# payment

How can I use PHP Omnipay to process online payments?
// plain

PHP Omnipay is a payment processing library for PHP that allows developers to quickly and easily integrate payment processing into their websites. It provides a unified API for working with various payment gateways, and supports a variety of payment methods such as credit cards, PayPal, Bitcoin, and more.

To use PHP Omnipay to process online payments, you first need to install the library via composer:

```
composer require omnipay/omnipay
```

Once the library is installed, you can use the provided API to create a gateway instance, set up the payment parameters, and then process the payment. Here is an example of how to process a credit card payment:

```
<?php

// Create a gateway instance
$gateway = Omnipay::create('Stripe');

// Set the payment parameters
$gateway->setApiKey('YOUR_STRIPE_API_KEY');
$params = [
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => [
        'number' => '4242424242424242',
        'expiryMonth' => '6',
        'expiryYear' => '2022',
        'cvv' => '123',
    ],
];

// Process the payment
$response = $gateway->purchase($params)->send();

if ($response->isSuccessful()) {
    echo "Payment successful!";
} else {
    echo "Payment failed: " . $response->getMessage();
}
```

The code above creates a gateway instance for Stripe, sets the payment parameters, and then sends the payment request. If the payment is successful, the `isSuccessful()` method will return `true`.

For more information, see the [PHP Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [payment

How can I use PHP Omnipay to process online payments?](https://onelinerhub.com/php-omnipay/payment--how-can-i-use-php-omnipay-to-process-online-payments)