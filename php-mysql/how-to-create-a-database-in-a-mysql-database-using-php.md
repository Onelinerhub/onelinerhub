# How to create a database in a MySQL database using PHP?
// plain

Creating a database in a MySQL database using PHP is a simple process. The following example code will create a database called `my_db`:
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

// Create database
$sql = "CREATE DATABASE my_db";
if ($conn->query($sql) === TRUE) {
    echo "Database created successfully";
} else {
    echo "Error creating database: " . $conn->error;
}

$conn->close();
?>
```
The output of the example code will be:
```
Database created successfully
```
The code consists of the following parts:
1. Establishing a connection to the MySQL server using `$conn = new mysqli($servername, $username, $password)`
2. Creating the database using `$sql = "CREATE DATABASE my_db"`
3. Checking if the database was created successfully using `if ($conn->query($sql) === TRUE)`
4. Closing the connection using `$conn->close()`

## Helpful links
- [MySQL Create Database](https://www.w3schools.com/php/php_mysql_create_db.asp)
- [MySQL Create Table](https://www.w3schools.com/php/php_mysql_create_table.asp)

onelinerhub: [How to create a database in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-create-a-database-in-a-mysql-database-using-php)