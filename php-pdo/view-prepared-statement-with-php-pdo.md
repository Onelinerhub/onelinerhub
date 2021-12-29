# View prepared statement with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test WHERE age = :52');
$st->execute([':age' => 52]);
$st->debugDumpParams();
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `debugDumpParams` - prints (instead or return) prepared query statement and list of bind values

## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test WHERE age = :52');
$st->execute([':age' => 52]);
$st->debugDumpParams();
```
```
SQL: [34] SELECT * FROM test WHERE age = :52
Params:  1
Key: Name: [4] :age
paramno=-1
name=[4] ":age"
is_param=1
param_type=2

```

