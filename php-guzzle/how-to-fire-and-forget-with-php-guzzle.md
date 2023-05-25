# How to fire and forget with PHP Guzzle?
// plain

Fire and forget with PHP Guzzle is a way to send a request without waiting for a response. This is useful when you don't need to know the response, or when you want to send a request without blocking the current thread.

## Example code

```
$client = new \GuzzleHttp\Client();
$client->requestAsync('GET', 'http://example.com/');
```

This code will send an asynchronous GET request to the URL `http://example.com/` without waiting for a response.

## Code explanation

- `$client = new \GuzzleHttp\Client();`: creates a new Guzzle client
- `$client->requestAsync('GET', 'http://example.com/');`: sends an asynchronous GET request to the URL `http://example.com/`

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to fire and forget with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-fire-and-forget-with-php-guzzle)