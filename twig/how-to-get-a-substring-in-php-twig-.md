# How to get a substring in PHP Twig?
// plain

Substrings can be obtained in PHP Twig using the `slice` filter. This filter takes two parameters, `start` and `length`, and returns a substring of the given string starting from the `start` index and with the given `length`.

```
{{ 'Hello World'|slice(6, 5) }}
```

## Output example

```
World
```

The `slice` filter takes two parameters:
- `start`: The index of the first character of the substring.
- `length`: The length of the substring.

## Helpful links
- [Twig Filters](https://twig.symfony.com/doc/2.x/filters/slice.html)

onelinerhub: [How to get a substring in PHP Twig?](https://onelinerhub.com/twig/how-to-get-a-substring-in-php-twig-)