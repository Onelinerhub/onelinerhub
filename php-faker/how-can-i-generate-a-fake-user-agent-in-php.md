# How can I generate a fake user agent in PHP?
// plain

You can generate a fake user agent in PHP using the `get_browser()` function. This function will return an object containing information about the user's browser, including the user agent string.

## Example code

```php
$browser = get_browser();
echo $browser->user_agent;
```

## Output example

```
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
```

## Code explanation


- `get_browser()`: This is the main function used to generate the fake user agent. It returns an object containing information about the user's browser.
- `$browser`: This is a variable used to store the object returned by `get_browser()`.
- `echo $browser->user_agent;`: This is used to output the user agent string.

## Helpful links

- [get_browser()](https://www.php.net/manual/en/function.get-browser.php)
- [User Agent Strings](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

onelinerhub: [How can I generate a fake user agent in PHP?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-user-agent-in-php)