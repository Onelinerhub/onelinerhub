# How to use the 'for' loop with PHP and Twig?
// plain

The `for` loop is a powerful tool for iterating over a set of data in PHP and Twig. It allows you to execute a block of code for each item in a set of data.

## Example code

```
{% for item in items %}
  <p>{{ item }}</p>
{% endfor %}
```

## Output example

```
<p>Item 1</p>
<p>Item 2</p>
<p>Item 3</p>
```

## Code explanation

- `for`: the keyword used to start the loop
- `item`: the variable used to store the current item in the loop
- `items`: the set of data being looped over
- `endfor`: the keyword used to end the loop

## Helpful links
- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html#for-tags)
- [PHP for Loops](https://www.php.net/manual/en/control-structures.for.php)

onelinerhub: [How to use the 'for' loop with PHP and Twig?](https://onelinerhub.com/twig/how-to-use-the--for--loop-with-php-and-twig-)