# How to alter a table in a MySQL database using PHP?
// plain

Altering a table in a MySQL database using PHP is a simple process. The following example code block shows how to add a new column to an existing table:

```
$sql = "ALTER TABLE table_name ADD column_name datatype";

if ($conn->query($sql) === TRUE) {
    echo "Column added successfully";
} else {
    echo "Error adding column: " . $conn->error;
}
```

## Output example

```
Column added successfully
```

## Code explanation


1. `$sql = "ALTER TABLE table_name ADD column_name datatype";` - This line of code creates a SQL query to alter the table. `table_name` is the name of the table to be altered, `column_name` is the name of the new column to be added, and `datatype` is the data type of the new column.

2. `if ($conn->query($sql) === TRUE) {` - This line of code checks if the query was successful.

3. `echo "Column added successfully";` - This line of code prints a success message if the query was successful.

4. `echo "Error adding column: " . $conn->error;` - This line of code prints an error message if the query was unsuccessful.

## Helpful links

- [MySQL ALTER TABLE Statement](https://www.w3schools.com/sql/sql_alter.asp)
- [MySQL PHP Reference](https://www.w3schools.com/php/php_ref_mysqli.asp)

onelinerhub: [How to alter a table in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-alter-a-table-in-a-mysql-database-using-php)