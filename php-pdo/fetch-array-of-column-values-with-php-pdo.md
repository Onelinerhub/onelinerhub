# Fetch array of column values with PHP PDO

```php
$st = $pdo->prepare('SELECT id FROM test');
$st->execute();
$cols = $st->fetchAll(PDO::FETCH_COLUMN);
```

- `$pdo->prepare` - prepare given query to execute
- `id` - column we want to get into resulting array
- `$st->execute(` - run query on the server
- `fetchAll` - returns all rows from result set
- `FETCH_COLUMN` - will return single column value per row rather than associative array
- `$cols` - resulting array of column values

group: fetch

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT id FROM test LIMIT 3');
$st->execute();
$cols = $st->fetchAll(PDO::FETCH_COLUMN);
print_r($cols);
```
```
Array
(
    [0] => 1
    [1] => 2
    [2] => 3
)

```

