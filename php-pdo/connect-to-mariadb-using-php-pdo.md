# Connect to MariaDB using PHP PDO

### Since MariaDB is fully compatible with Mysql, using it with PDO is the same as Mysql.

```php
try {
  $pdo = new PDO('mysql:host=localhost;dbname=test', 'user', 'pwd');
} catch ( PDOException $e ) {
  die($e->getMessage());
}
```

- `$pdo` - PDO connection object
- `new PDO` - create new PDO connection
- `PDOException $e` - exception will be thrown if connection failed
- `mysql:` - connect to MariaDB using Mysql protocol


