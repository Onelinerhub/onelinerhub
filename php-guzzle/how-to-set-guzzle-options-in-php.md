# How to set Guzzle options in PHP?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. Guzzle options can be set in PHP using the `setDefaultOption` method.

```php
$client = new GuzzleHttp\Client();
$client->setDefaultOption('headers/Content-Type', 'application/json');
```

This example sets the default Content-Type header to `application/json`.

The `setDefaultOption` method takes two parameters:

1. `$key` - The name of the option to set.
2. `$value` - The value of the option.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to set Guzzle options in PHP?](https://onelinerhub.com/php-guzzle/how-to-set-guzzle-options-in-php)