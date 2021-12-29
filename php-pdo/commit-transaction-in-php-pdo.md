# Commit transaction in PHP PDO

```php
$pdo->beginTransaction();
# queries inside transaction
$pdo->commit();
```

- `$pdo` - PDO connection object
- `beginTransaction` - starts transaction
- `commit` - commits transaction


