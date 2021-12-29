# Using utf8mb4 in PHP PDO

```php
$pdo = new PDO('mysql:host=localhost;dbname=test;charset=utf8mb4', 'usr', 'pwd');
```

- `new PDO` - create new PDO connection
- `charset=utf8mb4` - set charset to utf8mb4


