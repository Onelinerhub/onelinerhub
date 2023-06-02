# payment

How do I use Omnipay to send a payment using PHP?
// plain

Omnipay is a payment processing library for PHP that enables you to quickly and easily send payments. To use Omnipay to send a payment using PHP, you will need to include the Omnipay library and create a gateway object.

You can include the library using Composer:

```
composer require omnipay/omnipay
```

Then you will need to create a gateway object:

```php
use Omnipay\Omnipay;
$gateway = Omnipay::create('PayPal_Express');
```

The gateway object is used to set the payment parameters. For example, to set the payment amount, you can use the `setAmount()` method:

```php
$gateway->setAmount(10.00);
```

Once all the payment parameters have been set, you can send the payment using the `purchase()` method:

```php
$response = $gateway->purchase()->send();

if ($response->isSuccessful()) {
    echo "Payment was successful!\n";
} else {
    echo "Payment failed.\n";
}
```

The `purchase()` method will return a response object, which you can then use to check whether the payment was successful or not.

For more information, please refer to the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [payment

How do I use Omnipay to send a payment using PHP?](https://onelinerhub.com/php-omnipay/payment--how-do-i-use-omnipay-to-send-a-payment-using-php)