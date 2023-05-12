# How to insert an array into a MySQL database using PHP?
// plain

To insert an array into a MySQL database using PHP, the following steps should be taken:

1. Establish a connection to the MySQL database using the `mysqli_connect()` function.
```php
$conn = mysqli_connect("localhost", "username", "password", "database");
```

2. Create an array of values to be inserted into the database.
```php
$values = array("John", "Doe", "john@example.com");
```

3. Create a prepared statement using the `mysqli_prepare()` function.
```php
$stmt = mysqli_prepare($conn, "INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)");
```

4. Bind the array of values to the prepared statement using the `mysqli_stmt_bind_param()` function.
```php
mysqli_stmt_bind_param($stmt, "sss", $values[0], $values[1], $values[2]);
```

5. Execute the prepared statement using the `mysqli_stmt_execute()` function.
```php
mysqli_stmt_execute($stmt);
```

## Code explanation


- `mysqli_connect()`: Establishes a connection to the MySQL database.
- `mysqli_prepare()`: Creates a prepared statement.
- `mysqli_stmt_bind_param()`: Binds an array of values to the prepared statement.
- `mysqli_stmt_execute()`: Executes the prepared statement.

## Helpful links

- [MySQLi Introduction](https://www.w3schools.com/php/php_mysql_intro.asp)
- [MySQLi Prepared Statements](https://www.w3schools.com/php/php_mysql_prepared_statements.asp)

onelinerhub: [How to insert an array into a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-insert-an-array-into-a-mysql-database-using-php)