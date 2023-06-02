# How can I use PHP Omnipay to process a billing transaction?
// plain

PHP Omnipay is a library for processing payment transactions. It supports a wide range of popular payment gateways and provides an easy way to integrate with them. To process a billing transaction with PHP Omnipay:

1. Install the library using [Composer](https://getcomposer.org/):
```
composer require omnipay/omnipay
```
2. Initialize the gateway object with your credentials:
```php
$gateway = Omnipay::create('PayPal_Express');
$gateway->setUsername('your_username');
$gateway->setPassword('your_password');
$gateway->setSignature('your_signature');
```
3. Set the transaction parameters:
```php
$params = [
    'amount' => 10.00,
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
];
```
4. Send the transaction request:
```php
$response = $gateway->purchase($params)->send();
```
5. Check the response:
```php
if ($response->isSuccessful()) {
    // Payment was successful
} elseif ($response->isRedirect()) {
    // Redirect to offsite payment gateway
    $response->redirect();
} else {
    // Payment failed
    echo $response->getMessage();
}
```
6. Complete the transaction:
```php
$purchaseResponse = $gateway->completePurchase($params)->send();

if ($purchaseResponse->isSuccessful()) {
    // Payment was successful
} else {
    // Payment failed
    echo $purchaseResponse->getMessage();
}
```
7. Finally, check the transaction status:
```php
$statusResponse = $gateway->fetchTransaction($params)->send();

if ($statusResponse->isSuccessful()) {
    // Payment status is successful
} else {
    // Payment status failed
    echo $statusResponse->getMessage();
}
```

For more information, please refer to the [PHP Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How can I use PHP Omnipay to process a billing transaction?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-process-a-billing-transaction)