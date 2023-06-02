# How do I use the PHP Omnipay documentation to develop a payment gateway?
// plain

1. First, read the [Getting Started](https://omnipay.thephpleague.com/getting-started/) section of the Omnipay documentation to understand the basics of creating a payment gateway.

2. Next, create a new gateway class which extends the `Omnipay\Common\AbstractGateway` class. This class will contain all the necessary methods and properties to interact with the payment gateway.

3. Implement the `getName()` and `getDefaultParameters()` methods in your gateway class. The `getName()` method should return a string containing the name of the gateway, and the `getDefaultParameters()` method should return an array of parameters which are used to configure the gateway.

4. Create the `purchase()` method in your gateway class. This method is responsible for sending the payment request to the payment gateway.

5. Include the `Omnipay\Common\Message\AbstractRequest` class and create a new request class which extends this class. This class will contain all the necessary parameters to send the payment request.

6. Create the `send()` method in your request class. This method will be responsible for sending the payment request to the payment gateway and returning a response object.

7. Finally, create a test script to test your gateway. You can use the following example code to test your gateway:
```php
// Require the autoloader
require __DIR__ . '/vendor/autoload.php';

// Create a gateway object
$gateway = Omnipay::create('MyGateway');

// Initialize the gateway
$gateway->initialize(array(
    'param1' => 'value1',
    'param2' => 'value2',
));

// Create a credit card object
$card = new CreditCard(array(
    'firstName' => 'Example',
    'lastName' => 'User',
    'number' => '4111111111111111',
    'expiryMonth' => '01',
    'expiryYear' => '2020',
    'cvv' => '123',
));

// Do a purchase transaction on the gateway
$transaction = $gateway->purchase(array(
    'amount' => '10.00',
    'currency' => 'USD',
    'card' => $card,
));
$response = $transaction->send();

if ($response->isSuccessful()) {
    echo "Purchase transaction was successful!\n";
    $sale_id = $response->getTransactionReference();
    echo "Transaction reference = " . $sale_id . "\n";
}
```
## Output example

```
Purchase transaction was successful!
Transaction reference = 1234567890
```

onelinerhub: [How do I use the PHP Omnipay documentation to develop a payment gateway?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-php-omnipay-documentation-to-develop-a-payment-gateway)