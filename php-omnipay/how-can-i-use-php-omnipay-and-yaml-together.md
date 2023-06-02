# How can I use PHP Omnipay and YAML together?
// plain

PHP Omnipay and YAML can be used together to make the process of payment integration easier. YAML is used to store configuration information for the Omnipay library, while PHP is used to process the payment requests.

## Example code

```
<?php
require_once('vendor/autoload.php');

$gateway = Omnipay::create('Stripe');
$gateway->setApiKey('sk_test_1234567890');

$params = [
    'amount' => '10.00',
    'currency' => 'USD',
    'description' => 'Test Payment',
    'returnUrl' => 'https://example.com/return',
    'cancelUrl' => 'https://example.com/cancel',
];

$response = $gateway->purchase($params)->send();

if ($response->isSuccessful()) {
    // Payment was successful
    echo "Success!";
} elseif ($response->isRedirect()) {
    // Redirect to offsite payment gateway
    $response->redirect();
} else {
    // Payment failed
    echo $response->getMessage();
}
```

## Output example
 `Success!`

## Code explanation

- `require_once('vendor/autoload.php');` - This line is used to include the autoloader for the Omnipay library.
- `$gateway = Omnipay::create('Stripe');` - This line creates an Omnipay gateway object for Stripe.
- `$gateway->setApiKey('sk_test_1234567890');` - This line sets the API key for the Stripe gateway.
- `$params = [...]` - This line creates an array of parameters to be sent to the gateway.
- `$response = $gateway->purchase($params)->send();` - This line sends the payment request to the gateway.
- `if ($response->isSuccessful())` - This line checks if the payment was successful.
- `$response->redirect();` - This line redirects the customer to the payment gateway.

## Helpful links
- [PHP Omnipay Documentation](https://omnipay.thephpleague.com/docs/)
- [YAML Syntax](https://yaml.org/spec/1.2/spec.html)

onelinerhub: [How can I use PHP Omnipay and YAML together?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-and-yaml-together)