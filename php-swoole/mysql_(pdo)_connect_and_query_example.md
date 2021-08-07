# Mysql (PDO) connect and query example

```php
Co\run(function() {

  $pdo = new PDO('mysql:host=localhost', 'root', '');

  go(function () use ($pdo) {
    $st = $pdo->prepare("SELECT now()");
    $st->execute([]);
    print_r($st->fetch());
  });

});
```

- new PDO - connect to mysql server based on given config
- go( - execute async code
- "SELECT now()" - SQL query to execute
- print_r($st->fetch()) - prints result from Mysql server


## Example
```php
php mysql.php
```
```
Array
(
    [now()] => 2022-08-07 12:38:12
    [0] => 2022-08-07 12:38:12
)
```

group: mysql
