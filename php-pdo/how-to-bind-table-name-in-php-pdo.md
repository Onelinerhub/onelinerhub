# How to bind table name in PHP PDO

### You can't bind table names with PDO, but you can use white filtering and string injection:

```php
$allowed = ['test', 'users', 'messages'];
$table = 'test';

if ( in_array($table, $allowed) ) {
  $st = $pdo->prepare("SELECT * FROM {$table}");
  $st->execute();
  // ...
}
```

- `$allowed` - list of allowed table names (it is important to use this white filter for safety)
- `$table` - table name we want to "bind"
- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server

```
test
```

