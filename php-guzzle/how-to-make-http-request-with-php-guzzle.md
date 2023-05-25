# How to make HTTP request with PHP Guzzle?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services.

To make an HTTP request with Guzzle, you need to create a `GuzzleHttp\Client` object and pass it the base URI of the web service you are trying to access.

```php
$client = new GuzzleHttp\Client(['base_uri' => 'http://httpbin.org/']);
```

Then you can use the `$client` object to make an HTTP request. For example, to make a GET request:

```php
$response = $client->request('GET', 'get');
echo $response->getBody();
```

The output of the above code will be a JSON string containing the response from the web service:

```json
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "GuzzleHttp/6.3.3 curl/7.54.0 PHP/7.2.10"
  },
  "origin": "1.2.3.4",
  "url": "http://httpbin.org/get"
}
```

## Code explanation


1. `$client = new GuzzleHttp\Client(['base_uri' => 'http://httpbin.org/']);` - creates a `GuzzleHttp\Client` object and passes it the base URI of the web service you are trying to access.

2. `$response = $client->request('GET', 'get');` - uses the `$client` object to make an HTTP request. In this case, it is a GET request.

3. `echo $response->getBody();` - prints out the response from the web service.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Guzzle GitHub Repository](https://github.com/guzzle/guzzle)

onelinerhub: [How to make HTTP request with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-make-http-request-with-php-guzzle)