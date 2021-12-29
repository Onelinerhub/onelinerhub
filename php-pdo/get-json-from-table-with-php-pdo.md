# Get JSON from table with PHP PDO

### We have `test` table with `data` text column which stores data in JSON format.

```php
$st = $pdo->prepare('SELECT data FROM test WHERE id = 8');
$st->execute();
$json = json_decode($st->fetchColumn(), 1);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `json_decode(` - converts JSON string to associative array
- `$st->fetchColumn()` - return single column (`data` in our case) value from resulting set
- `$json =` - will store resulting JSON array

group: json

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT data FROM test WHERE id = 8');
$st->execute();
$json = json_decode($st->fetchColumn(), 1);
print_r($json);
```
```
Array
(
    [some] => value
    [key] => okay
)

```

