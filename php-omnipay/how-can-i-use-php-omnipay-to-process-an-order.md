# How can I use PHP Omnipay to process an order?
// plain

You can use PHP Omnipay to process an order by following the steps below:

1. Install the Omnipay library.

```
composer require omnipay/omnipay
```

2. Create an instance of the gateway you want to use.

```php
$gateway = Omnipay::create('PayPal_Express');
$gateway->setUsername('example@example.com');
$gateway->setPassword('password');
$gateway->setSignature('signature');
```

3. Initialize the purchase request.

```php
$purchaseRequest = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
));
```

4. Get the purchase response.

```php
$purchaseResponse = $purchaseRequest->send();
```

5. Redirect the customer to the payment gateway.

```php
$purchaseResponse->redirect();
```

6. Confirm the payment on the return URL.

```php
$confirmRequest = $gateway->completePurchase(array(
    'transactionReference' => $purchaseResponse->getTransactionReference(),
    'payerId' => $_GET['PayerID'],
));

$confirmResponse = $confirmRequest->send();
```

7. Process the order.

```php
if ($confirmResponse->isSuccessful()) {
    // Process the order
}
```

## Helpful links
- [Omnipay Documentation](https://omnipay.thephpleague.com/)
- [GitHub Repository](https://github.com/thephpleague/omnipay)

onelinerhub: [How can I use PHP Omnipay to process an order?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-process-an-order)