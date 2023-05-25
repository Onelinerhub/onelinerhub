# How to add an authorization header in PHP Guzzle?
// plain

Adding an authorization header in PHP Guzzle is a simple process.

```
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'http://httpbin.org/get', [
    'headers' => [
        'Authorization' => 'Bearer YOUR_TOKEN_HERE'
    ]
]);
```

The output of the above code will be a response object containing the response from the server.

The code consists of the following parts:

1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.
2. `$res = $client->request('GET', 'http://httpbin.org/get', [` - This sends a GET request to the specified URL.
3. `'headers' => [` - This is an array of headers to be sent with the request.
4. `'Authorization' => 'Bearer YOUR_TOKEN_HERE'` - This sets the Authorization header with the specified token.
5. `]);` - This closes the array of headers and the request method.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [HTTP Authorization Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)

onelinerhub: [How to add an authorization header in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-an-authorization-header-in-php-guzzle)