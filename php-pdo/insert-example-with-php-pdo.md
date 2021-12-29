# Insert example with PHP PDO

```php
$st = $pdo->prepare('INSERT INTO test SET name = :name, age = :age');
$st->execute([':name' => 'Donald', ':age' => 90]); 
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('INSERT INTO test SET name = :name, age = :age');
$st->execute([':name' => 'Donald', ':age' => 90]);

echo $pdo->lastInsertId();
```
```
6
```

