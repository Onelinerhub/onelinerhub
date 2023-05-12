# How to use utf8mb4_unicode_ci in MySQL with PHP?
// plain

MySQL supports the utf8mb4_unicode_ci character set, which allows for storing characters from a wide range of languages. To use this character set in PHP, you need to set the character set in the connection string when connecting to the database.

```php
$conn = new mysqli("localhost", "username", "password", "database", 3306, "", MYSQLI_CLIENT_SSL);
$conn->set_charset("utf8mb4_unicode_ci");
```

The code above creates a new connection to the database and sets the character set to utf8mb4_unicode_ci.

## Code explanation


1. `$conn = new mysqli("localhost", "username", "password", "database", 3306, "", MYSQLI_CLIENT_SSL);` - creates a new connection to the database.
2. `$conn->set_charset("utf8mb4_unicode_ci");` - sets the character set to utf8mb4_unicode_ci.

## Helpful links

- [MySQL 8.0 Reference Manual: Character Sets and Collations](https://dev.mysql.com/doc/refman/8.0/en/charset-collation-settings.html)
- [MySQLi: set_charset](https://www.php.net/manual/en/mysqli.set-charset.php)

onelinerhub: [How to use utf8mb4_unicode_ci in MySQL with PHP?](https://onelinerhub.com/php-mysql/how-to-use-utf8mb4_unicode_ci-in-mysql-with-php)