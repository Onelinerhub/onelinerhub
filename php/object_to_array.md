# Convert object to associative array

```php
$arr = json_decode(json_encode($obj), true);
```

- $arr - resulting array
- json_decode - decodes JSON string
- json_encode - encodes object to JSON string
- $obj - object to covert to array
- true - this will decode JSON to array
