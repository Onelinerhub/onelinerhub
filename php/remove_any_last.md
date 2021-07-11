# Remove any last character from a string

```php
$new_str = substr($str, 0, -1);
```

- $new_str - string without last character will be saved here
- substr - function to extract [part of the given string](https://www.php.net/manual/function.substr.php)
- $str - original string to remove last character from
- 0, - extract substring starting from beginning of original string ...
- -1) - ... and ending one character prior to the end of the original string

group: trim
