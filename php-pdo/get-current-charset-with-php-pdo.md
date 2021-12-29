# Get current charset with PHP PDO

```php
$charset = $pdo->query("SELECT COLLATION('')")->fetchColumn();
```

- `$pdo` - PDO connection object
- `query(` - executes specified SQL and return `PDOStatement`
- `SELECT COLLATION('')` - will return current charset (actually collation, but that's also ok for this task)
- `$charset` - will contain current charset (collation)

group: charset

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');
echo $pdo->query("SELECT COLLATION('')")->fetchColumn();
```
```
utf8mb4_general_ci
```

