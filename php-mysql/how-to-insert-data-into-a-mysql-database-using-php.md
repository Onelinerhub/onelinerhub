# How to insert data into a MySQL database using PHP?
// plain

Inserting data into a MySQL database using PHP is a common task. The following example code block shows how to do this:

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

$sql = "INSERT INTO MyGuests (firstname, lastname, email)
VALUES ('John', 'Doe', 'john@example.com')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
```

The output of this example code is:

```
New record created successfully
```

The code consists of the following parts:

1. Setting up the connection to the MySQL database:
   - `$servername`: The server name of the MySQL database.
   - `$username`: The username of the MySQL database.
   - `$password`: The password of the MySQL database.
   - `$dbname`: The name of the MySQL database.
   - `$conn`: The connection to the MySQL database.
2. Writing the SQL query to insert data into the database:
   - `$sql`: The SQL query to insert data into the database.
3. Executing the SQL query:
   - `$conn->query($sql)`: Executing the SQL query.
4. Checking the result of the query:
   - `if ($conn->query($sql) === TRUE)`: Checking if the query was successful.
5. Closing the connection to the MySQL database:
   - `$conn->close()`: Closing the connection to the MySQL database.

## Helpful links

- [MySQL INSERT INTO Statement](https://www.w3schools.com/sql/sql_insert.asp)
- [PHP MySQL Insert](https://www.w3schools.com/php/php_mysql_insert.asp)

onelinerhub: [How to insert data into a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-insert-data-into-a-mysql-database-using-php)