# How to handle whitespace in Twig with PHP 7.4?
// plain

Twig is a templating language for PHP 7.4 that allows developers to write concise and readable code. Whitespace in Twig can be handled by using the `spaceless` tag. This tag removes all whitespace between HTML tags, making the output more compact.

```
{% spaceless %}
  <div>
    <p>Hello World!</p>
  </div>
{% endspaceless %}
```

## Output example

```
<div><p>Hello World!</p></div>
```

## Code explanation

- `{% spaceless %}`: This tag marks the beginning of the block of code that will have whitespace removed.
- `<div>`: This is an HTML tag that will be affected by the `spaceless` tag.
- `<p>Hello World!</p>`: This is an HTML tag that will be affected by the `spaceless` tag.
- `{% endspaceless %}`: This tag marks the end of the block of code that will have whitespace removed.

## Helpful links
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)
- [Twig Spaceless Tag](https://twig.symfony.com/doc/2.x/tags/spaceless.html)

onelinerhub: [How to handle whitespace in Twig with PHP 7.4?](https://onelinerhub.com/twig/how-to-handle-whitespace-in-twig-with-php-7.4-)