# How can I use the Omnipay PHP library to process payments?
// plain

Omnipay is a PHP library that allows you to easily integrate payment processing into your PHP applications. It provides an abstracted interface for interacting with payment gateways, and supports a range of popular payment gateways.

To use the Omnipay library, you first need to install it using Composer.

```
composer require league/omnipay
```

Once installed, you can create an instance of the gateway you wish to use, and set the parameters for your payment.

```php
<?php

// Create an instance of the gateway
$gateway = Omnipay::create('Stripe');

// Set the parameters for the payment
$gateway->setApiKey('your_stripe_api_key');
$gateway->setTestMode(true);
```

To process the payment, you then need to call the `purchase` method, passing in the details of the payment.

```php
<?php

// Process the payment
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => $cardDetails,
])->send();
```

If the payment is successful, the `$response` object will contain the details of the payment.

```php
<?php

if ($response->isSuccessful()) {
    echo "Payment was successful!\n";
    echo "Transaction reference: " . $response->getTransactionReference() . "\n";
}
```

For more information, please see the [Omnipay documentation](https://omnipay.thephpleague.com/).

References:

- [Omnipay Documentation](https://omnipay.thephpleague.com/)

onelinerhub: [How can I use the Omnipay PHP library to process payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-the-omnipay-php-library-to-process-payments)