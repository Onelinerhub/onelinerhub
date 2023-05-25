# How to add an SSL certificate to a request with PHP Guzzle?
// plain

Adding an SSL certificate to a request with PHP Guzzle is easy.

```
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'https://example.com', [
    'verify' => '/path/to/certificate.pem'
]);
```

The above code will add an SSL certificate to the request.

- `$client`: Instantiates a new Guzzle client.
- `$res`: Makes a GET request to `https://example.com` with the specified SSL certificate.
- `verify`: Specifies the path to the SSL certificate.

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to add an SSL certificate to a request with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-an-ssl-certificate-to-a-request-with-php-guzzle)