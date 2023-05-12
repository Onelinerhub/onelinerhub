# How to bind parameters in a MySQL database using PHP?
// plain

Binding parameters in a MySQL database using PHP is a way to prevent SQL injection attacks. It is done by using the `mysqli_stmt_bind_param()` function.

## Example code

```
$stmt = mysqli_prepare($conn, "INSERT INTO table (name, age) VALUES (?, ?)");
mysqli_stmt_bind_param($stmt, "si", $name, $age);
mysqli_stmt_execute($stmt);
```

## Code explanation

- `mysqli_prepare($conn, "INSERT INTO table (name, age) VALUES (?, ?)")`: prepares an SQL statement for execution
- `mysqli_stmt_bind_param($stmt, "si", $name, $age)`: binds parameters to the prepared statement
- `mysqli_stmt_execute($stmt)`: executes the prepared statement

## Helpful links
- [PHP: mysqli_stmt_bind_param - Manual](https://www.php.net/manual/en/mysqli-stmt.bind-param.php)
- [MySQLi Prepared Statements](https://www.w3schools.com/php/php_mysql_prepared_statements.asp)

onelinerhub: [How to bind parameters in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-bind-parameters-in-a-mysql-database-using-php)