# How to hash password

```php
password_hash('pwd', PASSWORD_DEFAULT);
```

- password_hash - create password hash string (use [password_verify()](https://www.php.net/manual/function.password-verify.php) to validate inputs then)
- 'pwd' - password string to hash
- PASSWORD_DEFAULT - type of hasher to use

## Example

```php
$hash = password_hash('pwd', PASSWORD_DEFAULT);
if ( password_verify($_POST['password'], $hash) ) {
  echo 'Correct password';
}
```
```bash
Correct password # When "pwd" password is posted
```
