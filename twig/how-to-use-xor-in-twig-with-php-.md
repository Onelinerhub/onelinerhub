# How to use XOR in Twig with PHP?
// plain

XOR (Exclusive OR) is a logical operator in Twig that can be used to compare two values and return a boolean result. It is similar to the OR operator, but it only returns true if one of the values is true and the other is false.

## Example code

```
{% if (value1 XOR value2) %}
    <p>One of the values is true and the other is false.</p>
{% endif %}
```

## Output example

```
One of the values is true and the other is false.
```

## Code explanation

- `value1` and `value2`: two values to be compared
- `XOR`: the XOR operator
- `if`: the Twig conditional statement

## Helpful links
- [Twig Documentation - Logical Operators](https://twig.symfony.com/doc/2.x/templates.html#logical-operators)

onelinerhub: [How to use XOR in Twig with PHP?](https://onelinerhub.com/twig/how-to-use-xor-in-twig-with-php-)