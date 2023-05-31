# How to loop through an array in Twig and PHP?
// plain

Looping through an array in Twig and PHP is a common task. The following example code block shows how to loop through an array in Twig and PHP:

```
{% for item in array %}
    {{ item }}
{% endfor %}
```

The output of the above code would be the items in the array, each on a new line.

## Code explanation


- `{% for item in array %}`: This is the start of the loop. It declares a variable `item` which will be used to refer to each item in the array.
- `{{ item }}`: This is the code that will be executed for each item in the array. In this case, it will print the item.
- `{% endfor %}`: This is the end of the loop.

## Helpful links

- [Twig for Template Designers](https://twig.symfony.com/doc/2.x/templates.html)
- [PHP Arrays](https://www.php.net/manual/en/language.types.array.php)

onelinerhub: [How to loop through an array in Twig and PHP?](https://onelinerhub.com/twig/how-to-loop-through-an-array-in-twig-and-php-)