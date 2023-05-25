# How to add an authorization header bearer in PHP Guzzle?
// plain

Adding an authorization header bearer in PHP Guzzle can be done using the `setDefaultOption` method.

```php
$client = new GuzzleHttp\Client();
$client->setDefaultOption('headers/Authorization', 'Bearer {token}');
```

This will set the `Authorization` header with the value `Bearer {token}` for all requests made with the `$client` object.

- `$client`: The GuzzleHttp\Client object used to make requests.
- `setDefaultOption`: The method used to set the default option for all requests.
- `headers/Authorization`: The header to set.
- `Bearer {token}`: The value of the header.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to add an authorization header bearer in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-an-authorization-header-bearer-in-php-guzzle)