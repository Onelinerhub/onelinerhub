# How to perform a bulk insert in a MySQL database using PHP?
// plain

Bulk insert in MySQL database using PHP can be done using the `mysqli_multi_query()` function. This function allows multiple SQL statements to be executed at once.

## Example code

```
$sql = "INSERT INTO table1 (column1, column2, column3) VALUES ('value1', 'value2', 'value3');
INSERT INTO table2 (column1, column2, column3) VALUES ('value1', 'value2', 'value3');";

if (mysqli_multi_query($conn, $sql)) {
    echo "New records created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
```

## Output example

```
New records created successfully
```

## Code explanation

- `mysqli_multi_query()`: This function takes two parameters, the first one is the connection to the MySQL database and the second one is the SQL query.
- `INSERT INTO`: This is the SQL statement used to insert data into a table.
- `VALUES`: This is the clause used to specify the values to be inserted into the table.

## Helpful links
- [MySQL INSERT statement](https://dev.mysql.com/doc/refman/8.0/en/insert.html)
- [mysqli_multi_query()](https://www.php.net/manual/en/mysqli.multi-query.php)

onelinerhub: [How to perform a bulk insert in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-perform-a-bulk-insert-in-a-mysql-database-using-php)