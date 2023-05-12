# How to list tables in PHP MySQL?
// plain

To list tables in PHP MySQL, you can use the `SHOW TABLES` command. This command will return a list of all the tables in the current database.

## Example code

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

$sql = "SHOW TABLES";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Table: " . $row["Tables_in_myDB"];
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

## Output example

```
Table: mytable
Table: mytable2
Table: mytable3
```

## Code explanation


1. `$servername = "localhost";` - This line sets the variable `$servername` to the value `localhost`, which is the default server name for MySQL.

2. `$username = "username";` - This line sets the variable `$username` to the value `username`, which is the username used to connect to the MySQL server.

3. `$password = "password";` - This line sets the variable `$password` to the value `password`, which is the password used to connect to the MySQL server.

4. `$dbname = "myDB";` - This line sets the variable `$dbname` to the value `myDB`, which is the name of the database we are connecting to.

5. `$conn = new mysqli($servername, $username, $password, $dbname);` - This line creates a new MySQLi connection using the variables set in the previous lines.

6. `$sql = "SHOW TABLES";` - This line sets the variable `$sql` to the value `SHOW TABLES`, which is the command used to list all the tables in the current database.

7. `$result = $conn->query($sql);` - This line executes the `SHOW TABLES` command and stores the result in the variable `$result`.

8. `if ($result->num_rows > 0) {` - This line checks if the result of the `SHOW TABLES` command contains any rows.

9. `while($row = $result->fetch_assoc()) {` - This line loops through each row in the result of the `SHOW TABLES` command.

10. `echo "Table: " . $row["Tables_in_myDB"];` - This line prints out the name of each table in the result of the `SHOW TABLES` command.

11. `$conn->close();` - This line closes the MySQLi connection.

## Helpful links

- [MySQL SHOW TABLES](https://dev.mysql.com/doc/refman/8.0/en/show-tables.html)
- [MySQLi](https://www.php.net/manual/en/book.mysqli.php)

onelinerhub: [How to list tables in PHP MySQL?](https://onelinerhub.com/php-mysql/how-to-list-tables-in-php-mysql)