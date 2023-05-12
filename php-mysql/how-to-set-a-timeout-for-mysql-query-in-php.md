# How to set a timeout for MySQL query in PHP?
// plain

The `mysqli_query()` function in PHP can be used to set a timeout for a MySQL query. The `timeout` parameter of the function can be used to set the timeout value in seconds.

```
$mysqli = new mysqli("localhost", "user", "password", "database");
$query = "SELECT * FROM table";
$result = $mysqli->query($query, MYSQLI_STORE_RESULT, MYSQLI_OPT_CONNECT_TIMEOUT, 10);
```

The output of the above code will be a `mysqli_result` object if the query is successful, or `FALSE` if the query times out.

## Code explanation


- `$mysqli = new mysqli("localhost", "user", "password", "database");`: This line creates a new `mysqli` object with the given parameters.
- `$query = "SELECT * FROM table";`: This line sets the query to be executed.
- `$result = $mysqli->query($query, MYSQLI_STORE_RESULT, MYSQLI_OPT_CONNECT_TIMEOUT, 10);`: This line executes the query with a timeout of 10 seconds.

## Helpful links

- [mysqli_query()](https://www.php.net/manual/en/mysqli.query.php)
- [mysqli_options()](https://www.php.net/manual/en/mysqli.options.php)

onelinerhub: [How to set a timeout for MySQL query in PHP?](https://onelinerhub.com/php-mysql/how-to-set-a-timeout-for-mysql-query-in-php)