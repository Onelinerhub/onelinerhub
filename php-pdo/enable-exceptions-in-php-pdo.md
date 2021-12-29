# Enable exceptions in PHP PDO

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
```

- `$pdo` - PDO connection object
- `new PDO` - create new PDO connection
- `setAttribute` - sets configuration option for PDO
- `ATTR_ERRMODE` - error handing mode settings
- `ERRMODE_EXCEPTION` - will throw `PDOException` exceptions on errors

group: errors


