# Bind current datetime with PHP PDO

```php
$st = $pdo->prepare('INSERT INTO test SET name = :name, created_at = :now');
$st->execute([':name' => 'Donald', ':now' => date('Y-m-d H:i:s')]);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `created_at` - datetime column to be populated
- `:now` - placeholder for current date/time value
- `date('Y-m-d H:i:s')` - will return current time in `YYYY-MM-DD HH:mm:ss` format


