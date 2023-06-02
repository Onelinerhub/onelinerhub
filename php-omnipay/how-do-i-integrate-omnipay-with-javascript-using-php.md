# How do I integrate Omnipay with JavaScript using PHP?
// plain

Integrating Omnipay with JavaScript using PHP is fairly straightforward. First, you'll need to include the Omnipay library in your PHP file. This can be done with the following code:
```php
require_once('/path/to/Omnipay/autoload.php');
```

Once you have the library included, you can use the Omnipay class to create an instance of the payment gateway you want to use. For example, if you wanted to use PayPal Express, you could do this:
```php
$gateway = Omnipay::create('PayPal_Express');
```

Next, you'll need to configure the gateway with your credentials. This is done with the setters for each of the credentials:
```php
$gateway->setUsername('your_paypal_username');
$gateway->setPassword('your_paypal_password');
$gateway->setSignature('your_paypal_signature');
```

Once the gateway is configured, you can then use the `purchase` method to make a purchase. This method takes an array of parameters, including the amount, currency, and return URL. For example:
```php
$response = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'http://www.example.com/return_url'
))->send();
```

The `$response` variable will now contain the response from the payment gateway. If the purchase was successful, you can then redirect the user to the payment gateway's URL with the following code:
```php
$response->redirect();
```

Once the user has completed their payment, they will be redirected back to the return URL that was specified earlier.

## Helpful links
- [Omnipay Documentation](https://omnipay.thephpleague.com/getting-started/)
- [PayPal Express Documentation](https://omnipay.thephpleague.com/gateways/paypal-express/)

onelinerhub: [How do I integrate Omnipay with JavaScript using PHP?](https://onelinerhub.com/php-omnipay/how-do-i-integrate-omnipay-with-javascript-using-php)