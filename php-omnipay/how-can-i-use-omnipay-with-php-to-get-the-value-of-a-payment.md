# How can I use Omnipay with PHP to get the value of a payment?
// plain

Omnipay is a payment processing library for PHP that can be used to get the value of a payment. It provides a unified API across many payment gateways, so the same code can be used to process payments from different providers.

Example code for getting the value of a payment using Omnipay:

```php
// Create a gateway for the PayPal Express Checkout
// (routes to GatewayFactory.php)
$gateway = Omnipay::create('PayPal_Express');

// Initialize the gateway
$gateway->initialize(array(
    'username' => 'example@example.com',
    'password' => 'password',
    'signature' => 'signature',
    'testMode' => true, // Or false when you are ready for live transactions
));

// Do an authorize transaction on the gateway
$transaction = $gateway->authorize(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
));

// Get the response object
$response = $transaction->send();

// Get the value of the payment
$value = $response->getValue();

// Output the value
echo $value;
```

## Output example

```
10.00
```

The code above does the following:

1. Creates a gateway for the PayPal Express Checkout using the Omnipay::create() method.
2. Initializes the gateway with the necessary credentials.
3. Does an authorize transaction on the gateway.
4. Gets the response object from the transaction.
5. Gets the value of the payment from the response object.
6. Outputs the value.

## Helpful links

- Omnipay website: https://omnipay.thephpleague.com/
- PayPal Express Checkout documentation: https://omnipay.thephpleague.com/gateways/paypal-express/

onelinerhub: [How can I use Omnipay with PHP to get the value of a payment?](https://onelinerhub.com/php-omnipay/how-can-i-use-omnipay-with-php-to-get-the-value-of-a-payment)