# How to set the content-length for a Guzzle request in PHP?
// plain

The content-length of a Guzzle request in PHP can be set by using the `setBody` method.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://httpbin.org/post', [
    'body' => 'Hello World',
    'headers' => [
        'Content-Length' => 11
    ]
]);
```

The output of the above code will be a response object.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.
2. `$response = $client->request('POST', 'http://httpbin.org/post', [` - This sends a POST request to the specified URL.
3. `'body' => 'Hello World',` - This sets the body of the request to the string `Hello World`.
4. `'headers' => [` - This sets the headers of the request.
5. `'Content-Length' => 11` - This sets the content-length of the request to 11.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to set the content-length for a Guzzle request in PHP?](https://onelinerhub.com/php-guzzle/how-to-set-the-content-length-for-a-guzzle-request-in-php)