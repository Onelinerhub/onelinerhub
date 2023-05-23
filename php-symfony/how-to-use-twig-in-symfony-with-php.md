# How to use Twig in Symfony with PHP?
// plain

Twig is a templating language used in Symfony with PHP. It is used to create dynamic webpages with HTML, CSS, and JavaScript.

## Example code

```
{% extends 'base.html.twig' %}

{% block body %}
    <h1>Hello {{ name }}!</h1>
{% endblock %}
```

## Output example

```
<h1>Hello [name]!</h1>
```

## Code explanation

- `{% extends 'base.html.twig' %}`: This line tells Twig to use the base.html.twig file as the base template.
- `{% block body %}`: This line defines a block of code that can be overridden in a child template.
- `<h1>Hello {{ name }}!</h1>`: This line prints out a greeting with the name variable.
- `{% endblock %}`: This line closes the block of code.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Symfony Documentation](https://symfony.com/doc/current/index.html)

onelinerhub: [How to use Twig in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-use-twig-in-symfony-with-php)