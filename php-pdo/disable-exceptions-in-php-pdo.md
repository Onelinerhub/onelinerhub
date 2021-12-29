# Disable exceptions in PHP PDO

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
```

- `$pdo` - PDO connection object
- `new PDO` - create new PDO connection
- `setAttribute` - sets configuration option for PDO
- `ATTR_ERRMODE` - error handing mode settings
- `ERRMODE_WARNING` - will log warnings instead of exceptions

group: errors


