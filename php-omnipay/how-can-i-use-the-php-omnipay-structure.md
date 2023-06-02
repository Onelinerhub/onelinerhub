# How can I use the PHP Omnipay structure?
// plain

PHP Omnipay is a payment processing library for PHP. It provides a consistent interface for interacting with multiple payment gateways. It also provides a framework for developing your own payment gateway.

Using Omnipay is easy. All you need to do is require the library in your project and create a gateway instance:

```php
// Require the library
require_once 'vendor/autoload.php';

// Create a gateway for the PayPal ExpressCheckout Gateway
// (routes to GatewayFactory::create)
$gateway = Omnipay\Omnipay::create('PayPal_Express');
```

Once you have a gateway instance, you can use it to make requests to the payment gateway. For example, to initiate a purchase request:

```php
// Initialise the gateway
$gateway->initialize(array(
    'username' => 'example',
    'password' => 'secret',
    'signature' => 'signature',
));

// Do an authorisation transaction on the gateway
$transaction = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
));

// Process the transaction
$response = $transaction->send();

if ($response->isSuccessful()) {
    // The transaction was successful
    echo "Transaction successful!\n";
} elseif ($response->isRedirect()) {
    // Redirect to offsite payment gateway
    $response->redirect();
} else {
    // The transaction was not successful
    echo $response->getMessage();
}
```

## Code explanation


1. Require the library - `require_once 'vendor/autoload.php';`
2. Create a gateway instance - `$gateway = Omnipay\Omnipay::create('PayPal_Express');`
3. Initialise the gateway - `$gateway->initialize(array(...));`
4. Make a purchase request - `$transaction = $gateway->purchase(array(...));`
5. Process the transaction - `$response = $transaction->send();`
6. Check the response - `if ($response->isSuccessful()) {...}`
7. Redirect if necessary - `$response->redirect();`

## Helpful links

- [Omnipay Documentation](https://omnipay.thephpleague.com/getting-started/)
- [GitHub Repository](https://github.com/thephpleague/omnipay)

onelinerhub: [How can I use the PHP Omnipay structure?](https://onelinerhub.com/php-omnipay/how-can-i-use-the-php-omnipay-structure)