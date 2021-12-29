# Select IN array with PHP PDO

```php
$ids = [1, 2];

$sql = 'SELECT * FROM test WHERE id IN (:' . implode(', :', array_keys($ids)) . ')';
$st = $pdo->prepare($sql);

$bind = [];
array_walk($ids, function($v, $k) use (&$bind) { $bind[':' . $k] = $v; });

$st->execute($bind);
foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `$ids = [1, 2];` - array to use in `IN` expression
- `IN (:' . implode(', :', array_keys($ids)) . ')` - generate placeholders from given array
- `array_walk($ids` - generate bind values from given array and save it to `$bind` variable

group: select

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$ids = [1, 2];

$sql = 'SELECT * FROM test WHERE id IN (:' . implode(', :', array_keys($ids)) . ')';
$st = $pdo->prepare($sql);

$bind = [];
array_walk($ids, function($v, $k) use (&$bind) { $bind[':' . $k] = $v; });

$st->execute($bind);
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

```

