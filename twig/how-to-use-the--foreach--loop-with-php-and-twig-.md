# How to use the 'foreach' loop with PHP and Twig?
// plain

The `foreach` loop is a powerful tool in PHP and Twig for iterating over arrays and objects. It allows you to loop through each item in an array or object and perform an action on it.

## Example code

```
{% for item in items %}
    {{ item }}
{% endfor %}
```

## Output example

```
item1
item2
item3
```

## Code explanation

- `for`: This is the keyword used to start the loop.
- `item`: This is the variable used to store the current item in the loop.
- `in`: This is the keyword used to specify the array or object to loop through.
- `items`: This is the array or object to loop through.
- `endfor`: This is the keyword used to end the loop.

## Helpful links
- [Twig Documentation - For Tag](https://twig.symfony.com/doc/2.x/tags/for.html)
- [PHP Documentation - Foreach](https://www.php.net/manual/en/control-structures.foreach.php)

onelinerhub: [How to use the 'foreach' loop with PHP and Twig?](https://onelinerhub.com/twig/how-to-use-the--foreach--loop-with-php-and-twig-)