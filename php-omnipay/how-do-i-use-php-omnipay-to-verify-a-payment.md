# How do I use PHP Omnipay to verify a payment?
// plain

Using PHP Omnipay to verify a payment requires two steps:

1. Initialize the payment gateway:

```
require_once('vendor/autoload.php');

$gateway = Omnipay\Omnipay::create('PayPal_Express');
$gateway->setUsername('example@example.com');
$gateway->setPassword('1234567890');
$gateway->setSignature('ABCDEFGHIJKLMNOPQRSTUVWXYZ');
$gateway->setTestMode(true);
```

2. Verify the payment:

```
$response = $gateway->completePurchase([
    'transactionReference' => '1234567890',
    'amount' => '10.00',
    'currency' => 'USD',
])->send();

if ($response->isSuccessful()) {
    echo "Payment is verified!";
} else {
    echo "Payment is not verified!";
}
```

- `require_once('vendor/autoload.php')`: This line includes the Omnipay library.
- `$gateway = Omnipay\Omnipay::create('PayPal_Express')`: This line creates a new instance of the PayPal Express gateway.
- `$gateway->setUsername('example@example.com')`: This line sets the username of the gateway.
- `$gateway->setPassword('1234567890')`: This line sets the password of the gateway.
- `$gateway->setSignature('ABCDEFGHIJKLMNOPQRSTUVWXYZ')`: This line sets the signature of the gateway.
- `$gateway->setTestMode(true)`: This line sets the gateway to test mode.
- `$response = $gateway->completePurchase([])->send()`: This line sends the payment verification request to the gateway.
- `if ($response->isSuccessful())`: This line checks if the payment is successful.

## Helpful links
- [Omnipay Documentation](https://omnipay.thephpleague.com/)
- [PayPal Express Documentation](https://github.com/thephpleague/omnipay-paypal/blob/master/src/Message/ExpressCompletePurchaseRequest.php)

onelinerhub: [How do I use PHP Omnipay to verify a payment?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-to-verify-a-payment)