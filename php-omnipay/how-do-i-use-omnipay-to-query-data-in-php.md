# How do I use Omnipay to query data in PHP?
// plain

Omnipay is a payment processing library for PHP. It provides a unified API across many payment gateways. To use Omnipay to query data in PHP, you need to install the library and then use the gateway's specific methods.

For example, if you want to query data from Stripe, you can use the following code:
```php
// Require the Omnipay library
require 'vendor/autoload.php';

// Create a gateway
$gateway = Omnipay::create('Stripe');

// Initialize the gateway
$gateway->initialize(array(
    'apiKey' => 'YOUR_STRIPE_API_KEY',
));

// Get the data
$data = $gateway->fetchTransaction(array('transactionReference' => 'TRANSACTION_REFERENCE'))->send();

// Output the data
echo '<pre>';
print_r($data);
echo '</pre>';
```

This example code will output the following data:
```
Omnipay\Stripe\Message\FetchTransactionResponse Object
(
    [request:Omnipay\Common\Message\AbstractRequest:private] => Omnipay\Stripe\Message\FetchTransactionRequest Object
        (
            [apiKey:Omnipay\Stripe\Message\AbstractRequest:private] => YOUR_STRIPE_API_KEY
            [endpoint:Omnipay\Stripe\Message\AbstractRequest:private] =>
            [httpClient:Omnipay\Common\Http\Client:private] =>
            [httpRequest:Omnipay\Common\Http\Message\Request:private] =>
            [data:protected] => Array
                (
                    [transactionReference] => TRANSACTION_REFERENCE
                )

```

## Code explanation


1. Require the Omnipay library: `require 'vendor/autoload.php';`
2. Create a gateway: `$gateway = Omnipay::create('Stripe');`
3. Initialize the gateway: `$gateway->initialize(array('apiKey' => 'YOUR_STRIPE_API_KEY',));`
4. Get the data: `$data = $gateway->fetchTransaction(array('transactionReference' => 'TRANSACTION_REFERENCE'))->send();`
5. Output the data: `echo '<pre>'; print_r($data); echo '</pre>';`

For more information, please refer to the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use Omnipay to query data in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-to-query-data-in-php)