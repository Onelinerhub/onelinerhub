# View prepared statement with PHP PDO

```php
$st = $pdo->prepare('SELECT * FROM test WHERE age = :52');
$st->execute([':age' => 52]);
$st->debugDumpParams();
```


## Example: 
```php
<?php

$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test');
$st->execute();
$st->debugDumpParams();
```
```
SQL: [18] SELECT * FROM test
Params:  0

```

