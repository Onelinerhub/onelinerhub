# How to use a certificate with a Guzzle client in PHP?
// plain

Using a certificate with a Guzzle client in PHP is relatively straightforward.

```php
$client = new GuzzleHttp\Client([
    'verify' => '/path/to/certificate.pem'
]);
```

This code creates a new Guzzle client with the `verify` option set to the path of the certificate.

- `$client`: A new Guzzle client instance
- `verify`: The `verify` option is used to specify the path to the certificate
- `/path/to/certificate.pem`: The path to the certificate

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [PHP Manual: Stream Context Options](http://php.net/manual/en/context.ssl.php)

onelinerhub: [How to use a certificate with a Guzzle client in PHP?](https://onelinerhub.com/php-guzzle/how-to-use-a-certificate-with-a-guzzle-client-in-php)