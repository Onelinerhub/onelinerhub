# How to set headers in PHP Symfony?
// plain

In PHP Symfony, headers can be set using the `Response` class.

## Example code

```php
use Symfony\Component\HttpFoundation\Response;

$response = new Response();
$response->headers->set('Content-Type', 'application/json');
$response->headers->set('X-Custom-Header', 'MyValue');
```

The code above sets two headers: `Content-Type` and `X-Custom-Header`.

The `Response` class has a `headers` property which is an instance of `HeaderBag`. The `HeaderBag` class has a `set` method which takes two parameters: the header name and the header value.

## Helpful links

- [Symfony Response Class](https://symfony.com/doc/current/components/http_foundation/introduction.html#the-response-class)
- [Symfony HeaderBag Class](https://symfony.com/doc/current/components/http_foundation/introduction.html#the-headerbag-class)

onelinerhub: [How to set headers in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-set-headers-in-php-symfony)