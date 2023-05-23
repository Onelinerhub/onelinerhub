# How to return JSON from Symfony with PHP?
// plain

Symfony is a PHP framework that can be used to return JSON data. To do this, you can use the `json_encode()` function.

## Example code

```php
<?php
$data = array('name' => 'John', 'age' => 30);
echo json_encode($data);
```

## Output example

```
{"name":"John","age":30}
```

## Code explanation

- `$data`: an array containing the data to be encoded
- `json_encode()`: a PHP function that takes an array as an argument and returns a JSON string

## Helpful links
- [PHP json_encode() Function](https://www.w3schools.com/php/func_json_encode.asp)

onelinerhub: [How to return JSON from Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-return-json-from-symfony-with-php)