# How to hash a password in PHP and MySQL?
// plain

Hashing a password in PHP and MySQL is a secure way to store user passwords. It is done by using a one-way hashing algorithm to convert the plain text password into a random string of characters.

## Example code

```
$password = 'mypassword';
$hashed_password = password_hash($password, PASSWORD_DEFAULT);
```

## Output example

```
$2y$10$VX3/3VX3VX3VX3VX3VX3VX3VX3VX3VX3VX3VX3VX3VX3VX3VX3
```

## Code explanation

- `$password`: This is the plain text password that needs to be hashed.
- `password_hash()`: This is the PHP function used to hash the password.
- `PASSWORD_DEFAULT`: This is the algorithm used to hash the password.

## Helpful links
- [PHP password_hash()](https://www.php.net/manual/en/function.password-hash.php)
- [MySQL PASSWORD()](https://dev.mysql.com/doc/refman/8.0/en/encryption-functions.html#function_password)

onelinerhub: [How to hash a password in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-hash-a-password-in-php-and-mysql)