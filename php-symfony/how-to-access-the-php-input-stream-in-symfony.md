# How to access the PHP input stream in Symfony?
// plain

The PHP input stream can be accessed in Symfony using the `getContent()` method of the `Request` object.

## Example code

```
$request = Request::createFromGlobals();
$inputStream = $request->getContent();
```

The `getContent()` method returns the raw request body, which is the input stream.

## Code explanation

- `Request::createFromGlobals()`: creates a new Request object from the PHP global variables
- `getContent()`: returns the raw request body, which is the input stream

## Helpful links
- [Request class documentation](https://symfony.com/doc/current/components/http_foundation/introduction.html#the-request-class)

onelinerhub: [How to access the PHP input stream in Symfony?](https://onelinerhub.com/php-symfony/how-to-access-the-php-input-stream-in-symfony)