# How do I use PHP Omnipay to process a transaction?
// plain

PHP Omnipay is a payment processing library that makes it easy to integrate payments into any PHP application. To use PHP Omnipay to process a transaction, you need to first install the library and then create an instance of the gateway you want to use.

```php
// Include the Omnipay library
require_once 'vendor/autoload.php';

// Create an instance of the gateway
$gateway = Omnipay::create('PayPal_Express');
```

Next, you need to set the API credentials for the gateway. This is usually done by setting the `username`, `password` and `signature` parameters, but it may vary depending on the gateway.

```php
// Set the API credentials
$gateway->setUsername('your_api_username');
$gateway->setPassword('your_api_password');
$gateway->setSignature('your_api_signature');
```

Once the credentials are set, you can then create a `PurchaseRequest` object and set the details of the transaction. This includes the amount, currency, description, return URL, etc.

```php
// Create the purchase request
$purchaseRequest = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'description' => 'My purchase',
    'returnUrl' => 'https://example.com/return',
    'cancelUrl' => 'https://example.com/cancel',
));
```

Finally, you can send the purchase request and get the response. If the transaction is successful, you will get a `PurchaseResponse` object with the details of the transaction.

```php
// Send the purchase request and get the response
$purchaseResponse = $purchaseRequest->send();

// Get the transaction reference
$transactionReference = $purchaseResponse->getTransactionReference();

// Get the transaction data
$transactionData = $purchaseResponse->getData();
```

## Helpful links

- [PHP Omnipay Documentation](https://omnipay.thephpleague.com/docs/)
- [PayPal Express Documentation](https://omnipay.thephpleague.com/gateways/paypal-express/)

onelinerhub: [How do I use PHP Omnipay to process a transaction?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-to-process-a-transaction)