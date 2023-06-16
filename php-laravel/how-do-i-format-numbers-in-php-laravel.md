# How do I format numbers in PHP Laravel?
// plain

The most common way to format numbers in PHP Laravel is to use the `number_format()` function. This function allows you to specify a number of decimal places, a decimal point, and a thousands separator. Here is an example of how to use it:

```
$number = 123456.789;
echo number_format($number, 2, '.', ',');
```

The output of this code would be:

```
123,456.79
```

The `number_format()` function takes four parameters:

1. `$number`: The number to be formatted
2. `$decimals`: The number of decimal places to include
3. `$dec_point`: The character to use as a decimal point
4. `$thousands_sep`: The character to use as a thousands separator

You can also use the `format_number()` helper function provided by Laravel. This function takes the same four parameters as `number_format()`.

For more information, see the [Number Formatting](https://laravel.com/docs/7.x/helpers#method-number-format) section of the Laravel documentation.

onelinerhub: [How do I format numbers in PHP Laravel?](https://onelinerhub.com/php-laravel/how-do-i-format-numbers-in-php-laravel)