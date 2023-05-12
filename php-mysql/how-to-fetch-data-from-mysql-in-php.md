# How to fetch data from MySQL in PHP?
// plain

Fetching data from MySQL in PHP can be done using the `mysqli_query()` function. This function takes two parameters, the first being the connection to the MySQL database, and the second being the SQL query.

```php
$conn = mysqli_connect("localhost", "username", "password", "database");
$sql = "SELECT * FROM table";
$result = mysqli_query($conn, $sql);
```

The output of the above code will be a `mysqli_result` object, which can be used to loop through the results of the query.

```php
while ($row = mysqli_fetch_assoc($result)) {
    echo $row['column_name'];
}
```

## Code explanation


1. `mysqli_connect()` - Establishes a connection to the MySQL database.
2. `mysqli_query()` - Executes an SQL query on the database.
3. `mysqli_fetch_assoc()` - Fetches a row from the result set as an associative array.

## Helpful links

- [MySQLi Introduction](https://www.w3schools.com/php/php_mysql_intro.asp)
- [MySQLi Query](https://www.w3schools.com/php/func_mysqli_query.asp)
- [MySQLi Fetch Assoc](https://www.w3schools.com/php/func_mysqli_fetch_assoc.asp)

onelinerhub: [How to fetch data from MySQL in PHP?](https://onelinerhub.com/php-mysql/how-to-fetch-data-from-mysql-in-php)