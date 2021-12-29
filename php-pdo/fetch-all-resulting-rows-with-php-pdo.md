# Fetch all resulting rows with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test');
$st->execute();
$rows = $st->fetchAll(PDO::FETCH_ASSOC);
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `fetchAll` - returns all rows from result set
- `FETCH_ASSOC` - will return row as an associative array (rather than numbered array)
- `$rows` - resulting array of rows

group: fetch

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test LIMIT 3');
$st->execute();
$rows = $st->fetchAll(PDO::FETCH_ASSOC);
print_r($rows);
```
```
Array
(
    [0] => Array
        (
            [id] => 1
            [age] => 25
            [name] => A
            [data] => 
        )

    [1] => Array
        (
            [id] => 2
            [age] => 52
            [name] => B
            [data] => 
        )

    [2] => Array
        (
            [id] => 3
            [age] => 52
            [name] => C
            [data] => 
        )

)

```

## Additional keywords
- get
- retrieve
- query

