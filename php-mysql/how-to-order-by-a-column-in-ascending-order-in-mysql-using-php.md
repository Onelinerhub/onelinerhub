# How to order by a column in ascending order in MySQL using PHP?
// plain

To order by a column in ascending order in MySQL using PHP, the following code can be used:

```
$sql = "SELECT * FROM table_name ORDER BY column_name ASC";
$result = mysqli_query($conn, $sql);
```

This code will output the data from the table in ascending order based on the specified column.

The code consists of the following parts:

1. `$sql`: This is the SQL query that is used to select all the data from the table and order it in ascending order based on the specified column.

2. `$result`: This is the result of the query that is stored in a variable.

3. `mysqli_query($conn, $sql)`: This is the function that is used to execute the query and store the result in the `$result` variable.

## Helpful links

- [MySQL ORDER BY Clause](https://www.w3schools.com/sql/sql_orderby.asp)
- [PHP mysqli_query() Function](https://www.w3schools.com/php/func_mysqli_query.asp)

onelinerhub: [How to order by a column in ascending order in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-order-by-a-column-in-ascending-order-in-mysql-using-php)