# How do I register with PHP Omnipay?
// plain

PHP Omnipay is a payment processing library that allows developers to integrate payment gateways into their applications. To register with PHP Omnipay, you must first install the library via Composer:

```
composer require "omnipay/omnipay:~2.0"
```

Once the library is installed, you can create an instance of the gateway you wish to use. For example, to use the Stripe gateway:

```
$gateway = Omnipay::create('Stripe');
```

You can then set the gateway parameters, such as the API key and secret, using the `setApiKey()` method:

```
$gateway->setApiKey('abc123');
```

Finally, you can make a purchase request using the `purchase()` method:

```
$response = $gateway->purchase(
    [
        'amount' => '10.00',
        'currency' => 'USD',
        'card' => $card
    ]
)->send();
```

The `purchase()` method will return an instance of `Omnipay\Common\Message\ResponseInterface`, which you can use to check the status of the purchase.

For more information about using PHP Omnipay, please refer to the [official documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I register with PHP Omnipay?](https://onelinerhub.com/php-omnipay/how-do-i-register-with-php-omnipay)