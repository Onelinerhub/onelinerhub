# How to get a single value from query in PHP MySQL?
// plain

To get a single value from a query in PHP MySQL, you can use the `mysqli_fetch_assoc()` function. This function takes a result set as an argument and returns an associative array with the first row of the result set.

## Example code

```
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_assoc($result);
echo $row['column_name'];
```

## Output example

```
value
```

## Code explanation

- `mysqli_query($conn, $sql)`: This function executes the SQL query and returns a result set.
- `mysqli_fetch_assoc($result)`: This function takes a result set as an argument and returns an associative array with the first row of the result set.
- `$row['column_name']`: This is used to access the value of a particular column in the result set.

## Helpful links
- [PHP MySQLi](https://www.php.net/manual/en/book.mysqli.php)
- [mysqli_fetch_assoc()](https://www.php.net/manual/en/mysqli-result.fetch-assoc.php)

onelinerhub: [How to get a single value from query in PHP MySQL?](https://onelinerhub.com/php-mysql/how-to-get-a-single-value-from-query-in-php-mysql)