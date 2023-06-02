# How do I use the Omnipay library to get a customer's address in PHP?
// plain

Using the Omnipay library to get a customer's address in PHP is a simple process. First, you need to include the Omnipay library in your project.

```php
require_once('vendor/autoload.php');
```

Next, you need to create an instance of the gateway you are using.

```php
$gateway = Omnipay::create('Stripe');
```

Then, you need to set the API key, which is used to authenticate requests.

```php
$gateway->setApiKey('sk_test_123456789');
```

Finally, you need to call the `fetchCustomer` method to get the customer's address.

```php
$response = $gateway->fetchCustomer('cus_1234567890')->send();
$address = $response->getCustomer()->getAddress();
```

The `$address` variable will now contain an array of the customer's address.

## Helpful links

- [Omnipay Library](https://github.com/thephpleague/omnipay)
- [Stripe Gateway Documentation](https://omnipay.thephpleague.com/gateways/stripe/)
- [Fetch Customer Method Documentation](https://omnipay.thephpleague.com/api/gateways/stripe/#fetch-customer)

onelinerhub: [How do I use the Omnipay library to get a customer's address in PHP?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-omnipay-library-to-get-a-customer-s-address-in-php)