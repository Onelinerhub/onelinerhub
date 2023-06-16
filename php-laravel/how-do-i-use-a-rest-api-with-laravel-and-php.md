# How do I use a REST API with Laravel and PHP?
// plain

Using a REST API with Laravel and PHP is quite simple. The following example shows how to use Guzzle, a PHP HTTP client, to make a GET request to a REST API.

```php
// create a client
$client = new \GuzzleHttp\Client();

// make the request
$response = $client->request('GET', 'https://example.com/api/endpoint');

// get the response body
$body = $response->getBody();

// output the response
echo $body;
```

The response from the API will be outputted to the screen. You can also use the response to manipulate data, such as saving it to a database or displaying it on a page.

The example above is just one way to use a REST API with Laravel and PHP. There are other libraries available such as [Requests](http://requests.ryanmccue.info/) and [Guzzle](http://docs.guzzlephp.org/en/latest/).

For more information, see the following links:

- [Laravel Documentation - HTTP Client](https://laravel.com/docs/7.x/http-client)
- [Guzzle Documentation](http://docs.guzzlephp.org/en/latest/)
- [Requests Documentation](http://requests.ryanmccue.info/)

onelinerhub: [How do I use a REST API with Laravel and PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-a-rest-api-with-laravel-and-php)