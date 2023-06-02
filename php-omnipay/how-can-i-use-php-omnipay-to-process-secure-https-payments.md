# How can I use PHP Omnipay to process secure HTTPS payments?
// plain

PHP Omnipay is a payment processing library that makes it easy to integrate secure HTTPS payments into your website.

To use PHP Omnipay, you need to install the library using Composer. Once installed, you can use the library to process payments using the following code:

```php
// Create the gateway
$gateway = Omnipay::create('PayPal_Express');

// Set API credentials
$gateway->setUsername('your_username');
$gateway->setPassword('your_password');

// Send purchase request
$purchaseResponse = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://www.example.com/return',
    'cancelUrl' => 'https://www.example.com/cancel',
))->send();

// Process response
if ($purchaseResponse->isSuccessful()) {
    // Payment was successful
    echo "Payment successful\n";
} elseif ($purchaseResponse->isRedirect()) {
    // Redirect to offsite payment gateway
    $purchaseResponse->redirect();
} else {
    // Payment failed
    echo "Payment failed: " . $purchaseResponse->getMessage() . "\n";
}
```

## Output example

```
Payment successful
```

The code above:
- Creates a gateway object (`$gateway`) using the `Omnipay::create()` method
- Sets the API credentials (`setUsername()` and `setPassword()`)
- Sends a purchase request (`$gateway->purchase()`)
- Processes the response (`isSuccessful()`, `isRedirect()`, `getMessage()` and `redirect()`)

For more information, see the [PHP Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How can I use PHP Omnipay to process secure HTTPS payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-process-secure-https-payments)