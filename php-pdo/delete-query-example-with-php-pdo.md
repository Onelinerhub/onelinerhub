# Delete query example with PHP PDO

```php

$st = $pdo->prepare('DELETE FROM test WHERE age = :age');
$st->execute([':age' => 50]);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `DELETE FROM test` - sample `DELETE` query

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('DELETE FROM test WHERE age = :age');
$st->execute([':age' => 50]);
echo $st->rowCount();
```
```
5
```

