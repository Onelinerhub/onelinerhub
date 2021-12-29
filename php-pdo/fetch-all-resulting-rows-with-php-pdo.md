# Fetch all resulting rows with PHP PDO

### get
retrieve
query

```php
$st = $pdo->prepare('SELECT * FROM test LIMIT 10');
$st->execute();
$row = $st->fetchAll(PDO::FETCH_ASSOC);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server

group: fetch


