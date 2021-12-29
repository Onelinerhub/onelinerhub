# Select with prepared statement in PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test');
$st->execute();
foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st = ` - prepared statement object
- `$st->execute()` - run query on the server
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row

group: select

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test');
$st->execute();

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

