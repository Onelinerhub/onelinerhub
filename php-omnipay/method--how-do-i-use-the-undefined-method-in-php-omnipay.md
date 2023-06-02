# method

How do I use the undefined method in PHP Omnipay?
// plain

The undefined method in PHP Omnipay is a method that allows developers to access and use a payment gateway without having to define the gateway in the code. This is useful when dealing with multiple payment gateways, as it allows developers to easily switch between them without having to define each one.

To use the undefined method, developers must first include the Omnipay library in their code. This can be done by adding the following line at the top of the file:

```php
require_once('/path/to/omnipay/autoload.php');
```

Next, developers must create an instance of the Omnipay\Common\GatewayFactory class, passing in the name of the payment gateway they wish to use. For example, to use the Stripe gateway:

```php
$gateway = Omnipay\Common\GatewayFactory::create('Stripe');
```

The GatewayFactory will then return an instance of the gateway with the specified name. This instance can then be used to make requests to the payment gateway. For example, to make a purchase request:

```php
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => [
        'number' => '4111111111111111',
        'expiryMonth' => '01',
        'expiryYear' => '2021',
        'cvv' => '123'
    ]
])->send();

if ($response->isSuccessful()) {
    // payment was successful: update database
    print_r($response);
} else {
    // payment failed: display message to customer
    echo $response->getMessage();
}
```

The output of the above code would be something like:

```
Omnipay\Common\Message\AbstractResponse Object
(
    [data:protected] => Array
        (
            [id] => ch_1FfZb1LfQeQd2LjdYi4p8u6h
            [object] => charge
            ...
        )
    [statusCode:protected] => 200
    [request:protected] => Omnipay\Common\Message\AbstractRequest Object
        (
            [parameters:protected] => Array
                (
                    [amount] => 10.00
                    [currency] => USD
                    [card] => Array
                        (
                            [number] => 4111111111111111
                            [expiryMonth] => 01
                            [expiryYear] => 2021
                            [cvv] => 123
                        )
                    ...
                )
        )
)
```

The undefined method in PHP Omnipay is a powerful and convenient way to access and use payment gateways without having to define each gateway in the code. It is easy to use and can save developers time and effort when dealing with multiple payment gateways.

## Helpful links

- [Omnipay Docs](https://omnipay.thephpleague.com/)
- [GitHub Repository](https://github.com/thephpleague/omnipay)

onelinerhub: [method

How do I use the undefined method in PHP Omnipay?](https://onelinerhub.com/php-omnipay/method--how-do-i-use-the-undefined-method-in-php-omnipay)