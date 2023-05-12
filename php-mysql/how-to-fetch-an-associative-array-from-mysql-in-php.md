# How to fetch an associative array from MySQL in PHP?
// plain

Fetching an associative array from MySQL in PHP can be done using the `mysqli_fetch_assoc()` function. This function takes a result set as an argument and returns an associative array.

## Example code

```
$result = mysqli_query($conn, "SELECT * FROM table");
$row = mysqli_fetch_assoc($result);
```

## Output example

```
Array
(
    [column1] => value1
    [column2] => value2
    [column3] => value3
)
```

## Code explanation

- `mysqli_query($conn, "SELECT * FROM table")`: This line executes a query on the MySQL database and returns a result set.
- `mysqli_fetch_assoc($result)`: This line takes the result set as an argument and returns an associative array.

## Helpful links
- [PHP: mysqli_fetch_assoc - Manual](https://www.php.net/manual/en/mysqli-result.fetch-assoc.php)

onelinerhub: [How to fetch an associative array from MySQL in PHP?](https://onelinerhub.com/php-mysql/how-to-fetch-an-associative-array-from-mysql-in-php)