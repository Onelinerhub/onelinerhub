# How to get the current URL in PHP Symfony?
// plain

The current URL in PHP Symfony can be obtained using the `getPathInfo()` method of the `Request` object.

## Example code

```
$request = Request::createFromGlobals();
$currentUrl = $request->getPathInfo();
```

## Output example

```
/current/url
```

## Code explanation

- `Request::createFromGlobals()`: creates a new Request object from the PHP global variables.
- `getPathInfo()`: returns the path being requested relative to the executed script.

## Helpful links
- [Request class](https://api.symfony.com/4.4/Symfony/Component/HttpFoundation/Request.html)

onelinerhub: [How to get the current URL in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-get-the-current-url-in-php-symfony)