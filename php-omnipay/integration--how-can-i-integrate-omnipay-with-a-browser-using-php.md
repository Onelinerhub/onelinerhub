# integration

How can I integrate Omnipay with a browser using PHP?
// plain

Integrating Omnipay with a browser using PHP is fairly simple. To get started, you will need to include the Omnipay library in your project. This can be done with the following code:

```php
require_once('/path/to/Omnipay/autoload.php');
```

Once the library is included, you can create a gateway for your chosen payment provider. For example, to create a Stripe gateway:

```php
$gateway = Omnipay::create('Stripe');
```

Next, you will need to configure the gateway with your API keys. This can be done by setting the parameters:

```php
$gateway->setApiKey('your_stripe_api_key');
```

Finally, you can submit a payment request using the `purchase()` method. This will return a response object which can be used to obtain the payment status:

```php
$response = $gateway->purchase($params)->send();
if ($response->isSuccessful()) {
    // Payment was successful
} else {
    // Payment was unsuccessful
    echo $response->getMessage();
}
```

For more information on integrating Omnipay with PHP, please refer to the [official documentation](https://omnipay.thephpleague.com/).

onelinerhub: [integration

How can I integrate Omnipay with a browser using PHP?](https://onelinerhub.com/php-omnipay/integration--how-can-i-integrate-omnipay-with-a-browser-using-php)