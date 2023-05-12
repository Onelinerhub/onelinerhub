# How to check the result of an insert in PHP and MySQL?
// plain

To check the result of an insert in PHP and MySQL, you can use the `mysqli_affected_rows()` function. This function returns the number of rows affected by the last `INSERT`, `UPDATE`, `REPLACE` or `DELETE` query.

## Example code

```
$sql = "INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3)";
$result = mysqli_query($conn, $sql);

if (mysqli_affected_rows($conn) > 0) {
    echo "Insert successful";
} else {
    echo "Insert failed";
}
```

## Output example

```
Insert successful
```

## Code explanation

- `$sql`: This is the SQL query used to insert data into the table.
- `$result`: This is the result of the query.
- `mysqli_query($conn, $sql)`: This is the function used to execute the query. `$conn` is the connection to the database.
- `mysqli_affected_rows($conn)`: This is the function used to check the number of rows affected by the query.
- `if` statement: This is used to check if the query was successful or not.

## Helpful links
- [mysqli_affected_rows()](https://www.php.net/manual/en/mysqli.affected-rows.php)

onelinerhub: [How to check the result of an insert in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-check-the-result-of-an-insert-in-php-and-mysql)