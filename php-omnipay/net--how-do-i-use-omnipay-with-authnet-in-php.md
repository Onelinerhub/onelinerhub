# net

How do I use Omnipay with Authnet in PHP?
// plain

Omnipay is a payment processing library for PHP that provides a unified API across many payment gateways. It can be used to process payments with Authorize.net.

In order to use Omnipay with Authorize.net, you will need to install the Omnipay library and an Authorize.net gateway package.

For example, to install the Authorize.Net AIM package:

```
composer require omnipay/authorizenet
```

Once the library is installed, you can create an instance of the gateway:

```php
<?php
$gateway = Omnipay::create('AuthorizeNet_AIM');
$gateway->setApiLoginId('your_api_login_id');
$gateway->setTransactionKey('your_transaction_key');
```

You can then process a payment:

```php
<?php
$params = [
    'amount' => '10.00',
    'card' => [
        'number' => '4111111111111111',
        'expiryMonth' => '12',
        'expiryYear' => '2022',
        'cvv' => '123',
    ],
];

$response = $gateway->purchase($params)->send();

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

The code above will:

1. Create an instance of the Authorize.Net AIM gateway
2. Set the API login ID and transaction key
3. Process a payment of $10.00 with a test credit card
4. Check the response and either update the database, redirect the customer, or display an error message

For more information, please refer to the [Omnipay Authorize.Net AIM documentation](https://omnipay.thephpleague.com/drivers/authorizenet/).

onelinerhub: [net

How do I use Omnipay with Authnet in PHP?](https://onelinerhub.com/php-omnipay/net--how-do-i-use-omnipay-with-authnet-in-php)