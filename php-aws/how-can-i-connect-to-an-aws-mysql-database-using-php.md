# How can I connect to an AWS MySQL database using PHP?
// plain

To connect to an AWS MySQL database using PHP, you will need to use the PHP MySQLi extension. The following example code will connect to an AWS MySQL database:

```
<?php
$servername = "example.amazonaws.com";
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

This example code will output `Connected successfully` if the connection was successful.

## Code explanation


1. `$servername`: The hostname of the AWS MySQL database.
2. `$username`: The username used to connect to the AWS MySQL database.
3. `$password`: The password used to connect to the AWS MySQL database.
4. `$conn`: The variable which will store the connection object.
5. `new mysqli()`: The function used to create a new connection object.
6. `connect_error`: The property of the connection object which stores any errors that occur.
7. `die()`: The function used to terminate the script if an error occurs.
8. `echo`: The function used to output a string if the connection was successful.

## Helpful links

- [PHP MySQLi Extension](https://www.php.net/manual/en/book.mysqli.php)
- [PHP mysqli::connect_error](https://www.php.net/manual/en/mysqli.connect-error.php)
- [PHP die()](https://www.php.net/manual/en/function.die.php)
- [PHP echo](https://www.php.net/manual/en/function.echo.php)

onelinerhub: [How can I connect to an AWS MySQL database using PHP?](https://onelinerhub.com/php-aws/how-can-i-connect-to-an-aws-mysql-database-using-php)