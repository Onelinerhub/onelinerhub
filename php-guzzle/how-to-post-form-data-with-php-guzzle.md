# How to post form data with PHP Guzzle?
// plain

Posting form data with PHP Guzzle is easy and straightforward.

```
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://httpbin.org/post', [
    'form_params' => [
        'field_name' => 'abc',
        'other_field' => '123',
        'nested_field' => [
            'nested' => 'hello'
        ]
    ]
]);
```

The output of the above code will be a response object containing the response from the server.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.
2. `$response = $client->request('POST', 'http://httpbin.org/post', [` - This sends a POST request to the specified URL.
3. `'form_params' => [` - This is an array containing the form parameters to be sent with the request.
4. `'field_name' => 'abc',` - This is an example of a form parameter, in this case a field named 'field_name' with a value of 'abc'.
5. `]);` - This closes the array of form parameters and the request.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [HTTP POST Request with Guzzle](https://www.codementor.io/@juliangut/how-to-make-http-requests-with-guzzle-php-5-6-3hc5nh6ti)

onelinerhub: [How to post form data with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-post-form-data-with-php-guzzle)