# Test PHP PDO connection

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');
$now = $pdo->query('SELECT NOW()')->fetchColumn();
```

- `new PDO` - create new PDO connection
- `query(` - executes specified SQL and return `PDOStatement`
- `SELECT NOW()` - DB will return current date and time
- `fetchColumn` - will return single column value
- `$now` - if this variable contains date/time, our connection is fine

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');
echo $pdo->query('SELECT NOW()')->fetchColumn();
```
```
2021-12-29 15:38:09
```

