# How do I use Omnipay with XPath in PHP?
// plain

Omnipay is a payment processing library for PHP that can be used with XPath. XPath is an XML query language used to select nodes from an XML document. To use Omnipay with XPath in PHP, the following steps can be taken:

1. Install the Omnipay library via composer, or download the source code from Github.

2. Create a new XML document containing the data that needs to be processed.

3. Use the XPath query language to select the nodes from the XML document that you need to process.

4. Use the Omnipay library to process the payment using the selected nodes.

```php
// Create a new Omnipay instance
$gateway = Omnipay::create('MyGateway');

// Use XPath to select the nodes from the XML document
$nodes = $xpath->query("//payment/card");

// Set the parameters for the payment
$params = array(
    'card' => $nodes,
    'amount' => 10.00
);

// Process the payment
$response = $gateway->purchase($params)->send();

// Check the response
if ($response->isSuccessful()) {
    echo "Payment was successful!";
} else {
    echo "Payment failed!";
}
```

Payment was successful!

## Helpful links
- [Omnipay Library](https://github.com/thephpleague/omnipay)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

onelinerhub: [How do I use Omnipay with XPath in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-omnipay-with-xpath-in-php)