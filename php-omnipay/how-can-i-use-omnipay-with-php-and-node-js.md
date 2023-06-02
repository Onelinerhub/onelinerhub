# How can I use Omnipay with PHP and Node.js?
// plain

Omnipay is a payment processing library for PHP and Node.js that is designed to make it easy to integrate payment processing into your application. It can be used to accept payments from a variety of payment gateways, including PayPal, Stripe, Authorize.net, and others.

In PHP, you can use Omnipay to create a purchase request and handle the response from the payment gateway. For example:

```php
// Create a gateway for the Authorize.net Gateway
// (routes to GatewayFactory::create)
$gateway = Omnipay::create('AuthorizeNet_AIM');

// Initialise the gateway
$gateway->initialize(array(
    'apiLoginId' => 'API_LOGIN_ID',
    'transactionKey' => 'TRANSACTION_KEY'
));

// Create a credit card object
// This card can be used for testing.
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

In Node.js, you can use the [Node.js Omnipay library](https://github.com/omnipay/omnipay-node) to integrate payment processing into your application. For example:

```javascript
// Create a gateway for the Authorize.net Gateway
const gateway = require('omnipay-authorizenet').gateway;

// Initialise the gateway
const authNetGateway = gateway({
    apiLoginId: 'API_LOGIN_ID',
    transactionKey: 'TRANSACTION_KEY'
});

// Create a credit card object
const card = {
    firstName: 'Example',
    lastName: 'User',
    number: '4111111111111111',
    expiryMonth: '01',
    expiryYear: '2020',
    cvv: '123'
};

// Do a purchase transaction on the gateway
authNetGateway.purchase({
    amount: '10.00',
    currency: 'USD',
    card: card
}).then(function (data) {
    console.log(data);
    if (data.responseCode === '1') {
        console.log('Purchase transaction was successful!');
        const saleId = data.transactionId;
        console.log('Transaction reference = ' + saleId);
    }
});
```

The code above creates a gateway object for the Authorize.net payment gateway, initializes it with the API credentials, creates a credit card object, and then performs a purchase transaction. If the transaction is successful, it prints out the transaction reference.

## Helpful links

- [Omnipay PHP Documentation](https://omnipay.thephpleague.com/)
- [Node.js Omnipay Library](https://github.com/omnipay/omnipay-node)

onelinerhub: [How can I use Omnipay with PHP and Node.js?](https://onelinerhub.com/php-omnipay/how-can-i-use-omnipay-with-php-and-node-js)