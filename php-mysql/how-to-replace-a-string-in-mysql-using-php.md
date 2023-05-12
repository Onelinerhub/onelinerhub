# How to replace a string in MySQL using PHP?
// plain

Replacing a string in MySQL using PHP can be done using the `str_replace()` function.

```php
$string = "This is a string";
$new_string = str_replace("string", "sentence", $string);
echo $new_string;
```

## Output example

```
This is a sentence
```

The `str_replace()` function takes three parameters:
1. The string to be replaced
2. The string to replace it with
3. The string to search in

The function will then search for the first parameter in the third parameter and replace it with the second parameter.

## Helpful links
- [PHP str_replace() Function](https://www.w3schools.com/php/func_string_str_replace.asp)

onelinerhub: [How to replace a string in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-replace-a-string-in-mysql-using-php)