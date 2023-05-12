# How to create a table in a MySQL database using PHP?
// plain

Creating a table in a MySQL database using PHP is a simple process. The following example code block will create a table called `users` with three columns: `id`, `name`, and `email`:

```
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// sql to create table
$sql = "CREATE TABLE users (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
email VARCHAR(50),
reg_date TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
    echo "Table users created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

$conn->close();
?>
```

The output of the example code will be:

```
Table users created successfully
```

## Code explanation


1. `$servername`, `$username`, `$password`, `$dbname`: These variables are used to store the connection information for the MySQL database.
2. `$conn = new mysqli($servername, $username, $password, $dbname)`: This line creates a new connection to the MySQL database using the connection information stored in the variables.
3. `$sql = "CREATE TABLE users (...)`: This line creates a SQL query to create a table called `users` with three columns: `id`, `name`, and `email`.
4. `if ($conn->query($sql) === TRUE)`: This line executes the SQL query to create the table.
5. `echo "Table users created successfully"`: This line prints a message to the screen if the table was created successfully.

## Helpful links

- [MySQL CREATE TABLE statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [PHP MySQLi Introduction](https://www.w3schools.com/php/php_mysql_intro.asp)

onelinerhub: [How to create a table in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-create-a-table-in-a-mysql-database-using-php)