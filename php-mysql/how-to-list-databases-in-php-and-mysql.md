# How to list databases in PHP and MySQL?
// plain

To list databases in PHP and MySQL, you can use the `SHOW DATABASES` command.

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

$sql = "SHOW DATABASES";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Database: " . $row["Database"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

## Output example

```
Database: information_schema
Database: mysql
Database: performance_schema
Database: sys
Database: your_database_name
```

## Code explanation

- `$servername = "localhost";` - sets the server name to localhost
- `$username = "username";` - sets the username
- `$password = "password";` - sets the password
- `$conn = new mysqli($servername, $username, $password);` - creates a new connection to the MySQL server
- `$sql = "SHOW DATABASES";` - sets the SQL query to show databases
- `$result = $conn->query($sql);` - executes the query
- `if ($result->num_rows > 0) {` - checks if there are any results
- `while($row = $result->fetch_assoc()) {` - fetches the results
- `echo "Database: " . $row["Database"]. "<br>";` - prints the database name
- `$conn->close();` - closes the connection

## Helpful links
- [MySQL SHOW DATABASES](https://dev.mysql.com/doc/refman/8.0/en/show-databases.html)
- [MySQLi](https://www.php.net/manual/en/book.mysqli.php)

onelinerhub: [How to list databases in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-list-databases-in-php-and-mysql)