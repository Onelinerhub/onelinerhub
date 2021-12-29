# Select with prepared statement in PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test');
$st->execute();
foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st = ` - prepared statement object
- `$st->execute()` - run query on the server
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row

group: select


