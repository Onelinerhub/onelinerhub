# PHP PDO usage example

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'usr', 'pwd');

$st = $pdo->prepare('SELECT * FROM test');
$st->execute();

foreach ( $st as $row ) {
  print_r($row);
}
```

- `$pdo->prepare` - prepare given query to execute
- `$st->execute(` - run query on the server
- `new PDO` - create new PDO connection
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row
- `test` - database to use
- `usr` - db user
- `pwd` - db password


