# How can I use PHP Omnipay to process Yandex payments?
// plain

PHP Omnipay is a payment processing library that allows developers to easily integrate payment processing into their applications. It supports a wide range of payment gateways, including Yandex.

To use PHP Omnipay to process Yandex payments, first install the library via Composer:

```
composer require league/omnipay omnipay/yandex
```

Next, create an instance of the Omnipay gateway:

```php
use Omnipay\Omnipay;

$gateway = Omnipay::create('Yandex');
```

Then, set the gateway parameters, such as the shop ID and secret key:

```php
$gateway->setShopId('12345');
$gateway->setSecretKey('abcdef');
```

Finally, process the payment:

```php
$response = $gateway->purchase([
    'amount' => '10.00',
    'currency' => 'RUB',
    'returnUrl' => 'https://example.com/return',
    'cancelUrl' => 'https://example.com/cancel',
])->send();

if ($response->isRedirect()) {
    // redirect to offsite payment gateway
    $response->redirect();
} else {
    // payment failed
    echo $response->getMessage();
}
```

This code will send the purchase request to the Yandex gateway and handle the response. If the request is successful, the user will be redirected to the Yandex payment page.

## Helpful links
- https://omnipay.thephpleague.com/
- https://github.com/thephpleague/omnipay
- https://github.com/thephpleague/omnipay-yandex

onelinerhub: [How can I use PHP Omnipay to process Yandex payments?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-process-yandex-payments)