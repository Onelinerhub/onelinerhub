# How can I use the PHP Omnipay Key to process payments?
// plain

The PHP Omnipay Key is a library that enables developers to easily integrate payment processing into their PHP applications. It provides a unified API across many payment gateways, allowing developers to quickly and easily integrate payments into their applications.

To use the PHP Omnipay Key to process payments, you will first need to install the library. You can do this using Composer:

```
composer require league/omnipay
```

Once installed, you can use the Omnipay API to create a gateway instance. This is done by passing in the gateway name as a parameter, for example:

```
$gateway = Omnipay::create('Stripe');
```

You can then configure the gateway with your payment gateway credentials. This is done by passing an array of configuration options to the gateway's `initialize` method:

```
$gateway->initialize([
    'apiKey' => 'your_api_key',
    'secret' => 'your_secret_key'
]);
```

Once the gateway is configured, you can use the `purchase` method to initiate a purchase. This method takes an array of parameters, such as the amount to charge, currency, and customer details:

```
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => [
        'number' => '4111111111111111',
        'expiryMonth' => '12',
        'expiryYear' => '2021',
        'cvv' => '123'
    ]
]);
```

The `purchase` method returns a `Response` object, which contains information about the transaction, such as whether it was successful or not. You can then use this response to take appropriate action, such as displaying an error message or redirecting the user to a success page.

For more information, please see the [Omnipay documentation](https://omnipay.thephpleague.com/).

## Code explanation
**

1. `composer require league/omnipay` - This command is used to install the Omnipay library via Composer.
2. `$gateway = Omnipay::create('Stripe')` - This line creates a gateway instance, passing in the gateway name (in this case, Stripe) as a parameter.
3. `$gateway->initialize([...])` - This line configures the gateway with your payment gateway credentials.
4. `$response = $gateway->purchase([...])` - This line initiates a purchase, passing in the amount, currency, and customer details as parameters.
5. `$response->isSuccessful()` - This method can be used to check if the transaction was successful or not.

**## Helpful links**

- [Omnipay Documentation](https://omnipay.thephpleague.com/)

onelinerhub: [How can I use the PHP Omnipay Key to process payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-the-php-omnipay-key-to-process-payments)