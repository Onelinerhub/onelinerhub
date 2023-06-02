# How can I use PHP Omnipay ORM to process payments?
// plain

PHP Omnipay ORM is an open-source library that provides an object-oriented interface for processing payments with Omnipay. It allows developers to easily integrate payment processing into their applications.

To use PHP Omnipay ORM to process payments, you need to first install the library. You can do this with Composer by running the following command:

```
composer require omnipay/omnipay
```

Once you have installed the library, you can start using it to process payments. Here is an example of how you can use the library to create a payment gateway:

```php
// Create a gateway instance
$gateway = Omnipay::create('MyGateway');

// Set the parameters
$gateway->setUsername('username');
$gateway->setPassword('password');

// Process the payment
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => [
        'number' => '4111111111111111',
        'expiryMonth' => '12',
        'expiryYear' => '2022',
    ],
])->send();

// Check the response
if ($response->isSuccessful()) {
    echo "Payment was successful.";
} else {
    echo "Payment was not successful. Error message: " . $response->getMessage();
}
```

The code above will create a gateway instance, set the parameters, process the payment, and check the response. If the payment is successful, it will output `Payment was successful.`, otherwise it will output the error message.

For more information about using PHP Omnipay ORM to process payments, you can refer to the [official documentation](https://github.com/thephpleague/omnipay#getting-started).

## Code explanation
**
- `composer require omnipay/omnipay`: This command is used to install the library.
- `$gateway = Omnipay::create('MyGateway');`: This line creates a gateway instance.
- `$gateway->setUsername('username');`: This line sets the username for the gateway.
- `$gateway->setPassword('password');`: This line sets the password for the gateway.
- `$response = $gateway->purchase([...])->send();`: This line processes the payment.
- `if ($response->isSuccessful()) {...}`: This line checks the response and outputs the appropriate message.

onelinerhub: [How can I use PHP Omnipay ORM to process payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-orm-to-process-payments)