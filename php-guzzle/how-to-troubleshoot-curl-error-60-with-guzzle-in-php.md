# How to troubleshoot cURL error 60 with Guzzle in PHP?
// plain

To troubleshoot cURL error 60 with Guzzle in PHP, you can use the following code snippet:

```php
try {
    $client = new GuzzleHttp\Client();
    $res = $client->request('GET', 'https://example.com');
    echo $res->getStatusCode();
} catch (GuzzleHttp\Exception\RequestException $e) {
    echo $e->getMessage();
}
```

The output of the above code will be the error message associated with the cURL error 60.

## Code explanation


- Check the URL you are trying to access is valid and reachable.
- Check the SSL certificate of the URL is valid and up-to-date.
- Check the cURL version you are using is up-to-date.
- Check the Guzzle version you are using is up-to-date.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [cURL Documentation](https://curl.haxx.se/docs/)

onelinerhub: [How to troubleshoot cURL error 60 with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-troubleshoot-curl-error-60-with-guzzle-in-php)