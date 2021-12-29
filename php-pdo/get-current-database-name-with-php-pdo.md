# Get current database name with PHP PDO

```php
$db = $pdo->query('SELECT database()')->fetchColumn();

```

- `$pdo` - PDO connection object
- `query(` - executes specified SQL and return `PDOStatement` 
- `SELECT database()` - SQL query that will show current database name
- `fetchColumn` - will return single column value 
- `$db` - variable will contain database name

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

echo $pdo->query('SELECT database()')->fetchColumn();
```
```
test
```

