# How do I use the Omnipay PHP library to generate a hash?
// plain

The Omnipay PHP library can be used to generate a hash for payment processing. To do this, the library provides the `getHash()` function. This example code shows how to generate a hash:

```php
// Create a gateway for the PayPal ExpressGateway
$gateway = Omnipay::create('PayPal_Express');

// Initialise the gateway
$gateway->initialize(array(
    'username' => 'example',
    'password' => 'example',
    'signature' => 'example',
));

// Get the hash
$hash = $gateway->getHash();

echo $hash;
```

This example code will output the generated hash, which can then be used for payment processing.

The `getHash()` function takes three parameters: `username`, `password`, and `signature`. These parameters are used to authenticate the payment request.

For more information, see the [Omnipay documentation](https://github.com/thephpleague/omnipay#usage).

onelinerhub: [How do I use the Omnipay PHP library to generate a hash?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-omnipay-php-library-to-generate-a-hash)