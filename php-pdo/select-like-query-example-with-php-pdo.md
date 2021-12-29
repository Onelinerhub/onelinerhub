# Select LIKE query example with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test WHERE name LIKE :name');
$st->execute([':name' => '%A%']);
foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `LIKE :name` - use standard named placeholder in `LIKE` query
- `%A%` - wrap searched value around with `%` or `_` depending on your goals

group: select

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test WHERE name LIKE :name');
$st->execute([':name' => '%A%']);

foreach ( $st as $row ) {
  print_r($row);
}
```
```
Array
(
    [id] => 1
    [0] => 1
    [age] => 25
    [1] => 25
    [name] => A
    [2] => A
)

```

