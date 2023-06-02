# How do I use PHP Omnipay Wallet to make payments?
// plain

PHP Omnipay Wallet is a library that allows developers to easily integrate payment processing into their PHP applications. To use it, you first need to install the library using Composer:

```
composer require league/omnipay-wallet
```

After the library is installed, you can use it to make payments. The following code snippet shows an example of how to do this:

```php
$gateway = Omnipay::create('Wallet');
$gateway->setUsername('your_username');
$gateway->setPassword('your_password');

$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'transactionId' => '123456',
    'description' => 'Test transaction',
])->send();

if ($response->isSuccessful()) {
    echo "Transaction successful";
} else {
    echo "Transaction failed";
}
```

The code above will:

1. Create an instance of the Wallet gateway.
2. Set the username and password for the gateway.
3. Make a purchase request with the specified amount, currency, transaction ID, and description.
4. Send the request to the gateway.
5. Check the response and output a message depending on whether the transaction was successful or not.

For more information, please refer to the [PHP Omnipay Wallet documentation](https://omnipay.thephpleague.com/wallet/).

onelinerhub: [How do I use PHP Omnipay Wallet to make payments?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-wallet-to-make-payments)