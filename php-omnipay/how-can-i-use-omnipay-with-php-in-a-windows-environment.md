# How can I use Omnipay with PHP in a Windows environment?
// plain

Omnipay is a payment processing library for PHP that can be used in a Windows environment. It supports many popular payment gateways such as PayPal, Stripe, and Authorize.net.

To use Omnipay with PHP in a Windows environment, you will need to install the Omnipay library with Composer. First, create a `composer.json` file in the root of your project and add the following:

```json
{
    "require": {
        "omnipay/omnipay": "~3.0"
    }
}
```

Then run `composer install` from the command line. Once the installation is complete, you can access the Omnipay library in your project.

Here is an example of how to use Omnipay to process a credit card payment:

```php
// Include the Omnipay library
require 'vendor/autoload.php';

// Create an instance of the gateway
$gateway = Omnipay::create('Stripe');

// Set your secret key
$gateway->setApiKey('sk_test_1234567890');

// Process the payment
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => [
        'number' => '4242424242424242',
        'expiryMonth' => '6',
        'expiryYear' => '2021',
        'cvv' => '123',
    ],
])->send();

// Check the response
if ($response->isSuccessful()) {
    echo "Payment was successful!\n";
} else {
    echo "Payment failed.\n";
}
```

## Output example

```
Payment was successful!
```

For more information, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How can I use Omnipay with PHP in a Windows environment?](https://onelinerhub.com/php-omnipay/how-can-i-use-omnipay-with-php-in-a-windows-environment)