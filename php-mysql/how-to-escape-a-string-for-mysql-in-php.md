# How to escape a string for MySQL in PHP?
// plain

The best way to escape a string for MySQL in PHP is to use the `mysqli_real_escape_string()` function. This function takes two parameters, the first being the MySQL connection and the second being the string to be escaped.

```php
$conn = mysqli_connect("localhost", "username", "password", "database");
$escapedString = mysqli_real_escape_string($conn, $string);
```

The output of the above code will be the escaped string.

The `mysqli_real_escape_string()` function does the following:

- Escapes special characters in the string for use in an SQL statement
- Adds backslashes before characters that need to be escaped
- Prepares the string for use in a MySQL query

## Helpful links

- [PHP: mysqli_real_escape_string - Manual](https://www.php.net/manual/en/mysqli.real-escape-string.php)

onelinerhub: [How to escape a string for MySQL in PHP?](https://onelinerhub.com/php-mysql/how-to-escape-a-string-for-mysql-in-php)