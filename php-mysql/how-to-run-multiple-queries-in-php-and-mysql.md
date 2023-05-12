# How to run multiple queries in PHP and MySQL?
// plain

To run multiple queries in PHP and MySQL, you can use the `mysqli_multi_query()` function. This function allows you to execute multiple queries at once.

## Example

```
$mysqli = new mysqli("localhost", "user", "password", "database");
$query  = "SELECT * FROM table1; SELECT * FROM table2;";

if ($mysqli->multi_query($query)) {
    do {
        /* store first result set */
        if ($result = $mysqli->store_result()) {
            while ($row = $result->fetch_row()) {
                printf("%s\n", $row[0]);
            }
            $result->free();
        }
        /* print divider */
        if ($mysqli->more_results()) {
            printf("-----------------\n");
        }
    } while ($mysqli->next_result());
}
```

## Output example

```
value1
value2
-----------------
value3
value4
```

## Code explanation

- `$mysqli = new mysqli("localhost", "user", "password", "database");`: Establishes a connection to the MySQL server.
- `$query  = "SELECT * FROM table1; SELECT * FROM table2;";`: Defines the query string containing multiple queries.
- `if ($mysqli->multi_query($query)) {`: Executes the multiple queries.
- `if ($result = $mysqli->store_result()) {`: Stores the first result set.
- `while ($row = $result->fetch_row()) {`: Fetches the rows from the result set.
- `if ($mysqli->more_results()) {`: Checks if there are more results.
- `$mysqli->next_result();`: Moves to the next result set.

## Helpful links
- [MySQLi Multi Query](https://www.php.net/manual/en/mysqli.multi-query.php)

onelinerhub: [How to run multiple queries in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-run-multiple-queries-in-php-and-mysql)