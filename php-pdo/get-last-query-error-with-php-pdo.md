# Get last query error with PHP PDO

```php
$error = $pdo->errorInfo();
```

- `$error` - will contain error details
- `$pdo` - PDO connection object
- `errorInfo` - returns details of last error happened

group: errors

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$pdo->query('WRONG');

$error = $pdo->errorInfo();
print_r($error);
```
```
Array
(
    [0] => 42000
    [1] => 1064
    [2] => You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'WRONG' at line 1
)

```

