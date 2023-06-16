# How do I make a request in Laravel using PHP?
// plain

Making a request in Laravel using PHP is easy and straightforward. Here is an example of a GET request:

```
<?php
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://example.com/');

echo $response->getStatusCode(); // 200
echo $response->getHeaderLine('content-type'); // 'application/json; charset=utf8'
echo $response->getBody(); // '{"id": 1420053, "name": "guzzle", ...}
```

In the example above, we create a new `GuzzleHttp\Client` object, which is used to make the request. We then call the `request` method, passing in the HTTP verb (GET) and the URL to which we want to make the request. We then get the response status code, header line and body and echo them out.

## Code explanation


1. `$client = new \GuzzleHttp\Client();` - Creates a new `GuzzleHttp\Client` object which will be used to make the request.
2. `$response = $client->request('GET', 'https://example.com/');` - Calls the `request` method on the `$client` object, passing in the HTTP verb (GET) and the URL to which we want to make the request.
3. `echo $response->getStatusCode();` - Echoes out the response status code.
4. `echo $response->getHeaderLine('content-type');` - Echoes out the response header line.
5. `echo $response->getBody();` - Echoes out the response body.

For more information, please refer to the [Laravel Documentation](https://laravel.com/docs/7.x/requests) and [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/).

onelinerhub: [How do I make a request in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-make-a-request-in-laravel-using-php)