# How can I use PHP Omnipay Script to process payments?
// plain

PHP Omnipay is a payment processing library for PHP that supports many payment gateways. To use it, you need to install the library via Composer.

Once installed, you can use the following code to process payments:

```php
<?php
require 'vendor/autoload.php';

// Create a gateway for the PayPal ExpressGateway
// (routes to GatewayFactory::create)
$gateway = Omnipay::create('PayPal_Express');

// Initialise the gateway
$gateway->initialize(array(
    'username' => 'example@example.com',
    'password' => 'abc123',
    'signature' => '1234567890',
));

// Do an authorisation transaction on the gateway
$transaction = $gateway->authorize(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
));

$response = $transaction->send();

if ($response->isSuccessful()) {
    // Payment was successful
    $arr_response = $response->getData();
    echo "Payment was successful!\n";
    echo "Transaction Reference: " . $arr_response['TRANSACTIONID'];
} elseif ($response->isRedirect()) {
    // Redirect to offsite payment gateway
    $response->redirect();
} else {
    // Payment failed
    echo "Payment failed: " . $response->getMessage();
}
```

## Output example


```
Payment was successful!
Transaction Reference: 1234567890
```

The code above does the following:

1. Require the autoloader for the Omnipay library.
2. Create a gateway object for the PayPal Express gateway.
3. Initialise the gateway with the required credentials.
4. Do an authorisation transaction on the gateway.
5. Send the transaction and handle the response.

If the payment is successful, the response will contain the transaction reference.

## Helpful links

- [Omnipay Documentation](https://omnipay.thephpleague.com/getting-started/)
- [PayPal Express Documentation](https://omnipay.thephpleague.com/gateways/paypal-express/)

onelinerhub: [How can I use PHP Omnipay Script to process payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-script-to-process-payments)