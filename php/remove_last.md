# Trim specific last characters from a string

```php
$new_str = rtrim($str, ',;');
```

- $new_str - string without specified last character will be saved here
- rtrim - removed specified character from the end of the string
- $str - original string to trim characters from the end of
- ',;' - list of the characters to trim (specified as a string, will trim `,` and `;` in our case)

group: trim
