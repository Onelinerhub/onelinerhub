# How to get request parameters in PHP Symfony?
// plain

Request parameters in PHP Symfony can be accessed using the `$request->query->get()` method.

## Example code

```
$name = $request->query->get('name');
```

## Output example

```
$name = 'John Doe';
```

The code above will get the value of the `name` parameter from the request.

The `$request` variable is an instance of `Symfony\Component\HttpFoundation\Request` class. The `query` property is an instance of `Symfony\Component\HttpFoundation\ParameterBag` class. The `get()` method is used to get the value of the parameter from the request.

## Helpful links

- [Symfony - How to Get Request Parameters](https://symfony.com/doc/current/controller/request_parameters.html)
- [Symfony - The Request object](https://symfony.com/doc/current/components/http_foundation/introduction.html#the-request-object)

onelinerhub: [How to get request parameters in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-get-request-parameters-in-php-symfony)