# Get last inserted id with PHP PDO

```php
$st = $pdo->prepare('INSERT INTO test SET name = :name');
$st->execute([':name' => 'Donald']);
$id = $pdo->lastInsertId();
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `$pdo->lastInsertId` - will return last inserted ID of new row (if it's [autoincrement](https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html))

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('INSERT INTO test SET name = :name, age = :age');
$st->execute([':name' => 'Donald', ':age' => 90]);

echo $pdo->lastInsertId();
```
```
7
```

