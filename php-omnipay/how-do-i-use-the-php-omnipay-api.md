# How do I use the PHP Omnipay API?
// plain

The PHP Omnipay API is an open-source payment processing library for PHP. It provides a unified API across multiple payment gateways, making it easy to integrate payments into your application.

To use the PHP Omnipay API, you will need to install the Omnipay library and a gateway-specific package.

For example, to use the Stripe gateway, you would run the following commands:

```
composer require league/omnipay omnipay/stripe
```

Then, you can use the Omnipay API to set up a payment request and process it. Here is an example of how to do this:

```php
// Create a gateway for the Stripe Gateway
// (routes to GatewayFactory::create)
$gateway = Omnipay::create('Stripe');

// Initialise the gateway
$gateway->initialize([
    'apiKey' => 'my_stripe_api_key',
]);

// Do an authorize transaction on the gateway
$transaction = $gateway->authorize([
    'amount'   => '10.00',
    'currency' => 'USD',
    'card'     => $card_details,
]);

// Send off the transaction
$response = $transaction->send();

if ($response->isSuccessful()) {
    // Payment was successful
    echo "Payment was successful!\n";
} else {
    // Payment failed
    echo "Payment failed: " . $response->getMessage() . "\n";
}
```

The above code will send an authorize request to the Stripe gateway, and will output either "Payment was successful!" or "Payment failed: [error message]" depending on the response of the gateway.

For more information on using the PHP Omnipay API, see the [documentation](https://omnipay.thephpleague.com/).

Parts of the code explained:

- `composer require league/omnipay omnipay/stripe`: This command installs the Omnipay library and the Stripe gateway package.
- `$gateway = Omnipay::create('Stripe');`: This creates a gateway for the Stripe gateway.
- `$gateway->initialize([...]);`: This initialises the gateway with the given configuration.
- `$transaction = $gateway->authorize([...]);`: This creates an authorize transaction, with the given parameters.
- `$response = $transaction->send();`: This sends off the transaction to the gateway.
- `if ($response->isSuccessful()) {...}`: This checks if the response from the gateway was successful.

onelinerhub: [How do I use the PHP Omnipay API?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-php-omnipay-api)