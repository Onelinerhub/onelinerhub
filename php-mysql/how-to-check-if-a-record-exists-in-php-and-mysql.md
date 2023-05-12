# How to check if a record exists in PHP and MySQL?
// plain

To check if a record exists in PHP and MySQL, you can use the `SELECT` statement. For example, the following code will check if a record with the `id` of `1` exists in the `users` table:

```
$sql = "SELECT * FROM users WHERE id = 1";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    echo "Record exists";
} else {
    echo "Record does not exist";
}
```

## Output example

```
Record exists
```

## Code explanation

- `$sql`: This is the SQL query that will be used to check if the record exists.
- `$result`: This is the result of the query.
- `mysqli_query($conn, $sql)`: This is a function that will execute the query and return the result.
- `mysqli_num_rows($result)`: This is a function that will return the number of rows in the result.
- `if` statement: This is used to check if the number of rows in the result is greater than 0.

## Helpful links
- [MySQL SELECT statement](https://dev.mysql.com/doc/refman/8.0/en/select.html)
- [PHP mysqli_query() function](https://www.php.net/manual/en/mysqli.query.php)
- [PHP mysqli_num_rows() function](https://www.php.net/manual/en/mysqli-result.num-rows.php)

onelinerhub: [How to check if a record exists in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-check-if-a-record-exists-in-php-and-mysql)