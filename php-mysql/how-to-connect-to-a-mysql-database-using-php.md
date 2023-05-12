# How to connect to a MySQL database using PHP?
// plain

To connect to a MySQL database using PHP, you need to use the `mysqli_connect()` function. This function takes four parameters: the hostname, username, password, and database name.

```php
$hostname = "localhost";
$username = "username";
$password = "password";
$dbname = "database_name";

$conn = mysqli_connect($hostname, $username, $password, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
```

## Output example

```
Connected successfully
```

The `mysqli_connect()` function:
- `$hostname`: The hostname of the MySQL server. This is usually `localhost` if the MySQL server is running on the same machine as the PHP script.
- `$username`: The username of the MySQL user.
- `$password`: The password of the MySQL user.
- `$dbname`: The name of the database to connect to.

The function returns a connection resource if the connection is successful, or `FALSE` if the connection fails.

## Helpful links
- [MySQLi Introduction](https://www.w3schools.com/php/php_mysql_intro.asp)
- [MySQLi Connect](https://www.w3schools.com/php/func_mysqli_connect.asp)

onelinerhub: [How to connect to a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-connect-to-a-mysql-database-using-php)