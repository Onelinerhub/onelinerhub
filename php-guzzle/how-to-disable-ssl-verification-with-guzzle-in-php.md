# How to disable SSL verification with Guzzle in PHP?
// plain

To disable SSL verification with Guzzle in PHP, you can use the `verify` option in the request configuration array. This option takes a boolean value, where `false` will disable SSL verification.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'https://example.com', [
    'verify' => false
]);
```

The code above will create a new Guzzle client and make a GET request to `https://example.com` with SSL verification disabled.

- `$client = new GuzzleHttp\Client();` creates a new Guzzle client.
- `$response = $client->request('GET', 'https://example.com', [` makes a GET request to `https://example.com` with the following options.
- `'verify' => false` disables SSL verification.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to disable SSL verification with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-disable-ssl-verification-with-guzzle-in-php)