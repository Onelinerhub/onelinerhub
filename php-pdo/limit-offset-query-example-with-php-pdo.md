# LIMIT OFFSET query example with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test LIMIT :off, :lim');
$st->bindValue(':off', 2, PDO::PARAM_INT);
$st->bindValue(':lim', 2, PDO::PARAM_INT);
$st->execute();

foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `LIMIT :off, :lim` - use placeholders for LIMIT with offset
- `bindValue` - bind value with specified type
- `PDO::PARAM_INT` - bind specified limit and offset values with `integer` type
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test LIMIT :off, :lim');
$st->bindValue(':off', 2, PDO::PARAM_INT);
$st->bindValue(':lim', 2, PDO::PARAM_INT);
$st->execute();

foreach ( $st as $row ) {
  print_r($row);
}
```
```
Array
(
    [id] => 3
    [0] => 3
    [age] => 52
    [1] => 52
    [name] => C
    [2] => C
    [data] => 
    [3] => 
)
Array
(
    [id] => 4
    [0] => 4
    [age] => 90
    [1] => 90
    [name] => Donald
    [2] => Donald
    [data] => 
    [3] => 
)

```

