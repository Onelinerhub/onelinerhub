# How to escape JSON in PHP and MySQL?
// plain

JSON (JavaScript Object Notation) is a lightweight data-interchange format used for exchanging data between a server and a client. In PHP and MySQL, escaping JSON is done by using the `json_encode()` function. This function takes a PHP value and returns a JSON string representation of it.

```php
$data = array("name" => "John", "age" => 30);
$json_data = json_encode($data);
echo $json_data;
```

## Output example

```
{"name":"John","age":30}
```

The `json_encode()` function takes the following parameters:

- `$value`: The value to be encoded.
- `$options`: Bitmask consisting of `JSON_HEX_QUOT`, `JSON_HEX_TAG`, `JSON_HEX_AMP`, `JSON_HEX_APOS`, `JSON_NUMERIC_CHECK`, `JSON_PRETTY_PRINT`, `JSON_UNESCAPED_SLASHES`, `JSON_FORCE_OBJECT`, `JSON_PRESERVE_ZERO_FRACTION`, `JSON_UNESCAPED_UNICODE`, `JSON_PARTIAL_OUTPUT_ON_ERROR`.

The `json_encode()` function returns a JSON encoded string on success and `FALSE` on failure.

## Helpful links
- [PHP json_encode() Function](https://www.w3schools.com/php/func_json_json_encode.asp)
- [JSON - Overview](https://www.w3schools.com/js/js_json_intro.asp)

onelinerhub: [How to escape JSON in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-escape-json-in-php-and-mysql)