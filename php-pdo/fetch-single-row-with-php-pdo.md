# Fetch single row with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test LIMIT 1');
$st->execute();
$row = $st->fetch(PDO::FETCH_ASSOC);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `fetch` - returns single row from resulting set
- `FETCH_ASSOC` - will return row as an associative array (rather than numbered array)

group: fetch

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test LIMIT 1');
$st->execute();
$row = $st->fetch(PDO::FETCH_ASSOC);
print_r($row);
```
```
Array
(
    [id] => 1
    [age] => 25
    [name] => A
    [data] => 
)

```

## Additional keywords
- get
- retrieve
- query

