# How to check a checkbox using PHP and Twig?
// plain

Using PHP and Twig, you can check a checkbox by setting the `checked` attribute to `true` in the HTML element.

## Example code

```
<input type="checkbox" {{ checked ? 'checked' : '' }}>
```

## Output example

```
<input type="checkbox" checked>
```

The code above uses the ternary operator to check if the `checked` variable is true. If it is, the `checked` attribute is added to the HTML element, otherwise it is left blank.

Parts of the code:
- `<input type="checkbox">`: HTML element for the checkbox
- `{{ checked ? 'checked' : '' }}`: ternary operator to check if the `checked` variable is true
- `checked`: variable that holds the value of whether the checkbox should be checked or not

## Helpful links
- [Twig documentation](https://twig.symfony.com/doc/2.x/)
- [PHP documentation](https://www.php.net/manual/en/index.php)

onelinerhub: [How to check a checkbox using PHP and Twig?](https://onelinerhub.com/twig/how-to-check-a-checkbox-using-php-and-twig-)