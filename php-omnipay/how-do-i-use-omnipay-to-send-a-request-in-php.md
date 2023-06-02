# How do I use Omnipay to send a request in PHP?
// plain

Omnipay is a payment processing library for PHP. It can be used to send requests to payment gateways and other online payment services.

To use Omnipay to send a request in PHP, you need to do the following:

1. Install the Omnipay library:
```
composer require omnipay/omnipay
```

2. Create an instance of the gateway you want to use:
```php
$gateway = Omnipay::create('Stripe');
```

3. Set the gateway parameters:
```php
$gateway->setApiKey('abc123');
$gateway->setTestMode(true);
```

4. Create the request object:
```php
$request = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => $card,
]);
```

5. Send the request and get the response:
```php
$response = $request->send();
```

6. Check the response:
```php
if ($response->isSuccessful()) {
    echo "Payment was successful!";
} else {
    echo $response->getMessage();
}
```

7. Get the transaction reference:
```php
$transactionReference = $response->getTransactionReference();
```

For more information, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use Omnipay to send a request in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-to-send-a-request-in-php)