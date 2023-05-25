# How to use form data with PHP Guzzle?
// plain

Using PHP Guzzle to work with form data is quite simple.

```php
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
3. `'form_params' => [` - This is an array containing the form data to be sent.
4. `'field_name' => 'abc',` - This is an example of a field name and value pair.
5. `'nested_field' => [` - This is an example of a nested field.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Form Data with Guzzle](https://www.sitepoint.com/sending-form-data-with-guzzle/)

onelinerhub: [How to use form data with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-use-form-data-with-php-guzzle)