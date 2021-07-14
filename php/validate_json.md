# Check if string contains valid JSON

```php
$is_valid = json_decode($json) ? true : json_last_error() === JSON_ERROR_NONE;
```

- $is_valid - will contain `true` if specified variable is valid JSON
- json_decode - decodes string to object (or array)
- $json - string to check (if it's in JSON format)
- json_last_error - check parsing error if `$json` contains empty array/object/string (which is valid JSON)
