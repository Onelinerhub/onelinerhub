# How to trim a string in PHP Twig?
// plain

Trimming a string in PHP Twig is a simple task. You can use the `trim` filter to remove whitespace from the beginning and end of a string.

For example:
```
{{ '  Hello World  '|trim }}
```

## Output example

```
Hello World
```

The `trim` filter takes two optional parameters: `character_mask` and `side`.

- `character_mask`: A list of characters to be stripped.
- `side`: Specifies which side of the string to trim. Possible values are `left`, `right`, or `both` (default).

## Helpful links
- [Twig Filters](https://twig.symfony.com/doc/2.x/filters/trim.html)

onelinerhub: [How to trim a string in PHP Twig?](https://onelinerhub.com/twig/how-to-trim-a-string-in-php-twig-)