# How to perform a batch update in a MySQL database using PHP?
// plain

A batch update in a MySQL database using PHP can be performed using the `mysqli_query()` function. This function takes two parameters, the first being the connection to the database and the second being the SQL query.

## Example code

```
$conn = mysqli_connect("localhost", "username", "password", "database");
$sql = "UPDATE table SET column1 = 'value1', column2 = 'value2' WHERE condition";
$result = mysqli_query($conn, $sql);
```

## Output example

```
true
```

## Code explanation

- `mysqli_connect()`: Establishes a connection to the MySQL database.
- `$sql`: Contains the SQL query for the batch update.
- `mysqli_query()`: Executes the SQL query and returns a boolean value indicating the success of the query.

## Helpful links
- [MySQLi Introduction](https://www.w3schools.com/php/php_mysql_intro.asp)
- [MySQLi Query](https://www.w3schools.com/php/func_mysqli_query.asp)

onelinerhub: [How to perform a batch update in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-perform-a-batch-update-in-a-mysql-database-using-php)