# Get affected rows with PHP PDO

```php
$st = $pdo->prepare('UPDATE test SET updated_at = NOW()');
$st->execute();
$updated = $st->rowCount();
```

- `$pdo->prepare` - prepare given query to execute
- `UPDATE test` - sample query affecting multiple rows
- `$st->execute(` - run query on the server
- `rowCount` - returns affected rows
- `$updated` - will contain affected rows

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('UPDATE test SET age = age - 1');
$st->execute();
echo $st->rowCount();
```
```
11
```

