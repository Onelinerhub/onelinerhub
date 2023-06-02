# How do I use Omnipay with PHP to integrate PayPal into my website?
// plain

Omnipay is a payment processing library for PHP. It enables you to easily integrate PayPal into your website. To use Omnipay with PayPal, you will need to install the PayPal gateway:

```
composer require omnipay/paypal
```

You can then create an instance of the gateway and set your API credentials:

```php
// Create a gateway for the PayPal Express Gateway
// (routes to GatewayFactory::create)
$gateway = Omnipay::create('PayPal_Express');

// Initialise the gateway
$gateway->initialize(array(
    'username' => 'your_api_username',
    'password' => 'your_api_password',
    'signature' => 'your_api_signature',
    'testMode' => true, // Or false when you are ready for live transactions
));
```

You can then use the gateway to create a purchase request:

```php
// Create a credit card object
// This card can be used for testing.
$card = new CreditCard(array(
    'firstName' => 'Example',
    'lastName' => 'User',
    'number' => '4242424242424242',
    'expiryMonth' => '01',
    'expiryYear' => '2020',
    'cvv' => '123',
));

// Do a purchase transaction on the gateway
$transaction = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => $card,
));
$response = $transaction->send();
if ($response->isSuccessful()) {
    echo "Purchase transaction was successful!\n";
    $sale_id = $response->getTransactionReference();
    echo "Transaction reference = " . $sale_id . "\n";
}
```

The above code will create a purchase request and return a response object. If the transaction is successful, the response object will contain a transaction reference which can be used to complete the purchase.

For more information on using Omnipay with PayPal, see the [Omnipay PayPal documentation](https://github.com/thephpleague/omnipay-paypal).

onelinerhub: [How do I use Omnipay with PHP to integrate PayPal into my website?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-with-php-to-integrate-paypal-into-my-website)