# How to use var_dump with PHP and Twig?
// plain

Var_dump is a PHP function used to display structured information about variables and their content. It can be used with Twig to debug and inspect variables in a template.

## Example code

```
<?php
$var = array('a' => 1, 'b' => 2);
var_dump($var);
?>
```

## Output example

```
array(2) {
  ["a"]=>
  int(1)
  ["b"]=>
  int(2)
}
```

## Code explanation

- `$var = array('a' => 1, 'b' => 2);` - creates an array with two elements
- `var_dump($var);` - displays structured information about the array

## Helpful links
- [PHP var_dump() Function](https://www.w3schools.com/php/func_var_dump.asp)
- [Twig Documentation](https://twig.symfony.com/doc/2.x/)

onelinerhub: [How to use var_dump with PHP and Twig?](https://onelinerhub.com/twig/how-to-use-var_dump-with-php-and-twig-)