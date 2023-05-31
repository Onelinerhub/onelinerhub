# How to utiliser PHP in Twig?
// plain

Twig is a templating language for PHP, which allows developers to write concise and readable code. It is possible to use PHP in Twig by using the `{% set %}` tag. This tag allows you to set a variable in Twig, which can then be used in the template.

## Example code

```
{% set myVar = 'Hello World' %}
{{ myVar }}
```

## Output example

```
Hello World
```

## Code explanation

- `{% set %}`: This tag is used to set a variable in Twig.
- `myVar`: This is the name of the variable being set.
- `'Hello World'`: This is the value of the variable being set.
- `{{ myVar }}`: This is how the variable is used in the template.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)

onelinerhub: [How to utiliser PHP in Twig?](https://onelinerhub.com/twig/how-to-utiliser-php-in-twig-)