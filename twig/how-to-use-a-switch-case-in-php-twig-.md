# How to use a switch case in PHP Twig?
// plain

Switch case statements are a powerful tool for controlling the flow of a program. In PHP Twig, switch case statements can be used to control the flow of a template.

## Example code

```
{% switch variable %}
    {% case "value1" %}
        <p>The value is value1.</p>
    {% case "value2" %}
        <p>The value is value2.</p>
    {% default %}
        <p>The value is something else.</p>
{% endswitch %}
```

## Output example

```
The value is value1.
```

## Code explanation

- `{% switch variable %}`: This is the start of the switch statement. The `variable` is the variable that will be evaluated.
- `{% case "value1" %}`: This is the first case statement. If the `variable` is equal to `value1`, the code between this statement and the next `case` statement will be executed.
- `{% default %}`: This is the default case statement. If none of the `case` statements are true, the code between this statement and the `endswitch` statement will be executed.
- `{% endswitch %}`: This is the end of the switch statement.

## Helpful links
- [Twig Documentation - Control Structures](https://twig.symfony.com/doc/2.x/templates.html#control-structures)

onelinerhub: [How to use a switch case in PHP Twig?](https://onelinerhub.com/twig/how-to-use-a-switch-case-in-php-twig-)