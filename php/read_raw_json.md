# Read JSON from RAW posted data

```php
$json = json_decode(file_get_contents('php://input'), 1);
```

- $json - this variable will conain final JSON array
- json_decode - decode input text as JSON
- file_get_contents('php://input') - returns RAW posted data
