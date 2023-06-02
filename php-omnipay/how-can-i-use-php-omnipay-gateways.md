# How can I use PHP Omnipay Gateways?
// plain

PHP Omnipay is a payment processing library for PHP. It provides a consistent interface for talking to payment gateways. To use PHP Omnipay Gateways, you need to install the library and then create a gateway instance.

Here is an example of using PHP Omnipay to process a credit card payment:

```php
// Create a gateway for the PayPal ExpressGateway
// (routes to GatewayFactory::create)
$gateway = Omnipay::create('PayPal_Express');

// Initialise the gateway
$gateway->initialize(array(
    'username' => 'YOUR_USERNAME',
    'password' => 'YOUR_PASSWORD',
    'signature' => 'YOUR_SIGNATURE',
    'testMode' => true, // Or false when you are ready for live transactions
));

// Create a credit card object
// This card can be used for testing.
$card = new CreditCard(array(
    'firstName' => 'Example',
    'lastName' => 'User',
    'number' => '4111111111111111',
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

The code above will output:

```
Purchase transaction was successful!
Transaction reference = 4XW06843KJ7446042
```

The code above consists of the following parts:

1. Create a gateway instance with `Omnipay::create`
2. Initialise the gateway with credentials
3. Create a credit card object
4. Do a purchase transaction on the gateway
5. Send the transaction
6. Check if the transaction was successful
7. Get the transaction reference

For more information about using PHP Omnipay, please refer to the [official documentation](https://github.com/thephpleague/omnipay).

onelinerhub: [How can I use PHP Omnipay Gateways?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-gateways)