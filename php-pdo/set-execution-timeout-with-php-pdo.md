# Set execution timeout with PHP PDO

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd', [
  PDO::ATTR_TIMEOUT => 90
]);
```

- `$pdo` - PDO connection object
- `new PDO` - create new PDO connection
- `PDO::ATTR_TIMEOUT` - settings attribute that controls execution timeout
- `90` - value in seconds for timeout


