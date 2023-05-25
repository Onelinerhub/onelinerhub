# How to use multipart/form-data with PHP Guzzle?
// plain

Using multipart/form-data with PHP Guzzle is easy. Here is an example code block to demonstrate how to do it:
```
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://httpbin.org/post', [
    'multipart' => [
        [
            'name'     => 'field_name',
            'contents' => 'abc'
        ],
        [
            'name'     => 'file_name',
            'contents' => fopen('/path/to/file', 'r')
        ]
    ]
]);
```
The output of the example code will be a response object containing the data sent in the request.

## Code explanation

- `$client = new GuzzleHttp\Client();` - creates a new Guzzle client object
- `$response = $client->request('POST', 'http://httpbin.org/post', [` - sends a POST request to the specified URL
- `'multipart' => [` - specifies that the request should use multipart/form-data
- `[` - starts an array of data to be sent in the request
- `'name'     => 'field_name',` - specifies the name of the field
- `'contents' => 'abc'` - specifies the contents of the field
- `fopen('/path/to/file', 'r')` - opens the file to be sent in the request
- `]);` - ends the array of data to be sent in the request

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [PHP Manual - fopen](https://www.php.net/manual/en/function.fopen.php)

onelinerhub: [How to use multipart/form-data with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-use-multipart-form-data-with-php-guzzle)