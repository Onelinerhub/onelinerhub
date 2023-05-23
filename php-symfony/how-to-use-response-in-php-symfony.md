# How to use Response in PHP Symfony?
// plain

Using Response in PHP Symfony is easy. You can create a Response object with the `Response` class.

```php
$response = new Response('Hello World', 200);
```

The Response object can then be sent to the browser with the `send()` method.

```php
$response->send();
```

The Response class has several methods that can be used to modify the response:

- `setContent()`: Sets the response content
- `setStatusCode()`: Sets the response status code
- `setCharset()`: Sets the response charset
- `headers->set()`: Sets a response header

You can find more information about the Response class in the [Symfony documentation](https://symfony.com/doc/current/components/http_foundation.html#response).

onelinerhub: [How to use Response in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-response-in-php-symfony)