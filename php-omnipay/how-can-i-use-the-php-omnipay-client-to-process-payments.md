# How can I use the PHP Omnipay Client to process payments?
// plain

The PHP Omnipay Client is a library that simplifies the process of integrating payment processing into your web application. It provides a unified API across many different payment gateways, allowing you to easily switch between them as needed without needing to change your code.

To use the PHP Omnipay Client to process payments, you will need to first install the library via Composer. You can then create an instance of the gateway you want to use and set up your credentials.

```php
// Require the Omnipay library
require_once 'vendor/autoload.php';

// Create an instance of the gateway
$gateway = Omnipay::create('MyGateway');

// Set the gateway credentials
$gateway->setApiKey('abc123');
```

Once the gateway is set up, you can use the `purchase()` method to initiate a payment request. This method takes an array of parameters, such as the amount, currency, card details, and a return URL.

```php
// Create a payment request
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'GBP',
    'card' => [
        'number' => '4111111111111111',
        'expiryMonth' => '12',
        'expiryYear' => '2021',
        'cvv' => '123',
    ],
    'returnUrl' => 'https://www.example.com/payment/complete',
])->send();
```

The `purchase()` method will return an `Omnipay\Common\Message\ResponseInterface` object, which contains the response from the payment gateway. You can check the `isSuccessful()` method to determine if the payment was successful.

```php
// Check the response
if ($response->isSuccessful()) {
    // Payment was successful
    echo "Payment successful!";
} else {
    // Payment failed
    echo "Payment failed: " . $response->getMessage();
}
```

For more information, please refer to the [PHP Omnipay documentation](https://omnipay.thephpleague.com/).

## Code explanation
**
1. Require the Omnipay library (`require_once 'vendor/autoload.php';`)
2. Create an instance of the gateway (`$gateway = Omnipay::create('MyGateway');`)
3. Set the gateway credentials (`$gateway->setApiKey('abc123');`)
4. Create a payment request (`$response = $gateway->purchase([...])->send();`)
5. Check the response (`if ($response->isSuccessful()) {...}`)

**## Helpful links**
- [PHP Omnipay documentation](https://omnipay.thephpleague.com/)

onelinerhub: [How can I use the PHP Omnipay Client to process payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-the-php-omnipay-client-to-process-payments)