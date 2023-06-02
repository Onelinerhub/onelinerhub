# How can I use PHP Omnipay to integrate Yclients into my website?
// plain

PHP Omnipay is a payment processing library that can be used to integrate Yclients into your website. To do this, you'll need to install the Omnipay library and the YClients driver.

You can then use the following code to create a payment form and submit it to YClients:

```
<?php
require 'vendor/autoload.php';

$gateway = Omnipay::create('YClients');
$gateway->setApiKey('YOUR_API_KEY');

$formData = [
    'amount' => '10.00',
    'currency' => 'USD',
    'description' => 'Test Payment',
];

$response = $gateway->purchase($formData)->send();

if ($response->isSuccessful()) {
    // payment was successful: update database
    print_r($response);
} elseif ($response->isRedirect()) {
    // redirect to offsite payment gateway
    $response->redirect();
} else {
    // payment failed: display message to customer
    echo $response->getMessage();
}
```

The code above will create a payment form, submit it to YClients, and handle the response. If the payment is successful, it will print the response to the screen. If it's a redirect, it will redirect the customer to the offsite payment gateway. If the payment fails, it will display an error message.

Parts of the code:

- `require 'vendor/autoload.php'`: This loads the Omnipay library.
- `$gateway = Omnipay::create('YClients')`: This creates an instance of the YClients driver.
- `$gateway->setApiKey('YOUR_API_KEY')`: This sets the API key for YClients.
- `$response = $gateway->purchase($formData)->send()`: This sends the payment form data to YClients.
- `if ($response->isSuccessful())`: This checks if the payment was successful.
- `$response->redirect()`: This redirects the customer to the offsite payment gateway.
- `echo $response->getMessage()`: This displays an error message if the payment fails.

## Helpful links

- [Omnipay Library](https://github.com/thephpleague/omnipay)
- [YClients Driver](https://github.com/thephpleague/omnipay-yclients)

onelinerhub: [How can I use PHP Omnipay to integrate Yclients into my website?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-integrate-yclients-into-my-website)