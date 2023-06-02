# How do I use the PHP Omnipay code to process payments?
// plain

The PHP Omnipay code is a library of classes and functions that can be used to process payments. To use it, you need to include the Omnipay library in your script and then create an instance of the gateway you wish to use.

For example, to use the Stripe gateway:
```
// Include the Omnipay library
require_once('vendor/autoload.php');

// Create a gateway object
$gateway = Omnipay::create('Stripe');
```

Once the gateway object is created, you can set the parameters for the payment. This includes the payment amount, currency, card details, and customer information.

```
// Set payment parameters
$params = [
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => [
        'number' => '4242424242424242',
        'expiryMonth' => '6',
        'expiryYear' => '2022',
        'cvv' => '123',
    ],
    'clientIp' => $_SERVER['REMOTE_ADDR'],
];
```

Then, you can send the payment request to the gateway and receive a response.

```
// Send payment request
$response = $gateway->purchase($params)->send();

// Process response
if ($response->isSuccessful()) {
    echo "Payment successful!\n";
    echo "Transaction reference: " . $response->getTransactionReference();
} else {
    echo "Payment failed: " . $response->getMessage();
}
```

## Output example

```
Payment successful!
Transaction reference: abc123
```

For more detailed information, please see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use the PHP Omnipay code to process payments?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-php-omnipay-code-to-process-payments)