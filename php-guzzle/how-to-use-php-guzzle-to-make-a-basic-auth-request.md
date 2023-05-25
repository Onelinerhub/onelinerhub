# How to use PHP Guzzle to make a basic auth request?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. To make a basic auth request with Guzzle, you need to create a client and pass the username and password as part of the request options.

```php
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'auth' => ['username', 'password']
]);
```

The output of the above code will be an instance of `GuzzleHttp\Psr7\Response` class.

## Code explanation


1. `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client instance.
2. `$response = $client->request('GET', 'http://example.com', [` - sends a GET request to the specified URL.
3. `'auth' => ['username', 'password']` - passes the username and password as part of the request options.
4. `]);` - closes the request options array.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Guzzle Basic Auth](http://docs.guzzlephp.org/en/stable/request-options.html#auth)

onelinerhub: [How to use PHP Guzzle to make a basic auth request?](https://onelinerhub.com/php-guzzle/how-to-use-php-guzzle-to-make-a-basic-auth-request)