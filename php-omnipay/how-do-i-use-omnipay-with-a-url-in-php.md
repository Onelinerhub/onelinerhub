# How do I use Omnipay with a URL in PHP?
// plain

Omnipay is a payment processing library for PHP which can be used to accept payments from a URL. The following example shows how to use Omnipay with a URL:

```php
// Require the Omnipay library
require_once('vendor/autoload.php');

// Create a gateway object
$gateway = Omnipay::create('PayPal_Express');

// Initialize the gateway
$gateway->initialize([
    'username' => 'example_username',
    'password' => 'example_password',
    'signature' => 'example_signature',
    'testMode' => true
]);

// Create a purchase request
$purchaseRequest = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'returnUrl' => 'https://example.com/return',
    'cancelUrl' => 'https://example.com/cancel'
]);

// Send the purchase request
$response = $purchaseRequest->send();

// Get the URL to redirect the customer to
$redirectUrl = $response->getRedirectUrl();

// Redirect the customer to the payment page
header('Location: ' . $redirectUrl);
```

This code will create a purchase request and send it to the payment gateway. The response will contain a URL which the customer can be redirected to in order to complete the payment.

## Code explanation
**

1. `require_once('vendor/autoload.php');` - This line requires the Omnipay library.
2. `$gateway = Omnipay::create('PayPal_Express');` - This line creates a gateway object for the PayPal Express gateway.
3. `$gateway->initialize([...])` - This line initializes the gateway with the provided credentials.
4. `$purchaseRequest = $gateway->purchase([...])` - This line creates a purchase request with the provided parameters.
5. `$response = $purchaseRequest->send();` - This line sends the purchase request to the payment gateway.
6. `$redirectUrl = $response->getRedirectUrl();` - This line gets the URL which the customer should be redirected to in order to complete the payment.
7. `header('Location: ' . $redirectUrl);` - This line redirects the customer to the payment page.

**## Helpful links**

- [Omnipay - Official website](https://omnipay.thephpleague.com/)
- [Omnipay - Documentation](https://omnipay.thephpleague.com/docs/)

onelinerhub: [How do I use Omnipay with a URL in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-with-a-url-in-php)