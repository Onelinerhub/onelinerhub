# How can I use the PHP Omnipay library to create an array?
// plain

The PHP Omnipay library is a package that provides an interface for processing payments. It can be used to create an array of payment data by using the `createRequest()` method. The method takes an array of parameters and returns an array of data that can be used to process the payment.

For example, the following code will create an array of payment data:

```php
$data = Omnipay::createRequest([
    'amount' => 10.00,
    'currency' => 'USD',
    'description' => 'My Payment',
]);
```

The output of the above code will be an array of payment data, similar to the following:

```
Array
(
    [amount] => 10.00
    [currency] => USD
    [description] => My Payment
)
```

The `createRequest()` method also accepts other parameters, such as the payment gateway, card details, and more. These additional parameters can be used to further customize the payment data array.

The PHP Omnipay library also provides other methods for processing payments, such as `purchase()`, `refund()`, and `void()`.

For more information about using the PHP Omnipay library, see the [official documentation](https://github.com/thephpleague/omnipay).

onelinerhub: [How can I use the PHP Omnipay library to create an array?](https://onelinerhub.com/php-omnipay/how-can-i-use-the-php-omnipay-library-to-create-an-array)