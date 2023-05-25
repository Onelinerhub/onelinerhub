# How to add a bearer token in PHP Guzzle?
// plain

Adding a bearer token in PHP Guzzle is a simple process.

```
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com', [
    'headers' => [
        'Authorization' => 'Bearer {token}',
    ],
]);
```

The output of the above code will be the response from the server.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client.
2. `$response = $client->request('GET', 'http://example.com', [` - This sends a GET request to the specified URL.
3. `'headers' => [` - This is the headers array which contains the authorization header.
4. `'Authorization' => 'Bearer {token}',` - This is the authorization header which contains the bearer token.
5. `]);` - This closes the headers array and the request.

No relevant links.

onelinerhub: [How to add a bearer token in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-add-a-bearer-token-in-php-guzzle)