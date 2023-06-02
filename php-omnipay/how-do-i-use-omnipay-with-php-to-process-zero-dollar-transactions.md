# How do I use Omnipay with PHP to process zero-dollar transactions?
// plain

Omnipay is a payment processing library for PHP which helps to process payments. It can be used to process zero-dollar transactions.

To use Omnipay with PHP to process zero-dollar transactions, you need to first install it using Composer. Then, you need to create a gateway instance for the payment processor you are using. Finally, you can use the gateway instance to call the authorize() method to process the zero-dollar transaction.

```php
// Create gateway instance
$gateway = Omnipay::create('PayPal_Express');

// Set API credentials
$gateway->setUsername('username');
$gateway->setPassword('password');
$gateway->setSignature('signature');

// Process zero-dollar transaction
$response = $gateway->authorize(['amount' => 0])->send();

// Output response
if ($response->isSuccessful()) {
    echo "Transaction successful!\n";
} else {
    echo "Transaction failed.\n";
}
```

## Output example

```
Transaction successful!
```

## Code explanation

- `$gateway = Omnipay::create('PayPal_Express')` - this line creates a gateway instance for the PayPal Express payment processor.
- `$gateway->setUsername('username')`, `$gateway->setPassword('password')`, and `$gateway->setSignature('signature')` - these lines set the API credentials for the payment processor.
- `$response = $gateway->authorize(['amount' => 0])->send()` - this line calls the authorize() method to process the zero-dollar transaction.
- `if ($response->isSuccessful()) {...} else {...}` - this checks if the transaction was successful, and outputs the appropriate message.

## Helpful links
- [Omnipay Documentation](https://omnipay.thephpleague.com/docs/)
- [PayPal Express Documentation](https://omnipay.thephpleague.com/gateways/paypal-express/)

onelinerhub: [How do I use Omnipay with PHP to process zero-dollar transactions?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-with-php-to-process-zero-dollar-transactions)