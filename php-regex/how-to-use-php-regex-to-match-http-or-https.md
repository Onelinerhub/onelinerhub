# How to use PHP regex to match http or https?
// plain

The following example code uses PHP regex to match http or https:

```
$url = "https://www.example.com";

if (preg_match("/^(http|https):\/\/.*/", $url)) {
    echo "URL matches http or https";
}
```

## Output example

```
URL matches http or https
```

## Code explanation


1. `$url = "https://www.example.com";` - This line assigns the value of the URL to the variable `$url`.
2. `if (preg_match("/^(http|https):\/\/.*/", $url)) {` - This line uses the `preg_match()` function to check if the URL matches the regular expression `/^(http|https):\/\/.*/`. The `^` character indicates the start of the string, the `(http|https)` part matches either `http` or `https`, the `:\/\/` part matches the `://` part of the URL, and the `.*` part matches any character (including none) until the end of the string.
3. `echo "URL matches http or https";` - This line prints out the message `URL matches http or https` if the URL matches the regular expression.

## Helpful links

- [PHP preg_match() Function](https://www.w3schools.com/php/func_preg_match.asp)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to use PHP regex to match http or https?](https://onelinerhub.com/php-regex/how-to-use-php-regex-to-match-http-or-https)