# PHP Guzzle post request example
// plain

Guzzle is a PHP HTTP client that makes it easy to send HTTP requests and trivial to integrate with web services. Here is an example of a POST request using Guzzle:

```
<?php
$client = new GuzzleHttp\Client();
$res = $client->request('POST', 'http://httpbin.org/post', [
    'form_params' => [
        'field_name' => 'abc',
        'other_field' => '123',
        'nested_field' => [
            'nested' => 'hello'
        ]
    ]
]);
echo $res->getStatusCode();
// 200
echo $res->getHeaderLine('content-type');
// 'application/json; charset=utf8'
echo $res->getBody();
// '{"type":"User"...'
?>
```

The code above will send a POST request to the URL `http://httpbin.org/post` with the form parameters `field_name`, `other_field`, and `nested_field`. The response will be a status code of `200` and a `content-type` header of `application/json; charset=utf8`. The body of the response will be a JSON string.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.
2. `$res = $client->request('POST', 'http://httpbin.org/post', [` - This sends a POST request to the URL `http://httpbin.org/post` with the form parameters.
3. `'form_params' => [` - This is the array of form parameters that will be sent with the request.
4. `echo $res->getStatusCode();` - This will output the status code of the response.
5. `echo $res->getHeaderLine('content-type');` - This will output the content-type header of the response.
6. `echo $res->getBody();` - This will output the body of the response.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [HTTPBin](https://httpbin.org/)

onelinerhub: [PHP Guzzle post request example](https://onelinerhub.com/php-guzzle/php-guzzle-post-request-example)