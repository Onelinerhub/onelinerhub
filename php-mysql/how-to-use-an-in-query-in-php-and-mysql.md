# How to use an IN query in PHP and MySQL?
// plain

An IN query in PHP and MySQL is used to select multiple values from a database table. It is used when you need to select multiple values from a single column.

## Example code

```
$sql = "SELECT * FROM table_name WHERE column_name IN (value1, value2, value3)";
$result = mysqli_query($conn, $sql);
```

## Output example

```
Array of results
```

## Code explanation

- `$sql`: This is the SQL query that will be used to select multiple values from a single column.
- `SELECT * FROM table_name`: This is the command used to select all columns from a table.
- `WHERE column_name IN (value1, value2, value3)`: This is the command used to select multiple values from a single column.
- `$result`: This is the result of the query.

## Helpful links
- [MySQL IN Clause](https://www.w3schools.com/sql/sql_in.asp)
- [MySQLi Prepared Statements](https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php)

onelinerhub: [How to use an IN query in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-use-an-in-query-in-php-and-mysql)