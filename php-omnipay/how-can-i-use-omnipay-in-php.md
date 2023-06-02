# How can I use Omnipay in PHP?
// plain

Omnipay is a payment processing library for PHP. It provides a unified API across many payment gateways. To use Omnipay in PHP, you need to first install it via Composer:

```
composer require omnipay/omnipay
```

Once installed, you can then set up the gateway you want to use, such as PayPal:

```php
// Create a gateway for the PayPal Express Checkout
// (REST) Gateway
$gateway = Omnipay::create('PayPal_Express');

// Initialise the gateway
$gateway->initialize([
    'clientId' => 'YourPayPalClientId',
    'secret' => 'YourPayPalSecret',
    'testMode' => true, // Or false when you are ready for live transactions
]);
```

You can then process payments using the gateway's `purchase` method:

```php
// Do an authorisation transaction on the gateway
$transaction = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
]);

$response = $transaction->send();

if ($response->isSuccessful()) {
    // Payment was successful
    echo "Payment was successful!\n";
    $data = $response->getData();
    var_dump($data);
} elseif ($response->isRedirect()) {
    // Redirect to offsite payment gateway
    $response->redirect();
} else {
    // Payment failed
    echo "Payment failed: " . $response->getMessage() . "\n";
}
```

For more information on using Omnipay, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How can I use Omnipay in PHP?](https://onelinerhub.com/php-omnipay/how-can-i-use-omnipay-in-php)