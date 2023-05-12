# How to call a stored procedure in MySQL using PHP?
// plain

Calling a stored procedure in MySQL using PHP is a simple process. The following example code block shows how to call a stored procedure named `myProcedure`:

```
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}

/* call the stored procedure */
if ($mysqli->multi_query("CALL myProcedure()")) {
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

/* close connection */
$mysqli->close();
```

The output of the example code above would be the result of the stored procedure `myProcedure`:

```
Result of myProcedure
-----------------
More results of myProcedure
```

## Code explanation


1. `$mysqli = new mysqli("localhost", "my_user", "my_password", "world");` - This line creates a new MySQLi object with the given parameters.

2. `if (mysqli_connect_errno()) {` - This line checks if there is an error in the connection.

3. `if ($mysqli->multi_query("CALL myProcedure()")) {` - This line calls the stored procedure `myProcedure`.

4. `if ($result = $mysqli->store_result()) {` - This line stores the result of the stored procedure.

5. `while ($row = $result->fetch_row()) {` - This line fetches the result row by row.

6. `printf("%s\n", $row[0]);` - This line prints the result of the stored procedure.

7. `$result->free();` - This line frees the result of the stored procedure.

8. `if ($mysqli->more_results()) {` - This line checks if there are more results.

9. `$mysqli->close();` - This line closes the connection.

## Helpful links

- [MySQLi Procedural API](https://www.php.net/manual/en/book.mysqli.php)
- [MySQLi Object-oriented API](https://www.php.net/manual/en/class.mysqli.php)

onelinerhub: [How to call a stored procedure in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-call-a-stored-procedure-in-mysql-using-php)