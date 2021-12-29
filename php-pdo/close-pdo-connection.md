# Close PDO connection

```php
$pdo = new PDO('mysql:host=localhost;dbname=test', 'user', 'pwd');
# do some stuff with $pdo...
$pdo = null;
```

- `new PDO` - create new PDO connection
- `$pdo = null` - destroys PDO object and closes connection to database

group: connect


