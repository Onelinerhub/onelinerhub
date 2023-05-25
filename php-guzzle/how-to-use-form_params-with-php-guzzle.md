# How to use form_params with PHP Guzzle?
// plain

Using form_params with PHP Guzzle is a simple process.

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

The output of the above code will be a response object.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.
2. `$response = $client->request('POST', 'http://httpbin.org/post', [` - This sends a POST request to the specified URL.
3. `'form_params' => [` - This is the form_params array which contains the data to be sent in the request.
4. `'field_name' => 'abc',` - This is an example of a key-value pair in the form_params array.
5. `'nested_field' => [` - This is an example of a nested array in the form_params array.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Form Parameters](http://docs.guzzlephp.org/en/stable/request-options.html#form-params)

onelinerhub: [How to use form_params with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-use-form_params-with-php-guzzle)