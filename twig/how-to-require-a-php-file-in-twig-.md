# How to require a PHP file in Twig?
// plain

Twig is a templating language for PHP, and it is possible to require a PHP file in Twig. To do this, you can use the `include` tag. This tag takes a single argument, which is the path to the PHP file you want to include.

```
{% include 'path/to/file.php' %}
```

The `include` tag will execute the PHP code in the file and return the output.

- `include` tag: This tag is used to include a PHP file in Twig.
- `path/to/file.php`: This is the path to the PHP file you want to include.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to require a PHP file in Twig?](https://onelinerhub.com/twig/how-to-require-a-php-file-in-twig-)