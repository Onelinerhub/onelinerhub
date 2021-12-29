# Hash passwords for usage with PHP PDO

```php
$st = $pdo->prepare('INSERT INTO users SET login = :login, pwd = :pwd');
$st->execute([':login' => $_POST['login'], ':pwd' => password_hash($_POST['pwd'])]); 
```

- `$pdo->prepare` - prepare given query to execute
- `INSERT INTO users` - sample `INSERT` query
- `$st->execute(` - run query on the server
- `:pwd` - password placeholder
- `password_hash` - generates secure [password hash](https://onelinerhub.com/php/hash_pwd) used with `password_verify()` to check passwords on login
- `$_POST['pwd']` - original password (posted by user)


