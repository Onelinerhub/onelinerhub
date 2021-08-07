# Mysql (PDO) connection pool usage example

```php
Co\run(function() {

  $pool = new Swoole\Database\PDOPool( (
    new Swoole\Database\PDOConfig())->withHost('localhost')->withUsername('root')
  );

  for ( $i = 0; $i < 5; $i++ ) {
    go(function () use ($pool) {
      $pdo = $pool->get();
      $st = $pdo->prepare("SELECT now()"); $st->execute([]);
      print_r($st->fetch());
    });
  }

});
```

- new Swoole\Database\PDOPool - create PDO connection pool based on specified setting
- Swoole\Database\PDOConfig - configure database [credentials](https://www.swoole.co.uk/docs/modules/pdo-connection-pool-config)
- $i < 5; $i++ - let's execute 5 simultaneous queries
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
    [now()] => 2022-08-07 12:46:25
    [0] => 2022-08-07 12:46:25
)
Array
(
    [now()] => 2022-08-07 12:46:25
    [0] => 2022-08-07 12:46:25
)
Array
(
    [now()] => 2022-08-07 12:46:25
    [0] => 2022-08-07 12:46:25
)
Array
(
    [now()] => 2022-08-07 12:46:25
    [0] => 2022-08-07 12:46:25
)
Array
(
    [now()] => 2022-08-07 12:46:25
    [0] => 2022-08-07 12:46:25
)
```

group: mysql
