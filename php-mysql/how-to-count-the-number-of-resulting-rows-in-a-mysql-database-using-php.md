# How to count the number of resulting rows in a MySQL database using PHP?
// plain

The number of resulting rows in a MySQL database can be counted using PHP by executing a `SELECT COUNT(*)` query. The following example code will return the number of rows in the `users` table:

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

$sql = "SELECT COUNT(*) FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "Number of rows: " . $row["COUNT(*)"];
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

## Output example

```
Number of rows: 5
```

The code consists of the following parts:

1. Establishing a connection to the MySQL database using `$conn = new mysqli($servername, $username, $password, $dbname);`
2. Executing the `SELECT COUNT(*)` query using `$result = $conn->query($sql);`
3. Looping through the result set using `while($row = $result->fetch_assoc())`
4. Outputting the number of rows using `echo "Number of rows: " . $row["COUNT(*)"];`
5. Closing the connection using `$conn->close();`

## Helpful links
- [MySQL SELECT COUNT](https://www.w3schools.com/php/php_mysql_select_count.asp)
- [MySQLi](https://www.w3schools.com/php/php_mysqli.asp)

onelinerhub: [How to count the number of resulting rows in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-count-the-number-of-resulting-rows-in-a-mysql-database-using-php)