# What port to connect to MySQL from PHP?
// plain

The port to connect to MySQL from PHP is 3306. This port is the default port for MySQL and is used for both TCP and Unix sockets.

Example code to connect to MySQL from PHP:
```
<?php
$servername = "localhost";
$username = "username";
$password = "password";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
```

Output of example code:
```
Connected successfully
```

## Code explanation


1. `$servername = "localhost";` - This sets the server name to localhost.
2. `$username = "username";` - This sets the username for the connection.
3. `$password = "password";` - This sets the password for the connection.
4. `$conn = new mysqli($servername, $username, $password);` - This creates a new MySQLi connection using the server name, username, and password.
5. `if ($conn->connect_error) {` - This checks if there is an error in the connection.
6. `die("Connection failed: " . $conn->connect_error);` - This prints an error message if there is an error in the connection.
7. `echo "Connected successfully";` - This prints a success message if the connection is successful.

## Helpful links

- [MySQLi Connection](https://www.php.net/manual/en/mysqli.quickstart.connections.php)
- [MySQLi Reference](https://www.php.net/manual/en/book.mysqli.php)

onelinerhub: [What port to connect to MySQL from PHP?](https://onelinerhub.com/php-mysql/what-port-to-connect-to-mysql-from-php)