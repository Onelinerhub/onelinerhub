# How do I make a POST request using PHP Laravel?
// plain

Making a POST request using PHP Laravel is easy. The following example code block shows a basic POST request:

```
$client = new \GuzzleHttp\Client();
$response = $client->request('POST', 'http://example.com/api/endpoint', [
    'form_params' => [
        'param1' => 'value1',
        'param2' => 'value2'
    ]
]);
```

## Code explanation


- `$client = new \GuzzleHttp\Client();`: Instantiate a new `GuzzleHttp\Client` object, which is used to make the request.

- `$response = $client->request('POST', 'http://example.com/api/endpoint', [`: Make the POST request to the specified endpoint.

- `'form_params' => [`: Specify the parameters to be sent in the POST request.

- `'param1' => 'value1',`: Specify the first parameter, with its corresponding value.

- `'param2' => 'value2'`: Specify the second parameter, with its corresponding value.

- `]);`: Close the array of parameters.

For more information, please refer to the following links:

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Laravel Documentation](https://laravel.com/docs/5.7/requests)

onelinerhub: [How do I make a POST request using PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-make-a-post-request-using-php-laravel)