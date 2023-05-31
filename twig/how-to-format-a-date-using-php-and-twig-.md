# How to format a date using PHP and Twig?
// plain

Using PHP and Twig, you can format a date in a variety of ways. The following example code block will output the current date in the format of "Month Day, Year":

```
{{ "now"|date("F j, Y") }}
```

## Output example


```
July 15, 2020
```

The code block consists of three parts:

1. `{{ "now"|date("F j, Y") }}` - This is the Twig syntax for formatting a date. The `"now"` part is the date that you want to format, in this case the current date. The `date()` part is the Twig filter that formats the date. The `"F j, Y"` part is the format that you want to use.

2. `F` - This is the format for the month. `F` stands for full textual representation of a month, such as January or March.

3. `j` - This is the format for the day. `j` stands for day of the month without leading zeros, such as 1 or 15.

4. `Y` - This is the format for the year. `Y` stands for a full numeric representation of a year, such as 2020.

For more information on formatting dates with PHP and Twig, see the following links:

- [Twig Date Formatting](https://twig.symfony.com/doc/2.x/filters/date.html)
- [PHP Date Formatting](https://www.php.net/manual/en/function.date.php)

onelinerhub: [How to format a date using PHP and Twig?](https://onelinerhub.com/twig/how-to-format-a-date-using-php-and-twig-)