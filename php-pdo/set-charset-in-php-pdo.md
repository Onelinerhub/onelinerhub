# Set charset in PHP PDO

```php
$pdo = new PDO('mysql:host=localhost;dbname=test;charset=utf8mb4', 'usr', 'pwd');

```

- `$pdo` - PDO connection object
- `new PDO` - create new PDO connection
- `localhost` - Mysql host to connect to
- `utf8mb4` - which charset to use

group: charset

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test;charset=utf8mb4', 'usr', 'pwd');
print_r($pdo);
```
```
PDO Object
(
)

```

