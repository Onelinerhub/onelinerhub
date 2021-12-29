# Select with prepared statement and bind values in PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test WHERE age = :age');
$st->execute([':age' => 52]);
foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st = ` - prepared statement object
- `$st->execute()` - run query on the server
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row
- `:age` - safe value placeholder
- `[':age' => 52]` - bind values when executing query

group: select

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test WHERE age = :age');
$st->execute([':age' => 52]);

foreach ( $st as $row ) {
  print_r($row);
}
```
```
Array
(
    [id] => 2
    [0] => 2
    [age] => 52
    [1] => 52
    [name] => B
    [2] => B
)
Array
(
    [id] => 3
    [0] => 3
    [age] => 52
    [1] => 52
    [name] => C
    [2] => C
)

```

