# How do I integrate Omnipay with Bitbucket to process payments in PHP?
// plain

Integrating Omnipay with Bitbucket to process payments in PHP is relatively simple. First, you need to install the Omnipay library by including the following code in your project's composer.json file:

```
{
    "require": {
        "omnipay/omnipay": "~2.0"
    }
}
```

Once the library is installed, you can use it to set up a payment gateway. The following example code shows how to create a gateway instance for Bitbucket:

```
use Omnipay\Omnipay;

$gateway = Omnipay::create('Bitbucket');
$gateway->setApiKey('your_api_key');
$gateway->setSecret('your_secret');
```

Once the gateway is set up, you can use it to process payments. The following example code shows how to process a payment using the gateway:

```
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
])->send();

if ($response->isSuccessful()) {
    // Payment was successful
    echo "Transaction was successful!\n";
    $sale_id = $response->getTransactionReference();
    echo "Transaction reference = " . $sale_id . "\n";
} else {
    // Payment failed
    echo "Transaction failed.\n";
}
```

## Code explanation


1. `require` - Require the Omnipay library in the project's composer.json file.
2. `$gateway` - Create a gateway instance for Bitbucket.
3. `$response` - Process the payment using the gateway.
4. `isSuccessful` - Check whether the payment was successful or not.
5. `getTransactionReference` - Get the transaction reference for a successful payment.

## Helpful links

- Omnipay: https://omnipay.thephpleague.com/
- Bitbucket: https://bitbucket.org/

onelinerhub: [How do I integrate Omnipay with Bitbucket to process payments in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-integrate-omnipay-with-bitbucket-to-process-payments-in-php)