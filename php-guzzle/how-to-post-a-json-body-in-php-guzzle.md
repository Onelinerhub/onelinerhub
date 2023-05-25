# How to post a JSON body in PHP Guzzle?
// plain

Posting a JSON body in PHP Guzzle is easy. You can use the `json` option in the request options array to set the body of the request.

```php
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://example.com/api/v1/users', [
    'json' => [
        'name' => 'John Doe',
        'email' => 'john@example.com'
    ]
]);
```

The output of the above code will be a `GuzzleHttp\Psr7\Response` object.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client.
2. `$response = $client->request('POST', 'http://example.com/api/v1/users', [` - This sends a POST request to the specified URL.
3. `'json' => [` - This sets the body of the request to a JSON object.
4. `'name' => 'John Doe',` - This sets the name field of the JSON object.
5. `'email' => 'john@example.com'` - This sets the email field of the JSON object.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)

onelinerhub: [How to post a JSON body in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-post-a-json-body-in-php-guzzle)