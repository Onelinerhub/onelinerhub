# UPDATE query example with PHP PDO

```php
$st = $pdo->prepare('UPDATE test SET age = :new_age WHERE id = :id');
$st->execute([':new_age' => 53, ':id' => 1]);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `[':new_age' => 53, ':id' => 1]` - bind both update values (used in `SET`) and filter values (used `WHERE`)

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('UPDATE test SET age = :new_age WHERE id = :id');
$st->execute([':new_age' => 53, ':id' => 1]);

echo $st->rowCount();
```
```
1
```

