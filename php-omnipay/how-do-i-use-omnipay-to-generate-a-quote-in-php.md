# How do I use Omnipay to generate a quote in PHP?
// plain

Omnipay is a payment processing library for PHP. It provides an easy way to generate quotes in PHP. Here is an example:

```php
// Initialize Omnipay
$gateway = Omnipay::create('PayPal_Express');
$gateway->setUsername('your_username');
$gateway->setPassword('your_password');

// Setup parameters
$params = array(
    'amount' => '10.00',
    'currency' => 'USD',
    'description' => 'Test Payment',
    'returnUrl' => 'http://www.example.com/return',
    'cancelUrl' => 'http://www.example.com/cancel',
);

// Generate a quote
$response = $gateway->quote($params)->send();

// Check for a successful response
if ($response->isSuccessful()) {
    // Quote is successful
    $quote = $response->getQuote();
    echo "Quote generated successfully: ".$quote;
} else {
    // Quote was unsuccessful
    echo "Quote failed: ".$response->getMessage();
}
```

## Output example

```
Quote generated successfully: 10.00 USD
```

In the example above:
1. we create an instance of the PayPal_Express gateway using the `Omnipay::create()` method.
2. We set the username and password for the gateway using the `setUsername()` and `setPassword()` methods.
3. We then set the parameters for the quote, including the amount, currency, description, return URL, and cancel URL.
4. We generate the quote using the `quote()` method.
5. We check the response from the gateway using the `isSuccessful()` method.
6. If the response is successful, we get the quote using the `getQuote()` method.
7. We then output the generated quote.

## Helpful links
- [Omnipay Documentation](https://omnipay.thephpleague.com/docs/)
- [PayPal Express Documentation](https://omnipay.thephpleague.com/gateways/paypal-express/)

onelinerhub: [How do I use Omnipay to generate a quote in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-to-generate-a-quote-in-php)