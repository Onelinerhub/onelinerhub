# How to get the user agent in PHP Twig?
// plain

The user agent can be obtained in PHP Twig using the `app.request.server.get('HTTP_USER_AGENT')` method.

## Example code

```
{{ app.request.server.get('HTTP_USER_AGENT') }}
```

## Output example

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
```

## Code explanation

- `app.request`: This is an object that contains information about the current request.
- `server`: This is a property of the `app.request` object that contains information about the server environment.
- `get('HTTP_USER_AGENT')`: This is a method of the `server` object that returns the user agent string.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to get the user agent in PHP Twig?](https://onelinerhub.com/twig/how-to-get-the-user-agent-in-php-twig-)