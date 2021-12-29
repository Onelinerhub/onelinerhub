# Join query example with PHP PDO

```php
$st = $pdo->prepare('SELECT p.*, u.name FROM photos p JOIN users u ON (u.id = p.user_id)');
$st->execute();

foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `p.*, u.name` - selects all columns from `photos` table and `name` column from `users` table
- `$st->execute(` - run query on the server
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row


