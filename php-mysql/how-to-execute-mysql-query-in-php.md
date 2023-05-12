# How to execute MySQL query in PHP?
// plain

MySQL queries can be executed in PHP using the `mysqli_query()` function. This function takes two parameters, the first being the MySQLi connection object and the second being the query string.

```
$conn = mysqli_connect("localhost", "username", "password", "database");
$query = "SELECT * FROM table";
$result = mysqli_query($conn, $query);
```

The code above creates a connection to the MySQL database, then creates a query string and stores it in the `$query` variable. Finally, the `mysqli_query()` function is used to execute the query and store the result in the `$result` variable.

Parts of the code:

- `mysqli_connect()`: Establishes a connection to the MySQL database.
- `$query`: Stores the query string.
- `mysqli_query()`: Executes the query and stores the result.

## Helpful links

- [MySQLi Introduction](https://www.php.net/manual/en/book.mysqli.php)
- [MySQLi Query](https://www.php.net/manual/en/mysqli.query.php)

onelinerhub: [How to execute MySQL query in PHP?](https://onelinerhub.com/php-mysql/how-to-execute-mysql-query-in-php)