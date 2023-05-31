# How to use Twig in PHP to get the current year?
// plain

Twig is a templating engine for PHP that allows you to easily create and manipulate HTML, XML, and other markup languages. To get the current year using Twig in PHP, you can use the `date` filter.

```
{{ "now"|date("Y") }}
```

This will output the current year, for example:

```
2020
```

The code above consists of two parts:

1. `{{ "now"|date("Y") }}` - This is the Twig code that will be evaluated. The `"now"` string is passed to the `date` filter, which will format it according to the format string `"Y"` (which stands for year).

2. `date("Y")` - This is the PHP code that will be executed. The `date` function takes a format string as an argument and returns a string representing the current date and time in the specified format. In this case, the format string is `"Y"`, which will return the current year.

For more information, see the [Twig documentation](https://twig.symfony.com/doc/2.x/filters/date.html) and the [PHP documentation](https://www.php.net/manual/en/function.date.php).

onelinerhub: [How to use Twig in PHP to get the current year?](https://onelinerhub.com/twig/how-to-use-twig-in-php-to-get-the-current-year-)