# How to create an SSL connection to MySQL using PHP?
// plain

Creating an SSL connection to MySQL using PHP is a simple process.

```php
$mysqli = new mysqli("hostname", "username", "password", "database", 3306, "/path/to/certificate/file.pem");

if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
```

The code above will create a secure connection to the MySQL server.

1. `$mysqli = new mysqli("hostname", "username", "password", "database", 3306, "/path/to/certificate/file.pem");` - This line creates a new mysqli object with the hostname, username, password, database, port and path to the certificate file.
2. `if ($mysqli->connect_errno) {` - This line checks if there is an error connecting to the MySQL server.
3. `echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;` - This line prints out an error message if there is an error connecting to the MySQL server.

## Helpful links

- [PHP MySQLi](https://www.php.net/manual/en/book.mysqli.php)
- [MySQL SSL/TLS Setup](https://dev.mysql.com/doc/refman/8.0/en/using-secure-connections.html)

onelinerhub: [How to create an SSL connection to MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-create-an-ssl-connection-to-mysql-using-php)