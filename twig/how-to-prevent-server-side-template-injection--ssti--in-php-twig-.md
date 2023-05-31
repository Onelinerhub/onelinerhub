# How to prevent Server-Side Template Injection (SSTI) in PHP Twig?
// plain

Server-Side Template Injection (SSTI) is a type of attack that occurs when an attacker is able to inject malicious code into a web application template. To prevent SSTI in PHP Twig, it is important to use the built-in Twig escaping functions.

## Example code

```
{{ user_input|escape }}
```

## Output example

```
Escaped user input
```

The code above uses the `escape` filter to escape any user input before it is rendered in the template. This prevents malicious code from being executed.

It is also important to use the `raw` filter only when absolutely necessary, as it can be used to bypass the escaping functions.

## Helpful links
- [Twig Documentation - Escaping](https://twig.symfony.com/doc/2.x/filters/escape.html)
- [OWASP - Server-Side Template Injection](https://owasp.org/www-community/attacks/Server_Side_Template_Injection)

onelinerhub: [How to prevent Server-Side Template Injection (SSTI) in PHP Twig?](https://onelinerhub.com/twig/how-to-prevent-server-side-template-injection--ssti--in-php-twig-)