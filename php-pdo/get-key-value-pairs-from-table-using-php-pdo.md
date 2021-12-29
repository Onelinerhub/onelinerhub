# Get key-value pairs from table using PHP PDO

```php
$st = $pdo->prepare('SELECT id, name FROM test');
$st->execute();
$key_vals = $st->fetchAll(PDO::FETCH_KEY_PAIR);
```

- `$pdo->prepare` - prepare given query to execute
- `id, name` - 2 columns that will be used as `key` (1st column) and `value` (2nd column)
- `$st->execute(` - run query on the server
- `fetchAll` - returns all rows from result set
- `FETCH_KEY_PAIR` - will return key-value pairs based on selected columns in the resulting set

group: fetch

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT id, name FROM test LIMIT 3');
$st->execute();
$key_vals = $st->fetchAll(PDO::FETCH_KEY_PAIR);
print_r($key_vals);
```
```
Array
(
    [1] => A
    [2] => B
    [3] => C
)

```

