# Connect to Mysql with PHP PDO

```php
try {
  $pdo = new PDO('mysql:host=localhost;dbname=test', 'user', 'pwd');
} catch ( PDOException $e ) {
  die($e->getMessage());
}
```

- `new PDO` - create new PDO connection
- `mysql:` - connect to Mysql
- `localhost` - Mysql host to connect to
- `test` - database to use
- `user` - username
- `pwd` - password
- `PDOException $e` - exception will be thrown if connection failed

group: connect


