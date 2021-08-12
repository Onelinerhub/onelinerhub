# PostgreSQL connect and query example

Make sure to [install postgres extension](https://www.swoole.co.uk/docs/modules/swoole-coroutine-postgres) for Swoole.

```php
Co\run(function() {

  $pg = new Swoole\Coroutine\PostgreSQL();
  $pg->connect('host=127.0.0.1;port=5432;dbname=db;user=u;password=p');

  go(function () use ($pg) {
    $res = $pg->query('SELECT CURRENT_DATE;');
    print_r($pg->fetchAll($res));
  });

});
```

- Swoole\Coroutine\PostgreSQL - Postgres client for Swoole
- $pg->connect - init connection to DB
- $pg->query - execute sample query
- print_r($pg->fetchAll($res)) - print fetched results from DB
