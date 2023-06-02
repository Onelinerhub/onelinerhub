# How can I use PHP Omnipay to parse XML data?
// plain

Using PHP Omnipay to parse XML data is fairly simple.

First, you need to include Omnipay in your project. You can do this using Composer:

```
composer require league/omnipay
```

Once that is done, you can use the following code to parse the XML data:

```php
$xml = simplexml_load_string($xmlString);
$gateway = Omnipay::create('YourGatewayName');
$response = $gateway->parseXmlResponse($xml);
```

The `$response` variable will now contain the parsed data from the XML. You can then access the data using the `$response->getData()` method.

## Code explanation


1. `composer require league/omnipay` - This adds the Omnipay library to your project.
2. `simplexml_load_string($xmlString)` - This parses the XML string into an object.
3. `Omnipay::create('YourGatewayName')` - This creates an instance of the Omnipay gateway.
4. `$gateway->parseXmlResponse($xml)` - This parses the XML data and returns a response object.
5. `$response->getData()` - This returns the parsed data from the XML.

For more information, please refer to the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How can I use PHP Omnipay to parse XML data?](https://onelinerhub.com/php-omnipay/how-can-i-use-php-omnipay-to-parse-xml-data)