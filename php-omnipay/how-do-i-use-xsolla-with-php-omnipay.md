# How do I use Xsolla with PHP Omnipay?
// plain

Xsolla is a world-leading payment platform that can be integrated with PHP Omnipay. To use Xsolla with PHP Omnipay, you will need to install and configure the Xsolla Omnipay gateway. The following steps will help you get started:

1. Install the Xsolla Omnipay gateway via composer.

```
composer require xsolla/omnipay-xsolla
```

2. Configure the gateway in your project.

```
$gateway = Omnipay::create('Xsolla');
$gateway->setMerchantId('12345');
$gateway->setProjectId('12345');
$gateway->setApiKey('12345');
```

3. Set the parameters for the payment request.

```
$parameters = [
    'amount' => '10.00',
    'currency' => 'USD',
    'transactionId' => '123456',
    'description' => 'Test payment',
    'clientIp' => '123.456.789.012',
];
```

4. Send the payment request.

```
$response = $gateway->purchase($parameters)->send();
```

5. Process the response.

```
if ($response->isSuccessful()) {
    // payment was successful: update database
} elseif ($response->isRedirect()) {
    // redirect to offsite payment gateway
    $response->redirect();
} else {
    // payment failed: display message to customer
    echo $response->getMessage();
}
```

For more information, please refer to the [Xsolla Omnipay Gateway documentation](https://github.com/xsolla/omnipay-xsolla/blob/master/README.md).

onelinerhub: [How do I use Xsolla with PHP Omnipay?](https://onelinerhub.com/php-omnipay/how-do-i-use-xsolla-with-php-omnipay)