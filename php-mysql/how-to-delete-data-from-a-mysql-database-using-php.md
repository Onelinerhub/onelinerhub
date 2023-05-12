# How to delete data from a MySQL database using PHP?
// plain

To delete data from a MySQL database using PHP, the `DELETE` statement can be used. The following example code block shows how to delete a row from a table named `users` where the `id` is `1`:

```
$sql = "DELETE FROM users WHERE id=1";

if ($conn->query($sql) === TRUE) {
    echo "Record deleted successfully";
} else {
    echo "Error deleting record: " . $conn->error;
}
```

The output of the example code would be:

```
Record deleted successfully
```

The code consists of the following parts:

1. `$sql`: This is a variable that contains the `DELETE` statement.
2. `$conn->query($sql)`: This is a function that executes the `DELETE` statement.
3. `if` statement: This is a conditional statement that checks if the `DELETE` statement was executed successfully.
4. `echo` statement: This is a function that prints out a message depending on the result of the `DELETE` statement.

## Helpful links

- [MySQL DELETE Statement](https://www.w3schools.com/sql/sql_delete.asp)
- [PHP MySQL DELETE Query](https://www.w3schools.com/php/php_mysql_delete.asp)

onelinerhub: [How to delete data from a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-delete-data-from-a-mysql-database-using-php)