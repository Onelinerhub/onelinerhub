# How to make a GET request with a Guzzle client in PHP?
// plain

Making a GET request with a Guzzle client in PHP is easy. Here is an example code block:

```
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'https://api.github.com/user', [
    'auth' => ['user', 'pass']
]);
echo $res->getStatusCode();
```

The output of the example code is `200`.

## Code explanation


1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client.
2. `$res = $client->request('GET', 'https://api.github.com/user', [` - This makes a GET request to the specified URL.
3. `'auth' => ['user', 'pass']` - This is an optional parameter that allows you to specify authentication credentials.
4. `echo $res->getStatusCode();` - This prints out the response status code.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [Guzzle GitHub Repository](https://github.com/guzzle/guzzle)

onelinerhub: [How to make a GET request with a Guzzle client in PHP?](https://onelinerhub.com/php-guzzle/how-to-make-a-get-request-with-a-guzzle-client-in-php)