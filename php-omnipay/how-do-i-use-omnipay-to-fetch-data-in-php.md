# How do I use Omnipay to fetch data in PHP?
// plain

Omnipay is a payment processing library for PHP. It provides a unified interface to access various payment gateways. To use Omnipay to fetch data in PHP, you need to include the Omnipay library in your project and then call the relevant methods to make requests and receive responses.

For example, to make a request to the Stripe gateway, you can use the following code:

```php
$gateway = Omnipay::create('Stripe');
$response = $gateway->fetchData(['param1' => 'value1', 'param2' => 'value2'])->send();

if ($response->isSuccessful()) {
    // fetch data was successful
    $data = $response->getData();
    print_r($data);
} else {
    // fetch data failed
    echo $response->getMessage();
}
```

This code will create a gateway instance, make a request to the Stripe gateway to fetch data, and then check the response to see if the request was successful. If it was successful, it will print the data that was fetched.

The following parts of the code are relevant:

- `$gateway = Omnipay::create('Stripe');` creates a gateway instance for the Stripe payment gateway.
- `$response = $gateway->fetchData(['param1' => 'value1', 'param2' => 'value2'])->send();` makes a request to the Stripe gateway to fetch data.
- `if ($response->isSuccessful()) { ... }` checks the response to see if the request was successful.
- `$data = $response->getData();` gets the data that was fetched.

For more information, see the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use Omnipay to fetch data in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-to-fetch-data-in-php)