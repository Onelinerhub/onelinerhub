# Batch insert with PHP PDO

### We're going to generate `?` placeholders and use `VALUES(),(),()` SQL syntax to insert multiple rows at once.

```php
$data = [
  ['name' => 'Donald', 'age' => 90],
  ['name' => 'Joe', 'age' => 95],
];

$place_holder = '(' . implode(',', array_fill(0, count($data[0]), '?')) . ')';
$place_hoders = implode(',', array_fill(0, count($data), $place_holder));

$st = $pdo->prepare('INSERT INTO test(name, age) VALUES' . $place_hoders);

$flat = call_user_func_array('array_merge', array_map('array_values', $data));
$st->execute( $flat );
```

- `$data` - list with multiple arrays to batch insert into table
- `$place_holder` - generate single `(?,...)` format placeholder based on columns count
- `$place_hoders` - generate all `(?...),(?,...)...` format placeholders based on rows count
- `$pdo->prepare` - prepare given query to execute
- `$flat = ` - flatten our `$data` array so we have all values in one-dimensional array
- `$st->execute(` - run query on the server

group: insert

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$data = [
  ['name' => 'Donald', 'age' => 90],
  ['name' => 'Joe', 'age' => 95],
];

$place_holder = '(' . implode(',', array_fill(0, count($data[0]), '?')) . ')';
$place_hoders = implode(',', array_fill(0, count($data), $place_holder));

$st = $pdo->prepare('INSERT INTO test(name, age) VALUES' . $place_hoders);

$flat = call_user_func_array('array_merge', array_map('array_values', $data));
$st->execute( $flat );

echo $st->rowCount();
```
```
2
```

