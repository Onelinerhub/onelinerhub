# How to debug using PHP and Twig?
// plain

Debugging using PHP and Twig can be done by using the `debug` function. This function will output the contents of a variable in a human-readable format. For example:

```
$data = array('name' => 'John', 'age' => 25);
echo debug($data);
```

## Output example

```
Array
(
    [name] => John
    [age] => 25
)
```

The `debug` function can be used to inspect the contents of a variable, such as an array or object. It can also be used to inspect the contents of a Twig template, such as the variables and functions available.

To debug a Twig template, the `dump` function can be used. This function will output the contents of a variable in a human-readable format, similar to the `debug` function. For example:

```
{{ dump(data) }}
```

## Output example

```
Array
(
    [name] => John
    [age] => 25
)
```

The `dump` function can be used to inspect the contents of a variable, such as an array or object, within a Twig template.

## Helpful links
- [Twig Documentation - Debugging](https://twig.symfony.com/doc/2.x/api.html#debugging)
- [PHP Documentation - debug_backtrace](https://www.php.net/manual/en/function.debug-backtrace.php)

onelinerhub: [How to debug using PHP and Twig?](https://onelinerhub.com/twig/how-to-debug-using-php-and-twig-)