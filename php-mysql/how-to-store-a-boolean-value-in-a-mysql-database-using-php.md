# How to store a boolean value in a MySQL database using PHP?
// plain

MySQL databases can store boolean values using the `TINYINT` data type. This data type can store values of 0 (false) or 1 (true). To store a boolean value in a MySQL database using PHP, the following code can be used:

```
$boolean_value = true;
$sql = "INSERT INTO table_name (boolean_column) VALUES (?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $boolean_value);
$stmt->execute();
```

The code above:

1. Declares a variable `$boolean_value` and assigns it a boolean value of `true`.
2. Creates an SQL query to insert a value into a table.
3. Prepares the SQL query for execution.
4. Binds the boolean value to the SQL query.
5. Executes the SQL query.

## Helpful links

- [MySQL Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
- [MySQL Prepared Statements](https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php)

onelinerhub: [How to store a boolean value in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-store-a-boolean-value-in-a-mysql-database-using-php)