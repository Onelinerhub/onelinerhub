# How to get the number of affected rows in a MySQL using PHP?
// plain

The number of affected rows in a MySQL query can be obtained using the `mysqli_affected_rows()` function in PHP.

## Example code

```
$mysqli = new mysqli("localhost", "user", "password", "database");
$query = "DELETE FROM table WHERE id = 1";
$mysqli->query($query);
$affected_rows = mysqli_affected_rows($mysqli);
echo $affected_rows;
```

## Output example

```
1
```

## Code explanation

- `$mysqli = new mysqli("localhost", "user", "password", "database");` - creates a new mysqli object with the given parameters.
- `$query = "DELETE FROM table WHERE id = 1";` - creates a query to delete a row from the table.
- `$mysqli->query($query);` - executes the query.
- `$affected_rows = mysqli_affected_rows($mysqli);` - gets the number of affected rows from the query.
- `echo $affected_rows;` - prints the number of affected rows.

## Helpful links
- [mysqli_affected_rows()](https://www.php.net/manual/en/mysqli.affected-rows.php) - PHP manual page for the `mysqli_affected_rows()` function.

onelinerhub: [How to get the number of affected rows in a MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-get-the-number-of-affected-rows-in-a-mysql-using-php)