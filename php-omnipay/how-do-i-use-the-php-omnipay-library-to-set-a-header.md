# How do I use the PHP Omnipay library to set a header?
// plain

The PHP Omnipay library is a powerful library for processing payments. It can be used to set a header via the `setHeader` method. This method takes two parameters, the header name and the header value.

For example:

```php
$request = $gateway->purchase(...);
$request->setHeader('My-Header', 'My-Value');
```

The `setHeader` method returns the current request object, allowing for method chaining.

## Code explanation


1. `$request` - an instance of the `Request` class
2. `$gateway` - an instance of the `Gateway` class
3. `purchase` - a method of the `Gateway` class which returns an instance of the `Request` class
4. `setHeader` - a method of the `Request` class which takes two parameters, the header name and the header value

## Helpful links

- [PHP Omnipay Library](https://omnipay.thephpleague.com/)
- [Request Class](https://omnipay.thephpleague.com/api/request/)
- [Gateway Class](https://omnipay.thephpleague.com/api/gateway/)

onelinerhub: [How do I use the PHP Omnipay library to set a header?](https://onelinerhub.com/php-omnipay/how-do-i-use-the-php-omnipay-library-to-set-a-header)