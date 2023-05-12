# How to get the first row of a result in MySQL using PHP?
// plain

To get the first row of a result in MySQL using PHP, you can use the `mysqli_fetch_assoc()` function. This function takes a result set as an argument and returns an associative array of the first row.

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
- `mysqli_fetch_assoc($result)`: This line takes the result set as an argument and returns an associative array of the first row.

## Helpful links
- [PHP mysqli_fetch_assoc() Function](https://www.w3schools.com/php/func_mysqli_fetch_assoc.asp)

onelinerhub: [How to get the first row of a result in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-get-the-first-row-of-a-result-in-mysql-using-php)