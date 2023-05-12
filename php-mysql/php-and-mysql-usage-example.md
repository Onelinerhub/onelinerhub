# PHP and MySQL usage example
// plain

PHP and MySQL are commonly used together to create dynamic web applications. Here is an example of a simple PHP script that connects to a MySQL database and retrieves data from a table:

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

$sql = "SELECT id, firstname, lastname FROM MyGuests";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

## Output example

```
Connected successfully
id: 1 - Name: John Doe
id: 2 - Name: Mary Moe
id: 3 - Name: Julie Dooley
```

This example code does the following:

1. Establishes a connection to the MySQL server using the `mysqli()` function.
2. Checks the connection using the `connect_error` property.
3. Executes a SQL query using the `query()` method.
4. Retrieves the data from the query using the `fetch_assoc()` method.
5. Outputs the data.
6. Closes the connection using the `close()` method.

## Helpful links

- [PHP Manual: MySQLi](https://www.php.net/manual/en/book.mysqli.php)
- [MySQL Tutorial](https://www.w3schools.com/sql/default.asp)

onelinerhub: [PHP and MySQL usage example](https://onelinerhub.com/php-mysql/php-and-mysql-usage-example)