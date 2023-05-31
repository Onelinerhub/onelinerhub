# How to prevent Template Injection in PHP Twig?
// plain

Template Injection in PHP Twig can be prevented by using the `autoescape` tag. This tag will automatically escape any variables that are passed to the template. For example:

```
{% autoescape true %}
    {{ user_input }}
{% endautoescape %}
```

This will output the user input as escaped HTML, preventing any malicious code from being executed.

Additionally, the `raw` tag can be used to prevent any escaping of variables. For example:

```
{% raw %}
    {{ user_input }}
{% endraw %}
```

This will output the user input as is, without any escaping.

- `autoescape` tag: Automatically escapes any variables passed to the template.
- `raw` tag: Prevents any escaping of variables.

## Helpful links
- [Twig Documentation - Autoescape](https://twig.symfony.com/doc/2.x/tags/autoescape.html)
- [Twig Documentation - Raw](https://twig.symfony.com/doc/2.x/tags/raw.html)

onelinerhub: [How to prevent Template Injection in PHP Twig?](https://onelinerhub.com/twig/how-to-prevent-template-injection-in-php-twig-)