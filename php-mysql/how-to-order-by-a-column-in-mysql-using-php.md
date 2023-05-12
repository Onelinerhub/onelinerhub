# How to order by a column in MySQL using PHP?
// plain

To order by a column in MySQL using PHP, you can use the `ORDER BY` clause in a `SELECT` statement. For example:

```
$sql = "SELECT * FROM table_name ORDER BY column_name ASC";
$result = mysqli_query($conn, $sql);
```

This will output the results of the query in ascending order based on the values in the `column_name` column.

## Code explanation


- `SELECT * FROM table_name`: This is the query that will select all the data from the `table_name` table.
- `ORDER BY column_name ASC`: This clause will order the results of the query in ascending order based on the values in the `column_name` column.
- `mysqli_query($conn, $sql)`: This will execute the query and return the result set.

## Helpful links

- [MySQL ORDER BY Clause](https://www.w3schools.com/sql/sql_orderby.asp)
- [PHP mysqli_query() Function](https://www.w3schools.com/php/func_mysqli_query.asp)

onelinerhub: [How to order by a column in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-order-by-a-column-in-mysql-using-php)