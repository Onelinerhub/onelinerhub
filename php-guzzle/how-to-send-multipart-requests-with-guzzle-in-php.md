# How to send multipart requests with Guzzle in PHP?
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. To send a multipart request with Guzzle, you need to create a `multipart/form-data` request.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://httpbin.org/post', [
    'multipart' => [
        [
            'name'     => 'field_name',
            'contents' => 'abc'
        ],
        [
            'name'     => 'other_field',
            'contents' => '123'
        ],
        [
            'name'     => 'file_name',
            'contents' => fopen('/path/to/file', 'r')
        ]
    ]
]);
```

The output of the example code will be a response object containing the response from the server.

Parts of the code:

- `$client = new GuzzleHttp\Client();`: creates a new Guzzle client.
- `$response = $client->request('POST', 'http://httpbin.org/post', [`: sends a POST request to the specified URL.
- `'multipart' => [`: specifies that the request should be a multipart request.
- `[`: starts an array containing the fields and files to be sent.
- `'name' => 'field_name',`: specifies the name of the field.
- `'contents' => 'abc'`: specifies the contents of the field.
- `fopen('/path/to/file', 'r')`: opens the file to be sent.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Sending Multipart Requests with Guzzle](https://www.sitepoint.com/sending-multipart-requests-with-guzzle/)

onelinerhub: [How to send multipart requests with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-send-multipart-requests-with-guzzle-in-php)