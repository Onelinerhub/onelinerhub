# Insert JSON into table with PHP PDO

```php
$json = ['some' => 'value', 'key' => 'okay'];
$st = $pdo->prepare('INSERT INTO test SET data = :json');
$st->execute([':json' => json_encode($json)]);
```

- `$json` - example array to save as JSON in the table
- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `json_encode($json)` - we encode array to a `JSON` string to save it in the `TEXT` column

group: json

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$json = ['some' => 'value', 'key' => 'okay'];
$st = $pdo->prepare('INSERT INTO test SET data = :json');
$st->execute([':json' => json_encode($json)]);

echo $pdo->lastInsertId();
```
```
9
```

