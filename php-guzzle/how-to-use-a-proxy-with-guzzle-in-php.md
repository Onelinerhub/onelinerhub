# How to use a proxy with Guzzle in PHP?
// plain

Using a proxy with Guzzle in PHP is easy. You can specify the proxy to use when creating the client.

```php
$client = new GuzzleHttp\Client([
    'proxy' => 'http://username:password@host:port'
]);
```

The code above creates a new Guzzle client with the specified proxy.

1. `$client`: This is the Guzzle client object.
2. `GuzzleHttp\Client`: This is the class used to create the client.
3. `proxy`: This is the configuration option used to specify the proxy.
4. `http://username:password@host:port`: This is the proxy URL, which includes the username, password, host and port.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use a proxy with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-use-a-proxy-with-guzzle-in-php)