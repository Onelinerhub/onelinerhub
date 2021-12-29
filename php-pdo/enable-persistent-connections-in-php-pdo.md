# Enable persistent connections in PHP PDO

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd', [
  PDO::ATTR_PERSISTENT => true
]);
```

- `$pdo` - PDO connection object
- `new PDO` - create new PDO connection
- `PDO::ATTR_PERSISTENT` - enables or disables persistent connections

group: settings


## Additional keywords
- keep
- alive
- keepalive

