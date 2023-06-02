# payment gateways

How can I use Omnipay to integrate supported payment gateways into my PHP application?
// plain

Omnipay is a payment processing library for PHP. It provides a unified interface for working with multiple payment gateways. To integrate supported payment gateways into your PHP application, you can use the following steps:

1. Install Omnipay library using Composer:

```
composer require omnipay/omnipay
```

2. Create an instance of the gateway you want to use:

```php
$gateway = Omnipay::create('PayPal_Express');
```

3. Initialize the gateway with your API credentials:

```php
$gateway->initialize([
    'username' => 'your_username',
    'password' => 'your_password',
    'signature' => 'your_signature',
]);
```

4. Set the payment parameters:

```php
$params = [
    'amount' => 10.00,
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
];
```

5. Make the purchase request:

```php
$response = $gateway->purchase($params)->send();
```

6. Handle the response:

```php
if ($response->isSuccessful()) {
    echo "Purchase was successful!\n";
} elseif ($response->isRedirect()) {
    $response->redirect();
} else {
    echo $response->getMessage();
}
```

7. Redirect the customer to the payment gateway:

```php
$response->redirect();
```

For more information, please refer to the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [payment gateways

How can I use Omnipay to integrate supported payment gateways into my PHP application?](https://onelinerhub.com/php-omnipay/payment-gateways--how-can-i-use-omnipay-to-integrate-supported-payment-gateways-into-my-php-application)