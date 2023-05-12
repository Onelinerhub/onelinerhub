# How to get query error message in PHP MySQL?
// plain

To get the query error message in PHP MySQL, you can use the `mysqli_error()` function. This function returns the error message from the last MySQL operation.

## Example code

```
$mysqli = new mysqli("localhost", "user", "password", "database");

/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT * FROM table";
$result = $mysqli->query($query);

if (!$result) {
    printf("Error: %s\n", mysqli_error($mysqli));
    exit();
}
```

## Output example

```
Error: Table 'database.table' doesn't exist
```

## Code explanation

- `mysqli_error()`: This function returns the error message from the last MySQL operation.
- `mysqli_connect_errno()`: This function returns the error code from the last MySQL operation.
- `mysqli_connect_error()`: This function returns the error message from the last MySQL connection error.

## Helpful links
- [mysqli_error()](https://www.php.net/manual/en/mysqli.error.php)
- [mysqli_connect_errno()](https://www.php.net/manual/en/mysqli.connect-errno.php)
- [mysqli_connect_error()](https://www.php.net/manual/en/mysqli.connect-error.php)

onelinerhub: [How to get query error message in PHP MySQL?](https://onelinerhub.com/php-mysql/how-to-get-query-error-message-in-php-mysql)