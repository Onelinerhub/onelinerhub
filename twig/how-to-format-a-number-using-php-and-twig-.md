# How to format a number using PHP and Twig?
// plain

Using PHP and Twig, you can format a number to a specific format. For example, you can use the `number_format` function to format a number with a specific number of decimal places. The following code block shows an example of how to use `number_format` to format a number with two decimal places:

```
<?php
$number = 1234.5678;
echo number_format($number, 2);
```

The output of the above code would be `1,234.57`.

The `number_format` function takes two parameters:

1. `$number`: The number to be formatted.
2. `$decimals`: The number of decimal places to be used.

For more information, see the [PHP documentation for number_format](https://www.php.net/manual/en/function.number-format.php).

onelinerhub: [How to format a number using PHP and Twig?](https://onelinerhub.com/twig/how-to-format-a-number-using-php-and-twig-)