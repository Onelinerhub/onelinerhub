# How to set a timeout for a Guzzle client in PHP?
// plain

Setting a timeout for a Guzzle client in PHP is easy. You can set a timeout for a Guzzle client by passing a `timeout` option to the `GuzzleHttp\Client` constructor.

```php
$client = new GuzzleHttp\Client([
    'timeout' => 10.0,
]);
```

The above code will set the timeout to 10 seconds.

## Code explanation


- `GuzzleHttp\Client`: This is the Guzzle client class.
- `timeout`: This is the option used to set the timeout.
- `10.0`: This is the value of the timeout in seconds.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to set a timeout for a Guzzle client in PHP?](https://onelinerhub.com/php-guzzle/how-to-set-a-timeout-for-a-guzzle-client-in-php)