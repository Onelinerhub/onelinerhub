# How to write an update query in MySQL using PHP?
// plain

An update query in MySQL using PHP can be written using the `mysqli_query()` function. The syntax for this function is as follows:

```
mysqli_query($connection, "UPDATE table_name SET column1=value1, column2=value2 WHERE some_column=some_value");
```

This query will update the values of `column1` and `column2` in the table `table_name` where `some_column` is equal to `some_value`.

The parts of the code are as follows:

- `$connection`: This is the connection to the MySQL database.
- `UPDATE table_name`: This is the name of the table to be updated.
- `SET column1=value1, column2=value2`: This is the list of columns and values to be updated.
- `WHERE some_column=some_value`: This is the condition for which rows should be updated.

## Helpful links

- [MySQL UPDATE Query](https://www.w3schools.com/sql/sql_update.asp)
- [PHP mysqli_query() Function](https://www.w3schools.com/php/func_mysqli_query.asp)

onelinerhub: [How to write an update query in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-write-an-update-query-in-mysql-using-php)