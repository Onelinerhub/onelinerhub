# How to check if a string contains a substring in PHP Twig?
// plain

You can check if a string contains a substring in PHP Twig using the `contains` filter.

```
{% if 'Hello World'|contains('World') %}
    The string contains the substring.
{% endif %}
```

The output of the above code will be:

```
The string contains the substring.
```

The code consists of the following parts:

1. `{% if 'Hello World'|contains('World') %}` - This part checks if the string `Hello World` contains the substring `World`.
2. `The string contains the substring.` - This part is the output of the code.

## Helpful links

1. [Twig Filters](https://twig.symfony.com/doc/2.x/filters/index.html)
2. [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to check if a string contains a substring in PHP Twig?](https://onelinerhub.com/twig/how-to-check-if-a-string-contains-a-substring-in-php-twig-)