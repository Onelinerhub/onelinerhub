# How to upload a file with PHP Guzzle?
// plain

Using PHP Guzzle, you can upload a file with a POST request. The following example code will upload a file to a server:

```
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://example.com/upload', [
    'multipart' => [
        [
            'name'     => 'file',
            'contents' => fopen('/path/to/file', 'r')
        ]
    ]
]);
```

The output of the above code will be a response object containing the response from the server.

The code consists of the following parts:

1. Creating a new Guzzle client: `$client = new GuzzleHttp\Client();`
2. Sending a POST request to the server: `$response = $client->request('POST', 'http://example.com/upload', [`
3. Specifying the file to upload: `'multipart' => [ [ 'name' => 'file', 'contents' => fopen('/path/to/file', 'r') ] ]`
4. Storing the response from the server: `$response = $client->request('POST', 'http://example.com/upload', [`

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [PHP Guzzle Tutorial](https://www.cloudways.com/blog/guzzle-php-rest-api-client/)

onelinerhub: [How to upload a file with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-upload-a-file-with-php-guzzle)