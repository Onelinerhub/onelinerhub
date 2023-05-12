# How to create a socket connection to MySQL using PHP?
// plain

Creating a socket connection to MySQL using PHP is a simple process. The following example code will create a connection to a MySQL server:

```
<?php
$host = 'localhost';
$user = 'username';
$pass = 'password';
$dbname = 'database_name';

$conn = new mysqli($host, $user, $pass, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
```

The output of the above code will be:

```
Connected successfully
```

The code consists of the following parts:

1. Variables for the host, user, password and database name.
2. A new mysqli object is created with the given variables.
3. An if statement to check if the connection was successful.
4. An echo statement to print the success message.

## Helpful links

- [PHP MySQLi Introduction](https://www.w3schools.com/php/php_mysqli_intro.asp)
- [PHP MySQLi Connect](https://www.w3schools.com/php/php_mysqli_connect.asp)

onelinerhub: [How to create a socket connection to MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-create-a-socket-connection-to-mysql-using-php)