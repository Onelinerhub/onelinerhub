# How to access the request object in PHP Symfony?
// plain

The request object in PHP Symfony can be accessed using the `getRequest()` method of the `Controller` class.

```php
$request = $this->getRequest();
```

The `getRequest()` method returns an instance of the `Request` class which contains all the information about the request. This includes the request parameters, headers, cookies, etc.

## Code explanation


- `$this`: This is an instance of the `Controller` class.
- `getRequest()`: This is a method of the `Controller` class which returns an instance of the `Request` class.

## Helpful links

- [Symfony Documentation - Controller](https://symfony.com/doc/current/controller.html)
- [Symfony Documentation - Request](https://symfony.com/doc/current/components/http_foundation/introduction.html)

onelinerhub: [How to access the request object in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-access-the-request-object-in-php-symfony)