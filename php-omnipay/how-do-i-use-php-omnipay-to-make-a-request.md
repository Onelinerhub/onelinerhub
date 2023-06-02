# How do I use PHP Omnipay to make a request?
// plain

PHP Omnipay is a package for PHP which provides a standardised way to integrate payment gateways into a web application. To make a request using PHP Omnipay, the following steps should be taken:

1. Install the package using Composer:

```
composer require omnipay/omnipay
```

2. Set up your gateway instance:

```php
$gateway = Omnipay::create('MyGateway');
$gateway->setApiKey('abc123');
```

3. Set up the request parameters:

```php
$parameters = [
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
];
```

4. Send the request:

```php
$response = $gateway->purchase($parameters)->send();
```

5. Process the response:

```php
if ($response->isSuccessful()) {
    // payment was successful: update database
    print_r($response);
} elseif ($response->isRedirect()) {
    // redirect to offsite payment gateway
    $response->redirect();
} else {
    // payment failed: display message to customer
    echo $response->getMessage();
}
```

For more information, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use PHP Omnipay to make a request?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-to-make-a-request)