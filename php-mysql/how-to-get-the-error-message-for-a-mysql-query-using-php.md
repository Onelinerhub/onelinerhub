# How to get the error message for a MySQL query using PHP?
// plain

To get the error message for a MySQL query using PHP, you can use the `mysqli_error()` function. This function takes the connection object as an argument and returns the error message.

## Example code

```
$conn = mysqli_connect("localhost", "username", "password", "database");
$query = "SELECT * FROM table";
$result = mysqli_query($conn, $query);
if (!$result) {
    echo mysqli_error($conn);
}
```

## Output example

```
Table 'database.table' doesn't exist
```

## Code explanation

- `mysqli_connect()`: Establishes a connection to a MySQL server. Takes four arguments: hostname, username, password, and database name.
- `mysqli_query()`: Executes a query against the database. Takes two arguments: connection object and query string.
- `mysqli_error()`: Returns the error message for the last query executed. Takes one argument: connection object.

## Helpful links
- [PHP mysqli_connect() Function](https://www.w3schools.com/php/func_mysqli_connect.asp)
- [PHP mysqli_query() Function](https://www.w3schools.com/php/func_mysqli_query.asp)
- [PHP mysqli_error() Function](https://www.w3schools.com/php/func_mysqli_error.asp)

onelinerhub: [How to get the error message for a MySQL query using PHP?](https://onelinerhub.com/php-mysql/how-to-get-the-error-message-for-a-mysql-query-using-php)