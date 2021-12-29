# Fetch single column value with PHP PDO

```php
$st = $pdo->prepare('SELECT name FROM test LIMIT 1');
$st->execute();
$value = $st->fetchColumn();
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `$st->fetchColumn()` - return single column value from resulting set
- `name` - column to get value of

group: fetch

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT id FROM test LIMIT 1');
$st->execute();
$value = $st->fetchColumn();
echo $value;
```
```
1
```

## Additional keywords
- get
- retrieve
- query

