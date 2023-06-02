# How do I use Omnipay in a PHP project?
// plain

Omnipay is a payment processing library for PHP. It provides a unified API for various payment gateways.

To use Omnipay in a PHP project, you need to install the library via Composer. You can add the following to your `composer.json` file:

```
"require": {
    "omnipay/omnipay": "~2.0"
}
```

Then, you can install the library with `composer install` command.

Next, you need to initialize the gateway you want to use. For example, to use PayPal Express gateway, you can do:

```php
$gateway = Omnipay::create('PayPal_Express');
$gateway->setUsername('YOUR_USERNAME');
$gateway->setPassword('YOUR_PASSWORD');
$gateway->setSignature('YOUR_SIGNATURE');
$gateway->setTestMode(true);
```

Now, you can use the gateway object to make various requests, such as purchase, refund, etc. For example, to make a purchase request:

```php
$params = [
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'http://www.example.com/return',
    'cancelUrl' => 'http://www.example.com/cancel',
];

$response = $gateway->purchase($params)->send();
if ($response->isSuccessful()) {
    echo "Purchase transaction was successful!\n";
    $sale_id = $response->getTransactionReference();
    echo "Transaction reference = " . $sale_id . "\n";
}
```

The output of the above code will be:

```
Purchase transaction was successful!
Transaction reference = 12345
```

For more information, please see [the official documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use Omnipay in a PHP project?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-in-a-php-project)