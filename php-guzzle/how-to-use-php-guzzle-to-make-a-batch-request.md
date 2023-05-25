# How to use PHP Guzzle to make a batch request?
// plain

PHP Guzzle can be used to make batch requests. This is done by creating an array of requests and passing it to the `send()` method of the `GuzzleHttp\Client` class.

```php
$client = new GuzzleHttp\Client();
$requests = [
    'req1' => $client->getAsync('http://httpbin.org/get'),
    'req2' => $client->getAsync('http://httpbin.org/get?foo=bar'),
    'req3' => $client->getAsync('http://httpbin.org/get?baz=bam')
];
$results = GuzzleHttp\Promise\unwrap($requests);
```

The output of the above code will be an array of responses:

```
Array
(
    [req1] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            [statusCode:GuzzleHttp\Psr7\Response:private] => 200
            [headers:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [Date] => Array
                        (
                            [0] => Mon, 11 May 2020 11:45:00 GMT
                        )
                    [Content-Type] => Array
                        (
                            [0] => application/json
                        )
                    [Content-Length] => Array
                        (
                            [0] => 252
                        )
                    [Connection] => Array
                        (
                            [0] => close
                        )
                    [Server] => Array
                        (
                            [0] => gunicorn/19.9.0
                        )
                )
            [headerNames:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [date] => Date
                    [content-type] => Content-Type
                    [content-length] => Content-Length
                    [connection] => Connection
                    [server] => Server
                )
            [protocol:GuzzleHttp\Psr7\Response:private] => 1.1
            [stream:GuzzleHttp\Psr7\Response:private] => GuzzleHttp\Psr7\Stream Object
                (
                    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #20
                    [size:GuzzleHttp\Psr7\Stream:private] =>
                    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
                    [readable:GuzzleHttp\Psr7\Stream:private] => 1
                    [writable:GuzzleHttp\Psr7\Stream:private] => 1
                    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
                    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                        (
                        )
                )
        )
    [req2] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            [statusCode:GuzzleHttp\Psr7\Response:private] => 200
            [headers:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [Date] => Array
                        (
                            [0] => Mon, 11 May 2020 11:45:00 GMT
                        )
                    [Content-Type] => Array
                        (
                            [0] => application/json
                        )
                    [Content-Length] => Array
                        (
                            [0] => 252
                        )
                    [Connection] => Array
                        (
                            [0] => close
                        )
                    [Server] => Array
                        (
                            [0] => gunicorn/19.9.0
                        )
                )
            [headerNames:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [date] => Date
                    [content-type] => Content-Type
                    [content-length] => Content-Length
                    [connection] => Connection
                    [server] => Server
                )
            [protocol:GuzzleHttp\Psr7\Response:private] => 1.1
            [stream:GuzzleHttp\Psr7\Response:private] => GuzzleHttp\Psr7\Stream Object
                (
                    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #21
                    [size:GuzzleHttp\Psr7\Stream:private] =>
                    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
                    [readable:GuzzleHttp\Psr7\Stream:private] => 1
                    [writable:GuzzleHttp\Psr7\Stream:private] => 1
                    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
                    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                        (
                        )
                )
        )
    [req3] => GuzzleHttp\Psr7\Response Object
        (
            [reasonPhrase:GuzzleHttp\Psr7\Response:private] => OK
            [statusCode:GuzzleHttp\Psr7\Response:private] => 200
            [headers:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [Date] => Array
                        (
                            [0] => Mon, 11 May 2020 11:45:00 GMT
                        )
                    [Content-Type] => Array
                        (
                            [0] => application/json
                        )
                    [Content-Length] => Array
                        (
                            [0] => 252
                        )
                    [Connection] => Array
                        (
                            [0] => close
                        )
                    [Server] => Array
                        (
                            [0] => gunicorn/19.9.0
                        )
                )
            [headerNames:GuzzleHttp\Psr7\Response:private] => Array
                (
                    [date] => Date
                    [content-type] => Content-Type
                    [content-length] => Content-Length
                    [connection] => Connection
                    [server] => Server
                )
            [protocol:GuzzleHttp\Psr7\Response:private] => 1.1
            [stream:GuzzleHttp\Psr7\Response:private] => GuzzleHttp\Psr7\Stream Object
                (
                    [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #22
                    [size:GuzzleHttp\Psr7\Stream:private] =>
                    [seekable:GuzzleHttp\Psr7\Stream:private] => 1
                    [readable:GuzzleHttp\Psr7\Stream:private] => 1
                    [writable:GuzzleHttp\Psr7\Stream:private] => 1
                    [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
                    [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                        (
                        )
                )
        )
)
```

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new instance of the `GuzzleHttp\Client` class.
2. `$requests = [ ... ]` - This creates an array of requests.
3. `$results = GuzzleHttp\Promise\unwrap($requests);` - This sends the requests and returns an array of responses.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to use PHP Guzzle to make a batch request?](https://onelinerhub.com/php-guzzle/how-to-use-php-guzzle-to-make-a-batch-request)