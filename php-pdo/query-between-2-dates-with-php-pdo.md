# Query between 2 dates with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test WHERE date BETWEEN :start AND :end');
$st->execute([':start' => '2025-10-10', ':end' => '2020-10-10']);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `:start AND :end` - use placeholders for starting and ending date used for `BETWEEN`
- `:start` - bind start date value
- `:end` - bind end date value


