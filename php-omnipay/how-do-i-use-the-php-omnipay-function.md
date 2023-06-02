# How do I use the PHP Omnipay function?
// plain

The PHP Omnipay function is a library of payment processing classes that provides an abstracted interface for working with various payment gateways.

To use the PHP Omnipay function, you must first install the library using Composer:

```
composer require omnipay/omnipay
```

Once installed, you can create an instance of the Omnipay gateway class of your choice. For example, to create a Stripe gateway instance:

```
$gateway = Omnipay::create('Stripe');
```

You can then set the gateway's parameters, such as the API key, before making a purchase request:

```
$gateway->setApiKey('abc123');
$response = $gateway->purchase(['amount' => '10.00'])->send();
```

If the purchase request is successful, you can retrieve the transaction reference from the response object:

```
$ref = $response->getTransactionReference();
```

You can then use the transaction reference to perform other operations, such as a refund:

```
$response = $gateway->refund(['transactionReference' => $ref])->send();
```

For more information on using the PHP Omnipay function, refer to the official [documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use the PHP Omnipay function?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-php-omnipay-function)