# How to get results after PHP PDO statement execute()

```php
$st->execute();
foreach ( $st as $row ) {
  print_r($row);
}
```

- `$st->execute(` - run query on the server
- `foreach ( $st as $row )` - go through each row in result set
- `print_r($row)` - print each row


